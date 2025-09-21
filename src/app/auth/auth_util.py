import yaml
from pathlib import Path
from yaml.loader import SafeLoader

from streamlit_authenticator import Authenticate


def get_auth_path() -> Path:
    return Path(__file__).parent.parent / "data" / "config.yaml"


def get_authenticator() -> Authenticate:
    auth_path = get_auth_path()
    with auth_path.open() as file:
        config = yaml.load(file, Loader=SafeLoader)

        return Authenticate(
            credentials=config["credentials"],
            cookie_name=config["cookie"]["name"],
            cookie_key=config["cookie"]["key"],
            cookie_expiry_days=config["cookie"]["expiry_days"],
        )
