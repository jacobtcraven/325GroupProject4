
# CNN Article Summarizer
This project fetches CNN articles from provided URLs, summarizes them using OpenAI's GPT-3.5 model, and saves the summaries along with the original article titles and authors to text files.


### Prerequisites
- Python 3.8 or newer
- Conda (recommended for managing environments)


# Setup Instructions
## 1. Environment Setup
1. Clone the repository to your local machine and checkout p3 branch:
```console
git clone https://github.com/alyab0uzaid/NewsScraper
cd NewsScraper
git checkout p3
```
2. Use the requirements.yml file to create a new Conda environment.
```console
conda env create -f requirements.yml
```

3. Once the environment is created, you can activate it using:
```console
conda activate myopenaienv
```

## 2. Setting Up the OpenAI API Key
1. Visit the OpenAI API page: https://openai.com/blog/openai-api and log in or sign up for an account.
2. Once logged in, navigate to the API keys section of your account dashboard on the left side of the page.
3. Click on the " + Create new secret key" button to generate a new key.
4. Copy the generated API key for use in the next step.
5. To use the OpenAI API, you'll need to insert your API key into the project. Locate the run.py file and find the line:
```console
client = OpenAI(api_key="INSERT_YOUR_API_KEY_HERE")
```
Replace "INSERT_YOUR_API_KEY_HERE" with your actual OpenAI API key, enclosed in quotes.

## 3.Running the Application
If you're running your script through an IDE (Integrated Development Environment) like PyCharm, Visual Studio Code, or Jupyter notebook, ensure the IDE is set to use the Python interpreter from your the activated 'myopenaienv' environment.

To run the project and summarize an article, use the command:

```console
python run.py <article-url>
```
or
```console
python3 run.py <article-url>
```
Replace <article-url> with the actual URL of the CNN article you wish to summarize.

### File Locations
- Raw HTML Content: Saved in the Data/raw directory.
- Summarized Articles: Stored in the Data/processed directory.


