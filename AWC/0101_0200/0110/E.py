import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

class TrieNode:
    """Trie木のノード"""

    def __init__(self):
        self.children = {}
        # 文字列終了のノードか
        self.is_end_of_word = False
        # この文字が接頭辞に含まれる個数
        self.num = 0


class Trie:
    """Trie木"""

    def __init__(self):
        self.root = TrieNode()
        self.total = 0

    def insert(self, word):
        """データの挿入を行います"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.num += 1
        node.is_end_of_word = True

    def search(self, word):
        """データの検索を行います"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """先頭一致でデータの取得を行います"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def dfs(self, node: TrieNode | None, depth: int=0):
        """深さ優先探索（木DP）"""
        global IS_OK
        global RESULT
        if not IS_OK:
            return
        if node is None:
            node = self.root
        if node.is_end_of_word:
            if node.num != 1:
                IS_OK = False
                return
        if node.num == 1:
            RESULT += depth
            return
        for c in node.children:
            self.dfs(node.children[c], depth + 1)


N = int(input())
tree = Trie()
for _ in range(N):
    S = input()
    tree.insert(S)
RESULT = 0
IS_OK = True
tree.dfs(None, 0)
if IS_OK:
    print(RESULT)
else:
    print(-1)
