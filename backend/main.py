from fastapi import FastAPI
from backend.api import (
    robot_router,
    sensor_router,
    telemetry_router,
    prediction_router,
    maintenance_router,
    incident_router,
    notification_router,
    user_router,
)

app = FastAPI(
    title="FactoryOps AI",
    version="1.0.0",
    description="Predictive Maintenance API for Industrial Robot Arms"
)

app.include_router(robot_router)
app.include_router(sensor_router)
app.include_router(telemetry_router)
app.include_router(prediction_router)
app.include_router(maintenance_router)
app.include_router(incident_router)
app.include_router(notification_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to FactoryOps AI 🚀"
    }