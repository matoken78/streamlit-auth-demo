import csv
import yaml
from pathlib import Path

from streamlit_authenticator.utilities.hasher import Hasher

from app.auth.auth_util import get_auth_path

users_csv_path = Path(__file__).parent.parent / "data" / "userinfo.csv"
config_yaml_path = get_auth_path()

## Read user setting list
with users_csv_path.open(mode="r") as f:
    csvreader = csv.DictReader(f)
    users = list(csvreader)

## Read yaml setting
with config_yaml_path.open(mode="r") as f:
    yaml_data = yaml.safe_load(f)

## Hash password
users_dict = {}
for user in users:
    user["password"] = Hasher().hash(user["password"])
    one_user_dict = {
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
        "admin": int(user["admin"]) == 1,
    }
    users_dict[user["id"]] = one_user_dict

## Write yaml
yaml_data["credentials"]["usernames"] = users_dict
with open(config_yaml_path, "w") as f:
    yaml.dump(yaml_data, f)
    print("Completed")
