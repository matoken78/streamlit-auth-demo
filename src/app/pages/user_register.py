import streamlit as st
from app.auth.auth_util import get_authenticator, add_user

auth = get_authenticator()


def register():
    user_id = st.text_input("ログインIDを選択してください")
    name = st.text_input("ユーザー名を選択してください")
    password = st.text_input("パスワードを選択してください", type="password")
    email = st.text_input("メールアドレスを入力してください")
    admin = st.checkbox("管理者権限を付与する")
    if st.button("登録"):
        can_add = add_user(user_id, name, password, email, admin)
        if can_add:
            st.success("登録しました。ログインしてください。")
        else:
            st.error("そのログインIDは既に使われています。")


register()
