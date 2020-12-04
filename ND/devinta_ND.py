from flask import Flask,render_template

app =Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/zmones")
def home():
    vardai = ['Jonas', 'Antanas', 'Petras']
    return render_template("index.html", sarasas=vardai)





if __name__ =="__main__":
    app.run()




