import os
import openai
import time 
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
#def format_prompt(prompt_list):
    

def request_with_prompt_batch(prompts):

    def request_with_five_prompt(prompt):
        openai.api_key = ''

        response = openai.Completion.create(
        #model="text-davinci-002",
        model = "text-curie-001",
        prompt = prompt,
        temperature=0,
        max_tokens=512,
        top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
        )

        return response['choices'][0]['text']

    generated_contexts = []

    with ThreadPoolExecutor(max_workers=5) as inner_executor:
        for output in inner_executor.map(request_with_five_prompt, prompts):
            generated_contexts.append(output)
    return generated_contexts




def request_with_prompt(prompt):
    openai.api_key = ''

    response = openai.Completion.create(
    #model="text-davinci-002",
    model = "text-curie-001",
    prompt = prompt,
    temperature=0,
    max_tokens=512,
    top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
    )
    time.sleep(1)
    return response['choices'][0]['text']
