import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "employees.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def home():
    employees = None
    if request.form:
        try:
            employee = Employee(name=request.form.get("name"))
            db.session.add(employee)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    employees = Employee.query.all()
    return render_template("home.html", employees=employees)


@app.route("/update", methods=["POST"])
def update():
    try:
        new = request.form.get("new")
        old = request.form.get("old")
        employee = Employee.query.filter_by(name=old).first()
        employee.name = new
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    employee = Employee.query.filter_by(name=name).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")


class Employee(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Name: {}>".format(self.name)


if __name__ == "__main__":
    app.run(debug=True)
