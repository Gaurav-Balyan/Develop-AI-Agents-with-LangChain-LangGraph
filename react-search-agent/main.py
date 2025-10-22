from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse

tools = [TavilySearch()]
model = ChatOpenAI(model="gpt-4")

agent = create_agent(
    model,
    tools=tools,
    response_format=AgentResponse
)

def main():
    print("Hello from react-search-agent!")
    result = agent.invoke(
        {
            "messages":[
                {
                "content":"search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
                "role":"user"
                }
            ]
        }
    )
    print("Final Result:", result["structured_response"])

if __name__ == "__main__":
    main()
