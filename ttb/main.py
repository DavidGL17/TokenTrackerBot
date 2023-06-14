from .utils import get_access_token, get_token_price
from .settings import client_id, client_secret, region


def main():
    print(get_token_price(get_access_token(client_id, client_secret)["access_token"], region))


if __name__ == "__main__":
    main()
