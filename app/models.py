from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
    Boolean
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


# -------------------------
# 1. USERS
# -------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    role = Column(String(50), default="inspector")

    inspections = relationship(
        "Inspection",
        back_populates="inspector"
    )


# -------------------------
# 2. INSPECTIONS
# -------------------------

class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(Integer, primary_key=True, index=True)

    inspector_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    status = Column(
        String(50),
        default="pending"
    )

    inspector = relationship(
        "User",
        back_populates="inspections"
    )

    products = relationship(
        "Product",
        back_populates="inspection"
    )

    images = relationship(
        "ProductImage",
        back_populates="inspection"
    )

    compliance_results = relationship(
        "ComplianceResult",
        back_populates="inspection"
    )


# -------------------------
# 3. PRODUCTS
# -------------------------

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("inspections.id"),
        nullable=False
    )

    product_name = Column(String(200))
    category = Column(String(100))
    brand = Column(String(100))

    inspection = relationship(
        "Inspection",
        back_populates="products"
    )


# -------------------------
# 4. PRODUCT IMAGES
# -------------------------

class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("inspections.id"),
        nullable=False
    )

    image_path = Column(String(500), nullable=False)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    inspection = relationship(
        "Inspection",
        back_populates="images"
    )

    ocr_result = relationship(
        "OCRResult",
        back_populates="image",
        uselist=False
    )


# -------------------------
# 5. OCR RESULTS
# -------------------------

class OCRResult(Base):
    __tablename__ = "ocr_results"

    id = Column(Integer, primary_key=True, index=True)

    image_id = Column(
        Integer,
        ForeignKey("product_images.id"),
        nullable=False
    )

    raw_text = Column(Text, nullable=False)

    confidence = Column(Float)

    image = relationship(
        "ProductImage",
        back_populates="ocr_result"
    )


# -------------------------
# 6. DECLARATIONS
# -------------------------

class Declaration(Base):
    __tablename__ = "declarations"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("inspections.id"),
        nullable=False
    )

    mrp = Column(Float)

    net_quantity = Column(String(100))

    manufacturer = Column(String(300))

    manufacturing_date = Column(String(50))

    country_of_origin = Column(String(100))

    consumer_care = Column(String(300))

    inspection = relationship(
        "Inspection"
    )


# -------------------------
# 7. RULES
# -------------------------

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)

    rule_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    rule_title = Column(
        String(300),
        nullable=False
    )

    chapter = Column(
        String(200)
    )

    description = Column(
        Text,
        nullable=False
    )

    requirement = Column(
        Text
    )

    is_exempted_under_rule_26 = Column(
        Boolean,
        default=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    compliance_results = relationship(
        "ComplianceResult",
        back_populates="rule"
    )


# -------------------------
# 8. COMPLIANCE RESULTS
# -------------------------

class ComplianceResult(Base):
    __tablename__ = "compliance_results"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("inspections.id"),
        nullable=False
    )

    rule_id = Column(
        Integer,
        ForeignKey("rules.id"),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False
    )

    remarks = Column(Text)

    inspection = relationship(
        "Inspection",
        back_populates="compliance_results"
    )

    rule = relationship(
        "Rule",
        back_populates="compliance_results"
    )