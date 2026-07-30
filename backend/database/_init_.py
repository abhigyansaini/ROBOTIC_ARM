from backend.database.connection import Base, engine

# Import all models here
from backend.models import RobotArm

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Database and tables created successfully!")