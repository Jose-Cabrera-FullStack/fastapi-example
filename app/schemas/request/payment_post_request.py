from pydantic import (
    BaseModel,
    Field,
    validator
)


class PaymentUpdatePOSTRequest(BaseModel):
    fechaTxn: str = Field(..., description="Transaction date in YYYYMMDD format")
    horaTxn: str = Field(..., description="Transaction time in HHMMSS format")
    canalPago: str = Field(..., description="Payment channel")
    codigoBanco: str = Field(..., description="Bank code")
    numOperacionBanco: str = Field(..., description="ERP operation number")
    formaPago: str = Field(..., description="Payment method")
    tipoConsulta: str = Field(..., description="Query type")
    idConsulta: str = Field(..., description="Query ID")
    codigoProducto: str = Field(..., description="Product code")
    numDocumento: str = Field(..., description="Document number")
    importePagado: float = Field(..., description="Paid amount")
    monedaDoc: str = Field(..., description="Document currency")
    codigoEmpresa: str = Field(..., description="Company code")

    @validator("fechaTxn")
    def fechaTxn_length(cls, value: str) -> str:
        if len(value) != 8:
            raise ValueError("Must have length 8")
        return value

    @validator("horaTxn")
    def horaTxn_length(cls, value: str) -> str:
        if len(value) != 6:
            raise ValueError("Must have length 6")
        return value

    @validator("canalPago")
    def canalPago_length(cls, value: str) -> str:
        if len(value) != 2:
            raise ValueError("Must have length 2")
        return value

    @validator("codigoBanco")
    def codigoBanco_length(cls, value: str) -> str:
        if len(value) != 4:
            raise ValueError("Must have length 4")
        return value

    @validator("numOperacionBanco")
    def numOperacionBanco_length(cls, value: str) -> str:
        if len(value) != 12:
            raise ValueError("Must have length 12")
        return value

    @validator("formaPago")
    def formaPago_length(cls, value: str) -> str:
        if len(value) != 2:
            raise ValueError("Must have length 2")
        return value

    @validator("tipoConsulta")
    def tipoConsulta_length(cls, value: str) -> str:
        if len(value) != 1:
            raise ValueError("Must have length 1")
        return value

    @validator("idConsulta")
    def idConsulta_length(cls, value: str) -> str:
        if len(value) > 14:
            raise ValueError("Must have length 14")
        return value

    @validator("codigoProducto")
    def codigoProducto_length(cls, value: str) -> str:
        if len(value) != 3:
            raise ValueError("Must have length 3")
        return value

    @validator("numDocumento")
    def numDocumento_length(cls, value: str) -> str:
        if len(value) > 16:
            raise ValueError("Must have length 16")
        return value

    @validator("importePagado")
    def importePagado_length(cls, value: float) -> float:
        if len(str(value).replace('.', '')) > 12:
            raise ValueError("Must be less than 12 numbers")
        return value

    @validator("monedaDoc")
    def monedaDoc_length(cls, value: str) -> str:
        if len(value) != 1:
            raise ValueError("Must have length 1")
        return value

    @validator("codigoEmpresa")
    def codigoEmpresa_length(cls, value: str) -> str:
        if len(value) != 3:
            raise ValueError("Must have length 3")
        return value
