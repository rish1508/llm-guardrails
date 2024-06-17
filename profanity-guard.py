import openai
from guardrails import Guard
from guardrails.hub import ProfanityFree

prompt = """
    He is such a dickhead and a fucking idiot.
"""
# Define a Guard
guard = Guard().use(ProfanityFree, on_fail="exception")
# Validate a prompt
try:
    guard.validate(prompt)
except Exception as e:
    print(e)
# Wrap openai API call to validate response from llm
validated_response = guard(
    openai.chat.completions.create,
    prompt=prompt,
    model="gpt-3.5-turbo",
    max_tokens=100,

    temperature=0.0,
)

print(validated_response.validated_output)
print(guard.history.last)