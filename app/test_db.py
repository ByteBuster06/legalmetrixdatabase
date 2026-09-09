from app.database import SessionLocal
from app.models import Inspection, Declaration

db = SessionLocal()

try:
    # Find the existing inspection
    inspection = db.query(Inspection).first()

    if not inspection:
        print("Inspection not found!")
    else:
        declaration = Declaration(
            inspection_id=inspection.id,
            mrp=10.00,
            net_quantity="79g",
            manufacturer="Parle Products",
            manufacturing_date="2026-01",
            country_of_origin="India",
            consumer_care="1800-123-456"
        )

        db.add(declaration)
        db.commit()
        db.refresh(declaration)

        print("Declaration inserted successfully!")
        print("Declaration ID:", declaration.id)
        print("MRP:", declaration.mrp)
        print("Net Quantity:", declaration.net_quantity)
        print("Manufacturer:", declaration.manufacturer)
        print("Manufacturing Date:", declaration.manufacturing_date)
        print("Country:", declaration.country_of_origin)
        print("Consumer Care:", declaration.consumer_care)

finally:
    db.close()