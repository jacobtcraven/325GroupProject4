'''Main function for using and testing modules'''

## Import needed classes and functions
from module_1.RawData import RawData, InputOutput
from module_2.FormatData import FormatData
from module_3.Testing import Testing

## Import openai and api key
import openai
from other.sk import sr_key

## Set the api key
openai.api_key = sr_key

if __name__ == '__main__':

    ## Test that the file urls.txt exists and is accessible
    Testing.test_url_text_exists()

    ## Test that urls.txt contains urls and is readable
    Testing.test_read_urls()

    ## Read the URLs from the file
    urls = InputOutput.read_urls('other/urls.txt')

    ## initialize counter for file naming
    counter = 1

    ## Test that the scrape function works before looping
    Testing.test_scrape_object()

    ## For each url, scrape the raw data, format it, and write it to a file
    # for URL in urls:
    for URL in urls:
        source = RawData.scrape(URL)

        ## Write html to raw file
        InputOutput.write_to_file(str(source), f'Data/raw/raw{counter}.txt')

        ## Test that the title of the article can be extracted and is a string
        Testing.test_title()

        ## Get the title of the article
        title = FormatData.get_title(source)

        ## Format the raw file
        formatted = FormatData.remove_html(source)
        formatted = FormatData.add_newlines(formatted)

        ## Write the formatted file
        InputOutput.write_to_file(formatted, f'Data/processed/formatted{counter}.txt')
        
        ## Reset the messages variable so previous prompts aren't remembered
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

        ## Add new lines for readibility
        formatted_reply = FormatData.add_newlines(reply)

        ## Combine title with formatted summary of article
        summary = title + '\n' + formatted_reply

        ## Write summary to file
        InputOutput.write_to_file(summary, f'Data/summarized/summarized{counter}.txt')

        ## Increment counter so next url can be scraped and written to a new file
        counter += 1