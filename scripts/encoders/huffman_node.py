class HuffmanNode:
    def __init__(self, symbol: str, probability: float) -> None:
        self.symbol = symbol
        self.probability = probability
        self.active = True
        self.childs = []
        self.mark = ""

    def __str__(self) -> str:
        return str(self.symbol)

    def __repr__(self) -> str:
        return str(self.symbol)