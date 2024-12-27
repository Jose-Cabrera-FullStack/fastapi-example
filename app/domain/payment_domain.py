from datetime import datetime


class PaymentDomain:

    @staticmethod
    def formating_fields(payment: dict, status: str) -> dict:
        """Format fields and set missing ones to None if necessary, and prepare them for updating.
        Args:
            payment (dict): The payment information.
            status (str): The status of the payment.
        Returns:
            dict: The formatted payment data ready for updating.
        """

        all_fields = {
            "fechaTxn": None,
            "horaTxn": None,
            "canalPago": None,
            "codigoBanco": None,
            "numOperacionBanco": None,
            "formaPago": None,
            "tipoConsulta": None,
            "idConsulta": None,
            "codigoProducto": None,
            "numDocumento": None,
            "importePagado": None,
            "monedaDoc": None,
            "codigoEmpresa": None,
            "status": status
        }

        formatted_payment = {**all_fields, **payment}

        if 'fechaTxn' in formatted_payment and formatted_payment['fechaTxn']:
            formatted_payment['fechaTxn'] = datetime.strptime(
                formatted_payment['fechaTxn'], '%d%m%Y'
            )

        update_payment_data = {
            "operation_bank_number": formatted_payment.get("numOperacionBanco"),
            "emition_date": formatted_payment.get("fechaTxn"),
            "bank_code": formatted_payment.get("codigoBanco"),
            "gateway": formatted_payment.get("formaPago"),
            "payment_type": formatted_payment.get("tipoConsulta"),
            "payment_amount": formatted_payment.get("importePagado"),
            "status": formatted_payment.get("status"),
        }

        return update_payment_data
