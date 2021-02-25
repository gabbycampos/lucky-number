from flask import Flask, render_template, request, jsonify
from random import randint 
from forms import UserForm
import requests
from wtforms.validators import ValidationError
import wtforms_json
wtforms_json.init()

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=["POST"])
def create_user():
    """ Creates user from form and returns JSON """
    #input_json = request.get_json(force=True) 

    number = randint(1,100)
    year = request.json['year']
    num = requests.get(f"http://numbersapi.com/{number}")
    resp_year = requests.get(f"http://numbersapi.com/{year}")

    return {
        "number": {
            "fact": f"{num.text}",
            "num": number
        },
        "year": {
            "fact": f"{resp_year.text}",
            "year": year
        }
    }
########### SOLUTION ################################
# def get_fact_for_num(num, type="trivia"):
#     """Given a number, get a fact about it from numberapi."""

#     resp = requests.get(f"http://numbersapi.com/{num}/{type}")
#     return resp.text


# @app.route("/api/get-lucky-num", methods=["POST"])
# def get_lucky_num():
#     """Get lucky num, validating input & returning info about num."""

#     received = request.json

#     form = LuckyNumberRequestForm(csrf_enabled=False, data=received)

#     if form.validate_on_submit():
#         num = randint(1, 100)
#         year = received['year']

#         return jsonify(
#             num={"num": num,
#                  "fact": get_fact_for_num(num)},
#             year={"year": year,
#                   "fact": get_fact_for_num(year, type="year")},
#         )

#     else:
#         return jsonify(errors=form.errors)

########### ANOTHER SOLUTION ########################
# @app.route('/api/get-lucky-num', methods=["POST"])
# def create_user():
#     """ Creates user from form and returns JSON """

#     formdata = request.get_json() #get JSON data

#     form = UserForm.from_json(formdata=formdata)

#     if form.validate():
#         rand_num = randint(1, 100)
#         number = requests.get(f"http://numbersapi.com/{rand_num}")
#         year = requests.get(f"http://numbersapi.com/{form.year.data}")
#         return jsonify({
#             "num": {
#                 "fact": number.text,
#                 "num": rand_num
#             },
#             "year": {
#                 "fact": year.text,
#                 "year": year.text
#             }
#         }),200
#     return jsonify(form.errors)


    # dictToReturn = {'color':input_json['color'], 'email':input_json['email'], 'name':input_json['name'], 'year':input_json['year']}
    # return jsonify(dictToReturn)




