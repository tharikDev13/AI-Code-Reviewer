import jwt
import time
import requests


APP_ID = "3938627"

INSTALLATION_ID = "137413560"

PRIVATE_KEY_PATH = (
    "Keys/ai-code-reviewer01.2026-06-02.private-key.pem"
)


def generate_jwt():

    with open(
        PRIVATE_KEY_PATH,
        "r"
    ) as pem_file:

        private_key = pem_file.read()

    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": APP_ID
    }

    encoded_jwt = jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )

    return encoded_jwt


def generate_installation_token():

    jwt_token = generate_jwt()

    url = (
        "https://api.github.com/app/installations/"
        f"{INSTALLATION_ID}/access_tokens"
    )

    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        url,
        headers=headers
    )

    response.raise_for_status()

    data = response.json()

    return data["token"]