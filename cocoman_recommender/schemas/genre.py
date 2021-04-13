from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import List
from sqlalchemy.orm import relationship, Session

from cocoman_recommender.schemas.base_repository import BaseRepository
from cocoman_recommender.schemas.contents import contents_genre
from cocoman_recommender.schemas.conn import Base


class Genre(Base):
    __tablename__ = 'TB_GENRE'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=False)
    contents_set = relationship('Contents', secondary=contents_genre, back_populates='genres_id')


class GenreRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.query = self.session.query(Genre)

    def get_all(self) -> List[Genre]:
        return self.query.all()

    def get_by_id(self, id: int) -> Genre:
        return self.query.get(id=id)
