import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "employees.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    name = Employees(name=request.form.get("name"))
    phone = Employees(phone=request.form.get("phone"))
    email = Employees(email=request.form.get("email"))
    db.session.add_all([name, phone, email])
    db.session.commit()
    return render_template("employees.html")


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __repr__(self):
        return "<Employee Details:{}>".format(self.name, self.phone, self.email)


# return "<Name: {}>".format(self.name), "<Phone: {}>".format(self.phone), "<Email: {}>".format(self.email)


if __name__ == "__main__":
    app.run(debug=True)
