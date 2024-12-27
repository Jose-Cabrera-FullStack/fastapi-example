from pydantic import BaseModel, validator


class DebtStatusPOSTRequest(BaseModel):
    tipoConsulta: str
    idConsulta: str
    codigoBanco: str
    codigoProducto: str
    canalPago: str
    codigoEmpresa: str

    @validator("tipoConsulta")
    def validate_tipo_consulta(cls, value):
        if len(value) != 1:
            raise ValueError("tipoConsulta must be 1 character long")
        return value

    @validator("idConsulta")
    def validate_id_consulta(cls, value):
        if len(value) > 14:
            raise ValueError("idConsulta must be less than 14 characters")
        return value

    @validator("codigoBanco")
    def validate_codigo_banco(cls, value):
        if len(value) != 4:
            raise ValueError("codigoBanco must be 4 characters long")
        return value

    @validator("codigoProducto")
    def validate_codigo_producto(cls, value):
        if len(value) != 3:
            raise ValueError("codigoProducto must be 3 characters long")
        return value

    @validator("canalPago")
    def validate_canal_pago(cls, value):
        if len(value) != 2:
            raise ValueError("canalPago must be 2 characters long")
        return value

    @validator("codigoEmpresa")
    def validate_codigo_empresa(cls, value):
        if len(value) != 3:
            raise ValueError("codigoEmpresa must be 3 characters long")
        return value


class DebtPOSTRequest(BaseModel):
    fechaTxn: str
    horaTxn: str
    canalPago: str
    codigoBanco: str
    numOperacionERP: str
    formaPago: str
    tipoConsulta: str
    idConsulta: str
    codigoProducto: str
    numDocumento: str
    importePagado: float
    monedaDoc: str
    codigoEmpresa: str

    @validator("fechaTxn")
    def validate_fechatxn(cls, value):
        if len(value) != 8:
            raise ValueError("fechaTxn must be 8 characters long")
        return value

    @validator("horaTxn")
    def validate_horatxn(cls, value):
        if len(value) != 6:
            raise ValueError("horaTxn must be 6 characters long")
        return value

    @validator("canalPago")
    def validate_canal_pago(cls, value):
        if len(value) != 2:
            raise ValueError("canalPago must be 2 characters long")
        return value

    @validator("codigoBanco")
    def validate_codigo_banco(cls, value):
        if len(value) != 4:
            raise ValueError("codigoBanco must be 4 characters long")
        return value

    @validator("numOperacionERP")
    def validate_num_operacion_erp(cls, value):
        if len(value) > 15:
            raise ValueError("numOperacionERP must be less than 15 characters")
        return value

    @validator("formaPago")
    def validate_forma_pago(cls, value):
        if len(value) != 2:
            raise ValueError("formaPago must be 2 characters long")
        return value

    @validator("tipoConsulta")
    def validate_tipo_consulta(cls, value):
        if len(value) != 1:
            raise ValueError("tipoConsulta must be 1 character long")
        return value

    @validator("idConsulta")
    def validate_id_consulta(cls, value):
        if len(value) > 14:
            raise ValueError("idConsulta must be less than 14 characters")
        return value

    @validator("codigoProducto")
    def validate_codigo_producto(cls, value):
        if len(value) != 3:
            raise ValueError("codigoProducto must be 3 characters long")
        return value

    @validator("numDocumento")
    def validate_num_documento(cls, value):
        if len(value) > 20:
            raise ValueError("numDocumento must be less than 20 characters")
        return value

    @validator("monedaDoc")
    def validate_moneda_doc(cls, value):
        if len(value) != 1:
            raise ValueError("monedaDoc must be 1 character long")
        return value

    @validator("codigoEmpresa")
    def validate_codigo_empresa(cls, value):
        if len(value) != 3:
            raise ValueError("codigoEmpresa must be 3 characters long")
        return value
