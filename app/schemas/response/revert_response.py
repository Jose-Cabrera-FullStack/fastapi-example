import re

from pydantic import BaseModel, validator


class RevertDebtPaymentPOSTResponse(BaseModel):
    codigoRespuesta: str
    nombreCliente: str
    numOperacionERP: str
    descripcionResp: str

    @validator('codigoRespuesta')
    def validate_codigo_respuesta(cls, value):
        if len(value) != 2:
            raise ValueError('CodigoRespuesta debe tener exactamente 2 caracteres.')
        if not re.match(r'^[A-Za-z0-9]*$', value):
            raise ValueError('CodigoRespuesta debe ser alfanumérico.')
        return value

    @validator('nombreCliente')
    def validate_nombre_cliente(cls, value):
        if len(value) > 30:
            raise ValueError('NombreCliente no debe tener más de 30 caracteres.')
        if not re.match(r'^[A-Za-z0-9 .]*$', value):
            raise ValueError('NombreCliente debe contener solo letras, números, espacios y puntos.')
        return value

    @validator('numOperacionERP')
    def validate_num_operacion_erp(cls, value):
        if len(value) > 9:
            raise ValueError('NumOperacionERP no debe tener más de 9 caracteres.')
        if not re.match(r'^[A-Za-z0-9-]*$', value):
            raise ValueError('NumOperacionERP debe ser numérico y puede empezar con 0.')
        return value

    @validator('descripcionResp')
    def validate_descripcion_resp(cls, value):
        if len(value) > 200:
            raise ValueError('DescripcionResp no debe tener más de 200 caracteres.')
        return value
