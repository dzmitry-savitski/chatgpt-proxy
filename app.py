import json
import os

import openai
from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth

from crypto import decrypt, encrypt

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    os.environ["AUTH_USER"]: os.environ["AUTH_PASSWORD"]
}

encr_password = os.environ["ENCR_PASSWORD"]
openai.api_key = os.environ["OPENAI_API_KEY"]


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route("/")
@auth.login_required
def index():
    return render_template("index.html", encr_password=encr_password)


@app.route("/m", methods=["POST"])
@auth.login_required
def api():
    decrypted_message = decrypt(request.data, encr_password.encode())
    print(decrypted_message)
    messages = json.loads(decrypted_message)
    completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.model_dump_json())
    encrypted_reply = encrypt(completion.model_dump_json().encode(), encr_password.encode())
    return {"message": encrypted_reply.decode()}


if __name__ == '__main__':
    app.run()
