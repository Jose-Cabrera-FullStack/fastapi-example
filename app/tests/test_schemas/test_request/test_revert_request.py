import pytest
from pydantic import ValidationError

from app.schemas.request.revert_post_request import RevertDebtPaymentPOSTRequest


def test_valid_revert_debt_payment_request():
    valid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }

    request = RevertDebtPaymentPOSTRequest(**valid_data)
    assert request.fechaTxn == "01012024"
    assert request.horaTxn == "235959"
    assert request.codigoBanco == "1234"
    assert request.tipoConsulta == "5"
    assert request.idConsulta == "12345678901234"
    assert request.numOperacionBanco == "123456789012"
    assert request.numDocumento == "AB-1234567890123"
    assert request.codigoEmpresa == "512"


def test_invalid_fecha_txn_length():
    invalid_data = {
        "fechaTxn": "1012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "fechaTxn must be equal to 8 characters." in str(exc_info.value)


def test_invalid_fecha_txn_format():
    invalid_data = {
        "fechaTxn": "20240101",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "fechaTxn must be in the format DDMMAAAA." in str(exc_info.value)


def test_invalid_hora_txn_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "23595",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "horaTxn must be equal to 6 characters." in str(exc_info.value)


def test_invalid_hora_txn_format():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "999999",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "horaTxn must be in the format HHMMSS." in str(exc_info.value)


def test_invalid_codigo_banco_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "12",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "codigoBanco must have 4 characters." in str(exc_info.value)


def test_invalid_codigo_banco():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "12*4",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "codigoBanco must be alphanumeric." in str(exc_info.value)


def test_invalid_tipo_consulta_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "55",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "tipoConsulta must have 1 character." in str(exc_info.value)


def test_invalid_tipo_consulta():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "*",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "tipoConsulta must be alphanumeric." in str(exc_info.value)


def test_invalid_id_consulta_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "1234567890123456",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "idConsulta must not exceed 14 characters." in str(exc_info.value)


def test_invalid_id_consulta_with_special_character():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "abc*123",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "idConsulta must be alphanumeric and should not contain special characters, spaces, accents, or the letter Ñ." in str(exc_info.value)


def test_invalid_num_operacion_banco_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "1234567890123456",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "numOperacionBanco must not exceed 12 characters." in str(exc_info.value)


def test_invalid_num_documento_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-123456789012345678",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "numDocumento must not exceed 16 characters." in str(exc_info.value)


def test_invalid_codigo_empresa_length():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "51",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "codigoEmpresa must have exactly 3 characters." in str(exc_info.value)


def test_invalid_num_operacion_banco():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "12345*789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "numOperacionBanco must be alphanumeric." in str(exc_info.value)


def test_invalid_num_documento():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB&1234567890123",
        "codigoEmpresa": "512",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "numDocumento must be alphanumeric or contain hyphens." in str(exc_info.value)


def test_invalid_codigo_empresa():
    invalid_data = {
        "fechaTxn": "01012024",
        "horaTxn": "235959",
        "codigoBanco": "1234",
        "tipoConsulta": "5",
        "idConsulta": "12345678901234",
        "numOperacionBanco": "123456789012",
        "numDocumento": "AB-1234567890123",
        "codigoEmpresa": "51A",
    }
    with pytest.raises(ValidationError) as exc_info:
        RevertDebtPaymentPOSTRequest(**invalid_data)
    assert "codigoEmpresa must be numeric." in str(exc_info.value)
