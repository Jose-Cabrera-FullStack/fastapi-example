from datetime import datetime
from typing import List, Optional

from ormar import NoMatch

from app.database.models import Debt, Client
from app.domain import DebtDomain
from app.exceptions.custom_exception import UniqueIdentifierGenerationError


class DebtRepository:

    @staticmethod
    async def _generate_unique_operation_identifier(max_attempts: int = 5) -> str:
        """
        Args:
            max_attempts (int): Maximum number of attempts before failing.

        Returns:
            str: Unique operation identifier.

        Raises:
            Exception: If a unique identifier cannot be generated after the
            allowed attempts.
        """
        attempts = 0
        while attempts < max_attempts:
            identifier = DebtDomain.generate_operation_identifier()
            try:
                await Debt.objects.get(operation_identifier=identifier)
            except NoMatch:
                return identifier
            except Exception as e:
                raise e
            attempts += 1

        raise UniqueIdentifierGenerationError(
            f"Failed to generate a unique identifier after {max_attempts} attempts"
        )

    @staticmethod
    async def add_debt(
        client: Client,
        description: str,
        emition_date: datetime,
        expiration_date: datetime,
        total_debt: float,
        default_debt: float,
        administration_expenses: float,
        minimum_payment: float,
        period: str,
        fee: str,
        product_code: str,
        currency: str,
    ) -> Debt:
        """
        Use this method to create a new debt instance.

        Args:
            client (Client): The client associated with the debt.
            description (str): Description of the debt.
            emition_date (datetime): The date the debt was issued.
            expiration_date (datetime): The expiration date of the debt.
            total_debt (float): The total amount of the debt.
            default_debt (float): The amount of default debt.
            administration_expenses (float): The administrative expenses related to the debt.
            minimum_payment (float): The minimum payment required.
            period (str): The payment period.
            fee (str): The payment fee associated with the debt.
            product_code (str): The product code associated with the debt.
            currency (str): The currency used in the transaction.

        Returns:
            Debt: The created debt instance.
        """
        debt = await Debt.objects.create(
            operation_identifier=await DebtRepository._generate_unique_operation_identifier(),
            client=client,
            description=description,
            emition_date=emition_date,
            expiration_date=expiration_date,
            total_debt=total_debt,
            default_debt=default_debt,
            administration_expenses=administration_expenses,
            minimum_payment=minimum_payment,
            period=period,
            fee=fee,
            product_code=product_code,
            currency=currency,
        )
        return debt

    @staticmethod
    async def get_debt_by_operation_identifier(operation_identifier: str) -> Optional[Debt]:
        """
        Args:
            operation_identifier (str): The unique identifier of the debt.

        Returns:
            Optional[Debt]: The debt instance if found, None otherwise.
        """
        try:
            return await Debt.objects.select_related('client').get(
                operation_identifier=operation_identifier
            )
        except NoMatch as exc:
            raise NoMatch(
                f"Debt with operation identifier {operation_identifier} not found."
            ) from exc
        except Exception as e:
            raise e

    @staticmethod
    async def get_debts_by_client_identifier(client_identifier: str, codigo_producto: str) -> List[Debt]:
        """
        Use this method to retrieve all debts with pending payments associated with a client.

        Args:
            client_identifier (str): The unique identifier of the client.

        Returns:
            List[Debt]: A list of debts associated with the client.
        """
        try:
            return await Debt.objects.select_related(
                'client'
            ).prefetch_related(
                'payments'
            ).filter(
                client__document_identifier=client_identifier,
                product_code=codigo_producto,
                payments__status="pending"
            ).all()
        except Exception as e:
            raise e

    @staticmethod
    async def get_all_debts() -> List[Debt]:
        """
        Returns:
            List[Debt]: A list of all debt instances.
        """
        try:
            debts = await Debt.objects.select_related('client').all()
            return debts
        except Exception as e:
            raise e

    @staticmethod
    async def update_debt(operation_identifier: str, **kwargs) -> Optional[Debt]:
        """
        Args:
            operation_identifier (str): The unique identifier of the debt.
            **kwargs: Arbitrary keyword arguments to update the debt attributes.

        Returns:
            Optional[Debt]: The updated debt instance if found, None otherwise.
        """
        try:
            debt = await Debt.objects.get(operation_identifier=operation_identifier)
            for key, value in kwargs.items():
                setattr(debt, key, value)
            await debt.update()
            return debt
        except NoMatch:
            return None
        except Exception as e:
            raise e

    @staticmethod
    async def delete_debt(operation_identifier: str) -> bool:
        """
        Args:
            operation_identifier (str): The unique identifier of the debt.

        Returns:
            bool: True if the debt was deleted, False otherwise.
        """
        try:
            debt = await Debt.objects.get(operation_identifier=operation_identifier)
            await debt.delete()
            return True
        except NoMatch:
            return False
        except Exception as e:
            raise e
