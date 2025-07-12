### This File will be having the CoreLogic of Agent

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent 
from langchain_core.messages.ai import AIMessage
from app.config.settings import Settings



def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):
    ## Load the GroqModel
    llm = ChatGroq(model=llm_id)
    #To allow the TavilySearch for thr LLM
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    #Create a ReactAgent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    #State with messages, sending the user query
    state = {"messages" : query}

    response = agent.invoke(state)

    messages = response.get("messages")
    #Get all the AIMessages from the response 
    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]
    #Get the Latest Messages
    return ai_messages[-1]





