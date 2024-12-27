from fastapi import FastAPI

from app.database.config import database
from app.schemas.request import DebtStatusPOSTRequest
from app.schemas.request.payment_post_request import PaymentUpdatePOSTRequest
from app.schemas.response import DebtUpdatePOSTResponse, DebtStatusPOSTResponse
from app.schemas.request import RevertDebtPaymentPOSTRequest
from app.schemas.response import RevertDebtPaymentPOSTResponse
from app.service import PaymentService, DebtService


app = FastAPI(
    title="Payment Service",
    description="API to validate the Client Debts status",
    version="0.1.0",
    docs_url="/",
)

API_VERSION = "v1"


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.post(
    f"/{API_VERSION}/debt-status",
    response_model=DebtStatusPOSTResponse,
    status_code=200
)
async def payment_post_endpoint(post_request: DebtStatusPOSTRequest):
    """
    POST endpoint to check the debts of a client

    Args:
        post_request (POSTRequest): Request body

    Returns:
        DebtStatusPOSTResponse: Response body

    Examples:

        {
            "CodigoRespuesta": "00",
            "DescRespuesta": "OK",
            "deudasPendientes": [
                {
                    "CodigoProducto": "001",
                    "NumDocumento": "B01-0000000001",
                    "DescDocumento": "FACTURA",
                    "FechaVencimiento": "11092019",
                    "FechaEmision": "11092019",
                    "Deuda": 2080.00,
                    "Mora": 0.00,
                    "GastosAdm": 0.00,
                    "PagoMinimo": 100.00,
                    "Periodo": "00",
                    "Anio": "2019",
                    "Cuota": "00",
                    "MonedaDoc": "1"
                }
            ]
        }

    """
    service_payment = await DebtService.debt_status(post_request.dict())
    
    return DebtStatusPOSTResponse(**service_payment)


@app.post(
    f"/{API_VERSION}/update-debt-payment",
    response_model=DebtUpdatePOSTResponse,
    status_code=200
)
async def update_debt_payment_endpoint(post_request: PaymentUpdatePOSTRequest):
    """
    POST endpoint to check the debts of a client

    Args:
        post_request (POSTRequest): Request body

    Returns:
        POSTResponse: Response body

    Examples:

        {
            "fechaTxn": "01012024",
            "horaTxn": "235959",
            "canalPago": "0001",
            "codigoBanco": "0001",
            "numOperacionERP": "654321234567",
            "formaPago": "00",
            "tipoConsulta": "1",
            "idConsulta": "10000002",
            "codigoProducto": "MGK",
            "numDocumento": "B01-0000000002",
            "importePagado": 100.00,
            "monedaDoc": "1",
            "codigoEmpresa": "512"
        }
    """

    debt_service = await PaymentService.update_debt_payment(post_request.dict())

    return DebtUpdatePOSTResponse(**debt_service)


@app.post(
    f"/{API_VERSION}/revert-debt-payment",
    response_model=RevertDebtPaymentPOSTResponse,
    status_code=200
)
async def revert_debt_payment_endpoint(post_request: RevertDebtPaymentPOSTRequest):
    """
    POST endpoint to check the debts of a client

    Args:
        post_request (POSTRequest): Request body

    Returns:
        POSTResponse: Response body

    Examples:
    """

    reverse_service = await PaymentService.revert_payment_debt(post_request.dict())

    return RevertDebtPaymentPOSTResponse(**reverse_service)
