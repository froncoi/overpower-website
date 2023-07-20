from flask import Flask, render_template, request, session
from oauth import Oauth
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route("/")
def home():
    return render_template("index.html", discord_url=Oauth.discord_login_url, invite_url=Oauth.discord_invite_url)


@app.route("/login", methods=["GET"])
def login():
    code = request.args.get("code")
    at = Oauth.get_access_token(code)
    session["token"] = at

    user = Oauth.get_user_json(at)
    user_name, user_id = user.get("username"), user.get("discriminator")

    return f"Success, logged in as {user_name}#{user_id}"


if __name__ == "__main__":
    app.run(debug=True)
