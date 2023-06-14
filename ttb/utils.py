import base64
import requests
from typing import Dict, Tuple
import datetime
from .constants import TOKEN_URLS, OAUTH_US_HOST


def get_access_token(client_id: str, client_secret: str) -> Dict[str, str]:
    """
    Get an access token from the Blizzard API

    :return: A dictionary containing the access token
    """
    basic_auth: str = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    body_data: Dict[str, str] = {"grant_type": "client_credentials", "scope": "wow.profile openid"}

    try:
        token_resp = requests.post(
            f"{OAUTH_US_HOST}/token",
            data=body_data,
            headers={"Authorization": f"Basic {basic_auth}", "Content-Type": "application/x-www-form-urlencoded"},
        )

        if token_resp.ok:
            return token_resp.json()
        else:
            return {"err": "no token resp 1"}

    except requests.exceptions.RequestException:
        return {"err": "no token resp 2"}


# return the datetime of the last token update and the price
def get_token_price(access_token: str, region: str) -> Tuple[int, datetime.datetime]:
    token_url = TOKEN_URLS.get(region.lower())
    if token_url is None:
        raise ValueError(f"Invalid region: {region}")

    response = requests.get(f"{token_url}&access_token={access_token}", headers={"Accept": "application/json"})

    if response.ok:
        gold_price = response.json()["price"] / 100 / 100
        date = datetime.datetime.fromtimestamp(response.json()["last_updated_timestamp"] / 1000)
        return gold_price, date
    else:
        return -10000, datetime.datetime.fromtimestamp(0)
