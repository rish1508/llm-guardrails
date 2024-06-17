# Import Guard and Validator
from pydantic import BaseModel, Field
from guardrails.hub import DetectPII
from guardrails import Guard

# Initialize Validator
val = DetectPII(pii_entities=["EMAIL_ADDRESS", "PHONE_NUMBER"], on_fail="fix")


# Create Pydantic BaseModel
class UserHistory(BaseModel):
    name: str
    last_msg: str = Field(description="Last message sent by user", validators=[val])


# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=UserHistory)

# Run LLM output generating JSON through guard
try:
    guard.parse(
        """
    {
        "name": "John Smith",
        "last_msg": "My account isn't working. My username is not_a_real_email@guardrailsai.com"
    }
    """
    )
except Exception as e:
    print(e)