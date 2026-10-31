from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    name = request.form.get("name")
    gender = request.form.get("gender")
    employee_type = request.form.get("employee_type")
    hours_worked = float(request.form.get("hours_worked"))
    hourly_rate = float(request.form.get("hourly_rate"))

    normal_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    normal_pay = normal_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5

    gross_pay = normal_pay + overtime_pay

    if employee_type == "full_time":
        tax = gross_pay * 0.15
    elif employee_type == "part_time":
        tax = gross_pay * 0.10

    if gender == "female":
        deduction = gross_pay * 0.05
    else:
        deduction = 0

    net_pay = gross_pay - tax - deduction

    # Temporary output for testing
    print("Normal Pay:", normal_pay)
    print("Overtime Pay:", overtime_pay)
    print("Gross Pay:", gross_pay)
    print("Tax:", tax)
    print("Further Deduction:", deduction)
    print("Net Pay:", net_pay)

    return render_template(
        "index.html",
        name=name,
        gender=gender,
        employee_type=employee_type,
        hours_worked=hours_worked,
        normal_pay=normal_pay,
        overtime_pay=overtime_pay,
        gross_pay=gross_pay,
        tax=tax,
        deduction=deduction,
        net_pay=net_pay
    )

if __name__ == "__main__":
    app.run(debug=True)

