import requests
import unittest


BASE_URL = 'http://localhost'
PORT = '8000'
ENDPOINT = 'notes'

title =  "test title",
message = "This is just a title string"

class TestEndpoint(unittest.TestCase):
    def test_post_note(self):
        payload = {
                "title": title,
                "message": message
            }
        r = requests.post(BASE_URL + ":" + PORT + "/" + ENDPOINT, json=payload)
        try:
            data = r.json()
            self.assertEqual(int(data['code']), 200)
        except:
            self.assertTrue(False)

    def test_get_note(self):
        r = requests.post(BASE_URL + ":" + PORT + "/" + ENDPOINT)
        try:
            data = r.json()
            self.assertGreater(len(data), 0)
        except:
            self.assertTrue(False)

    def test_get_title(self):
        payload = {
                "title": title
            }
        r = requests.post(BASE_URL + ":" + PORT + "/" + ENDPOINT, json=payload)
        try:
            data = r.json()
            self.assertEqual((data['title']), title)
            self.assertEqual((data['message']), message)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
