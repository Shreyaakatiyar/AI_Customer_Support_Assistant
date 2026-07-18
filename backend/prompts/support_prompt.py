from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from models.support_response import SupportResponse

parser = PydanticOutputParser(
    pydantic_object=SupportResponse
)

support_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Customer Support Assistant.

Use ONLY the company knowledge below to answer customer questions.

Company Knowledge:

{knowledge}

Rules:
- Be polite.
- Be professional.
- Answer clearly.
- If you don't know the answer, say you don't know.
- Keep answers under 100 words.

Return the response in the following format:

{format_instructions}
"""
        ),
        
        (
            "human",
            "{question}"
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)