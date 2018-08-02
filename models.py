from sqlalchemy import Column, Integer, String
from db import Base

class BookShelf(Base):
    __table_name__ = 'bookshelf'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    # FIXME 画像パスや撮影日時等を追加！

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<BookShelf %r>' % (self.name)
