import logging

from app.adapter.payment_adapter import PaymentAdapter
from app.schemas.request import PaymentUpdatePOSTRequest
from app.schemas.request.revert_post_request import RevertDebtPaymentPOSTRequest


class PaymentService:

    @staticmethod
    async def update_debt_payment(payment: dict) -> dict:
        """ Update payment data

        Args:
            payment (dict): Payment data

        Returns:
            dict: Updated payment data

        Examples:
            {
                "codigoRespuesta": "00",
                "descripcionResp": "OK",
                "nombreCliente": "Juan Perez",
                "numOperacionERP": "654321"
            }
        """

        try:

            validated_payment = PaymentUpdatePOSTRequest(**payment).dict()

            return await PaymentAdapter.update_payments(
                payment_data=validated_payment,
                status="paid"
            )
        except Exception as e:
            logging.error(e)
            return {
                "codigoRespuesta": "99",
                "nombreCliente": "",
                "numOperacionERP": "",
                "descripcionResp": "ERROR DESCONOCIDO",
            }

    @staticmethod
    async def revert_payment_debt(payment: dict) -> dict:
        """ Update payment data

        Args:
            payment (dict): Payment data

        Returns:
            dict: Updated payment data

        Examples:
            {
                "codigoRespuesta": "00",
                "descripcionResp": "OK",
                "nombreCliente": "Juan Perez",
                "numOperacionERP": "654321"
            }

        """

        try:

            validated_payment = RevertDebtPaymentPOSTRequest(**payment).dict()

            return await PaymentAdapter.update_payments(
                payment_data=validated_payment,
                status="pending"
            )
        except Exception as e:
            logging.error(e)
            return {
                "codigoRespuesta": "99",
                "nombreCliente": "",
                "numOperacionERP": "",
                "descripcionResp": "ERROR DESCONOCIDO",
            }
