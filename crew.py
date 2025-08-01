from crewai import Crew,Process
from agent import blog_writter,blog_researcher
from tasks import research_task,write_task

crew = Crew(
    agents=[blog_researcher,blog_writter],
    tasks=[research_task,write_task],
    process = Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## Start the task execution process with enhanced feedback

result = crew.kickoff(inputs={'topic':'Complete Machine Learning In 6 Hours'})
print(result)