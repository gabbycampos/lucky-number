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

    formdata = request.get_json() #get JSON data

    form = UserForm.from_json(formdata=formdata)

    if form.validate():
        rand_num = randint(1, 100)
        number = requests.get(f"http://numbersapi.com/{rand_num}")
        year = requests.get(f"http://numbersapi.com/{form.year.data}")
        return jsonify({
            "num": {
                "fact": number.text,
                "num": rand_num
            },
            "year": {
                "fact": year.text,
                "year": year.text
            }
        }),200
    return jsonify(form.errors)



    #name = request.json["name"]
    # email = request.json["email"]
    #year = request.json["year"]
    # color = request.json["color"]

    # rand_num = random.randint(1, 100)
    # result_num = requests.get(f"http://numbersapi.com{rand_num}")
    # result_year = requests.get(f"http://numbersapi.com{year}")

    # new_user = User(name=name, email=email, year=year, color=color, rand_num=rand_num, result_num=result_num, result_year=result_year)
    # db.session.add(new_user)
    # db.session.commit()
    # serialized = serialize_dessert(new_user)

    # return (jsonify(user=serialized), 201)
    
    #return jsonify(data)
    # return {
    #     "num": {
    #         "fact": f"{result_num.text}",
    #         "num": rand_num
    #     },
    #     "year": {
    #         "fact": f"{result_year.text}",
    #         "year": year
    #     }
    # }