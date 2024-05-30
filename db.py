import streamlit as st
from sqlalchemy import text

conn = st.connection("postgresql")


def update_btf(book_id, user_id=None, title=None, exclude=None):
    params = {"book_id": int(book_id)}
    values_string = ""
    if title:
        values_string += " title=:title"
        params.update({"title": str(title)})
    if exclude:
        values_string += " exclude=:exclude"
        params.update({"exclude": str(exclude)})
    if user_id:
        values_string += " user_id=:user_id"
        params.update({"user_id": int(user_id)})
    with conn.session as s:
        s.execute(
            text("UPDATE books_1 SET" + values_string + " WHERE id=:book_id;"),
            params=params,
        )
        s.commit()


def delete_btf(book_id):
    with conn.session as s:
        s.execute(
            text(f"DELETE from books_1  WHERE id=:{book_id};"),
        )
        s.commit()


def add_btf(user_id=None, title=None, exclude=None):
    with conn.session as s:
        s.execute(
            text(
                "INSERT INTO books_1  VALUES (title=:title, user_id=:user_id, excluded=:excluded);"
            ),
            params=dict(user_id=user_id, title=title, excluded=exclude),
        )
        s.commit()


def get_btf():
    btf = conn.query("SELECT * FROM books_1")
    return btf
