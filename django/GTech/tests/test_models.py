from django.test import TestCase
from ZooMaps.models import .
import random


class TagTestCase(TestCase):
    def setUp(self):
        # Create list of tags with random names
        num_tags = random.randint(10, 35)
        tag_names = [str(random.randint(100, 1000)) for i in range(num_tags)]
        tags = [Tag.objects.create(tagName=name) for name in tag_names]

    def test_all_tags_return_their_names(self):
        # Tag '__str__' property should return the tagName property
        tags = Tags.objects
        for tag in tags:
            assertEqual(tag.tagName, str(tag))

    def test_get_absolute_url(self):
        # TODO, check that the url conf is defined
        pass
