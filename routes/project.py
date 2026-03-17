from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.project import Project
from models.user import User
from schemas.project_schema import ProjectCreate
from dependencies.auth_dependency import get_current_user


router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_project = Project(
        name=project.name,
        owner_id=current_user.id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/")
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    projects = db.query(Project).filter(Project.owner_id == current_user.id).all()

    return projects


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()

    if not project:
        return {"error": "Project not found"}

    db.delete(project)
    db.commit()

    return {"message": "Project deleted"}