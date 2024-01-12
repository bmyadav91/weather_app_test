from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods = ["POST"])
def weatherapp():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': request.form.get("city"),
        'units' : request.form.get("units"),
        'appid' : request.form.get("appid")
    }
    data = requests.get(url, params)
    city = data["cityt"]
    datajson = data.json()
    return f"{datajson} city: {city}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)