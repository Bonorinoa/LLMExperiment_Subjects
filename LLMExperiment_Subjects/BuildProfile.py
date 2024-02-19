import asyncio
from utils.search import get_results
from utils.process_and_index import chunk_and_index

class ProfileBuilder:
    def __init__(self, tribe_name, relevant_factors):
        """
        Initializes the ProfileBuilder with a tribe name and a list of relevant factors
        to include in the profile.
        
        Parameters:
            tribe_name (str): The name of the tribe or target population.
            relevant_factors (list of str): A list of socio-economic factors to be covered in the profile.
        """
        self.tribe_name = tribe_name
        self.relevant_factors = relevant_factors

    async def build_profile(self):
        """
        Asynchronously builds the profile by performing web scraping, processing,
        and indexing the content related to the query.
        Returns:
            An object (e.g., a retriever) capable of fetching relevant content based on queries.
        """
        search_query = f"{self.tribe_name} {' '.join(self.relevant_factors)}"
        
        try:
            # Get structured response from web scraping
            structured_response = await get_results(search_query)
            if structured_response is None:
                raise ValueError("No data retrieved from web scraping")

            # Process and index the structured response
            retriever = chunk_and_index(structured_response)
            if retriever is None:
                raise ValueError("Failed to process and index content")

            return retriever
        
        except Exception as e:
            print(f"Error building profile: {e}")
            # Optionally, log the error details to a file or external logging service
            return None

    def build_profile_sync(self):
        """
        Synchronous wrapper around the asynchronous build_profile_async method.
        This allows for the method to be called without directly dealing with asyncio.
        Returns:
            The output from the build_profile_async method.
        """
        try:
            return asyncio.run(self.build_profile())
        except Exception as e:
            print(f"Error in build_profile_sync: {e}")
            return None

