import pytest
from pydantic import ValidationError

from app.schemas.response import (
    PendingDebts,
    DebtStatusPOSTResponse,
    DebtUpdatePOSTResponse
)


def test_pending_debts_valid_data():
    valid_data = {
        "CodigoProducto": "123",
        "NumDocumento": "1234567890123456",
        "DescDocumento": "Factura",
        "FechaVencimiento": "01012024",
        "FechaEmision": "01012023",
        "Deuda": 100.0,
        "Mora": 5.0,
        "GastosAdm": 2.0,
        "PagoMinimo": 50.0,
        "Periodo": "01",
        "Anio": "2024",
        "Cuota": "01",
        "MonedaDoc": "1"
    }
    pending_debt = PendingDebts(**valid_data)
    assert pending_debt.CodigoProducto == "123"


def test_pending_debts_invalid_codigo_producto():
    invalid_data = {
        "CodigoProducto": "12",
        "NumDocumento": "1234567890123456",
        "DescDocumento": "Factura",
        "FechaVencimiento": "01012024",
        "FechaEmision": "01012023",
        "Deuda": 100.0,
        "Mora": 5.0,
        "GastosAdm": 2.0,
        "PagoMinimo": 50.0,
        "Periodo": "01",
        "Anio": "2024",
        "Cuota": "01",
        "MonedaDoc": "1"
    }
    with pytest.raises(ValidationError) as exc_info:
        PendingDebts(**invalid_data)
    assert "El CodigoProducto debe tener una longitud de 3" in str(exc_info.value)


def test_pending_debts_invalid_num_documento():
    invalid_data = {
        "CodigoProducto": "123",
        "NumDocumento": "12345",
        "DescDocumento": "Factura",
        "FechaVencimiento": "01012024",
        "FechaEmision": "01012023",
        "Deuda": 100.0,
        "Mora": 5.0,
        "GastosAdm": 2.0,
        "PagoMinimo": 50.0,
        "Periodo": "01",
        "Anio": "2024",
        "Cuota": "01",
        "MonedaDoc": "1"
    }
    with pytest.raises(ValidationError) as exc_info:
        PendingDebts(**invalid_data)
    assert "El NumDocumento debe tener una longitud de 16" in str(exc_info.value)


def test_debt_status_post_response_valid_data():
    valid_data = {
        "Cliente": "John Doe",
        "CodigoRespuesta": "00",
        "DescRespuesta": "Operación exitosa",
        "deudasPendientes": [
            {
                "CodigoProducto": "123",
                "NumDocumento": "1234567890123456",
                "DescDocumento": "Factura",
                "FechaVencimiento": "01012024",
                "FechaEmision": "01012023",
                "Deuda": 100.0,
                "Mora": 5.0,
                "GastosAdm": 2.0,
                "PagoMinimo": 50.0,
                "Periodo": "01",
                "Anio": "2024",
                "Cuota": "01",
                "MonedaDoc": "1"
            }
        ]
    }
    response = DebtStatusPOSTResponse(**valid_data)
    assert response.CodigoRespuesta == "00"


def test_debt_status_post_response_invalid_codigo_respuesta():
    invalid_data = {
        "CodigoRespuesta": "0",
        "DescRespuesta": "Operación exitosa",
        "deudasPendientes": [
            {
                "CodigoProducto": "123",
                "NumDocumento": "1234567890123456",
                "DescDocumento": "Factura",
                "FechaVencimiento": "01012024",
                "FechaEmision": "01012023",
                "Deuda": 100.0,
                "Mora": 5.0,
                "GastosAdm": 2.0,
                "PagoMinimo": 50.0,
                "Periodo": "01",
                "Anio": "2024",
                "Cuota": "01",
                "MonedaDoc": "1"
            }
        ]
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTResponse(**invalid_data)
    assert "El codigoRespuesta debe tener una longitud de 2" in str(exc_info.value)


def test_debt_update_post_response_valid_data():
    valid_data = {
        "codigoRespuesta": "00",
        "nombreCliente": "John Doe",
        "numOperacionERP": "A123456789012",
        "descripcionResp": "Operación completada exitosamente"
    }
    response = DebtUpdatePOSTResponse(**valid_data)
    assert response.codigoRespuesta == "00"


def test_debt_update_post_response_invalid_codigo_respuesta():
    invalid_data = {
        "codigoRespuesta": "000",
        "nombreCliente": "John Doe",
        "numOperacionERP": "A123456789012",
        "descripcionResp": "Operación completada exitosamente"
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtUpdatePOSTResponse(**invalid_data)
    assert "El codigoRespuesta debe tener una longitud de 2" in str(exc_info.value)


def test_debt_update_post_response_invalid_nombre_cliente():
    invalid_data = {
        "codigoRespuesta": "00",
        "nombreCliente": "John Doe Exceeded Character Limit for the Field",
        "numOperacionERP": "A123456789012",
        "descripcionResp": "Operación completada exitosamente"
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtUpdatePOSTResponse(**invalid_data)
    assert "El nombreCliente no debe exceder los 30 caracteres" in str(exc_info.value)
