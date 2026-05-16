from datetime import datetime

from src.infraestructure.models.payment_method_model import (
    PaymentMethodModel
)
from src.domain.entities.payment_method import (
    PaymentMethod
)


class PaymentMethodRepository:

    def __init__(self, db_session):
        self.db = db_session

    def create(
        self,
        entity
    ) -> PaymentMethod:

        model = PaymentMethodModel(
            user_id=entity.user_id,
            type=entity.type,
            alias=entity.alias,
            institution=entity.institution,
            currency=entity.currency,
            identifier_hash=entity.identifier_hash,
            identifier_last4=entity.identifier_last4,
            is_active=entity.is_active
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_domain(model)

    def list_by_user(
    self,
    user_id: int,
    page: int,
    page_size: int,
    type: str | None = None,
    status: str | None = None,
):
        query = self.db.query(PaymentMethodModel).filter(
            PaymentMethodModel.user_id == user_id
        )

        if type:
            query = query.filter(PaymentMethodModel.type == type)

        if status:
            query = query.filter(PaymentMethodModel.is_active == (status == "active"))

        total = query.count()

        models = (
            query
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        items = [self._to_domain(model) for model in models]

        return {
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size
        }

    def get_by_id(
        self,
        user_id: int,
        payment_method_id: int
    ):
        model = (
            self.db.query(
                PaymentMethodModel
            )
            .filter(
                PaymentMethodModel.id == payment_method_id,
                PaymentMethodModel.user_id == user_id
            )
            .first()
        )

        if not model:
            return None

        return self._to_domain(model)

    def deactivate(
        self,
        user_id: int,
        payment_method_id: int
    ):
        model = (
            self.db.query(
                PaymentMethodModel
            )
            .filter(
                PaymentMethodModel.id == payment_method_id,
                PaymentMethodModel.user_id == user_id
            )
            .first()
        )

        if not model:
            return None

        model.is_active = False
        model.deleted_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(model)

        return self._to_domain(model)

    def _to_domain(
        self,
        model
    ) -> PaymentMethod:
        return PaymentMethod(
            id=model.id,
            user_id=model.user_id,
            type=model.type,
            alias=model.alias,
            institution=model.institution,
            currency=model.currency,
            identifier_last4=model.identifier_last4,
            identifier_hash= model.identifier_hash,
            is_active=model.is_active
        )
    
    def exists_duplicate(
        self,
        user_id: int,
        method_type: str,
        institution: str,
        identifier_last4: str
    ):
        return (
            self.db.query(
                PaymentMethodModel
            )
            .filter(
                PaymentMethodModel.user_id == user_id,
                PaymentMethodModel.type == method_type,
                PaymentMethodModel.institution == institution,
                PaymentMethodModel.identifier_last4 == identifier_last4,
                PaymentMethodModel.is_active == True
            )
            .first()
        )