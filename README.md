Company Research with Crew AI
This repository contains a Crew AI implementation for automated company research. The project uses Crew AI agents to gather information from the web, analyze it, and generate a detailed company report in JSON format.
Key Features:
Automated Research: The agents handle web scraping, data analysis, and report writing, streamlining the research process.
Scalable: The code can be easily adapted to research multiple companies.
JSON Output: The final report is presented in JSON format for easy data analysis and integration with other systems.
Getting Started:
Set up Environment:
Install the necessary Python libraries:
pip install crewai fastapi uvicorn
Use code with caution.
Bash
Install the required tools, like SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool.
Configure API Keys:
Obtain an API key for Serper (replace SERPER_API_KEY with your actual key).
Set your OpenAI API key as the environment variable OPENAI_MODEL_NAME.
Set the OPENAI_API_KEY environment variable with your OpenAI API key.
Run the Application:
Start the FastAPI server:
uvicorn main:app --reload
Use code with caution.
Bash
Send a POST request to the / endpoint with a JSON payload containing the company name you want to research. For example:
{
  "query": "Google"
}
Use code with caution.
Json
Example Usage:
To research the company "Google", send a POST request to the / endpoint with the following JSON payload:
{
  "query": "Google"
}
Use code with caution.
Json
Output:
The API will return a JSON object containing the research report on Google.
Example Report Structure:
{
  "Company's Name": "Google",
  "Company's Team": {
    "Leadership": {
      "CEO": "Sundar Pichai",
      ...
    },
    "Key Personnel": [
      {
        "Name": "Larry Page",
        "Role": "Co-Founder"
      },
      ...
    ]
  },
  "Products and Services": {
    "Core Offerings": [
      "Search Engine",
      "Android Operating System",
      ...
    ],
    "Unique Features": [
      "Google Assistant",
      "Google Cloud Platform",
      ...
    ]
  },
  "Culture": {
    "Mission": "To organize the world's information and make it universally accessible and useful",
    "Values": [
      "Don't be evil",
      "Focus on the user",
      ...
    ],
    "Employee Engagement": {
      "Programs": [
        "Google's 20% Time",
        ...
      ]
    }
  },
  "Benefits": {
    "Compensation": {
      "Salary Ranges": {
        "Software Engineer": {
          "Entry Level": "$120,000 - $180,000",
          ...
        }
      }
    },
    "Health Insurance": {
      "Plans": [
        "PPO",
        "HSA",
        ...
      ]
    },
    "Retirement Plans": {
      "401(k)": {
        "Matching Contribution": "50% of your contributions up to 6% of your salary"
      }
    }
  },
  "Financials": {
    "Revenue": {
      "2022": "$282.84 billion",
      ...
    },
    "Profitability": {
      "Net Income": {
        "2022": "$76.03 billion"
      }
    }
  },
  "Recent News and Developments": [
    {
      "Date": "2023-02-06",
      "Headline": "Google Announces New AI-Powered Features for Search"
    },
    ...
  ]
}
Use code with caution.
Json
Contribution:
Contributions are welcome! You can:
Improve the agents' logic: Enhance the agents' capabilities to gather more accurate and comprehensive information.
Add new features: Implement new functionalities to the research process, such as competitor analysis or sentiment analysis.
Enhance the JSON output: Customize the JSON format to include more specific data fields or restructure the report for better organization.
Contact:
If you have any questions or suggestions, please feel free to contact me.
