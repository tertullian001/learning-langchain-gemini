from langchain_core.runnables import chain
from langchain_core.prompts import ChatPromptTemplate


import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
    
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


@chain
async def chatbot(values):
    prompt = await template.ainvoke(values)
    return await model.ainvoke(prompt)


async def main():
    return await chatbot.ainvoke({"question": "Which model providers offer LLMs?"})

if __name__ == "__main__":
    import asyncio
    print(asyncio.run(main()))
