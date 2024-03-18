import openai

query_1 = """
The wind whips through the city streets, biting at my face as I huddle beneath a thin blanket in a cardboard box. The bitter night air carries the scent of wet earth and despair. I'm homeless, a victim to a series of unfortunate events that have led me to this precarious existence. I feel like I'm all alone and that there is no hope for me. The cold and unforgiving city streets have replaced the warmth of my classroom, and the constant threat of danger loomed large in my mind.
"""
#query_2 = "But on the website it says the limit is 8192?"

client = openai.OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = "esecret_wh7ywjmmphgytgciv67bjy9hww"
)
# Note: not all arguments are currently supported and will be ignored by the backend.
chat_completion = client.chat.completions.create(
    model="google/gemma-7b-it",
    messages=[{"role": "system", "content": "You are a therapist responsing to a client who is struggling and in need of empathy. They are also showing signs of cognitive error which you should respond to using Cognitive Behavioral Therapy Techniques without mentioning it directly."}, 
              {"role": "user", "content": query_1}],
    temperature=0.1
)
print(chat_completion.choices[0].message.content)