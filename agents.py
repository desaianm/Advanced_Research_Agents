import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool

os.environ['OPENAI_MODEL_NAME'] = 'gpt-4-0125-preview'
search_tool = SerperDevTool()
web_search = WebsiteSearchTool()
web_scrape = ScrapeWebsiteTool()

class Agents():
# Define your agents with roles and goals
    def research_analyst(self): 
        return Agent(
        role='Research Analyst',
        goal='find fascinating insights and keep an eye for details. draft a report on the company.',
        backstory=""" You have been world renowed for your research on companies.""",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool,web_search,web_scrape],
        max_iter=5
        
        )
    
    def web_researcher(self):
        return Agent(
        role='Web Researcher',
        goal='Research about company on the internet about AI Companies',
        backstory="""You have been expert at finding information about Companies on the internet.""",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool,web_scrape]
        )
    
    def senior_research_manager(self):
        return Agent(
        role='Senior Research Manager',
        goal='Monitor and Direct the Research Analyst as well as write final draft on research',
        backstory="""You have been expert at managing people. You have great eye to detail and can write well.""",
        verbose=True,
        allow_delegation=True
        )