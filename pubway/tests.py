from django.contrib.auth.models import *
from django.contrib.auth import views as auth_views
from django.test import TestCase
from django.urls import *
from django.urls import reverse

from pubway.views import *
from pubway.models import *
from pubway.forms import *
from pubway.urls import *

import pubway.test_utils as test_utils

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

    def test_place_form_is_displayed_correctly(self):

        try:
            response = self.client.get(reverse('add_place'))
        except:
            try:
                response = self.client.get(reverse('pubway:add_place'))
            except:
                return False

        #Check rendering of form
        self.assertIn('<strong>Add Place</strong><br />'.lower(), response.content.decode('ascii').lower())
        self.assertTrue(isinstance(response.context['place_form'], PlaceForm))

class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_pubway import populate
            populate()
        except ImportError:
            print('The module populate_pubway does not exist')
        except NameError:
            print('The function populate() does not exist or is incorrect')
        except:
            print('Something went wrong in the populate() function')

    def get_station(self, name):

        from pubway.models import Station
        try:
            station = Station.objects.get(name=name)
        except Station.DoesNotExist:
            station = None
        return station

    def test_hillhead_station_added(self):
        station = self.get_station('Hillhead')
        self.assertIsNotNone(station)

    def test_15_stations_populated(self):
        stations = Station.objects.all()
        self.assertTrue(stations.count()==15)

    def get_place(self, name):

        from pubway.models import Place
        try:
            place = Place.objects.get(name=name)
        except Place.DoesNotExist:
            place = None
        return place

    def test_hive_place_populated(self):
        place = self.get_place('Hive')
        self.assertIsNotNone(place)

    def test_place_has_likes(self):
        place = self.get_place('GUU')
        self.assertIsNotNone(place.likes)

    def test_place_has_address(self):
        place = self.get_place('QMU')
        self.assertIsNotNone(place.address)

class SubcrawlTests(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUsernameSub", "test@gmail.com", "testPassword")
        hh = Station.objects.get_or_create(name='Hillhead')[0]
        subcrawl = Subcrawl.objects.get_or_create(sub_name="test sub", sub_organiser = user, first_st=hh)[0]
    def testSubcrawlExists(self):
        # Test that the new subcrawl exists
        try:
            Subcrawl.objects.get(sub_name="test sub")
        except:
            self.fail("Subcrawl testsub doesn't exist")
        # Test that the number of users is 1
        self.assertEqual(1, Subcrawl.objects.count(), "Number of Subcrawls must be 1")

    def testSubcrawlOptions(self):
        subcrawl = Subcrawl.objects.get(sub_name="test sub")
        hh = Station.objects.get_or_create(name='Hillhead')[0]
        self.assertEqual('testUsernameSub', subcrawl.sub_organiser.username, "Organiser should be testUsernameSub")
        self.assertEqual(hh, subcrawl.first_st, "First station should be Hillhead")
        self.assertEqual('test-sub',subcrawl.sub_slug, "slug should be test-sub")

    def testPlaces(self):
        subcrawl = Subcrawl.objects.get(sub_name="test sub")
        self.assertEqual(0, subcrawl.sub_places.count(), "Number of places must be initially 0")
        qmu = Place.objects.get_or_create(name='QMU')[0]
        subcrawl.sub_places.add(qmu)
        self.assertEqual(1, subcrawl.sub_places.count(), "Number of places must be 1")