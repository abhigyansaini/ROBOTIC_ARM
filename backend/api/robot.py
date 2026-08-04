from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.schemas.robot_arm import (
    RobotArmCreate,
    RobotArmUpdate,
    RobotArmResponse,
)
from backend.services.robot_service import (
    create_robot,
    get_all_robots,
    get_robot_by_id,
    update_robot,
    delete_robot,
)

router = APIRouter(
    prefix="/robots",
    tags=["Robots"]
)


@router.post("/", response_model=RobotArmResponse)
def add_robot(robot: RobotArmCreate, db: Session = Depends(get_db)):
    return create_robot(db, robot)


@router.get("/", response_model=list[RobotArmResponse])
def fetch_all_robots(db: Session = Depends(get_db)):
    return get_all_robots(db)


@router.get("/{robot_id}", response_model=RobotArmResponse)
def fetch_robot(robot_id: int, db: Session = Depends(get_db)):
    robot = get_robot_by_id(db, robot_id)

    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    return robot


@router.put("/{robot_id}", response_model=RobotArmResponse)
def edit_robot(
    robot_id: int,
    robot: RobotArmUpdate,
    db: Session = Depends(get_db),
):
    updated_robot = update_robot(db, robot_id, robot)

    if not updated_robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    return updated_robot


@router.delete("/{robot_id}")
def remove_robot(robot_id: int, db: Session = Depends(get_db)):
    deleted = delete_robot(db, robot_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Robot not found")

    return {"message": "Robot deleted successfully"}