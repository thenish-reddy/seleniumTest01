from flask import Flask, request, jsonify
from dependencies import get_driver
from Testcases import login_to_salesforce

app = Flask(__name__)

@app.route('/run-test', methods=['POST'])
def run_test():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    secret_key = data.get("secret_key")

    if not (username and password and secret_key):
        return jsonify({"error": "Missing required fields"}), 400

    driver = get_driver()
    try:
        login_to_salesforce(driver, username, password, secret_key)
        return jsonify({"message": "Test executed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
