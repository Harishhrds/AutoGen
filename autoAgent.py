import autogen
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# define assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=({"model":"gpt-4","temperature":0, "api_key":openai_api_key,}),
   
)

#  user agent
user = autogen.UserProxyAgent(
    name="User",
    
    code_execution_config={"work_dir":"agent_code","use_docker":False}
) # start the conversation and code saved in this directory

user.initiate_chat(
    assistant,
    message="write code for factorial of a number"
)
