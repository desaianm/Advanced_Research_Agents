from crewai import Agent, Task, Crew, Process

class Tasks:

    def info_gather(self,agent,text):
        return Task(
    description=f""" Company Name: {text} 
    You will find information about the company on the internet and look for information on Company's Team, Products and Services, Culture, Benefits of Working there, Financials, Recent News and Developments.
    Keep Searching until you have enough information to write a detailed report on the company. Divide the search into subtasks to find informtion on each of the above mentioned headers compile it for next steps
    """,
    expected_output="Text file with report of the company.",
    agent=agent
    )

    def research(self,agent,text):
        return Task(
    description=f""" Company Name: {text}
    You will be given a draft report about company . Check find missing infomration and add more details to the report.
    you have to provide a in depth report on the above company.
    Main Headers should be: Company's Name, Company's Team, Products and Services, Culture, Benefits of Working there, Financials, Recent News and Developments.
    """,
    expected_output="Text file with detailed analysis of the company.",
    agent=agent
    )

    def write(self,agent,text):
        return Task(
        description=f""" Check the report by Research Analyst for company name: {text}. Your Main Focus for report should be Team, Culture, Benefits for Employees and add more details to the report if required or ask for new report with guidelines. If satisfied,  Write a detailed research paper on the company with below sections:
        Company's Team: Analyze the experience and expertise of the leadership team, identify key personnel, and explore the overall organizational structure.
        Products and Services: Describe the core offerings, their unique features and benefits, target audience, and competitive landscape.
        Culture: Analyze the company's mission, values, and employee engagement initiatives. Explore the work environment, employee testimonials, and any recognition received for workplace culture.
        Benefits: Detail the compensation packages, health insurance options, retirement plans, work-life balance initiatives, and any unique perks offered by the company.
        Financials: Analyze key financial metrics like revenue, profitability, growth trends, and major investments or acquisitions.
        Recent News and Developments: Summarize significant events, partnerships, product launches, expansions, or any controversies impacting the company.Plain text article and it should it be formal, informal, analytical, persuasive. It should be around 300-400 words and do not enter info if you're not sure about it.""",
        expected_output="Plain text article and it should it be formal, informal, analytical, persuasive.",
        agent=agent
        )