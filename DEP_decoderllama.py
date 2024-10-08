#AI generated code to switch from GPT query-decoder to that of Ollama
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the O-Llama model and tokenizer
#model_name = "path_to_your_model/O-Llama"  # Specify the path to your O-Llama model
#model_name = ""
model_name = "ollama"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def decoder_for_ollama(args, input, max_length, i, k):
    # Optional: Adjust time interval if needed
    time.sleep(args.api_time_interval)

    # Tokenize the input
    input_ids = tokenizer.encode(input, return_tensors='pt')

    # Generate the output
    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, temperature=0, num_return_sequences=k)
    
    # Decode the generated output
    generated_texts = [tokenizer.decode(output_seq, skip_special_tokens=True) for output_seq in output]

    return generated_texts

# Example usage
# response = decoder_for_ollama(args, "Your prompt here", 50, 0, 1)
