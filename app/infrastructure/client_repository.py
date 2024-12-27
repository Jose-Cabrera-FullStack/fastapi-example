from ormar.exceptions import NoMatch

from app.database.models import Client


class ClientRepository:
    @staticmethod
    async def get_client_by_document_identifier(document_identifier: str) -> Client:
        """
        Retrieves a client by their unique ID.

        Args:
            document_identifier (str): The unique identifier of the client.

        Returns:
            Client: The Client object corresponding to the provided ID.
        """
        try:
            return await Client.objects.get(document_identifier=document_identifier)
        except NoMatch:
            return None

    @staticmethod
    async def create_client(
        document_identifier: str,
        name: str,
        company: str,
        product_type: str
    ) -> Client:
        """
        Creates a new client with the given details.

        Args:
            document_identifier (str): The document identifier of the client.
            name (str): The name of the client.
            company (str): The company the client works for.
            product_type (str): The type of product the client is interested in.

        Returns:
            Client: The newly created Client object.
        """
        client = await Client.objects.create(
            document_identifier=document_identifier,
            name=name,
            company=company,
            product_type=product_type
        )
        return client

    @staticmethod
    async def update_client(
        document_identifier: str,
        new_name: str,
        new_company: str,
        new_product_type: str
    ) -> Client:
        """
        Updates the details of an existing client.

        Args:
            document_identifier (str): The document identifier for the client.
            new_name (str): The new name for the client.
            new_company (str): The new company for the client.
            new_product_type (str): The new product type of interest for the client.

        Returns:
            Client: The updated Client object.
        """
        client = await Client.objects.get(document_identifier=document_identifier)
        client.name = new_name
        client.company = new_company
        client.product_type = new_product_type
        await client.save()
        return client

    @staticmethod
    async def delete_client(document_identifier: int) -> bool:
        """
        Deletes a client by their unique ID.

        Args:
            document_identifier (int): The unique identifier of the client to delete.

        Returns:
            bool: True if the client was deleted successfully, False otherwise.
        """
        try:
            client = await Client.objects.get(document_identifier=document_identifier)
            await client.delete()
            return True
        except NoMatch:
            return False
