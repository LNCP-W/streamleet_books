import streamlit as st

st.set_page_config(layout="wide")

columns = st.columns([0.3, 0.7])
book_name = st.query_params.get("name")
if not book_name:
    st.switch_page("main.py")
price = st.query_params.get("price")
with columns[0]:
    st.header("Book")
    st.write(book_name)
    filename = "_".join(book_name.split()) + ".jpg"
    st.markdown(
        f'<img src="./app/static/{filename}" height="333" style="border: 5px solid orange">',
        unsafe_allow_html=True,
    )
    if st.button(f"Купити: {price} грн"):
        st.toast("куплено")

with columns[1]:
    text = """ljkh;uhdf;he
    uiygeifygowehfdguitelsd
    ui helw fg iuhe; ruiwhuu"""
    st.write(text)
