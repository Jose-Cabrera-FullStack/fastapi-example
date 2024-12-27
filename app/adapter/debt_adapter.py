import logging

from app.database.models import Debt, Client
from app.domain import DebtDomain
from app.infrastructure import DebtRepository
from app.infrastructure import ClientRepository

class DebtAdapter:
    @staticmethod
    async def checking_debt_status(debt_data: dict) -> list[dict]:
        """
        Check the debt status of a client

        Args:
            debt_data (dict): Debt data

        Returns:
            list[dict]: List of debts
        """

        try:
            
            client = await ClientRepository.get_client_by_document_identifier(debt_data["idConsulta"])
            
            if not client:
                return {
                    "Cliente": "",
                    "CodigoRespuesta": "16",
                    "DescRespuesta": "OK",
                    "deudasPendientes": []
                }
            
            debts = await DebtRepository.get_debts_by_client_identifier(debt_data["idConsulta"], debt_data["codigoProducto"])
            
            if not debts:
                return {
                    "Cliente": "",
                    "CodigoRespuesta": "22",
                    "DescRespuesta": "CLIENTE SIN DEUDAS PENDIENTES",
                    "deudasPendientes": []
                }
                   
            return DebtAdapter._formating_debts(debts, client)

        except Exception as e:
            logging.error(e)
            return {
                "Cliente": "",
                "codigoRespuesta": "99",
                "descripcionResp": "ERROR DESCONOCIDO",
                "deudasPendientes": []
            }

    @staticmethod
    def _formating_debts(debts: list[Debt], cliente: Client) -> dict:
        """
        Format the debts data

        Args:
            debts (list): List of debts

        Returns:
            dict: Formatted response data
        """

        debt_list = []
        
        for debt in debts:
            debt_data = {
                "CodigoProducto": debt.product_code,
                "NumDocumento": debt.operation_identifier,
                "DescDocumento": debt.description,
                "FechaVencimiento": debt.expiration_date.strftime('%d%m%Y'),
                "FechaEmision": debt.emition_date.strftime('%d%m%Y'),
                "Deuda": float(debt.total_debt),
                "Mora": float(debt.default_debt),
                "GastosAdm": float(debt.administration_expenses),
                "PagoMinimo": float(debt.minimum_payment),
                "Periodo": debt.period,
                "Anio": str(debt.date_created.year),
                "Cuota": debt.fee,
                "MonedaDoc": debt.currency,
            }

            debt_list.append(debt_data)
            
        print(f"Valor de Cliente antes de la validación: {cliente}")
        return {
            "Cliente": cliente.name,
            "CodigoRespuesta": "00",
            "DescRespuesta": "OK",
            "deudasPendientes": debt_list
        }
