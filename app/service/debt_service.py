import logging

from app.adapter import DebtAdapter
from app.schemas.request import DebtStatusPOSTRequest


class DebtService:
    @staticmethod
    async def debt_status(debt: dict) -> dict:
        """ Check debts of a client

        Args:
            debt (dict): Debt data

        Returns:
            dict: Updated Debt data
        """
        try:
            validated_debt_request = DebtStatusPOSTRequest(**debt).dict()
            
            return await DebtAdapter.checking_debt_status(validated_debt_request)
        
        except Exception as e:
            logging.error(e)
            return {
                "Cliente": "",
                "codigoRespuesta": "99",
                "descripcionResp": "ERROR DESCONOCIDO",
                "deudasPendientes": []
            }