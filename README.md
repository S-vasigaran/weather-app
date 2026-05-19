# 🌦 Python Weather App

A command-line weather application built with Python that integrates the **OpenWeatherMap REST API** to fetch and display real-time weather data including temperature, humidity, wind speed, and a **5-day forecast** for any city in the world.

---

## 📸 Demo

```
╔══════════════════════════════════════════╗
║        🌦  Python Weather App  🌦        ║
╚══════════════════════════════════════════╝

  Enter city name (or 'quit' to exit): Chennai

  Fetching weather data for 'Chennai'...

=============================================
  📍 Weather in Chennai, IN
=============================================
  🌡  Temperature  : 32.5°C  (Feels like 36.0°C)
  🌤  Condition    : Broken clouds
  💧 Humidity     : 75%
  💨 Wind Speed   : 4.2 m/s
  👁  Visibility   : 8 km
=============================================

  📅  5-Day Forecast
---------------------------------------------
  Saturday, 01 Jun       33.0°C  Clear sky                 💧70%
  Sunday, 02 Jun         31.5°C  Light rain                💧78%
  Monday, 03 Jun         30.0°C  Overcast clouds           💧82%
  Tuesday, 04 Jun        34.2°C  Clear sky                 💧65%
  Wednesday, 05 Jun      29.8°C  Moderate rain             💧88%
---------------------------------------------
```

---

## 🚀 Features

- 🌡 **Real-time weather** — temperature, feels-like, humidity, wind speed, visibility
- 📅 **5-day forecast** — daily summary with condition and humidity
- 🔁 **Multi-city support** — search any city in a loop without restarting
- ⚠️ **Error handling** — handles invalid cities, bad API keys, and network issues
- 🔐 **Secure config** — API key stored in `.env` file, never hardcoded

---

## 🛠 Tech Stack

| Technology             | Usage                                  |
| ---------------------- | -------------------------------------- |
| **Python 3.8+**        | Core application language              |
| **Requests**           | HTTP calls to OpenWeatherMap REST API  |
| **python-dotenv**      | Secure API key management via `.env`   |
| **OpenWeatherMap API** | Weather data source (free tier)        |
| **unittest + mock**    | Unit testing with mocked API responses |

---

## 📁 Project Structure

```
weather-app/
│
├── weather_app.py          # Main application
├── test_weather_app.py     # Unit tests
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a free API key

- Go to [https://openweathermap.org/api](https://openweathermap.org/api)
- Sign up for a free account
- Navigate to **API Keys** and copy your key

### 5. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and replace `your_api_key_here` with your actual key:

```
OPENWEATHER_API_KEY=abc123yourkeyhere
```

### 6. Run the app

```bash
python weather_app.py
```

---

## 🧪 Running Tests

```bash
python -m unittest test_weather_app.py -v
```

Expected output:

```
test_display_current_weather_runs ... ok
test_get_5day_forecast_success ... ok
test_get_current_weather_success ... ok
test_invalid_city_raises_http_error ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```

---

## 🌐 API Reference

This app uses two OpenWeatherMap endpoints:

| Endpoint             | Description                          |
| -------------------- | ------------------------------------ |
| `/data/2.5/weather`  | Current weather by city name         |
| `/data/2.5/forecast` | 5-day / 3-hour forecast by city name |

All data is fetched in **metric units** (°C, m/s).

---

## 📌 Example Cities to Try

- `Chennai` — India
- `London` — UK
- `New York` — USA
- `Tokyo` — Japan
- `Sydney` — Australia

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Vasigaran**  
📧 vasigaran2356@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/vasi-garan-723304285) | [GitHub](https://github.com/S-vasigaran)
