from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "John Doe"}]
    return jsonify(users)

if __name__ == "__main__":
    app.run(port=5001)