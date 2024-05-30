from pydantic import BaseModel


class BookInput(BaseModel):
    book_id: int
    image: str | None = None
    title: str
    price: int | None = None

    @classmethod
    def from_args(cls, book_id: str, image: str, title: str, price: str):
        return cls(book_id=book_id, image=image, title=title, price=price)


books = [
    BookInput.from_args(
        1,
        "https://ireland.apollo.olxcdn.com/v1/files/zo5fbkpyq7le3-UA/image;s=1000x700",
        "Генри Марш Не навреди",
        300,
    ),
    BookInput.from_args(
        2,
        "https://ireland.apollo.olxcdn.com/v1/files/1bkzo955u3h42-UA/image;s=1000x700",
        "Збірник рецептів «швидко, просто, смачно»",
        190,
    ),
    BookInput.from_args(
        3,
        "https://ireland.apollo.olxcdn.com/v1/files/hkkp29avoep21-UA/image;s=1000x700",
        "Грицько Чупринка",
        200,
    ),
    BookInput.from_args(
        4,
        "https://ireland.apollo.olxcdn.com/v1/files/egc05fpkq80v-UA/image;s=1000x700",
        'Продам книжку" Кобзарик"',
        200,
    ),
    BookInput.from_args(
        5,
        "https://ireland.apollo.olxcdn.com/v1/files/i1omhths221p-UA/image;s=1000x700",
        "Одна істинна королева, Дженніфер Бенкау. Нова",
        330,
    ),
    BookInput.from_args(
        6,
        "https://ireland.apollo.olxcdn.com/v1/files/cw90m13iadle1-UA/image;s=1000x700",
        "Марсело Фигерас «Камчатка»",
        150,
    ),
]
