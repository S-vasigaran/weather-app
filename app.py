from flask import Flask, render_template, request
from datetime import datetime
import weather_app as wa

app = Flask(__name__)

@app.template_filter('datefmt')
def datefmt(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%a, %d %b")

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = wa.get_current_weather(city)
        forecast = wa.get_5day_forecast(city)
    return render_template("index.html", weather=weather, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)
