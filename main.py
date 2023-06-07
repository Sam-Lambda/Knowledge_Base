import os
from Server.loader import text_content_chunks
from langchain.chat_models import Message

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
text = "Tell me the recent news about gaming"
#message = [HumanMessage(content=text)]
#print(chat(message))

# Initialize the conversation with a system message
messages = [Message(role="system", content="You are a helpful assistant.")]

# Add user messages for each chunk of text
for chunk in text_content_chunks:
    messages.append(Message(role="user", content=f"Do something with this text: '{chunk}'"))

# Create the chat completion
response = chat(messages)

# Print the assistant's responses
for message in response.messages:
    print(message.content)
