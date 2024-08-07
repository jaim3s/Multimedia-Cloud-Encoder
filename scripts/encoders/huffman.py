from scripts.source_code import SourceCode
from scripts.encoders.coding_method import CodingMethod
from scripts.encoders.huffman_node import HuffmanNode
from typing import List

class Huffman(CodingMethod):
    """
    A class of the Huffman code method.

        Attributes
        ----------

        source : "Source" 
            Source of the text file (Symbols, Probability Distribution)
        output_symbols : List[str]
            The output symbols of the coding method
        d : int
            The arity of the Huffman code 
        n : int
            Number of symbols

        Methods
        -------

        __str__(self) -> str:
            Represents the Huffman codification in a string format.
        __repr__(self) -> str:
            Represents the Huffman codification in a string format for data structures.
        init(self) -> List["HuffmanNode"]:
            Sort the symbols based on it's probabilities and generate the initial nodes.
        run(self) -> "HuffmanNode":
            Execute the entire Huffman codification algorihtm.
        mark(self, root: "HuffmanNode") -> None:
            Mark each node of the tree with it's code word.
        get_leaves(self, root: "HuffmanNode") -> List:
            Get the leaves of the tree.
        aux_get_leaves(self, root: "HuffmanNode", result: List[str]) -> None:
            Auxiliary funciton to get the leaves of the tree.
        get_source_code(self) -> "SourceCode":
            Get the source code from the Huffman code.
    """

    def __init__(self, source: "Source", output_symbols: List[str]) -> None: 
        super().__init__(source)
        self.output_symbols = output_symbols
        self.d = len(self.output_symbols)
        self.n = len(self.source.symbols)

    def init(self) -> List["HuffmanNode"]:
        """
        Sort the symbols based on it's probabilities and generate the initial nodes.

            Parameters
                None
    
            Returns
                return List of Huffman nodes
        """

        sorted_source = sorted(self.source.source, key=lambda symbol: symbol[1])
        return [HuffmanNode(sorted_source[i][0], sorted_source[i][1]) for i in range(self.n)]

    def run(self) -> "HuffmanNode":
        """
        Execute the entire Huffman codification algorihtm.

            Parameters
                None
    
            Returns
                return The root of the tree
        """

        nodes = self.init()
        r = (self.n-1)%(self.d-1)
        running = True

        while running:
            # Step 2
            child_nodes = nodes[:self.d-r]
            total_probability = 0
            for child_node in child_nodes:
                child_node.active = False
                total_probability += child_node.probability
            for i in range(r):
                child_node = HuffmanNode("", 0)
                child_node.active = None
                child_nodes.append(child_node)
            node = HuffmanNode("", total_probability)
            node.childs = child_nodes

            # Remove the inactive nodes from the node list
            for i in range(self.d-r):
                if nodes:
                    nodes.pop(0)
            nodes.append(node)

            # Sort the nodes list
            nodes = sorted(nodes, key=lambda node: node.probability)

            # Step 3
            if len(nodes) <= 1:
                running = False
            else:
                r = 0
        return node

    def mark(self, root: "HuffmanNode") -> None:
        """
        Mark each node of the tree with it's code word.

            Parameters
                root ("HuffmanNode"): The root of the tree
    
            Returns
                return None
        """

        if not root:
            return []
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                for i in range(len(node.childs)):
                    node.childs[i].mark = node.mark + self.output_symbols[i]
                    queue.append(node.childs[i])

    def get_leaves(self, root: "HuffmanNode") -> List:
        """
        Get the leaves of the tree.

            Parameters
                root ("HuffmanNode"): The root of the tree
    
            Returns
                return List with the leaves of the tree
        """

        result = []
        self.aux_get_leaves(root, result)
        return result

    def aux_get_leaves(self, root: "HuffmanNode", result: List[str]) -> None:
        """
        Auxiliary funciton to get the leaves of the tree.

            Parameters
                root ("HuffmanNode"): The root of the tree
                result (List): List for save the leaves of the tree
    
            Returns
                return None
        """

        if not root.childs:
            result.append(root.mark)
        else:
            for child in root.childs:
                self.aux_get_leaves(child, result)

    def get_source_code(self) -> "SourceCode":
        """
        Get the source code from the Huffman code.

            Parameters
                None
    
            Returns
                return Source code of the Huffman code
        """
        
        root = self.run()
        self.mark(root)
        return SourceCode(
            symbols1=self.source.symbols, 
            symbols2=self.get_leaves(root)
        )
