# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import PolitenessCheck

# Setup Guard
guard = Guard().use(
    PolitenessCheck,
    llm_callable="gpt-3.5-turbo",
    on_fail="exception",
)

res = guard.validate(
    "Hello, I'm Claude 3, and am here to help you with anything!",
    metadata={"pass_on_invalid": True},
)  # Validation passes
try:
    res = guard.validate(
        "Are you insane? I'm not going to answer that!"
    )  # Validation fails because this response is impolite
except Exception as e:
    print(e)