from crewai import Agent
from tools import hrds_tool
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4-0125-preview'
# senior researcher for blog content
blog_researcher = Agent(
    role = 'Blog Researcher for Youtue videos',
    goal = 'get the relevant video content for the topic{topic} from yt channel',
    verbose = True,
    memory = True,
    backstory = (
        'Expert in understanding videos in AI Data Science, Machine Learning, GENAI and providing recommendations'
    ) ,
    tools=[hrds_tool
           ],
    allow_delegation = True 
)

# Blog Writer with yt tool
blog_writter = Agent(
    role = 'Blog writter',
    goal = 'narrating compelling tech stories about the video content for the video{topic} from yt channel',
    verbose = True, # Enables detailed logs and	Useful for debugging and transparency
    memory = True, # Remembers previous interactions	Maintains context and improves consistency
    backstory = (
        'Dedicated to fairly simplifying complex video topics for broader understanding.' 
        # Makes output more human-like and aligned and adds background/personality

    ) ,
    tools=[hrds_tool],
    allow_delegation = True # 	Allows agent to assign tasks to other agents
)