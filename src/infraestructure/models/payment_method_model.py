from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from src.infraestructure.db.base import Base
from datetime import datetime


class PaymentMethodModel(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    type = Column(String(50), nullable=False)  # card, bank_account, clabe

    alias = Column(String(100), nullable=False)

    institution = Column(String(100), nullable=False)

    currency = Column(String(10), nullable=False)

    identifier_hash = Column(String(255), nullable=False)

    status = Column(String(20), default="active")

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    deleted_at = Column(DateTime, nullable=True)

    identifier_last4 = Column(
        String(4),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )
