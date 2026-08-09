from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models.telemetry import Telemetry
from backend.schemas.health import HealthRequest


def calculate_health(db: Session, data: HealthRequest):

    # Fetch the latest telemetry for the given robot
    telemetry = (
        db.query(Telemetry)
        .filter(Telemetry.robot_id == data.robot_id)
        .order_by(Telemetry.timestamp.desc())
        .first()
    )

    # If no telemetry exists
    if telemetry is None:
        raise HTTPException(
            status_code=404,
            detail="No telemetry data found for this robot."
        )

    # Start with 100% health
    health = 100

    # Temperature
    if telemetry.temperature > 60:
        health -= 20

    # Vibration
    if telemetry.vibration > 0.5:
        health -= 30

    # Motor Current
    if telemetry.motor_current > 5:
        health -= 25

    # Torque
    if telemetry.torque > 25:
        health -= 25

    # Prevent negative score
    health = max(0, health)

    # Determine health status
    if health >= 90:
        status = "Excellent"
    elif health >= 75:
        status = "Good"
    elif health >= 60:
        status = "Warning"
    elif health >= 40:
        status = "Critical"
    else:
        status = "Failure Likely"

    return {
        "robot_id": telemetry.robot_id,
        "temperature": telemetry.temperature,
        "vibration": telemetry.vibration,
        "motor_current": telemetry.motor_current,
        "torque": telemetry.torque,
        "health_score": health,
        "health_status": status
    }