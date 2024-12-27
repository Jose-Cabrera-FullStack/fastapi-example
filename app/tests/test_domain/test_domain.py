import pytest

from app.domain.debt_domain import DebtDomain


@pytest.mark.parametrize("length", [16, 10, 20])
def test_generate_operation_identifier(length):
    identifier = DebtDomain.generate_operation_identifier(length)

    assert len(identifier) == length
    assert all(char.isalnum() or char == '-' for char in identifier)


@pytest.mark.parametrize("identifier,expected", [
    ("abcd-1234-efgh-5678", False),
    ("abcd1234efgh5678", True),
    ("abcd_1234-efgh-5678", False),
    ("abcd-1234-efgh-567", False),
    ("abcd-1234-efgh-56789", False),
])
def test_validate_operation_identifier(identifier, expected):
    result = DebtDomain.validate_operation_identifier(identifier)

    assert result == expected
