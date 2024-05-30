import requests
import streamlit as st
from streamlit_timeline import st_timeline
import altair as alt
from datetime import datetime, time
from urllib import request
from pydantic import BaseModel
from typing import List
from st_pages import Page, Section, show_pages, add_page_title, hide_pages
from book_list import books
st.set_page_config(layout="wide")

columns = st.columns([.3,.7])
book_name = st.query_params.get('name')
if not book_name:
    st.switch_page('main.py')
price = st.query_params.get('price')
with columns[0]:
    st.header('Book')
    st.write(book_name)
    filename = "_".join(book_name.split()) + '.jpg'
    st.markdown(
        f'<img src="./app/static/{filename}" height="333" style="border: 5px solid orange">',
        unsafe_allow_html=True,
    )
    if st.button(f'Купити: {price} грн'):
        st.toast('куплено')

with columns[1]:
    text = '''ljkh;uhdf;he
    uiygeifygowehfdguitelsd
    ui helw fg iuhe; ruiwhuu'''
    st.write(text)


