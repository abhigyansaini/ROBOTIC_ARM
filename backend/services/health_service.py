from backend.schemas.health import HealthRequest


def calculate_health(data: HealthRequest):

    health = 100

    if data.temperature > 60:
        health -= 20

    if data.vibration > 0.5:
        health -= 30

    if data.current > 5:
        health -= 25

    if data.torque > 25:
        health -= 25

    health = max(0, health)

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
        "health_score": health,
        "health_status": status
    }