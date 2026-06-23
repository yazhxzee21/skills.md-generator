from app.config import llm


def generate_skills(document_text):

    prompt = f"""
You are an expert business analyst.

Analyze the document below.

Generate a complete skills.md file.

Format exactly as:

# Skill Name

## Purpose

## Capabilities

## Required Knowledge

## Workflow

## Inputs

## Outputs

Document:

{document_text}
"""

    response = llm.invoke(prompt)

    return response.content