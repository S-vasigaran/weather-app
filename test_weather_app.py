import unittest
from unittest.mock import patch, MagicMock
from weather_app import get_current_weather, get_5day_forecast, display_current_weather


MOCK_CURRENT = {
    "name": "Chennai",
    "sys": {"country": "IN"},
    "main": {"temp": 32.5, "feels_like": 36.0, "humidity": 75},
    "weather": [{"description": "broken clouds"}],
    "wind": {"speed": 4.2},
    "visibility": 8000
}

MOCK_FORECAST = {
    "list": [
        {
            "dt_txt": "2024-06-01 12:00:00",
            "main": {"temp": 33.0, "humidity": 70},
            "weather": [{"description": "clear sky"}]
        },
        {
            "dt_txt": "2024-06-02 12:00:00",
            "main": {"temp": 31.5, "humidity": 78},
            "weather": [{"description": "light rain"}]
        }
    ]
}


class TestWeatherApp(unittest.TestCase):

    @patch("weather_app.requests.get")
    def test_get_current_weather_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_CURRENT
        mock_get.return_value = mock_response

        result = get_current_weather("Chennai")
        self.assertEqual(result["name"], "Chennai")
        self.assertEqual(result["main"]["temp"], 32.5)

    @patch("weather_app.requests.get")
    def test_get_5day_forecast_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_FORECAST
        mock_get.return_value = mock_response

        result = get_5day_forecast("Chennai")
        self.assertIn("list", result)
        self.assertEqual(len(result["list"]), 2)

    def test_display_current_weather_runs(self):
        # Should print without raising any exceptions
        try:
            display_current_weather(MOCK_CURRENT)
        except Exception as e:
            self.fail(f"display_current_weather raised an exception: {e}")

    @patch("weather_app.requests.get")
    def test_invalid_city_raises_http_error(self, mock_get):
        import requests
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            response=MagicMock(status_code=404)
        )
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_current_weather("InvalidCityXYZ")


if __name__ == "__main__":
    unittest.main()
