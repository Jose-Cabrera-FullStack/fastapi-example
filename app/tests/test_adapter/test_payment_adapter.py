from unittest.mock import AsyncMock, patch

import pytest
from ormar import NoMatch

from app.adapter import PaymentAdapter


@pytest.mark.asyncio
@patch(
    'app.infrastructure.debt_repository.DebtRepository.get_debt_by_operation_identifier',
    new_callable=AsyncMock)
@patch('app.domain.payment_domain.PaymentDomain.formating_fields', new_callable=AsyncMock)
@patch('app.adapter.PaymentAdapter._update_or_create_payment', new_callable=AsyncMock)
async def test_update_payments_success(
        mock_update_or_create_payment,
        mock_formatting_fields,
        mock_get_debt
):

    mock_debt = AsyncMock()
    mock_debt.client.name = "CLIENT001"
    mock_get_debt.return_value = mock_debt

    mock_payment = AsyncMock()
    mock_payment.id = "654321"
    mock_update_or_create_payment.return_value = mock_payment

    payment_data = {
        "numDocumento": "123320000013",
        "operation_bank_number": "1234567890",
        "payment_amount": 100.0,
        "gateway": "some_gateway",
        "bank_code": "001",
        "payment_type": "credit_card",
        "emition_date": "2024-08-10T10:00:00",
    }

    formatted_payment_data = AsyncMock()
    mock_formatting_fields.return_value = formatted_payment_data

    result = await PaymentAdapter.update_payments(payment_data)

    expected_result = {
        "codigoRespuesta": "00",
        "nombreCliente": "CLIENT001",
        "numOperacionERP": "654321",
        "descripcionResp": "OK",
    }

    assert result == expected_result
    mock_get_debt.assert_awaited_once_with("123320000013")
    mock_formatting_fields.assert_called_once_with(payment_data, "paid")


@pytest.mark.asyncio
@patch('app.infrastructure.PaymentRepository.get_payments_by_debt', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.update_payment_status', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.create_payment', new_callable=AsyncMock)
async def test_update_or_create_payment_existing_payment(
        mock_create_payment,
        mock_update_payment,
        mock_get_payments_by_debt
):
    mock_payment = AsyncMock()
    mock_get_payments_by_debt.return_value = [mock_payment]

    payment_data = {
        'operation_bank_number': '1234567890',
        'emition_date': '2024-08-22T18:52:06',
        'bank_code': '001',
        'gateway': 'Gateway',
        'payment_type': 'credit_card',
        'payment_amount': 100.00,
        'status': 'pending'
    }

    debt = AsyncMock()

    await PaymentAdapter._update_or_create_payment(debt=debt, payment_data=payment_data)

    mock_get_payments_by_debt.assert_awaited_once_with(debt=debt)

    mock_update_payment.assert_awaited_once_with(debt=debt, status='pending')


@pytest.mark.asyncio
@patch('app.infrastructure.PaymentRepository.get_payments_by_debt', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.update_payment_status', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.create_payment', new_callable=AsyncMock)
async def test_update_or_create_payment_no_existing_payment(
        mock_create_payment,
        mock_update_payment,
        mock_get_payments_by_debt
):

    mock_get_payments_by_debt.return_value = []

    payment_data = {
        'operation_bank_number': '1234567890',
        'emition_date': '2024-08-22T18:52:06',
        'bank_code': '001',
        'gateway': 'Gateway',
        'payment_type': 'credit_card',
        'payment_amount': 100.00,
        'status': 'pending'
    }
    debt = AsyncMock()

    await PaymentAdapter._update_or_create_payment(debt=debt, payment_data=payment_data)

    mock_get_payments_by_debt.assert_awaited_once_with(debt=debt)

    mock_create_payment.assert_awaited_once_with(
        debt=debt,
        emition_date='2024-08-22T18:52:06',
        bank_code='001',
        operation_bank_number='1234567890',
        gateway='Gateway',
        payment_type='credit_card',
        payment_amount=100.00,
        status='pending'
    )


@pytest.mark.asyncio
@patch('app.infrastructure.PaymentRepository.get_payments_by_debt', new_callable=AsyncMock)
async def test_update_or_create_payment_raises_exception(mock_get_payments_by_debt):

    mock_get_payments_by_debt.side_effect = Exception("Unexpected error")

    payment_data = {
        'operation_bank_number': '1234567890',
        'emition_date': '2024-08-22T18:52:06',
        'bank_code': '001',
        'gateway': 'Gateway',
        'payment_type': 'credit_card',
        'payment_amount': 100.00,
        'status': 'pending'
    }
    debt = AsyncMock()

    with pytest.raises(Exception, match="Unexpected error"):
        await PaymentAdapter._update_or_create_payment(debt=debt, payment_data=payment_data)

    mock_get_payments_by_debt.assert_awaited_once_with(debt=debt)


@pytest.mark.asyncio
@patch(
    'app.infrastructure.debt_repository.DebtRepository.get_debt_by_operation_identifier',
    new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.get_payments_by_debt', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.update_payment_status', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.create_payment', new_callable=AsyncMock)
@patch('app.domain.payment_domain.PaymentDomain.formating_fields', new_callable=AsyncMock)
async def test_update_payments_debt_not_found(
        mock_formatting,
        mock_create_payment,
        mock_update_payment,
        mock_get_payment,
        mock_get_debt
):
    mock_get_debt.side_effect = NoMatch("No matching record found")

    payment_data = {
        "numDocumento": "123320000013",
        "operation_bank_number": "1234567890",
        "payment_amount": 100.0,
        "gateway": "some_gateway",
        "bank_code": "001",
        "payment_type": "credit_card",
        "emition_date": "2024-08-10T10:00:00",
    }

    result = await PaymentAdapter.update_payments(payment_data)

    expected_result = {
        "codigoRespuesta": "99",
        "nombreCliente": "",
        "numOperacionERP": "",
        "descripcionResp": "DEUDA NO ENCONTRADA",
    }

    assert result == expected_result
    mock_get_debt.assert_awaited_once_with("123320000013")
    mock_create_payment.assert_not_awaited()
    mock_update_payment.assert_not_awaited()


@pytest.mark.asyncio
@patch(
    'app.infrastructure.debt_repository.DebtRepository.get_debt_by_operation_identifier',
    new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.get_payments_by_debt', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.create_payment', new_callable=AsyncMock)
@patch('app.infrastructure.PaymentRepository.update_payment_status', new_callable=AsyncMock)
@patch('app.domain.payment_domain.PaymentDomain.formating_fields', new_callable=AsyncMock)
async def test_update_payments_unexpected_exception(
        mock_formatting,
        mock_update_payment,
        mock_create_payment,
        mock_get_payment,
        mock_get_debt
):
    mock_get_debt.side_effect = Exception("Unexpected error")

    payment_data = {
        "numDocumento": "123320000013",
        "operation_bank_number": "1234567890",
        "payment_amount": 100.0,
        "gateway": "some_gateway",
        "bank_code": "001",
        "payment_type": "credit_card",
        "emition_date": "2024-08-10T10:00:00",
    }

    with pytest.raises(Exception, match="Unexpected error"):
        await PaymentAdapter.update_payments(payment_data)

    mock_get_debt.assert_awaited_once_with("123320000013")
    mock_create_payment.assert_not_awaited()
    mock_update_payment.assert_not_awaited()
