from app.config import llm


def chat_with_document(document, question):

    prompt = f"""
You are a helpful AI assistant.

The user may ask questions about an uploaded document or ask general knowledge questions.

Rules:
1. If the user's question is related to the uploaded document, answer using the document.
2. If the answer is not present in the document but you know it from your general knowledge, answer normally.
3. If the document contains relevant information, prioritize the document over your own knowledge.
4. Be concise, clear, and professional.

Uploaded Document:
------------------
{document}

User Question:
--------------
{question}
"""

    response = llm.invoke(prompt)

    return response.content