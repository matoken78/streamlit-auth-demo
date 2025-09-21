import os
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth
from dotenv import load_dotenv

from app.auth.auth_util import get_authenticator

load_dotenv(Path(__file__).parent.parent / ".env")

auth = get_authenticator()
