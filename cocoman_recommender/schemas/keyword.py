from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import List
from sqlalchemy.orm import relationship, Session

from cocoman_recommender.schemas.base_repository import BaseRepository
from cocoman_recommender.schemas.contents import contents_keyword
from cocoman_recommender.schemas.conn import Base


class Keyword(Base):
    __tablename__ = 'TB_KEYWORD'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    contents_set = relationship('Contents', secondary=contents_keyword, back_populates='keywords_id')


class KeywordRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.query = self.session.query(Keyword)

    def get_all(self) -> List[Keyword]:
        return self.query.all()

    def get_by_id(self, id: int) -> Keyword:
        return self.query.get(id=id)
