from notion.block import Block

class ExplainBlock:
    def __init__(self, parent: Block) -> None:
        self.parent = parent
    
    def template