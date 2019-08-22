from flask import Flask, escape, request, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    print(request.cookies)
    name = request.args.get("name", "World")
    resp = make_response(f'Hello, {escape(name)}!')
    resp.set_cookie("foo", name)
    return resp
