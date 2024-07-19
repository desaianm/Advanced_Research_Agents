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
  "query": "Cohere"
}


Output:

The API will return a JSON object containing the research report on Google.

Example Report Structure:

{
  "Company's Team": "Cohere boasts a multidisciplinary team of ML/AI engineers, thinkers, and innovators, led by visionaries like Aidan Gomez, Nick Frosst, and Ivan Zhang. The leadership team's expertise and experience drive Cohere's mission to revolutionize natural language processing solutions, supported by a diverse and collaborative team culture.",
  "Products and Services": "Cohere offers a suite of products built on Transformer architecture, including Command, Embed, Rerank, and Fine-tuning. These tools enable developers to create applications with advanced language understanding capabilities, catering to a wide range of business applications and showcasing Cohere's commitment to advancing practical applications of language AI.",
  "Culture": "Cohere fosters an environment where innovation is encouraged, supported by initiatives like internal hackathons and tech talks. The company emphasizes a comprehensive benefits package focusing on health, lifestyle, family support, and continuous learning opportunities, enabling employees to pursue the best work of their careers in a supportive environment.",
  "Benefits": "Cohere provides a comprehensive benefits package that emphasizes health, lifestyle, family support, and continuous learning opportunities, allowing employees to thrive both professionally and personally.",
  "Financials": "In 2023, Cohere raised $450 million at a $5 billion valuation, with significant investments from major players like Nvidia and Salesforce. This financial milestone highlights Cohere's solid financial standing, market position, and potential for sustained growth and influence in the AI market.",
  "Recent News and Developments": "Cohere was recently recognized as one of the most innovative companies in 2024, reflecting its growing reputation and market confidence in its solutions. The company's commitment to advancing the field of AI and its supportive environment for its team positions Cohere for continued success and innovation."
}

```
