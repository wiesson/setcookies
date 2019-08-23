from flask import Flask, escape, request, make_response

app = Flask(__name__)

def update_visits(visit = 0):
    try:
        return int(visit) + 1
    except ValueError:
        return 0
    except:
        return 0


@app.route('/')
def hello():
    #  log request cookies to console
    print(request.cookies)
    visits = update_visits(request.cookies.get('page_visits'))
    name_from_request = request.args.get("name", "stranger")
    resp = make_response(f'Hello {escape(name_from_request)}, you have visited this page {escape(visits)} times!')
    resp.set_cookie("page_visits", str(visits))
    resp.set_cookie("evil_tracking_cookie", name_from_request)
    return resp
