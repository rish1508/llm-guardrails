from guardrails import Guard
import openai
from pydantic import BaseModel, Field

class Pet(BaseModel):
    pet_type: str = Field(description="Species of pet")
    name: str = Field(description="a unique pet name")

prompt = """
    What kind of pet should I get and what should I name it?

    ${gr.complete_xml_suffix_v2}
"""
guard = Guard.from_pydantic(output_class=Pet, prompt=prompt)

raw_output, validated_output, *rest = guard(
    llm_api=openai.completions.create,
    engine="gpt-3.5-turbo-instruct"
)
print(raw_output)
print(f"{validated_output}")