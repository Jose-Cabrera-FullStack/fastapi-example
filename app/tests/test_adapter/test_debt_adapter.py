from unittest.mock import AsyncMock, patch

import pytest

from app.adapter import DebtAdapter
from app.tests.mock import debt_instance, client_instance


@pytest.mark.asyncio
@patch('app.infrastructure.DebtRepository.get_debts_by_client_identifier', new_callable=AsyncMock)
@patch('app.infrastructure.ClientRepository.get_client_by_document_identifier', new_callable=AsyncMock)
async def test_checking_debt_status_success(mock_get_client, mock_get_debts):

    mock_get_client.return_value = client_instance
    mock_get_debts.return_value = [debt_instance]
    
    debt_data = {
        "idConsulta": "123320000013",
        "codigoProducto": "OJw",
    }

    result = await DebtAdapter.checking_debt_status(debt_data)

    expected_result = {
        "Cliente": "John Doe",
        "CodigoRespuesta": "00",
        "DescRespuesta": "OK",
        "deudasPendientes": [
            {
                "CodigoProducto": "OJw",
                "NumDocumento": "123320000013",
                "DescDocumento": "Bank little rest.",
                "FechaVencimiento": "02092024",
                "FechaEmision": "26042021",
                "Deuda": 75663.38,
                "Mora": 5000.00,
                "GastosAdm": 585.86,
                "PagoMinimo": 273.96,
                "Periodo": "02",
                "Anio": "2023",
                "Cuota": "00",
                "MonedaDoc": "2",
            }
        ]
    }

    assert result["Cliente"] == expected_result["Cliente"]
    assert result["deudasPendientes"][0]["Anio"] == expected_result["deudasPendientes"][0]["Anio"]


@pytest.mark.asyncio
@patch('app.infrastructure.DebtRepository.get_debts_by_client_identifier', new_callable=AsyncMock)
@patch('app.infrastructure.ClientRepository.get_client_by_document_identifier', new_callable=AsyncMock)
async def test_checking_debt_status_failure(mock_get_client, mock_get_debts):
    mock_get_debts.side_effect = Exception("Error al obtener las deudas")

    debt_data = {"idConsulta": "123456789"}

    result = await DebtAdapter.checking_debt_status(debt_data)

    expected_result = {
        "codigoRespuesta": "99",
        "descripcionResp": "ERROR DESCONOCIDO",
        "numOperacionERP": "000258967",
        "numOperacionResp": "654321234567"
    }

    assert result["codigoRespuesta"] == expected_result["codigoRespuesta"]
    assert result["descripcionResp"] == expected_result["descripcionResp"]


@pytest.mark.asyncio
@patch('app.infrastructure.DebtRepository.get_debts_by_client_identifier', new_callable=AsyncMock)
async def test_formating_debts(mock_get_debts):
    mock_get_debts.return_value = [debt_instance]

    debts = [debt_instance]
    client =  client_instance

    result = DebtAdapter._formating_debts(debts, client)

    expected_result = {
        "Cliente": "John Doe",
        "CodigoRespuesta": "00",
        "DescRespuesta": "OK",
        "deudasPendientes": [
            {
                "CodigoProducto": "OJw",
                "NumDocumento": "123320000013",
                "DescDocumento": "Bank little rest.",
                "FechaVencimiento": "02092024",
                "FechaEmision": "26042021",
                "Deuda": 75663.38,
                "Mora": 5000.00,
                "GastosAdm": 585.86,
                "PagoMinimo": 273.96,
                "Periodo": "02",
                "Anio": "2023",
                "Cuota": "00",
                "MonedaDoc": "2",
            }
        ]
    }

    assert result["Cliente"] == expected_result["Cliente"]
    assert result["deudasPendientes"][0]["CodigoProducto"] == expected_result["deudasPendientes"][0]["CodigoProducto"]
