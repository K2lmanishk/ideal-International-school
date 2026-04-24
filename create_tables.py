from app import app, db

with app.app_context():
    db.create_all()
    print("✅ All missing tables (including class_fees) have been created.")