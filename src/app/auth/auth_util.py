import yaml
from pathlib import Path
from yaml.loader import SafeLoader

from streamlit_authenticator import Authenticate
from streamlit_authenticator.utilities.hasher import Hasher


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


def add_user(user_id: str, name: str, password: str, email: str, admin: bool) -> bool:
    auth_path = get_auth_path()
    with auth_path.open() as file:
        config = yaml.load(file, Loader=SafeLoader)

    if user_id in config["credentials"]["usernames"]:
        return False

    new_user = {
        "name": name,
        "password": Hasher().hash(password),
        "email": email,
        "admin": admin,
    }
    config["credentials"]["usernames"][user_id] = new_user

    with auth_path.open("w") as file:
        yaml.dump(config, file)

    return True
