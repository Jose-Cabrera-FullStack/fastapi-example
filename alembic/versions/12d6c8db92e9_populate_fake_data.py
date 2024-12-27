"""Populate fake data

Revision ID: populate_fake_data
Revises: b1b4b618e741
Create Date: 2024-08-02 01:03:54.250468

"""
import asyncio

from faker import Faker

from app.database.config import database
from app.database.models import Client, Debt, Payment
from app.domain import DebtDomain

fake = Faker()

# revision identifiers, used by Alembic.
revision = 'populate_fake_data'
down_revision = 'b1b4b618e741'
branch_labels = None
depends_on = None


async def create_fake_clients():
    random_clients_id = [
        "10000001",
        "10000002",
        "10000003",
        "10000004",
        "10000005",
    ]

    for client_id in random_clients_id:
        client = Client(
            document_identifier=client_id,
            name=fake.name(),
            company=fake.company(),
            product_type=fake.word(),
            date_created=fake.date_time_this_decade(),
            date_updated=fake.date_time_this_decade(),
        )
        await client.save()


async def create_fake_debts():
    clients = await Client.objects.all()
    for _ in range(10):
        debt = Debt(
            operation_identifier=DebtDomain.generate_operation_identifier(),
            client=fake.random_element(elements=clients),
            description=fake.text(max_nb_chars=20),
            emition_date=fake.date_time_this_decade(),
            expiration_date=fake.future_datetime(end_date='+30d'),
            total_debt=fake.pydecimal(left_digits=6, right_digits=2, positive=True),
            default_debt=fake.pydecimal(left_digits=6, right_digits=2, positive=True),
            administration_expenses=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            minimum_payment=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            period=fake.random_element(elements=['01', '02', '03']),
            fee="00",
            product_code=fake.lexify(text='???'),
            currency=fake.currency_code(),
            date_created=fake.date_time_this_decade(),
            created_by=fake.name(),
            date_updated=fake.date_time_this_decade(),
            updated_by=fake.name(),
        )
        await debt.save()


async def create_fake_payments():
    random_operation_bank_number = [
        "A05478452120",
        "A05478452121",
        "A05478452122",
        "A05478452123",
        "A05478452124",
        "A05478452125",
        "A05478452126",
        "A05478452127",
        "A05478452128",
        "A05478452129",
        "A05478452130",
    ]
    debts = await Debt.objects.all()
    for operation_bank_number in random_operation_bank_number:
        payment = Payment(
            debt=fake.random_element(elements=debts),
            emition_date=fake.date_time_this_decade(),
            bank_code=fake.lexify(text='????'),
            operation_bank_number=operation_bank_number,
            gateway=fake.word(),
            payment_type=fake.random_element(elements=['credit', 'debit']),
            payment_amount=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            status=fake.random_element(elements=['pending', 'paid']),
            date_created=fake.date_time_this_decade(),
            date_updated=fake.date_time_this_decade(),
        )
        await payment.save()


async def populate_db():
    await database.connect()
    try:
        await create_fake_clients()
        await create_fake_debts()
        await create_fake_payments()
    finally:
        await database.disconnect()


def upgrade() -> None:
    asyncio.run(populate_db())


def downgrade() -> None:
    pass
