#!/usr/bin/env python3
from Flask import Flask, jsonify, request
from werkzeug.security import generate_passwod_hash as generate, check_password_hash as check
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
        "user1": {"username": "user1", "password": generate("password"), "role": "user"},
        "admin1": {"username": "admin1", "password": generate("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check(user['password'], password):
        return username

@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized accedd"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(identity=user['username'], additional_claims={"role": user['role']})
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# -----------------
# JWT Error Handlers (return 401 for auth errors)
# -----------------

@jwt.unauthorized_loader
def unauthorized_callback(err_str):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(err_str):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# -----------------
# Run the app
# -----------------
if __name__ == '__main__':
    app.run(debug=True)

