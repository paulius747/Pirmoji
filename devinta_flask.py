from flask import Flask,render_template   ## sukuriam maza puslapi

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/zmones")
def zmones():
    return render_template("login.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)                 ## sukuriam maza puslapi