from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import List
from sqlalchemy.orm import Session

from cocoman_recommender.schemas.base_repository import BaseRepository
from cocoman_recommender.schemas.conn import Base


class Ott(Base):
    __tablename__ = 'TB_OTT'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    image_path = Column(String(length=255))


class OttRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.query = self.session.query(Ott)

    def get_all(self) -> List[Ott]:
        return self.query.all()

    def get_by_id(self, id: int) -> Ott:
        return self.query.get(id=id)
