from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "keepitsecret" 

@app.route('/')
def index():
    
    if "visits" not in session:
        session ["visits"] = 0
    session ["visits"] =+1
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
