import os
from Server.loader import text_content_chunks
from langchain.prompts import PromptTemplate, ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = "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"
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
chat = ChatOpenAI(client=None, model="gpt-3.5-turbo", temperature=0.9)
text = "Considering the texts I sent please summarize them"
message = HumanMessage(content=text)
#print(chat(message))

# Initialize the conversation with a system message
#messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Add user messages for each chunk of text

messages = [message]
i = 0
for chunk in text_content_chunks:
    # if i == 2:
    #     messages.append(HumanMessage(content = f"{chunk}"))
    #     print(chunk)
    # i += 1
    response = chat(messages=[HumanMessage(content=f"Consider the following texts: {chunk}")])
    print(response.content)
    print()

# Create the chat completion
response = chat(messages=messages)
print()
# print(response)
# Print the assistant's responses
print(response.content)
