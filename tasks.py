from crewai import Task
from tools import hrds_tool
from agent import blog_researcher,blog_writter

## Research Task
research_task = Task(
    description=(
        'Identify the video {topic}'
        'Get the detail information about the video from channel'
    ),
    expected_output="A Comprehensive 3 paragragphs long report based on {topic} of video content",
    tools = [hrds_tool],
    agent = blog_researcher
)

# writting task
write_task = Task(
    description=(
        'Identify the video {topic}'
        'Get the detail information about the video from channel'
    ),  
    expected_output="Summarize the info from youtube channel  video on {topic} and create content for blog",
    tools = [hrds_tool],
    agent = blog_writter,
    async_execution=False,
    output_file='new-blog-post.md'
)
