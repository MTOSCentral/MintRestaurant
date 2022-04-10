from datetime import datetime
from classes import *
from flask import Flask, redirect, Markup, url_for, render_template, request, session, flash, send_file, abort
import random
import string
app = Flask(__name__)
codes = {1: 'ABC'}
tbobj = {1: Table(10, "10:04", [])}
cat = [Catergory(0, "Some Test Catergory", ("06:00", "24:00"))]
foods = [Food(0, "Some Random Food", 0, 20, Options([Option("Choose An Object", [
              Selection("Some Rice", 20, 1), Selection("Some Rice2", 20, 1)], 1, 0),Option("Choose An Object2", [
              Selection("Some Rice", 20, 1), Selection("Some Rice2", 20, 1)], 1, 0)])), ]
tables = 20
app.secret_key = "ThEMoSTSeCuRePassWORdINThEWorLD"


def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]


def now():
    return datetime.strftime(datetime.now(), "%H:%M")


app.jinja_env.globals.update(is_between=is_between)
app.jinja_env.globals.update(now=now)


@app.route('/')
def home():
    return "Home"


@app.route('/table/<table>')
def table(table: int):
    table = int(table)
    if table in codes:
        return redirect(url_for("order", secure=codes[table]))
    else:
        if table > tables or table <= 0:
            return "Table Wrong"
        else:
            letters = string.ascii_letters
            letters = letters+string.digits
            codes[table] = ''.join(random.choice(letters) for i in range(128))
            tbobj[table] = Table(1, "00:00", [])
            return redirect(url_for("order", secure=codes[table]))


@app.route('/order/<secure>')
def order(secure):
    valid = False
    tableid = ""
    for code in codes:
        if codes[code] == secure:
            valid = True
            tableid = code
        else:
            pass
    if valid == True:
        return render_template("list.html", cater=cat, foods=foods)
    else:
        abort(404)


@app.route('/food/<fid>')
def food(fid):
    if int(fid) > len(foods) - 1:
        abort(404)
    else:
        return render_template("food.html", food=foods[int(fid)])


if __name__ == "__main__":
    app.run(port=8888, debug=True, host="0.0.0.0")
