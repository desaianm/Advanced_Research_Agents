import os
from crewai import Agent, Task, Crew, Process
from agents import Agents
from tasks import Tasks
import streamlit as st

# set serper API key in environment variable SERPER_API_KEY


tasks = Tasks()
agents = Agents()

web_agent = agents.web_researcher()
researcher = agents.research_analyst()
writer = agents.senior_research_manager()

st.title("Research Company")
company_name = st.text_input("Enter Company Name")
if company_name:
    task0 = tasks.info_gather(web_agent,company_name)
    task1 = tasks.research(researcher, company_name)
    task2 = tasks.write(writer)
    # Instantiate your crew with a sequential process
    crew = Crew(
    agents=[researcher, writer,web_agent],
    tasks=[task0,task1, task2],
    verbose=2, 
    )

    # Get your crew to work!
    result = crew.kickoff()

    st.info(result)