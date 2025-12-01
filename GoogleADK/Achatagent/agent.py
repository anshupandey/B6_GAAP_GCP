from google.adk.agents import LlmAgent
from google.adk.tools import google_search

root_agent = LlmAgent(name="tredenceAgent",
                      model="gemini-2.0-flash",
                      instruction="""you are an expert assistant to human users, 
                      who can provide correct information based on internet search results""",
                      description="Assistant Agent",
                      tools=[google_search]
                      )