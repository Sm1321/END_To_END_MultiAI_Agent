### This File will be having the CoreLogic of Agent

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent 
from langchain_core.messages.ai import AIMessage
from app.config.settings import Settings
