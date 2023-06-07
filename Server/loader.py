import textwrap
from langchain.document_loaders import UnstructuredHTMLLoader

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
max_chars = 4096*4

# List to store the text content chunks of each document
text_content_chunks = []

# Load each HTML file and extract the text content
for html_file in html_files:
    loader = UnstructuredHTMLLoader(html_file)
    document = loader.load()
    text_content = document[0].page_content
    
    # Split the text content into chunks that are small enough to fit within the token limit
    chunks = textwrap.wrap(text_content, max_chars)
    
    # Add the chunks to the list
    text_content_chunks.extend(chunks)

# Now, `text_content_chunks` is a list of strings, 
# where each string is a chunk of text that is within the token limit.