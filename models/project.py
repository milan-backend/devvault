from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer,primary_key=True,index=True)

    name = Column(String,nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
