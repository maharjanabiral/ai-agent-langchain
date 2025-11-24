from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

load_dotenv()
gemini_model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
groq_model = ChatGroq(model="llama-3.3-70b-versatile")
system_prompt = "You are a AI chatbot. Be friendly and polite"
search_tool = TavilySearch(max_results=2)

agent = create_agent(
    model=gemini_model,
    system_prompt=system_prompt,
    tools=[search_tool],   
)

prompt = "Tell me about trends in cryptomarket"
state={"messages": prompt}
response = agent.invoke(state)
print(response)