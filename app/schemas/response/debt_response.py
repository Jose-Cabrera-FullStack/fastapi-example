from typing import List

from pydantic import BaseModel, validator


class PendingDebts(BaseModel):
    CodigoProducto: str
    NumDocumento: str
    DescDocumento: str
    FechaVencimiento: str
    FechaEmision: str
    Deuda: float
    Mora: float
    GastosAdm: float
    PagoMinimo: float
    Periodo: str
    Anio: str
    Cuota: str
    MonedaDoc: str

    @validator('CodigoProducto')
    def codigo_producto_length(cls, value):
        if value is None:
            raise ValueError('El CodigoProducto no puede ser nulo')

        if len(value) != 3:
            raise ValueError('El CodigoProducto debe tener una longitud de 3')

        return value

    @validator('NumDocumento')
    def num_documento_length(cls, value):
        if value is None:
            raise ValueError('El NumDocumento no puede ser nulo')

        if len(value) < 16:
            raise ValueError('El NumDocumento debe tener una longitud de 16')

        return value

    @validator('DescDocumento')
    def desc_documento_length(cls, value):
        if value is None:
            raise ValueError('El DescDocumento no puede ser nulo')

        if len(value) > 20:
            raise ValueError('El DescDocumento no debe exceder los 20 caracteres')

        return value

    @validator('FechaVencimiento')
    def fecha_vencimiento_length(cls, value):
        if value is None:
            raise ValueError('El FechaVencimiento no puede ser nulo')

        if len(value) != 8:
            raise ValueError('El FechaVencimiento debe tener una longitud de 8')

        return value

    @validator('FechaEmision')
    def fecha_emision_length(cls, value):
        if value is None:
            raise ValueError('El FechaEmision no puede ser nulo')

        if len(value) != 8:
            raise ValueError('El FechaEmision debe tener una longitud de 8')

        return value

    @validator('Periodo')
    def periodo_length(cls, value):
        if value is None:
            raise ValueError('El Periodo no puede ser nulo')

        if len(value) != 2:
            raise ValueError('El Periodo debe tener una longitud de 2')

        return value

    @validator('Anio')
    def anio_length(cls, value):
        if value is None:
            raise ValueError('El Anio no puede ser nulo')

        if len(value) != 4:
            raise ValueError('El Anio debe tener una longitud de 4')

        return value

    @validator('Cuota')
    def cuota_length(cls, value):
        if value is None:
            raise ValueError('El Cuota no puede ser nulo')

        if len(value) != 2:
            raise ValueError('El Cuota debe tener una longitud de 2')

        return value

    @validator('MonedaDoc')
    def moneda_doc_length(cls, value):
        if value is None:
            raise ValueError('El MonedaDoc no puede ser nulo')

        if len(value) != 1:
            raise ValueError('El MonedaDoc debe tener una longitud de 1')

        return value


class DebtStatusPOSTResponse(BaseModel):
    Cliente: str
    CodigoRespuesta: str
    DescRespuesta: str
    deudasPendientes: List[PendingDebts]

    @validator('CodigoRespuesta')
    def codigo_respuesta_length(cls, value):
        if value is None:
            raise ValueError('El codigoRespuesta no puede ser nulo')

        if len(value) != 2:
            raise ValueError('El codigoRespuesta debe tener una longitud de 2')

        return value

    @validator('DescRespuesta')
    def descripcion_resp_length(cls, value):
        if value is None:
            raise ValueError('El descripcionResp no puede ser nulo')

        if len(value) > 30:
            raise ValueError('El descripcionResp no debe exceder los 30 caracteres')
        return value


class DebtUpdatePOSTResponse(BaseModel):
    codigoRespuesta: str
    nombreCliente: str
    numOperacionERP: str
    descripcionResp: str

    @classmethod
    def _no_none_value(cls, value, mensaje_error):
        if value is None:
            raise ValueError(mensaje_error)

    @validator('codigoRespuesta')
    def codigo_respuesta_length(cls, value):
        cls._no_none_value(value, 'El codigoRespuesta no puede ser nulo')

        if len(value) != 2:
            raise ValueError('El codigoRespuesta debe tener una longitud de 2')

        return value

    @validator('nombreCliente')
    def descripcion_resp_length(cls, value):
        cls._no_none_value(value, 'El nombreCliente no puede ser nulo')

        if len(value) > 30:
            raise ValueError('El nombreCliente no debe exceder los 30 caracteres')
        return value

    @validator('numOperacionERP')
    def num_operacion_erp_length(cls, value):
        cls._no_none_value(value, 'El numOperacionERP no puede ser nulo')

        if len(value) > 13:
            raise ValueError('El numOperacionERP no debe exceder los 13 caracteres')

        return value

    @validator('descripcionResp')
    def num_operacion_resp_length(cls, value):
        cls._no_none_value(value, 'El descripcionResp no puede ser nulo')

        if len(value) > 200:
            raise ValueError('El descripcionResp no debe exceder los 200 caracteres')

        return value
