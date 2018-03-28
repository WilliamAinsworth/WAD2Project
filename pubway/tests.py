from django.test import TestCase
from django.urls import reverse

from pubway.models import UserProfile, User, Station, Place
from django.contrib.auth import views as auth_views


# Test case In the area of the user profile
class UserManagementTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUsername", "test@gmail.com", "testPassword")
        UserProfile.objects.create(user=user)

    def testUserExists(self):
        # Test that the new user exists
        user = User.objects.get(username="testUsername")
        UserProfile.objects.get(user=user)

        # Test that the number of users is 1
        self.assertEqual(1, UserProfile.objects.count(), "Number of Profiles must be 1")

    def testLogIn(self):
        login = self.client.login(username='testUsername', password='testPassword')
        self.assertTrue(login)

    def testPasswordChange(self):
        # Get created user
        user = User.objects.get(username="testUsername")

        # Test Change Password Form is found
        response = self.client.get(reverse('changepassword'))
        assert (response.status_code == 200 or response.status_code == 302)

        # Test Password Change Form is validated
        form = auth_views.PasswordChangeForm(user=user, data={
            'old_password': 'testPassword',
            'new_password1': 'newTestPassword',
            'new_password2': 'newTestPassword'})
        self.assertTrue(form.is_valid())

class StationTests(TestCase):

    def test_slug_creation(self):
        station = Station('St. something different,')
        station.save()
        self.assertEqual(station.slug,'st-something-different')