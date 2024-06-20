class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Trieを作成
trie = Trie()

# 単語を挿入
trie.insert("apple")
trie.insert("app")
trie.insert("application")

# 検索
print(trie.search("apple"))      # 出力: True
print(trie.search("app"))        # 出力: True
print(trie.search("appl"))       # 出力: False
print(trie.search("application"))# 出力: True
print(trie.search("applica"))    # 出力: False

# 接頭辞の検索
print(trie.starts_with("app"))   # 出力: True
print(trie.starts_with("appli")) # 出力: True
print(trie.starts_with("bat"))   # 出力: False

