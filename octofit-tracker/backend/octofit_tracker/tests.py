from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)
        self.assertIn(self.user, self.team.members.all())

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(user=self.user, activity_type='Run', duration=30, calories_burned=300, date='2024-01-01')

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(user=self.user, name='Cardio', description='Cardio session', date='2024-01-01', personalized=True)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_calories=1000, total_duration=120)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
