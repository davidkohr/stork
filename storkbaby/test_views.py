from django.test import TestCase, Client

class HomeRouteTestCase(TestCase):

    def test_home_get_returns_200(self):
        """Home page returns a 200"""
        c = Client()
        response = c.get('/storkbaby/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_post_returns_200(self):
        """Home page returns a 200"""
        c = Client()
        response = c.post('/storkbaby/')
        self.assertEqual(response.status_code, 200)

    def test_home_delete_returns_200(self):
        """Home page returns a 200"""
        c = Client()
        response = c.update('/storkbaby/')
        self.assertEqual(response.status_code, 200)