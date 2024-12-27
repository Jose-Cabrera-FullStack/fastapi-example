import pytest
from pydantic import ValidationError

from app.schemas.request.debt_post_request import DebtPOSTRequest, DebtStatusPOSTRequest


def test_debt_status_post_request_valid_data():
    valid_data = {
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoBanco": "1234",
        "codigoProducto": "123",
        "canalPago": "01",
        "codigoEmpresa": "001",
    }
    request = DebtStatusPOSTRequest(**valid_data)
    assert request.tipoConsulta == "1"
    assert request.idConsulta == "12345678901234"
    assert request.codigoBanco == "1234"
    assert request.codigoProducto == "123"
    assert request.canalPago == "01"
    assert request.codigoEmpresa == "001"


def test_debt_status_post_request_invalid_tipo_consulta():
    invalid_data = {
        "tipoConsulta": "12",
        "idConsulta": "12345678901234",
        "codigoBanco": "1234",
        "codigoProducto": "123",
        "canalPago": "01",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "tipoConsulta must be 1 character long" in str(exc_info.value)


def test_debt_status_post_request_invalid_id_consulta():
    invalid_data = {
        "tipoConsulta": "1",
        "idConsulta": "1234567890123456789",
        "codigoBanco": "1234",
        "codigoProducto": "123",
        "canalPago": "01",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "idConsulta must be less than 14 characters" in str(exc_info.value)


def test_debt_status_post_request_invalid_codigo_banco():
    invalid_data = {
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoBanco": "12",
        "codigoProducto": "123",
        "canalPago": "01",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "codigoBanco must be 4 characters long" in str(exc_info.value)


def test_debt_status_post_request_invalid_codigo_producto():
    invalid_data = {
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoBanco": "1234",
        "codigoProducto": "12",
        "canalPago": "01",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "codigoProducto must be 3 characters long" in str(exc_info.value)


def test_debt_status_post_request_invalid_canal_pago():
    invalid_data = {
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoBanco": "1234",
        "codigoProducto": "123",
        "canalPago": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "canalPago must be 2 characters long" in str(exc_info.value)


def test_debt_status_post_request_invalid_codigo_empresa():
    invalid_data = {
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoBanco": "1234",
        "codigoProducto": "123",
        "canalPago": "01",
        "codigoEmpresa": "01",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtStatusPOSTRequest(**invalid_data)
    assert "codigoEmpresa must be 3 characters long" in str(exc_info.value)


def test_debt_post_request_valid_data():
    valid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    request = DebtPOSTRequest(**valid_data)
    assert request.fechaTxn == "01012024"
    assert request.horaTxn == "235959"
    assert request.canalPago == "01"
    assert request.codigoBanco == "1234"
    assert request.numOperacionERP == "A123456789012"
    assert request.formaPago == "00"
    assert request.tipoConsulta == "1"
    assert request.idConsulta == "12345678901234"
    assert request.codigoProducto == "123"
    assert request.numDocumento == "B01-0000000002"
    assert request.importePagado == 100.00
    assert request.monedaDoc == "1"
    assert request.codigoEmpresa == "001"


def test_debt_post_request_invalid_fechatxn():
    invalid_data = {
        "fechaTxn": "24052",
        "horaTxn": "153105",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "fechaTxn must be 8 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_horatxn():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "2359",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "horaTxn must be 6 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_codigo_banco():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "123",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "codigoBanco must be 4 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_canal_pago():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "1",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "canalPago must be 2 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_num_operacion_erp():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012345678",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "numOperacionERP must be less than 15 characters" in str(exc_info.value)


def test_debt_post_request_invalid_forma_pago():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "0",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "formaPago must be 2 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_tipo_consulta():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "12",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "tipoConsulta must be 1 character long" in str(exc_info.value)


def test_debt_post_request_invalid_id_consulta():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "123456789012345678",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "idConsulta must be less than 14 characters" in str(exc_info.value)


def test_debt_post_request_invalid_codigo_producto():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "12",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "codigoProducto must be 3 characters long" in str(exc_info.value)


def test_debt_post_request_invalid_num_documento():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-00000000022222222222",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "numDocumento must be less than 20 characters" in str(exc_info.value)


def test_debt_post_request_invalid_moneda_doc():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "12",
        "codigoEmpresa": "001",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "monedaDoc must be 1 character long" in str(exc_info.value)


def test_debt_post_request_invalid_codigo_empresa():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "canalPago": "01",
        "codigoBanco": "1234",
        "numOperacionERP": "A123456789012",
        "formaPago": "00",
        "tipoConsulta": "1",
        "idConsulta": "12345678901234",
        "codigoProducto": "123",
        "numDocumento": "B01-0000000002",
        "importePagado": 100.00,
        "monedaDoc": "1",
        "codigoEmpresa": "01",
    }
    with pytest.raises(ValidationError) as exc_info:
        DebtPOSTRequest(**invalid_data)
    assert "codigoEmpresa must be 3 characters long" in str(exc_info.value)
