from django.test import TestCase
from django.urls.resolvers import URLResolver

from news.admin import NewsAdminSite


class TestAdminSite(TestCase):

    def setUp(self):
        self.admin_site = NewsAdminSite()
        
    def test_api_urls_in_admin_site(self):

        expected = "'api/'"

        urls_objects = self.admin_site.get_urls()
        urls = list(
            filter(lambda x: isinstance(x, URLResolver), urls_objects)
        )
        result = urls[0].pattern.describe()

        self.assertEqual(result, expected)
