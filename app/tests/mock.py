from datetime import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from faker import Faker

from app.database.models import Debt, Client, Payment

fake = Faker()


def create_mock_result_proxy(data: dict) -> MagicMock:
    """ Create a mock object that simulates a ResultProxy.

    Args:
        data (dict): The data to be returned by the mock object.

    Returns:
        MagicMock: The mock object that simulates a ResultProxy.
    """
    mock_row = MagicMock()
    mock_row.__getitem__.side_effect = data.__getitem__
    return mock_row


client_data = {
    'document_identifier': "10000001",
    'name': fake.name(),
    'company': fake.company(),
    'product_type': fake.word(),
    'date_created': datetime.now(),
    'date_updated': datetime.now(),
}

debt_status_valid_data = {
    "tipoConsulta": "5",
    "idConsulta": "10000001",
    "codigoBanco": "1230",
    "codigoProducto": "001",
    "canalPago": "MA",
    "codigoEmpresa": "512"
}

debt_update_data = {
    "fechaTxn": "24052024",
    "horaTxn": "153105",
    "canalPago": "10",
    "codigoBanco": "1020",
    "numOperacionBanco": "A05478452120",
    "formaPago": "01",
    "tipoConsulta": "1",
    "idConsulta": "10000003",
    "codigoProducto": "001",
    "numDocumento": "B01-0000000002",
    "importePagado": 1500,
    "monedaDoc": "2",
    "codigoEmpresa": "998"
}

debt_update_invalid_data = {
    "fechaTxn": "",
    "horaTxn": "",
    "canalPago": "",
    "codigoBanco": "",
    "numOperacionBanco": "",
    "formaPago": "",
    "tipoConsulta": "",
    "idConsulta": "",
    "codigoProducto": "",
    "numDocumento": "",
    "importePagado": True,
    "monedaDoc": "",
    "codigoEmpresa": ""
}

mock_debt_update_service_response = {
    "codigoRespuesta": "00",
    "nombreCliente": "John Doe",
    "numOperacionERP": "A05478452120",
    "descripcionResp": "OK"
}


mock_update_debt_payment = {
    "fechaTxn": "01012024",
    "horaTxn": "235959",
    "canalPago": "0001",
    "codigoBanco": "0001",
    "numOperacionERP": "654321234567",
    "formaPago": "00",
    "tipoConsulta": "1",
    "idConsulta": "10000002",
    "codigoProducto": "MGK",
    "numDocumento": "B01-0000000002",
    "importePagado": 100.00,
    "monedaDoc": "1",
    "codigoEmpresa": "512"
}
client_instance = Client(
    document_identifier='10000001',
    name='John Doe',
    company='Doe & Partners',
    product_type='Credit Card',
    date_created=datetime(2021, 4, 26, 9, 48, 14),
    date_updated=datetime(2022, 5, 5, 23, 58, 17),
)

debt_instance = Debt(
    operation_identifier='123320000013',
    client=client_instance,
    description='Bank little rest.',
    emition_date=datetime(2021, 4, 26, 9, 48, 14),
    expiration_date=datetime(2024, 9, 2, 10, 2, 59),
    total_debt=Decimal('75663.38'),
    default_debt=Decimal('5000.00'),
    administration_expenses=Decimal('585.86'),
    minimum_payment=Decimal('273.96'),
    period='02',
    fee='00',
    product_code='OJw',
    currency='INR',
    date_created=datetime(2023, 9, 25, 5, 30, 6),
    created_by='Jennifer Stevenson',
    date_updated=datetime(2022, 5, 5, 23, 58, 17),
    updated_by='David Wilson'
)


payment_instance = Payment(
    id=1,
    debt=debt_instance,
    emition_date=datetime(2024, 8, 22, 18, 52, 6),
    bank_code="001",
    operation_bank_number="1234567890",
    gateway="Gateway",
    payment_type="credit_card",
    payment_amount=Decimal('100.00'),
    status="pending",
    date_created=datetime(2024, 8, 22, 18, 52, 4),
    date_updated=datetime(2024, 8, 22, 18, 52, 4)
)
