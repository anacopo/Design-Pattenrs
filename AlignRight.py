from AlignStrategy import AlignStrategy
from Paragraph import Paragraph

class AlignRight(AlignStrategy):
    def render(self, p: Paragraph):
        print(f"######{p.text}")