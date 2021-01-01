from django.test import TestCase
from django.urls import reverse

from languageTests.models import Topic
import random
import pprint

class TopicListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_topics = 13
        levels=['b','i','e']
        for topic_id in range(number_of_topics):
            Topic.objects.create(
                title=f'title {topic_id}',
                level=levels[random.randint(0,2)]
            )
            print("########")
            
    def test_view_url_exists_at_desired_location(self):
        pass
        response = self.client.get('/languageTests/topics/')
        self.assertEqual(response.status_code, 200)            