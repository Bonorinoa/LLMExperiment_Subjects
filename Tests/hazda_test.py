import asyncio
from utils.search import get_results
#from LLMExperiment_Subjects.BuildProfile import ProfileBuilder

async def test_build_profile():
    builder = ProfileBuilder(tribe_name="Hazda", relevant_factors=["lifestyle", "average age"])
    profile = await builder.build_profile()
    assert profile is not None  # Adjust according to what build_profile returns
    # Add more assertions here based on the expected structure and content of the profile
    print("Test passed, profile is not None")
    # Optionally, print part of the profile or other details for manual verification

# This block runs the test function using asyncio's event loop
if __name__ == "__main__":
    import sys
    print(sys.path)
    #asyncio.run(test_build_profile())
