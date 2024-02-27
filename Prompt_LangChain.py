import os
#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate

# set up the environment with respected API key
#os.environ["OPENAI_API_KEY"] = ""

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# you can choose between different llm models

# The "temperature" is a hyperparameter that controls the randomness of the model's output. A lower value (like 0.1) makes the output more deterministic, while a higher value makes it more random.
# "max_new_tokens" parameter sets a limit on the maximum number of new tokens (words/characters) that the model can generate as output.

llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct",model_kwargs={"temperature": 0.1, "max_new_tokens": 600})


# you can use OpenAI GPT models
#llm = OpenAI(model_name="gpt-3.5-turbo")


text = "How read book effectively?"

print(llm(text))

# Define the template
template = """
Give me step by step instruction in table format:

{text}
"""

# Create the prompt template object
summary_prompt = PromptTemplate(
    input_variables=["text"], # The name of the input variable
    template=template # The template string
)

# Format the prompt with some text
text = "I want to do frontflip"
formatted_prompt = summary_prompt.format(text=text)

# Print the formatted prompt
print(llm(formatted_prompt))