import re
from datetime import datetime

from pydantic import BaseModel, validator


class RevertDebtPaymentPOSTRequest(BaseModel):
    fechaTxn: str
    horaTxn: str
    codigoBanco: str
    tipoConsulta: str
    idConsulta: str
    numOperacionBanco: str
    numDocumento: str
    codigoEmpresa: str

    @validator('fechaTxn')
    def validate_fecha_txn(cls, value):
        if len(value) != 8:
            raise ValueError('fechaTxn must be equal to 8 characters.')
        try:
            datetime.strptime(value, "%d%m%Y")
        except ValueError as exc:
            raise ValueError('fechaTxn must be in the format DDMMAAAA.') from exc
        return value

    @validator('horaTxn')
    def validate_hora_txn(cls, value):
        if len(value) != 6:
            raise ValueError('horaTxn must be equal to 6 characters.')
        try:
            datetime.strptime(value, "%H%M%S")
        except ValueError as exc:
            raise ValueError('horaTxn must be in the format HHMMSS.') from exc
        return value

    @validator('codigoBanco')
    def validate_codigo_banco(cls, value):
        if len(value) != 4:
            raise ValueError('codigoBanco must have 4 characters.')
        if not re.match(r'^[A-Za-z0-9]*$', value):
            raise ValueError('codigoBanco must be alphanumeric.')
        return value

    @validator('tipoConsulta')
    def validate_tipo_consulta(cls, value):
        if len(value) != 1:
            raise ValueError('tipoConsulta must have 1 character.')
        if not re.match(r'^[A-Za-z0-9]$', value):
            raise ValueError('tipoConsulta must be alphanumeric.')
        return value

    @validator('idConsulta')
    def validate_id_consulta(cls, value):
        if len(value) > 14:
            raise ValueError('idConsulta must not exceed 14 characters.')
        if not re.match(r'^[A-Za-z0-9]*$', value):
            raise ValueError(
                'idConsulta must be alphanumeric and should not contain special characters, spaces, accents, or the letter Ñ.'
            )
        return value

    @validator('numOperacionBanco')
    def validate_num_operacion_banco(cls, value):
        if len(value) > 12:
            raise ValueError('numOperacionBanco must not exceed 12 characters.')
        if not re.match(r'^[A-Za-z0-9]*$', value):
            raise ValueError('numOperacionBanco must be alphanumeric.')
        return value

    @validator('numDocumento')
    def validate_num_documento(cls, value):
        if len(value) > 16:
            raise ValueError('numDocumento must not exceed 16 characters.')
        if not re.match(r'^[A-Za-z0-9-]*$', value):
            raise ValueError('numDocumento must be alphanumeric or contain hyphens.')
        return value

    @validator('codigoEmpresa')
    def validate_codigo_empresa(cls, value):
        if len(value) != 3:
            raise ValueError('codigoEmpresa must have exactly 3 characters.')
        if not re.match(r'^\d{3}$', value):
            raise ValueError('codigoEmpresa must be numeric.')
        return value
