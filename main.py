# Langgraph packages
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

def main():
    print("Hello from tableau-agent!")

 # langchain and langgraph package imports
 from langchain_openai import ChatOpenAI
 from langgraph.prebuilt import create_react_agent
 # langchain_tableau imports
 from langchain_tableau.tools.simple_datasource_qa import initialize_simple_datasource_qa

 # initialize an LLM
 llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

 # initalize `simple_datasource_qa` for querying a Tableau Published Datasource through VDS
 analyze_datasource = initialize_simple_datasource_qa(
     domain='https://your-tableau-cloud-or-server.com',
     site='Tableau site name',
     jwt_client_id='from an enabled Tableau Connected App',
     jwt_secret_id='from an enabled Tableau Connected App',
     jwt_secret='from an enabled Tableau Connected App',
     tableau_api_version='Tableau REST API version',
     tableau_user='user to query the Agent with',
     datasource_luid='unique data source ID can be obtained via REST or Metadata APIs',
     tooling_llm_model='model to use for the data query tool'
 )

 # Add the tool to the array of tools used by the Agent
 tools = [ analyze_datasource ]

 # Build the Agent using the minimum components (LLM + Tools)
 tableauAgent = create_react_agent(llm, tools)

 # Run the Agent
 messages = tableauAgent.invoke({"messages": [("human",'which states sell the most? Are those the same states with the most profits?')]})


if __name__ == "__main__":
    main()
