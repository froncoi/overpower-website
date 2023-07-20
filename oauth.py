import requests


class Oauth:
    client_id = "1090971580357673084"
    client_secret = "xCvDJDbFEE5j4a9uciECuliD-GwdLsvG"
    redirect_uri = "http://127.0.0.1:5000/login"
    scope = "guilds.join%20email%20guilds%20identify"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=1090971580357673084&redirect_uri=https%3A%2F%2Fdiscord.gg%2FE4vnewmZ33&response_type=code&scope=guilds.join%20email%20guilds%20identify"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_invite_url = "https://discord.com/api/oauth2/authorize?client_id=1090971580357673084&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FE4vnewmZ33&scope=bot"
    discord_api_url = "https://discord.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }
        access_token = requests.post(url=Oauth.discord_token_url, data=payload).json()
        return access_token.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}

        user_object = requests.get(url=url, headers=headers).json()
        return user_object
