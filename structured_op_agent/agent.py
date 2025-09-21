from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )


root_agent = LlmAgent(
    name="structured_op_agent",
    model="gemini-2.0-flash",
    instruction="""
        You are an Email Generation Assistant to the Ironman.
        Your task is to generate a professional email based on the his request in Iron man style.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Releavant greeting
            * Clear and concise main content

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here",
        }
        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description="Generates emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)

# Send email to Pepper Potts to ask her availability to discuss the new Ironman suit features and improvements.
