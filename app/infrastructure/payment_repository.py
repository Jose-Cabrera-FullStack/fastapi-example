from datetime import datetime

from ormar import NoMatch

from app.database.models import Payment, Debt


class PaymentRepository:

    @staticmethod
    async def create_payment(
        debt: Debt,
        emition_date: datetime,
        bank_code: str,
        operation_bank_number: str,
        gateway: str,
        payment_type: str,
        payment_amount: float,
        status: str,
        date_updated: datetime = datetime.now(),
        date_created: datetime = datetime.now(),
    ) -> Payment:
        """
          Args:
            debt (Debt): The debt associated with the payment.
            emition_date (datetime): The date of payment emition.
            bank_code (str): The bank code.
            operation_bank_number (str): The operation bank number.
            gateway (str): The payment gateway.
            payment_type (str): The type of payment.
            payment_amount (float): The amount of payment.
            status (str): The status of the payment.
            date_updated (datetime, optional): The date of last update.
            date_created (datetime, optional): The date of creation.

        Returns:
            Payment: The created payment record.
        """
        payment = await Payment.objects.create(
            debt=debt,
            emition_date=emition_date,
            bank_code=bank_code,
            operation_bank_number=operation_bank_number,
            gateway=gateway,
            payment_type=payment_type,
            payment_amount=payment_amount,
            status=status,
            date_created=date_created,
            date_updated=date_updated
        )
        return payment

    @staticmethod
    async def get_payments_by_debt(debt: Debt) -> Payment:
        """
        Args:
            operation_bank_number (str): The unique identifier of the payment.

        Returns:
            Optional[Payment]: The payment instance if found, None otherwise.

        """
        try:
            payments = await Payment.objects.select_related(
                'debt'
            ).filter(debt=debt).all()
            return payments
        except NoMatch:
            return []
        except Exception as e:
            raise e

    @staticmethod
    async def update_payment_status(
        debt: Debt,
        status: str,
    ) -> Payment:
        """
        Args:
            debt (Debt): The debt associated with the payment.
            status (str): The status of the payment.

        Returns:
            Payment: An updated "Payment" instance.
        """

        await Payment.objects.filter(
            debt=debt,
        ).update(
            status=status
        )
        try:
            return await Payment.objects.filter(debt=debt).first()
        except NoMatch as exc:
            raise ValueError("Payment not found") from exc
        except Exception as e:
            raise e

    @staticmethod
    async def delete_payment(payment_id: int) -> bool:
        """
        Args:
            payment_id (int): The unique identifier of the payment to delete.

        Returns:
            bool: True if the payment was deleted successfully, False otherwise.
        """
        try:
            payment = await Payment.objects.get(id=payment_id)
            await payment.delete()
            return True
        except NoMatch:
            return False
