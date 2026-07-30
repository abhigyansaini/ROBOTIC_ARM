from backend.database.connection import Base, engine

# Import all models here
from backend.models import (
    RobotArm,
    Telemetry,
    Prediction,
    Maintenance,
    Incident,
    Notification,
    User,
)
print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")