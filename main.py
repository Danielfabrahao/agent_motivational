import os
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, OpenAIServerModel
from openai import OpenAI
from tools import *

# This will be used to load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get the OpenAI API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

model = InferenceClientModel(
    model_id="gpt-4o",
    provider="openai",                     # <- evita lookup no Hub
    api_key=os.environ["OPENAI_API_KEY"]
)
agent = CodeAgent(tools=[generate_10_quotes], model=model)
result=agent.run("Com base no termo chave: 'work' Busque as melhores 5 máximas, citando o nome do autor no banco e retorne em um json")
print( result)


# if __name__ == '__main__':
#     main()