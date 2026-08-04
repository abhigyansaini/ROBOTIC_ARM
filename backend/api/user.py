from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.connection import get_db

from backend.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)

from backend.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserResponse)
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def fetch_users(
    db: Session = Depends(get_db),
):
    return get_all_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def fetch_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


@router.put("/{user_id}", response_model=UserResponse)
def edit_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    updated = update_user(
        db,
        user_id,
        user,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return updated


@router.delete("/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_user(
        db,
        user_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "message": "User deleted successfully"
    }