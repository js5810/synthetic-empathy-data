import openai

query_1 = """
Produce a short first person summary for the story, with one example below.

Story: Sarah had always been a hard worker, but when her hours were cut at the restaurant where she worked as a server, she struggled to make ends meet. Eventually, Sarah fell behind on rent and was evicted from her apartment.

With nowhere else to turn, Sarah found herself living on the streets. She spent her days searching for shelter and food, often relying on soup kitchens and shelters for survival. Despite her best efforts to find work and improve her situation, Sarah faced numerous barriers including lack of access to clean clothes for job interviews and limited resources available in the community.

Feeling hopeless and alone, Sarah's mental health began to deteriorate as she grappled with feelings of shame and worthlessness. As winter approached, finding warmth became an even greater challenge for Sarah as she tried to navigate the harsh conditions while also battling hunger and exhaustion.

Despite facing overwhelming odds against her homelessness situation improving any time soon,Sarah remained determined not give up hope that one day things would get better - no matter how dire they may seem at present moment in life being homeless person without home or family support system nearby which could help provide necessary assistance during these tough times ahead.

First Person Explanation: I know I'm just a burden on society now. No one wants to hire me because I can't even afford clean clothes for an interview. And with winter coming, it's only going to get worse. I don't see how things could ever improve for me.

Story: The wind whipped through the city streets, biting at Maria's face as she huddled beneath a thin blanket in a cardboard box. The bitter night air carried the scent of wet earth and despair. Maria was homeless, a victim to a series of unfortunate events that had led her to this precarious existence.

Once a proud teacher, Maria had lost everything due to financial difficulties and the sudden breakdown of her marriage. With nowhere to turn, she had been forced onto the streets, her life reduced to a single cardboard box in the cold. The once-familiar warmth of her classroom had been replaced by the cold and unforgiving city streets, and the constant threat of danger loomed large in her mind.

The day had been filled with challenges. Finding food was a constant battle, and the threat of malnutrition loomed large. The constant cold seeped into her bones, and the lack of proper shelter meant she was susceptible to illness. The loneliness and isolation were crushing, and the whispers of people passing by, "homeless woman," "poor soul," pierced her heart like shards of glass.
"""

client = openai.OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = "esecret_wh7ywjmmphgytgciv67bjy9hww"
)
# Note: not all arguments are currently supported and will be ignored by the backend.
chat_completion = client.chat.completions.create(
    model="google/gemma-7b-it",
    messages=[{"role": "system", "content": "You are a client explaining your tough situation to a therapist. You display negative cognitive error about your situation."}, 
              {"role": "user", "content": query_1}],
    temperature=0.1
)
print(chat_completion.choices[0].message.content)