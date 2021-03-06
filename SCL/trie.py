
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

# Trie functions. Source: https://www.geeksforgeeks.org/trie-insert-and-search/
def _charToIndex(ch):
    return ord(ch)-ord('A')

def insert(root,key):
    pCrawl = root
    length = len(key)
    for level in range(length):
        index = _charToIndex(key[level])
        if not pCrawl.children[index]:
            pCrawl.children[index] = TrieNode()
        pCrawl = pCrawl.children[index]
    pCrawl.isEndOfWord = True

def search(root, key):
    pCrawl = root
    length = len(key)
    for level in range(length):
        index = _charToIndex(key[level])
        if not pCrawl.children[index]:
            return False
        pCrawl = pCrawl.children[index]
    return pCrawl != None and pCrawl.isEndOfWord


# Another way to build tries
# Trie = lambda: collections.defaultdict(Trie)
# trie = Trie()
# #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
# nodes = [reduce(dict.__getitem__, word[::-1], trie)
#          for word in words]
