from flask import Flask, render_template, request, jsonify
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.orders import place_order
from bot.logging_config import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/place-order", methods=["POST"])
def place_order_route():
    symbol = request.form.get("symbol")
    side = request.form.get("side")
    order_type = request.form.get("order_type")
    quantity = request.form.get("quantity")
    price = request.form.get("price")

    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        result = place_order(symbol, side, order_type, quantity, price)

        return jsonify({"success": True, "order": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)