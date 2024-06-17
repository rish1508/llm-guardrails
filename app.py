# Import Guard and Validator
from guardrails.hub import RegexMatch
from guardrails import Guard, OnFailAction

# Use the Guard with the validator
guard = Guard().use(RegexMatch, regex="Open.*", on_fail=OnFailAction.EXCEPTION)

# Test passing response
guard.validate(
    "OpenAI's GPT3.5 model is the latest in the GPT series. It is a powerful language model."
)

try:
    # Test failing response
    guard.validate(
        "MetaAI's Llama2 is the latest in their open-source LLM series. It is a powerful language model."
    )
except Exception as e:
    print(e)
