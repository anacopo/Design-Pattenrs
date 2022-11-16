from AlignStrategy import AlignStrategy
from Paragraph import Paragraph

class AlignCenter(AlignStrategy):
    def render(self, p: Paragraph):
        print(f"###{p.text}###")