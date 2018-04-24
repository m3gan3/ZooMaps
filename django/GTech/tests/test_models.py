from django.test import TestCase
from ZooMaps.models import Tag, UserModel, User, Event, RatingEvent, MessageEvent
import random
import unittest
from hypothesis import given, example
import hypothesis.strategies as st
from hypothesis.extra.django.models import models
from hypothesis.extra.django import TestCase
from django.urls import reverse

@classmethod
def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    try:
        import hypothesis
    except ImportError as e:
            print('Cannot load module: {0!r}'.format(e))


class TagTestCase(TestCase):
    def setUp(self):
        # Create list of tags with random names
        num_tags = random.randint(10, 35)
        tag_names = [str(random.randint(100, 1000)) for i in range(num_tags)]
        tags = [Tag.objects.create(tagName=name) for name in tag_names]


    def test_all_tags_return_their_names(self):
        # Tag '__str__' property should return the tagName property
        tags = Tag.objects.all()
        for tag in tags:
            self.assertEqual(tag.tagName, str(tag))


    def test_tagName_max_length(self):
        # Any random tag's 'max_length' field is 200.
        tags = Tag.objects.all()
        random_tag = random.choice(tags)
        tag_max_length_field = random_tag._meta.get_field('tagName').max_length
        self.assertEquals(tag_max_length_field, 200)


    @unittest.expectedFailure
    @given(invalid_tag_names=st.lists(st.floats()))
    def test_invalid_tagName_raises_exceptions(invalid_tag_names):
        # Attempt to create invalid tags. Test will fail if any pass
        for invalid_tag_name in invalid_tag_names:
            try:
                Tag.objects.create(tagName=invalid_tag_name)
            except Exception as e:
                raise e


class UserModelTestCase(TestCase):
    def setUp(self):
        # TODO: Create list of users with random names
        pass

    @given(random_users=st.lists(models(UserModel)))
    def test_all_users_return_usernames(self, random_users):
        for random_user in random_users:
            self.assertEquals(random_user.username, str(random_user))


class EventTestCase(TestCase):

    @given(random_events=st.lists(models(Event)))
    def test_all_events_return_name(self, random_events):
        for random_event in random_events:
            self.assertEquals(random_event.name, str(random_event))

    @given(random_events=st.lists(models(Event)))
    def test_get_absolute_url(self, random_events):
        for random_event in random_events:
            self.assertEquals(random_event.get_absolute_url(), reverse('event-detail', args=[str(random_event.id)]))


class RatingEventTestCase(TestCase):

    @given(random_RatingEvents=st.lists(models(RatingEvent)))
    def test_all_RatingEvents_return_name(self, random_RatingEvents):
        for random_RatingEvent in random_RatingEvents:
            self.assertEquals(random_RatingEvent.name, str(random_RatingEvent))


class MessageEventTestCase(TestCase):

    @given(random_MessageEvents=st.lists(models(MessageEvent,
                                                username=models(User),
                                                event=models(Event)
                                                )))
    def test_all_MessageEvents_return_name(self, random_MessageEvents):
        for random_MessageEvent in random_MessageEvents:
            self.assertEquals(random_MessageEvent.event.name, str(random_MessageEvent))
