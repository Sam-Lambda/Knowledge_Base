import re
import time
from notion.client import NotionClient

client = NotionClient(token_v2="v02:user_token_or_cookies:0V-vI1mVN4W_SilkpXOPAZvXbB2J37L4h_ndZ3wbDX8n750p6dkVDXV-UMJ5-1bMMtuwKnngm40hFcv7KMN7akqJGfYMRyhVD8nLTSm8ouT4Wxj4tfyHN62vd2xB05sfR1Xd")

page = client.get_block("https://www.notion.so/ac9cfd8065574ae98726ea959535be99")

print("The old title is:", page.title)

page.title = "Workspace for knowledge base"

def on_change(record, difference):
    print("The record's title is now:", record.title)
    print("Here's what was changed:")
    print(difference)


# for child in page.children:
#     child.remove_callbacks()
#     child.add_callback(on_change)

def find_request(page):
    for child in page.children:
        matched = re.match(r'Explain: (.*)', child.title)
        if matched:
            print("Topic to explain found: ", matched.group(1))

while True:
    
    time.sleep(5)
    page.refresh()
    find_request(page)