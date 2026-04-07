from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    personalized = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'Personalized' if self.personalized else 'General'})"

class Leaderboard(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name='leaderboard')
    total_calories = models.PositiveIntegerField(default=0)
    total_duration = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Leaderboard for {self.team.name}"