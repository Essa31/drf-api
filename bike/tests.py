from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Bike


# Create your tests here.
class BikeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test', password='test1234')
        test_user.save()
        test_bike = Bike.objects.create(name="api_test", purchaser=test_user, desc="api_test")
        test_bike.save()

    def test_thing_model(self):
        bike = Bike.objects.get(pk=1)
        self.assertEqual(str(bike.purchaser), 'test')
        self.assertEqual(str(bike.name), 'api_test')
        self.assertEqual(str(bike.desc), 'api_test')