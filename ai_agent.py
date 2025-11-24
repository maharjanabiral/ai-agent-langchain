from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch

load_dotenv()
gemini_model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
groq_model = ChatGroq(model="llama-3.3-70b-versatile")
system_prompt = "You are a AI chatbot. Be friendly and polite"
search_tool = TavilySearch(max_results=2)


def get_response_from_agent(llm_name, prompt, allow_search, provider):
    if(provider=="Groq"):
        llm=ChatGroq(model=llm_name)
    else:
        llm=ChatGoogleGenerativeAI(model=llm_name)

    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )
    state={"messages": prompt}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return (ai_messages[-1])


