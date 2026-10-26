
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Update these settings for your MySQL server
DB_CONFIG = {
    "host": "localhost",
    "user": "flaskuser",
    "password": "FlaskPass123!",
    "database": "employee_data"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form.get("employee_name", "").strip()
        employee_id = request.form.get("employee_id", "")
        salary = request.form.get("salary", "")

        try:
            employee_id = int(employee_id)
            salary = int(salary)

            if not name or len(name) > 50:
                raise ValueError("Enter a name up to 50 characters.")

            if not 0 <= employee_id <= 99:
                raise ValueError("Employee ID must be at most two digits.")

            if not 0 <= salary <= 999999:
                raise ValueError("Salary must be at most six digits.")

            new_salary = salary * 1.05

            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()

            cursor.execute(
                """INSERT INTO employee_salary
                   (employee_name, employee_id, salary)
                   VALUES (%s, %s, %s)""",
                (name, employee_id, salary)
            )

            connection.commit()
            cursor.close()
            connection.close()

            result = {
                "employee_name": name,
                "employee_id": employee_id,
                "salary": salary,
                "new_salary": new_salary
            }

        except ValueError as error:
            return str(error), 400

    return render_template(
        "index_moncriefffe.html", result=result
    )

if __name__ == "__main__":
    app.run(debug=True, port=5002)
