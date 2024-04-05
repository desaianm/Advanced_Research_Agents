from crewai import Agent, Task, Crew, Process

class Tasks:

    def info_gather(self,agent,text):
        return Task(
    description=f""" Company Name: {text} 
    You will find information about the company on the internet and look for information on Company's Team, Products and Services, Culture, Benefits of Working there, Financials, Recent News and Developments.
    Keep Searching until you have enough information to write a detailed report on the company. Divide the search into subtasks and keep track of the progress.
    """,
    expected_output="Text file with report of the company.",
    agent=agent
    )

    def research(self,agent,text):
        return Task(
    description=f""" Company Name: {text}
    You will be given a draft report about company . Check find missing infomration and add more details to the report.
    you have to provide a in depth report on the above company.
    Main Headers should be: Company's Team, Products and Services, Culture, Benefits of Working there, Financials, Recent News and Developments.
    """,
    expected_output="Text file with detailed analysis of the company.",
    agent=agent
    )

    def write(self,agent):
        return Task(
        description="""Using the report given by the Research Analyst, write a research paper on the company.
        Main Headers should be: Company's Team, Products and Services, Culture, Benefits of Working there, Financials, Recent News and Developments.""",
        expected_output="A Plain text blog post of at least 8 paragraphs with above mentioned headers.",
        agent=agent
        )