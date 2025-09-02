from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return send_from_directory("static", "Thakur_Suryaveer_Resume.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
