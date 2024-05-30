
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")

conn = st.connection("gsheets", type=GSheetsConnection)
st.markdown(
    '<style>[data-testid="column"] img {width:100%}</style>', unsafe_allow_html=True
)

df = conn.read(
    worksheet="All",
    ttl="10m",
    usecols=[0, 1, 2, 3, 4, 5],
    nrows=482,
)
col = 0
columns = st.columns(5)
for ind, book_tuple in df.iterrows():
    book = dict(book_tuple)
    with columns[col]:
        with st.container(border=True):
            name = book["Назва"]
            join_name = "_".join(name.split())
            filename = "_".join(name.split()) + ".jpg"
            # st.image(f'.app/static/{filename}.jpg', use_column_width=True)
            st.markdown(
                f"[![Click me](app/static/{filename})](http://192.168.0.103:8501/book?name={join_name}&price={int(book['Купівля'])})"
            )

            st.write(name)
            st.write(f"Ціна: {int(book['Купівля'])} грн")
    col += 1
    if col == 5:
        col = 0
        columns = st.columns(5)

st.dataframe(df)
