from flask import Flask, jsonify, request, abort

app = Flask(__name__)

API_KEY = "0a7f023c8cf0a211ded0cc3185b793d469ceffe88e1d25daf91598e2e0089ca1"  # Change this to something unique

@app.route('/api/private', methods=['GET'])
def private():
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        abort(401)
    return jsonify({"message": "Hello from private API!"})

if __name__ == '__main__':
    app.run()
