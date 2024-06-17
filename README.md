## Company Research with Crew AI

This repository contains a Crew AI implementation for automated company research. The project uses Crew AI agents to gather information from the web, analyze it, and generate a detailed company report in JSON format.

**Key Features:**

* **Automated Research:** The agents handle web scraping, data analysis, and report writing, streamlining the research process.
* **Scalable:** The code can be easily adapted to research multiple companies.
* **JSON Output:** The final report is presented in JSON format for easy data analysis and integration with other systems.

**Getting Started:**

1. **Set up Environment:**
   * Install the necessary Python libraries:
     ```bash
     pip install crewai fastapi uvicorn
     ```
   * Install the required tools, like SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool.
2. **Configure API Keys:**
   * Obtain an API key for Serper (replace `SERPER_API_KEY` with your actual key).
   * Set your OpenAI API key as the environment variable `OPENAI_MODEL_NAME`.
   * Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.
3. **Run the Application:**
   * Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```
   * Send a POST request to the `/` endpoint with a JSON payload containing the company name you want to research. For example:
     ```json
     {
       "query": "Google"
     }
     ```

**Example Usage:**

To research the company "Google", send a POST request to the `/` endpoint with the following JSON payload:

```json
{
  "query": "Google"
}


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

```
