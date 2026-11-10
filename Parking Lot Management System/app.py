from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

parking_rates = {
    "lockup garage": 20,
    "under cover": 15,
    "open bay": 10
}

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

@app.route("/calculate", methods=["POST"])
def calculate():

    registration = request.form.get("registration")
    parking_type = request.form.get("parking_type")
    time_in = request.form.get("time_in")
    time_out = request.form.get("time_out")

    if parking_type not in parking_rates:
        return render_template(
            "index.html",
            error = "Please select a valid parking type."
        )

    try:
        start_time = datetime.strptime(time_in, "%H:%M")
        end_time = datetime.strptime(time_out, "%H:%M")

        duration = end_time - start_time

        #handle parking that continues past midnight
        if duration.total_seconds() < 0:
            duration += timedelta(days=1)

        # Check parking duration is greater than zero
        if duration.total_seconds() == 0:
            return render_template(
                "index.html",
                error = "Time-out must be different must Time-in"
            )

        duration_hours = duration.total_seconds() / 3600

        hourly_rate = parking_rates[parking_type]

        parking_cost = duration_hours * hourly_rate

        #Display parking slip
        return render_template(
            "result.html",
            registration=registration,
            parking_type=parking_type,
            duration_hours=duration_hours,
            parking_cost=parking_cost
        )

    except (ValueError, TypeError) as e:
        print("ERROR:", e)

        return render_template(
            "index.html",
            error = "Please enter valid parking information"
        )

if __name__ == "__main__":
    app.run(debug=True)