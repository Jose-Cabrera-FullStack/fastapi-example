from datetime import datetime
from unittest.mock import patch, AsyncMock

import pytest

from app.tests.mock import fake, create_mock_result_proxy, client_data as mock_client_data
from app.infrastructure.client_repository import ClientRepository


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.fetch_all', new_callable=AsyncMock)
async def test_get_client_by_id(mock_fetch_all):

    mock_result_proxy = create_mock_result_proxy(mock_client_data)

    mock_fetch_all.return_value = [mock_result_proxy]

    client = await ClientRepository.get_client_by_document_identifier(
        document_identifier=mock_client_data['document_identifier']
    )

    mock_fetch_all.assert_called_once()
    assert client.document_identifier == mock_client_data['document_identifier']
    assert client.name == mock_client_data['name']
    assert client.company == mock_client_data['company']
    assert client.product_type == mock_client_data['product_type']


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.fetch_all', new_callable=AsyncMock)
async def test_get_client_by_id_not_found(mock_fetch_all):
    mock_fetch_all.return_value = []

    result = await ClientRepository.get_client_by_document_identifier(
        document_identifier=mock_client_data['document_identifier']
    )

    assert result is None


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.execute', new_callable=AsyncMock)
async def test_create_client(mock_execute):

    mock_execute.return_value = None

    client = await ClientRepository.create_client(
        name=mock_client_data['name'],
        company=mock_client_data['company'],
        product_type=mock_client_data['product_type'],
        document_identifier=mock_client_data['document_identifier']
    )

    assert client.document_identifier == mock_client_data['document_identifier']
    assert client.name == mock_client_data['name']
    assert client.company == mock_client_data['company']
    assert client.product_type == mock_client_data['product_type']


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.execute', new_callable=AsyncMock)
@patch('app.database.models.Client.Meta.database.fetch_all', new_callable=AsyncMock)
async def test_update_client(mock_fetch_all, mock_execute):

    updated_client_data = {
        **mock_client_data,
        'name': fake.name(),
        'company': fake.company(),
        'product_type': fake.word(),
        'document_identifier': mock_client_data['document_identifier'],
        'date_updated': datetime.now(),
    }

    mock_fetch_all.return_value = [create_mock_result_proxy(mock_client_data)]
    mock_execute.return_value = None

    result = await ClientRepository.update_client(
        document_identifier=mock_client_data['document_identifier'],
        new_name=updated_client_data['name'],
        new_company=updated_client_data['company'],
        new_product_type=updated_client_data['product_type'],
    )

    assert result.document_identifier == updated_client_data['document_identifier']
    assert result.name == updated_client_data['name']
    assert result.company == updated_client_data['company']
    assert result.product_type == updated_client_data['product_type']


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.execute', new_callable=AsyncMock)
@patch('app.database.models.Client.Meta.database.fetch_all', new_callable=AsyncMock)
async def test_delete_client(mock_fetch_all, mock_execute):

    mock_fetch_all.return_value = [create_mock_result_proxy(mock_client_data)]
    mock_execute.return_value = None

    result = await ClientRepository.delete_client(
        document_identifier=mock_client_data['document_identifier']
    )

    assert result is True


@pytest.mark.asyncio
@patch('app.database.models.Client.Meta.database.execute', new_callable=AsyncMock)
@patch('app.database.models.Client.Meta.database.fetch_all', new_callable=AsyncMock)
async def test_delete_client_not_found(mock_fetch_all, mock_execute):
    mock_fetch_all.return_value = []

    result = await ClientRepository.delete_client(
        document_identifier=mock_client_data['document_identifier']
    )

    assert result is False
