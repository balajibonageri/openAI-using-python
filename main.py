import openai
openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = str(input("Enter your Prompt:"))

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_token = 1024,
    n = 1,
    stop = None,
    temperature = 0.9,
)
response = completion.choices[0].text
print(response)