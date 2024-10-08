
import ollama

def decoder_for_ollama(args, input, max_length, i, k):
    
    # GPT-3 API allows each users execute the API within 60 times in a minute ...
    # time.sleep(1)
    #time.sleep(args.api_time_interval)
    
    # https://beta.openai.com/account/api-keys
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    #print(openai.api_key)
    
    # Specify engine ...
    # Instruct GPT3
    #if args.model == "gpt3":
    #    engine = "text-ada-001"
    #elif args.model == "gpt3-medium":
    #    engine = "text-babbage-001"
    #elif args.model == "gpt3-large":
    #    engine = "text-curie-001"
    #elif args.model == "gpt3-xl":
    #    engine = "text-davinci-002"
    #else:
    #    raise ValueError("model is not properly defined ...")
    #engine = "gpt-3.5-turbo-0125"
    #response = openai.Completion.create(
    #  engine=engine,
    #  prompt=input,
    #  max_tokens=max_length,
    #  temperature=0,
    #  stop=None
    #)

    print(f"input is {input}")
    response = ollama.chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': input,
  },
])
    print(f"response is {response}")

    print(f"response['message']['content'] is {response['message']['content']}")
    #print(response['choices']['text'])
    #return(response['choices']['text'])
    return(response['message']['content'])
    #return response["choices"][0]["text"]
