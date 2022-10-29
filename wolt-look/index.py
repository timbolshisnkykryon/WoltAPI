import json

from flask import Flask, request, session
from flask_session import Session
from main import Wolt

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'BAD_SECRET_KEY'

Session(app)


def success_response(json_body: dict):
    return app.response_class(
        response={
            json.dumps(json_body)
        },
        status=200,
        mimetype='application/json'
    )


def fail_response(error_message: str):
    return app.response_class(
        response={
            json.dumps({"error": error_message})
        },
        status=500,
        mimetype='application/json'
    )


@app.route("/setup", methods=['POST'])
def setup_search():
    location = request.args.get('location')
    w = Wolt(address=location)
    if w.ready:
        session['search_object'] = vars(w)
        return success_response({'place_id': w.place_id,
                                 'lat_lan': w.lat_lan})
    return fail_response(w.error)


@app.route("/search", methods=['GET'])
def search_product():
    product = request.args.get('q')
    if session.get('search_object'):
        w = Wolt(lat_lan=session.get('search_object')['lat_lan'])
    else:
        location = request.args.get('location')
        w = Wolt(address=location)

    search_results = w.search_for_product(product_name=product)
    if search_results:
        return success_response(search_results)
    return fail_response("Could not retrieve items from search")

@app.route("/filter-search", methods=['GET'])
def filtered_search_product():
    product = request.args.get('q')
    if session.get('search_object'):
        w = Wolt(lat_lan=session.get('search_object')['lat_lan'])
    else:
        location = request.args.get('location')
        w = Wolt(address=location)

    search_results = w.filtered_search_for_product(product_name=product,
                                                   filters=json.loads(request.form["filters"]))
    if search_results:
        return success_response(search_results)
    return fail_response("Could not retrieve items from search")

app.run(debug=True)
