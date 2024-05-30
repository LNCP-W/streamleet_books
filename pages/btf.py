import streamlit as st
from db import get_btf, update_btf, delete_btf

st.set_page_config(layout="wide")
ss = st.session_state


def change():
    for i, changes in ss.ed["edited_rows"].items():
        book_id = ss.edited_df[ss.edited_df.index == i].iloc[0].id
        update_btf(int(book_id), **changes)
    for i in ss.ed["deleted_rows"]:
        book = ss.edited_df[ss.edited_df.index == i].iloc[0]
        delete_btf(int(book.id))



with st.container(border=True):
    btf = get_btf()
    ss.edited_df = st.data_editor(
        btf,
        num_rows="dynamic",
        use_container_width=True,
        on_change=change,
        key="ed",
        hide_index=True,
    )
