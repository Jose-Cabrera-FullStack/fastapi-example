from datetime import datetime

import ormar

from app.database.config import BaseMeta


class Client(ormar.Model):
    class Meta(BaseMeta):
        tablename = "client"

    document_identifier: str = ormar.String(
        primary_key=True,
        unique=True,
        nullable=False,
        max_length=14,
        name="document_identifier",
        description="Número de documento de identificación del cliente. Ejemplo: 10000001"
    )
    name: str = ormar.String(
        max_length=255,
        nullable=False,
        name="name",
        description="Nombre completo del cliente"
    )
    company: str = ormar.String(
        max_length=255,
        nullable=True,
        name="company",
        description="Nombre de la empresa asociada al cliente"
    )
    product_type: str = ormar.String(
        max_length=255,
        nullable=True,
        name="product_type",
        description="Tipo de producto que utiliza el cliente"
    )

    date_created: datetime = ormar.DateTime(
        default=datetime.now,
        name="date_created",
        description="Fecha de creación del registro del cliente"
    )
    date_updated: datetime = ormar.DateTime(
        default=datetime.now,
        onupdate=datetime.now,
        name="date_updated",
        description="Fecha de la última actualización del registro del cliente"
    )


class Debt(ormar.Model):
    class Meta(BaseMeta):
        tablename = "debt"

    operation_identifier: str = ormar.String(
        primary_key=True,
        max_length=16,
        nullable=False,
        name="operation_identifier",
        description="Identificador único de la operación de la deuda"
    )

    client: Client = ormar.ForeignKey(
        Client,
        related_name="debts",
        nullable=False,
        name="client",
        description="Identificador del cliente asociado con la deuda"
    )

    description: str = ormar.String(
        max_length=255,
        nullable=False,
        name="description",
        description="Descripción de la deuda. Ejemplo: FACTURA"
    )

    emition_date: datetime = ormar.DateTime(
        nullable=False,
        name="emition_date",
        description="Fecha y hora en que se genero la deuda"
    )

    expiration_date: datetime = ormar.DateTime(
        nullable=False,
        name="expiration_date",
        description="Fecha y hora en que expira la deuda"
    )

    total_debt: float = ormar.Decimal(
        max_digits=12,
        decimal_places=2,
        nullable=False,
        name="total_debt",
        description="Monto total a pagar en la transacción"
    )

    default_debt: float = ormar.Decimal(
        max_digits=12,
        decimal_places=2,
        nullable=False,
        name="default_debt",
        description="Monto de Mora asociado a la deuda"
    )

    administration_expenses: float = ormar.Decimal(
        max_digits=10,
        decimal_places=2,
        nullable=False,
        name="administration_expenses",
        description="Gastos administrativos asociados a la deuda"
    )

    minimum_payment: float = ormar.Decimal(
        max_digits=10,
        decimal_places=2,
        nullable=False,
        name="minimum_payment",
        description="Pago mínimo requerido para la deuda"
    )

    period: str = ormar.String(
        max_length=2,
        nullable=False,
        name="period",
        description="Periodo de pago de la deuda"
    )

    fee: str = ormar.String(
        max_length=2,
        nullable=False,
        name="fee",
        description="Cuota de pago asociada a la deuda"
    )

    product_code: str = ormar.String(
        max_length=3,
        nullable=False,
        name="product_code",
        description="Código del producto asociado con el pago. Ejemplo: 512"
    )

    currency: str = ormar.String(
        max_length=10,
        nullable=False,
        name="currency",
        description="Moneda utilizada para el pago (por ejemplo, USD, EUR)"
    )

    date_created: datetime = ormar.DateTime(
        default=datetime.now,
        name="date_created",
        description="Fecha de creación del registro de pago"
    )

    created_by: str = ormar.String(
        max_length=255,
        nullable=True,
        name="created_by",
        description="Usuario o sistema que creó el registro de pago"
    )

    date_updated: datetime = ormar.DateTime(
        default=datetime.now,
        onupdate=datetime.now,
        name="date_updated",
        description="Fecha de la última actualización del registro de pago"
    )

    updated_by: str = ormar.String(
        max_length=255,
        nullable=True,
        name="updated_by",
        description="Usuario o sistema que actualizó por última vez el registro de pago"
    )


class Payment(ormar.Model):
    class Meta(BaseMeta):
        tablename = "payment"

    id: int = ormar.Integer(
        primary_key=True,
        description="Identificador único del pago en la base de datos"
    )

    debt: Debt = ormar.ForeignKey(
        Debt,
        related_name="payments",
        nullable=True,
        name="debt",
        description="Identificador del pago asociado con la deuda"
    )

    emition_date: datetime = ormar.DateTime(
        nullable=False,
        name="emition_date",
        description="Fecha de emisión del pago"
    )

    bank_code: str = ormar.String(
        max_length=255,
        nullable=False,
        name="bank_code",
        description="Código del banco involucrado en el pago"
    )

    operation_bank_number: str = ormar.String(
        max_length=12,
        nullable=False,
        unique=True,
        name="operation_bank_number",
        description="Número de operación del banco asociado con el pago"
    )

    gateway: str = ormar.String(
        max_length=255,
        nullable=False,
        name="gateway",
        description="Pasarela de pago utilizada para procesar el pago"
    )

    payment_type: str = ormar.String(
        max_length=255,
        nullable=False,
        name="payment_type",
        description="Tipo de pago realizado (por ejemplo, crédito, débito)"
    )

    payment_amount: float = ormar.Decimal(
        max_digits=10,
        decimal_places=2,
        nullable=False,
        name="payment_amount",
        description="Monto total pagado en la transacción"
    )

    status: str = ormar.String(
        max_length=20,
        nullable=False,
        name="status",
        description="Estado actual del pago (pending o paid)"
    )

    date_created: datetime = ormar.DateTime(
        default=datetime.now,
        name="date_created",
        description="Fecha de creación del registro del pago"
    )

    date_updated: datetime = ormar.DateTime(
        default=datetime.now,
        onupdate=datetime.now,
        name="date_updated",
        description="Fecha de la última actualización del registro del pago"
    )
