from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Menu with safe keys (no spaces), matching image filenames
MENU = {
    "Coffee": 50,
    "Tea": 30,
    "Burger": 90,
    "Fries": 40,
    "Sandwich": 70,
    "Pizza": 120,
    "Brownie": 60,
    "Water_Bottle": 20  # Use underscore here
}

@app.route('/')
def home():
    return render_template("index.html", menu=MENU)

@app.route('/bill', methods=['POST'])
def bill():
    selected_items = {}
    total = 0

    for item, price in MENU.items():
        quantity = request.form.get(item)
        if quantity and quantity.isdigit() and int(quantity) > 0:
            qty = int(quantity)
            selected_items[item] = {
                "price": price,
                "quantity": qty,
                "subtotal": qty * price
            }
            total += qty * price

    return render_template("bill.html", items=selected_items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
