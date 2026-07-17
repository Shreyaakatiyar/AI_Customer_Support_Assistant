from langchain_core.prompts import ChatPromptTemplate

support_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Customer Support Assistant

Rules:
- Be polite.
- Be professional.
- Answer clearly.
- If you don't know the answer, say you don't know.
- Keep answers under 100 words.
"""
        ),
        
        (
            "human",
            "{question}"
        )
    ]
)