import logging

from ormar import NoMatch

from app.domain.payment_domain import PaymentDomain
from app.infrastructure import PaymentRepository
from app.infrastructure.debt_repository import DebtRepository


class PaymentAdapter:
    @staticmethod
    async def update_payments(payment_data: dict, status: str = "paid") -> dict:
        """ Send payment data to repository

        Args:
            payment (dict): Payment data

        Returns:
            dict: Formatted response data

        Examples:
            return {
                "codigoRespuesta": "00",
                "nombreCliente": "CLIENT001",
                "numOperacionERP": "654321",
                "descripcionResp": "OK",
            }
        """

        try:
            debt = await DebtRepository.get_debt_by_operation_identifier(
                payment_data['numDocumento']
            )

            domain_payment = PaymentDomain.formating_fields(payment_data, status)

            payment = await PaymentAdapter._update_or_create_payment(debt, domain_payment)

            return {
                "codigoRespuesta": "00",
                "nombreCliente": debt.client.name,
                "numOperacionERP": payment.id,
                "descripcionResp": "OK",
            }

        except NoMatch:
            logging.error("Debt not found")
            return {
                "codigoRespuesta": "99",
                "nombreCliente": "",
                "numOperacionERP": "",
                "descripcionResp": "DEUDA NO ENCONTRADA",
            }
        except Exception as e:
            logging.error(e)
            raise e

    @staticmethod
    async def _update_or_create_payment(debt: dict, payment_data: dict) -> dict:

        try:
            payments = await PaymentRepository.get_payments_by_debt(
                debt=debt
            )

            if payments:
                return await PaymentRepository.update_payment_status(
                    debt=debt,
                    status=payment_data['status']
                )

            return await PaymentRepository.create_payment(
                debt=debt,
                emition_date=payment_data['emition_date'],
                bank_code=payment_data['bank_code'],
                operation_bank_number=payment_data['operation_bank_number'],
                gateway=payment_data['gateway'],
                payment_type=payment_data['payment_type'],
                payment_amount=payment_data['payment_amount'],
                status=payment_data['status']
            )

        except Exception as e:
            raise e
