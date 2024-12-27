from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app
from app.tests.mock import (
    debt_update_data,
    mock_debt_update_service_response,
    debt_update_invalid_data
)


@patch(
    'app.service.PaymentService.update_debt_payment',
    return_value=mock_debt_update_service_response
)
def test_update_debt_payment_endpoint(mock_update_debt_payment):
    client = TestClient(app)
    request_data = debt_update_data

    response = client.post("/v1/update-debt-payment", json=request_data)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["codigoRespuesta"] == "00"
    assert response_data["nombreCliente"] == "John Doe"
    assert response_data["numOperacionERP"] == "A05478452120"
    assert response_data["descripcionResp"] == "OK"

    mock_update_debt_payment.assert_called_once_with(request_data)


@patch('app.service.PaymentService.update_debt_payment', return_value={})
def test_update_debt_payment_invalid_data_endpoint(mock_update_debt_payment):
    client = TestClient(app)
    request_data = debt_update_invalid_data

    response = client.post("/v1/update-debt-payment", json=request_data)

    assert response.status_code == 422

    response_data = response.json()
    print(response_data)

    assert "detail" in response_data
    assert isinstance(response_data["detail"], list)
    assert all("msg" in error for error in response_data["detail"])
    assert any("value_error" in error["type"] for error in response_data["detail"])

    mock_update_debt_payment.assert_not_called()
