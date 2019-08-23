from flask import Flask, escape, request, make_response
from datetime import datetime

app = Flask(__name__)


def update_visits(visit=0):
    try:
        return int(visit) + 1
    except ValueError:
        return 1
    except:
        return 1


@app.route('/')
def hello():
    #  log request cookies to console
    print(request.cookies)
    visits = update_visits(request.cookies.get('visits'))
    last_visit = request.cookies.get('last_visit')
    name_from_request = request.args.get("name", "stranger")

    hello_text = f'Hello {escape(name_from_request)}, you have visited this page {escape(visits)} times!'
    last_visit_text = f' Your last visit was on {escape(last_visit)}' if last_visit else ''

    resp = make_response(hello_text + last_visit_text)
    resp.set_cookie("visits", str(visits))
    resp.set_cookie("last_visit", str(datetime.now().isoformat()))
    return resp
