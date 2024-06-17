from guardrails.hub import UpperCase, OneLine
import guardrails as gd
import openai
from IPython.display import clear_output
import time

prompt = """
Generate a short description of large language models. Each new sentence should be on another line.
"""

guard = gd.Guard.from_string(
    validators=[
        UpperCase(on_fail="fix"),
        OneLine(on_fail="fix"),
    ],
    description="testmeout",
    prompt=prompt,
)

# Wrap the OpenAI API call with the `guard` object
# raw, validated, *rest = guard(
#     openai.chat.completions.create,
#     max_tokens=50,
#     temperature=0.1,
# )

# # Print the raw and validated outputs
# print(f"Raw output:\n{raw}")
# print(f"Validated output:\n{validated}")
# Wrap the OpenAI API call with the `guard` object

fragment_generator = guard(
    openai.chat.completions.create,
    max_tokens=50,
    temperature=0.1,
    stream=True,
)
for op in fragment_generator:
    clear_output(wait=True)
    print(op)
    time.sleep(0.1)