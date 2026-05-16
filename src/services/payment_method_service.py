from fastapi import HTTPException

from src.domain.entities.payment_method import PaymentMethod
from src.presentation.schemas.payment_method_schemas import PaymentMethodResponse
from src.helpers.security_helper import SecurityHelper

from src.config.audit.collector import AuditCollector
from src.config.audit.events import AuditEvents


class PaymentMethodService:

        def __init__(self, payment_repo):
            self.payment_repo = payment_repo


        def _to_response(self, payment) -> PaymentMethodResponse:
            return PaymentMethodResponse(
                id=payment.id,
                type=payment.type,
                alias=payment.alias,
                institution=payment.institution,
                currency=payment.currency,
                is_active=payment.is_active,
                masked_identifier="****" + payment.identifier_last4
            )

        def create(self, dto, user_id: int):

            identifier = dto.identifier

            if len(identifier) < 4:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid identifier"
                )

            last4 = identifier[-4:]

            existing = self.payment_repo.exists_duplicate(
                user_id=user_id,
                method_type=dto.type,
                institution=dto.institution,
                identifier_last4=last4
            )

            if existing:
                raise HTTPException(
                    status_code=409,
                    detail="Payment method already registered"
                )


            identifier_hash = SecurityHelper.hash_identifier(identifier)

            entity = PaymentMethod(
                id=None,
                user_id=user_id,
                type=dto.type,
                alias=dto.alias,
                institution=dto.institution,
                currency=dto.currency,
                identifier_hash=identifier_hash,
                identifier_last4=last4,
                is_active=True
            )

            saved = self.payment_repo.create(entity)

            AuditCollector.add(
                action=AuditEvents.PAYMENT_CREATED,
                entity="payment_method",
                entity_id=saved.id
            )

            return self._to_response(saved)


        def get_detail(self, user_id: int, payment_method_id: int):

            payment = self.payment_repo.get_by_id(
                user_id,
                payment_method_id
            )

            if not payment:
                raise HTTPException(
                    status_code=404,
                    detail="Payment method not found"
                )

            return self._to_response(payment)

        def list_by_user(
            self,
            user_id: int,
            page: int,
            page_size: int,
            type: str | None = None,
            status: str | None = None
        ):
            result = self.payment_repo.list_by_user(
                user_id=user_id,
                page=page,
                page_size=page_size,
                type=type,
                status=status
            )

            return {
                "items": [
                    self._to_response(p) for p in result["items"]
                ],
                "total": result["total"],
                "page": result["page"],
                "page_size": result["page_size"]
            }


        def deactivate(self, user_id: int, payment_method_id: int):

            payment = self.payment_repo.deactivate(
                user_id,
                payment_method_id
            )

            if not payment:
                raise HTTPException(
                    status_code=404,
                    detail="Payment method not found"
                )
            

            AuditCollector.add(
                action=AuditEvents.PAYMENT_DELETED,
                entity="payment_method",
                entity_id=payment.id
            )


            return self._to_response(payment)