class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def helper(node, word, idx):
            # Base Case
            if len(word) == idx:
                return node.word

            # Explore and traverse
            if word[idx] in node.children:
                return helper(node.children[word[idx]], word, idx + 1)
            elif word[idx] == ".":
                for c in node.children:
                    if helper(node.children[c], word, idx + 1):
                        return True
                return False
            else:
                return False

        return helper(self.root, word, 0)

class Node:
    def __init__(self):
        self.children = {}
        self.word = False
        
