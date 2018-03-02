from django.test import TestCase
from .models import Entry
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

#While testing Django looks through all the classes starting with Test en excutes all functions starting with test_

class TestEntry(TestCase):

    def setUp(self):
        self.entry = Entry(
            name='name',
            author=User.objects.create(),
            date=timezone.now(),
            description='Combine strudel, chickpeas and eggs. jumble with whole curry and serve sliced with chicken. Enjoy!'
        )

    setUp()

    def test_short_description(self):
        self.assertEquals(self.entry.short_description(), 'Combine strudel')

