import streamlit as st
from app.auth.auth_util import get_authenticator

auth = get_authenticator()


def protected():
    if st.session_state.get("authentication_status"):
        # 認証済みユーザーのみ表示
        st.write("This is a protected route.")
    else:
        st.warning("ログインしてください。")


def login():
    auth.login()
    print(st.session_state)
    if st.session_state["authentication_status"]:
        ## ログイン成功
        with st.sidebar:
            st.markdown(f"## Welcome *{st.session_state['name']}*")
            auth.logout("Logout", "sidebar")
            st.divider()
        st.write("# ログインしました!")

    elif st.session_state["authentication_status"] is False:
        ## ログイン成功ログイン失敗
        st.error("Username/password is incorrect")

    elif st.session_state["authentication_status"] is None:
        ## デフォルト
        st.warning("Please enter your username and password")


def register():
    username = st.text_input("ユーザー名を選択してください")
    password = st.text_input("パスワードを選択してください", type="password")
    if st.button("登録"):
        pass


login()
