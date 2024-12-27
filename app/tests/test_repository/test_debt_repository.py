from datetime import datetime
from unittest.mock import patch, AsyncMock

import pytest
from ormar import NoMatch

from app.infrastructure.debt_repository import DebtRepository
from app.database.models import Debt


@pytest.mark.asyncio
@patch('app.infrastructure.debt_repository.Debt.objects.get', new_callable=AsyncMock)
@patch('app.infrastructure.debt_repository.Debt.objects.create', new_callable=AsyncMock)
@patch('app.database.models.Debt.Meta.database.fetch_all', new_callable=AsyncMock)
@patch(
    'app.domain.debt_domain.DebtDomain.generate_operation_identifier',
    return_value="existing_id"
)
async def test_generate_unique_operation_identifier_retry(
        mock_generate_id,
        mock_fetch_all,
        mock_get,
        mock_create
):
    mock_debt_data = {
        "operation_identifier": "existing_id",
        "client": "valid_client_id",
        "description": "Test Debt",
        "emition_date": datetime.now(),
        "expiration_date": datetime.now(),
        "total_debt": 1000.00,
        "default_debt": 100.00,
        "administration_expenses": 50.00,
        "minimum_payment": 150.00,
        "period": "M",
        "fee": "10",
        "product_code": "001",
        "currency": "USD",
        "date_created": datetime.now(),
        "date_updated": datetime.now(),
        "created_by": None,
        "updated_by": None
    }

    amount_of_attempts = 3

    mock_get.side_effect = Debt(**mock_debt_data)

    mock_fetch_all.return_value = [mock_debt_data]

    with pytest.raises(Exception) as exc_info:
        await DebtRepository._generate_unique_operation_identifier(max_attempts=amount_of_attempts)

    assert str(exc_info.value) == (
        f"Failed to generate a unique identifier after {amount_of_attempts} attempts"
    )
    assert mock_generate_id.call_count == amount_of_attempts


@pytest.mark.asyncio
@patch('app.database.models.Debt.objects.get', new_callable=AsyncMock)
@patch('app.database.models.Debt.Meta.database.fetch_all', new_callable=AsyncMock)
@patch('app.database.models.Debt.Meta.database.execute', new_callable=AsyncMock)
async def test_delete_debt(mock_execute, mock_fetch_all, mock_get):

    mock_debt_instance = AsyncMock(spec=Debt)
    mock_debt_instance.delete = AsyncMock()
    mock_get.return_value = mock_debt_instance

    mock_get.side_effect = NoMatch("Debt not found")
    result = await DebtRepository.delete_debt("non-existent-id")
    assert result is False
