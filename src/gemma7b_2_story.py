import openai

scenario = "homelessness"
query_1 = f"""
Come up with a specific story about someone dealing with {scenario}
"""

client = openai.OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = "esecret_wh7ywjmmphgytgciv67bjy9hww"
)
# Note: not all arguments are currently supported and will be ignored by the backend.
chat_completion = client.chat.completions.create(
    model="google/gemma-7b-it",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, 
              {"role": "user", "content": query_1}],
    temperature=0.1
)
print(chat_completion.choices[0].message.content)