from langchain_core.prompts import ChatPromptTemplate


import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
    
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"

# the building blocks

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# combine them with the | operator

chatbot = template | model

# use it

response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response.content)

# streaming

for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)
