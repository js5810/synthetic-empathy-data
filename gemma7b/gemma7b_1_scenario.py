import openai
import json
import time


client = openai.OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = "esecret_wh7ywjmmphgytgciv67bjy9hww"
)


scenario_list = []
summary_str = ""
for index in range(3):
    
    print("This is the {}th group...".format(index))

    try:
        query_1 = """
        Generate 10 different hopeless scenarios in which the person in that situation would benefit from receiving empathy from others. Never include ** in your response and use plain text only. Generate scenarios that are completely different from those listed below:
        {}
        """.format(summary_str)  # length of summary_str is bottleneck b/c context limit
        chat_completion = client.chat.completions.create(
            model="google/gemma-7b-it",
            messages=[{"role": "system", "content": "You are a creative brainstorming assistant generating new ideas and returning only a single json list with key called output without any other text before or after the json object."}, 
                    {"role": "user", "content": query_1}],
            temperature=0.1
        )

        new_scenario = json.loads(chat_completion.choices[0].message.content)["output"]
        scenario_list.extend(new_scenario)

        query_2 = """
        Aggressively compress each item in the list so that the original meaning remains but they are much shorter. Never include ** in your response and produce plain text only.
        {}
        """.format('\n'.join(new_scenario))
        chat_completion = client.chat.completions.create(
            model="google/gemma-7b-it",
            messages=[{"role": "system", "content": "You are a creative brainstorming assistant generating new ideas and returning only a single json list with key called output without any other text before or after the json object."}, 
                    {"role": "user", "content": query_2}],
            temperature=0.1
        )
        new_summaries = json.loads(chat_completion.choices[0].message.content)["output"]
        for s in new_summaries:
            summary_str += ("\n" + s)


        print(query_1)
        print("\n")
        print(query_2)
        print("\n")
    except:
        print("an error occured, moving on\n")
        time.sleep(15)
        continue

for i in range(len(scenario_list)):
    print("{}. ".format(i+1) + scenario_list[i] + "\n")
 
print("\n\n" + summary_str)