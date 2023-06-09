from notion.block import Block, TodoBlock
import re

def extract_topic(block: Block) -> str | None:
    matched = re.match(r'Explain: (.*)\.', block.title)
    if matched:
        return matched.group(1)
    return None

class ExplainBlock:
    def __init__(self, parent: Block) -> None:
        self.parent = parent
        self._topic = extract_topic(self.parent)
        self._checked = False
        self.init_template()
        self._checked = self.block.checked
        self.block.add_callback(self.update_checked)
        self.parent.add_callback(self.update_topic)
    
    def update_topic(self):
        self._topic = extract_topic(self.parent)
        self.update_title()

    def update_checked(self):
        self._checked = self.block.checked
        self.update_title()

    def update_title(self):
        self.block.title = f"Ask knowledge base to explain: {self._topic}.{ ' This is checked!' if self._checked else ''}"

    def init_template(self) -> None:
        self.block = self.parent.children.add_new(TodoBlock, title=f"Ask knowledge base to explain: {self._topic}.{ ' This is checked!' if self._checked else ''}")