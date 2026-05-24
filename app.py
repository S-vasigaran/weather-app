from flask import Flask, render_template, request
import weather_app as wa

app = Flask(__name__)

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
