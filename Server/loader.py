import textwrap
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter,  Language

# List of paths to HTML files
html_files = [
    ".\\Doc1.html",
    ".\\Doc2.html",
    ".\\Doc3.html",
    ".\\Doc4.html",
    ".\\Doc5.html",
]

# Set maximum tokens limit. For GPT-3.5, it's 4096 tokens.
# 1 token ~= 4 chars in English, set the maximum characters to 4096*4
max_chars = 4096

# Create an instance of the EnglishTextSplitter
splitter = RecursiveCharacterTextSplitter.from_language(Language.HTML, chunk_size=max_chars)
# splitter._chunk_size = max_chars

# List to store the text content chunks of each document
text_content_chunks = []

# Load each HTML file and extract the text content
for html_file in html_files:
    loader = UnstructuredHTMLLoader(html_file)
    document = loader.load()
    text_content = document[0].page_content
    
    # Split the text content into chunks that are small enough to fit within the token limit
    splits = splitter.split_text(text_content)
    
    # Add the chunks to the list
    text_content_chunks.extend(splits)
# list of strings, each string is a chunk of text that is within the token limit.