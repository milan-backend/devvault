from database import engine,Base

from models.user import User
from models.project import Project
from models.secret import Secret

Base.metadata.create_all(bind=engine)