# app.py
from flask import Flask, render_template
import requests
import json


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    github_app = "https://github.com/evanesoteric/nordvpn-geolocator"
    github_website = "https://github.com/evanesoteric/nordvpn-geolocator-website"
    last_updated_url = requests.get('https://raw.githubusercontent.com/evanesoteric/nordvpn-geolocate/main/last_updated.txt')
    last_updated = last_updated_url.text
    if last_updated_url.status_code == 404:
        last_updated = "Error loading"
    vpns_url = requests.get('https://raw.githubusercontent.com/evanesoteric/nordvpn-geolocate/main/vpns.json')
    vpns = json.loads(vpns_url.text)
    return render_template('index.html', vpns=vpns, github_app=github_app, github_website=github_website, last_updated=last_updated)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
