import pytest
from pydantic import ValidationError

from app.schemas.request.payment_post_request import PaymentUpdatePOSTRequest


def test_payment_update_post_request_valid_data():
    valid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    request = PaymentUpdatePOSTRequest(**valid_data)
    assert request.fechaTxn == "20240101"
    assert request.horaTxn == "235959"
    assert request.canalPago == "01"
    assert request.codigoBanco == "1234"
    assert request.numOperacionBanco == "A12345678901"
    assert request.formaPago == "01"
    assert request.tipoConsulta == "1"
    assert request.idConsulta == "12345678901234"
    assert request.codigoProducto == "123"
    assert request.numDocumento == "B01-0000000002"
    assert request.importePagado == 100.00
    assert request.monedaDoc == "1"
    assert request.codigoEmpresa == "001"


def test_payment_update_post_request_invalid_fechaTxn():
    invalid_data = {
        "fechaTxn": "202401",  # Longitud incorrecta, no cumple con la validación
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 8" in str(exc_info.value)


def test_payment_update_post_request_invalid_horaTxn():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "2359",  # Longitud incorrecta, no cumple con la validación
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 6" in str(exc_info.value)


def test_payment_update_post_request_invalid_canalPago():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "1",  # Longitud incorrecta
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 2" in str(exc_info.value)


def test_payment_update_post_request_invalid_codigoBanco():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "123",  # Longitud incorrecta
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 4" in str(exc_info.value)


def test_payment_update_post_request_invalid_numOperacionBanco():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A1234567890",  # Longitud incorrecta
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 12" in str(exc_info.value)


def test_payment_update_post_request_invalid_formaPago():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "1",  # Longitud incorrecta
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 2" in str(exc_info.value)


def test_payment_update_post_request_invalid_tipoConsulta():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "12",  # Longitud incorrecta
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 1" in str(exc_info.value)


def test_payment_update_post_request_invalid_idConsulta():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "1234567890123456789",  # Longitud incorrecta
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 14" in str(exc_info.value)


def test_payment_update_post_request_invalid_codigoProducto():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "12",  # Longitud incorrecta
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 3" in str(exc_info.value)


def test_payment_update_post_request_invalid_numDocumento():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-000000000212345",  # Longitud incorrecta
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 16" in str(exc_info.value)


def test_payment_update_post_request_invalid_importePagado():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 1234567890123.45,  # Número demasiado grande
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must be less than 12 numbers" in str(exc_info.value)


def test_payment_update_post_request_invalid_monedaDoc():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "12",  # Longitud incorrecta
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 1" in str(exc_info.value)


def test_payment_update_post_request_invalid_codigoEmpresa():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionBanco": "A12345678901",
        "formaPago": "01",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "12",  # Longitud incorrecta
    }
    with pytest.raises(ValidationError) as exc_info:
        PaymentUpdatePOSTRequest(**invalid_data)
    assert "Must have length 3" in str(exc_info.value)
