from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool


import requests,json
def get_current_weather(city:str)->dict:
    """ this function can be used to get/fetch current weather information for a city name
    arguments:
    - city: name of the city to get weather data for e.g. Delhi, New York
    returns: JSON with weather information
    """
    api_key = "6a8b0ac166a37e2b7a38e64416b3c3fe"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response = response.content.decode()
    response = json.loads(response)
    output = {"City Name":city,"weather":response["weather"][0]['description'],
              "temperature":response['main']['temp'],
              "unit":"kelvin"}

    return output

get_current_weather_tool = FunctionTool(get_current_weather)


# Langchain Tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

def wiki_tool(query:str):
    """ thi function can be used to fetch historical information about people, places, events etc.
    arguments:
    - query: query to serach for on wikipedia
    returns: wikipedia search results
    """
    output = wiki.run(query)
    return output

wiki_tool_adk = FunctionTool(wiki_tool)



prompt = """
you are an expert assistant to human users who can provide correct information.
You are provided with multiple tools, you can use appropriate tool for the specific use case based on user query.
"""


root_agent = LlmAgent(name="tredenceAgent",
                      model="gemini-2.0-flash",
                      instruction=prompt,
                      description="Assistant Agent",
                      tools=[get_current_weather_tool,wiki_tool_adk]
                      )