import streamlit as st
from book_list import books


st.set_page_config(layout="wide")
st.markdown(
    '<style>[data-testid="column"] img {width:100%}</style>', unsafe_allow_html=True
)


def bought(id):
    st.toast([i for i in books if i.book_id == id][0])


title = st.sidebar.selectbox("Restaurants", ["Rest1", "Resta2"])

with st.container(border=True):
    row1 = st.columns(3)
    for row, book in zip(row1, books[:3]):
        with row:
            with st.container(
                border=True,
            ):
                st.markdown(
                    f"[![Foo]({book.image})](http://192.168.0.103:8501/book?id={book.book_id})"
                )
                st.link_button(
                    book.title, f"http://192.168.0.103:8501/book?id={book.book_id}"
                )
                st.markdown(book.price, unsafe_allow_html=True)
                if st.button("Купити", key=book.book_id):
                    bought(book.book_id)
    row1 = st.columns(3)
    for row, book in zip(row1, books[3:6]):
        with row:
            with st.container(border=True):
                st.image(book.image, use_column_width=True)
                st.markdown(book.title, unsafe_allow_html=True)
                st.markdown(book.price, unsafe_allow_html=True)
                if st.button("Купити", key=book.book_id):
                    bought(book.book_id)
