from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

@app.route("/calculate", methods=["POST"])
def calculate():
    tv_type = request.form.get("tv_type")
    price = float(request.form.get("price"))
    quantity = int(request.form.get("quantity"))
    address = request.form.get("address")
    kilometers = float(request.form.get("kilometers"))

    delivery_fee = kilometers * 10

    total = (price * quantity) + delivery_fee

    return render_template(
        "index.html",
        tv_type=tv_type,
        price=price,
        quantity=quantity,
        address=address,
        kilometeres=kilometers,
        delivery_fee=delivery_fee,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)