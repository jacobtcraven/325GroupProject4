# Web Scraping Project  
This project contains a Python script main.py that scrapes information from a list of sports news articles and writes the content of each article to a separate text file.


## Getting Started:  
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites:  
The project requires Python and Conda to be installed on your machine.


## Installing:  
Follow these steps to set up a new Conda environment and run the program:

1. Open your terminal.

2. Navigate to the project directory:  
    ```
    cd path/to/your/project
    ```
    (please replace "path/to/your/project" with your path to the file)

3. Create a new Conda environment and install the required packages using the requirements.yml file:  
    ```
    conda create -n myenv --file requirements.yml
    ```
    (please replace "myenv" with your desired environment name)

4. Activate the new environment:  
    ```
    conda activate myenv
    ```
    (please replace "myenv" with environment name created in previous step)


## Running the Program:
After setting up the environment, you can run the program using the following command:  
    ```
    python3 run.py
    ```

## How to create a LLM API:
1. Create an OpenAI account at www.openai.com

2. Navigate to the API Keys tab on the sidebar

3. Select "Create new secret key"
    a. Save this key as it will be needed in a future step soon

4. Run `pip install openai` to install the needed dependencies __It is recommended to use a virtual Environment__

5. Define a string variable that contains your API key

6. Connect API key to openAI agent with this code block:
    ```
    openai.api_key = sr_key
    ```
    
   a. replace "sr_key" with whatever you named your API key string variable.

7. Determine how you will implement the API and then start by creating a list of dictionaries such as:
    ```
    messages = [ {"role": "system", "content": 
                "You are a intelligent assistant."} ] 
    ```
   a. In this example, "role" is defined as "system" but three different values can be used instead of "system".
      
      *system*: This sets up how the API should interact

      *user*: This acts as a message to the API for it to respond.

      *assistant*: This also acts as a message, but typically is used in instances when previous prompts and answers are to be remembered.

   b. In this example "content" is defined as "You are a intelligent assistant." Depending on the specified role, "content" can contain a behavior or prompt for the API.

8. Append to the list a dictionary that contains the desired role and content. An example is:
    ```
    messages.append( 
            {"role": "user", "content": message}, 
        ) 
    ```

9. Create an implementation of the API such as used in this project:
    ```
    messages = [ {"role": "system", "content": 
                "You are a intelligent assistant."} ] 
            
            ## Prompt to summarize article
            message = f"Make this article concise in under 50 words\n {formatted}" 
            
            ## Append user message to messages list so api can access it
            messages.append( 
                {"role": "user", "content": message}, 
            ) 

            ## Send the prompt to the api
            chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=messages 
            ) 

            ## Seperate the summary from other returned data
            reply = chat.choices[0].message.content 
    ```
    
   a. The lines 

    ```
    chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    ```

   sends the prompt and stores it in a variable "chat"

   b. The line `reply = chat.choices[0].message.content` extracts the reply from a set of data returned by the API.

10. Test and customize as you please!

## File Description:  
__run.py__: This is the main Python script that performs the web scraping task. First it reads a list of URLs from a text file, scrapes the content of each URL using requests and beautifulsoup4, formats the content by adding a newline every 20 words. The raw and formatted data are written to seperate files before the article contents are sent to the OpenAI API to be summarized. The reply containing the summarized article is placed into a file corresponding to its article. 

__Data__: This folder contains three folders for raw, processed and summarized data.

   __Raw__: This folder contains the raw data scraped from the news articles, including html tags

   __Processed__: This folder contains the full text of the scraped articles without any html tags.

   __Summarized__: This folder contains the titles and summaries of each article in under 50 words.

__Module_1__: This folder contains the __RawData.py__ file which contains the functions to scrape the raw data from a website.

__Module_2__: This folder contains the __FormatData.py__ file which contains the functions for retrieving the article title, removing html tags, and adding newlines to a string.

__Other__: This folder contains the conda environment yml file, __urls.txt__ file, and the python file __sk.py__ containing the API key.

__urls.txt__: This file contains the five URLs that will be scraped in main.py.

__sk.py__: This file contains the API key to be used with OpenAI's API.

__requirements.yml__: This file contains the conda environment to run the program.

------------------------------------------------------------------------------------------------------------

### Other important information
Please replace the placeholders "myenv" and "path/to/your/project" with the name of your Conda environment and the actual path to your project.

