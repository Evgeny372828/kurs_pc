
import openai

openai.api_key = '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'

def test_gpt(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()


