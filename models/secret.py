from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from database import Base
from datetime import datetime

class Secret(Base):
    __tablename__ = "secrets"

    id = Column(Integer, primary_key=True, index=True)

    key = Column(String, nullable=False)

    encrypted_value = Column(String, nullable=False)

    project_id = Column(Integer, ForeignKey("projects.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    