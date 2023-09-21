from flask import Flask, request  # object
import base64


app = Flask(__name__)

HOSTNAME = "http://127.0.0.1:5000/"


@app.route('/')  # decorator adds additional functionality
def home():
    return '<h1>URL Shortner hello</h1>'


# only accepting post request, acceps the list
@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['longURL']
    encoded = base64.urlsafe_b64encode(long_url.encode())
    suffix = encoded.decode()[:5]
    short_URL = HOSTNAME + suffix
    print(suffix)
    print(long_url)
    print(short_URL)
    return {"shortURL": short_URL}
