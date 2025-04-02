from flask import Flask, request, url_for, render_template, redirect
from stairs import stairs

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number_steps = stairs(request.form["steps"])
        return redirect(url_for("show_stairs", number_steps=number_steps))
    return render_template("index.html")

@app.route("/stais")
def show_stairs():

    return 

if __name__ == '__main__':
    app.run(debug=True)
