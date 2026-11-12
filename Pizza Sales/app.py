from flask import Flask, render_template, request
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

pizza_prices = {
    "veg": Decimal(11.99),
    "chicken": Decimal(14.99)
}

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        cash = request.form.get("cash")
        pizza_type = request.form.get("pizza_type")
        quantity = request.form.get("quantity")

        try:
            cash = Decimal(cash)

            if not cash.is_finite() or cash <= 0:
                raise ValueError("Enter a valid cash amount.")

            if pizza_type not in pizza_prices:
                raise ValueError("Please select a pizza type.")

            quantity = int(quantity)

            if quantity < 1 or quantity > 5:
                raise ValueError("Quantity must be between 1 and 5")

            amount_spent = pizza_prices[pizza_type] * quantity

            if cash < amount_spent:
                raise ValueError("Insufficient cash for this purchase.")

            change = cash - amount_spent

        except (InvalidOperation, ValueError, TypeError):

            return render_template(
                "index.html",
                error = "Please enter valid information and try again."
            )

        return render_template(
            "index.html",
            amount_spent=f"R{amount_spent:.2f}",
            change=f"{change:.2f}"
        )

    return render_template(
        "index.html"
    )

if __name__ == "__main__":
    app.run(debug=True)