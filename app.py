
from flask import Flask, render_template, request,redirect, url_for,session
import sqlite3
app = Flask(__name__)
app.secret_key = "technatics"

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/base")
def base():
    return render_template("base.html")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")
@app.route("/intro")
def intro():
    return render_template("intro.html")
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        conn = sqlite3.connect("darkside.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        return redirect(url_for("contact"))
    
    return render_template("contact.html")  
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        password = request.form["password"]
        print("Password entered:", password)

        if password == "Darkside123":
            print("LOGIN SUCCESS")
            session["admin"] = True
            print(session)
            return redirect(url_for("admin"))
        else:
            return "Invalid password. Please try again."

    return render_template("admin_login.html") 

@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect("darkside.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    messages = cursor.fetchall()

    conn.close()

    return render_template("admin.html", messages=messages)
@app.route("/flasky")
def flasky():
    return render_template("flasky.html")
@app.route("/flask-dashboard")
def flask_dashboard():
    return render_template("flask_dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)