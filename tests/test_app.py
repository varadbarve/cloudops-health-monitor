import unittest
from unittest.mock import patch

from app import check_website


class TestHealthMonitor(unittest.TestCase):

    @patch("app.urllib.request.urlopen")
    def test_healthy_website(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.status = 200

        result = check_website("https://example.com")

        self.assertTrue(result["healthy"])
        self.assertEqual(result["status"], 200)

    @patch("app.urllib.request.urlopen")
    def test_unhealthy_website(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.status = 503

        result = check_website("https://example.com")

        self.assertFalse(result["healthy"])
        self.assertEqual(result["status"], 503)


if __name__ == "__main__":
    unittest.main()