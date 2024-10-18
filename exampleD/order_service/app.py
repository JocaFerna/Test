from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [{"order_id": 101, "user_id": 1, "product": "Laptop"}]
    return jsonify(orders)

if __name__ == "__main__":
    app.run(port=5002)