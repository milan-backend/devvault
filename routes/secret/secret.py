from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.secret import Secret
from models.project import Project
from models.user import User
from schemas.secret_schema import SecretCreate
from dependencies.auth_dependency import get_current_user
from routes.secret.secret_security import encrypt_value, decrypt_value


router = APIRouter(prefix="/secrets", tags=["Secrets"])


@router.post("/projects/{project_id}")
def create_secret(
    project_id: int,
    secret: SecretCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    encrypted_value = encrypt_value(secret.value)

    new_secret = Secret(
        key=secret.key,
        encrypted_value=encrypted_value,
        project_id=project_id
    )

    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)

    return {"message": "Secret stored successfully"}


@router.get("/projects/{project_id}")
def get_secrets(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
    Project.id == project_id,
    Project.owner_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail= "Project not found")
    
    secrets = db.query(Secret).filter(Secret.project_id == project_id).all()

    return [
        {
            "id": secret.id,
            "key": secret.key,
            "value": decrypt_value(secret.encrypted_value)
        }
        for secret in secrets
    ]


@router.delete("/{secret_id}")
def delete_secret(
    secret_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    secret = db.query(Secret).join(Project).filter(
    Secret.id == secret_id,
    Project.owner_id == current_user.id
    ).first()

    if not secret:
       raise HTTPException(status_code=404, detail="Secret not found")

    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")

    db.delete(secret)
    db.commit()

    return {"message": "Secret deleted"}


@router.get("/projects/{project_id}/env")
def get_env_file(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    secrets = db.query(Secret).filter(
        Secret.project_id == project_id
    ).all()

    env_data = {}

    for secret in secrets:
        env_data[secret.key] = decrypt_value(secret.encrypted_value)

    return env_data