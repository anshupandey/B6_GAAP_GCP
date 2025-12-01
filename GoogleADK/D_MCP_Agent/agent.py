from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams

server_parameters = {"command":"python",
                     "args":["/home/zadmin/Desktop/B6_GAAP_GCP/mcpserver/mcpserver2.py","stdio"]}

conn = StdioConnectionParams(server_params = server_parameters, timeout=120)
tools = MCPToolset(connection_params = conn)

prompt = """
you are an expert assistant to human users who can provide correct information.
You are provided with multiple tools, you can use appropriate tool for the specific use case based on user query.
"""


root_agent = LlmAgent(name="tredenceMCPAgent",
                      model="gemini-2.0-flash",
                      instruction=prompt,
                      description="Assistant Agent",
                      tools=[tools]
                      )
