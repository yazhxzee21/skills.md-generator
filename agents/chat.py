from app.config import llm

def chat(user_message: str):
    response = llm.invoke(user_message)
    return response.content