from collections import deque


class AhoCorasick:
    def __init__(self):
        self.trie = {}
        self.fail = {}
        self.output = {}

    def add_word(self, word):
        """Trie木に単語を追加"""
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        if "output" not in node:
            node["output"] = []
        node["output"].append(word)

    def build_automaton(self):
        """失敗遷移を構築"""
        queue = deque()
        # ルートノードのすべての子ノードを初期化
        for char, child in self.trie.items():
            self.fail[id(child)] = self.trie  # 子ノードの失敗遷移をルートに設定
            queue.append(child)

        # BFS で失敗遷移を設定
        while queue:
            current_node = queue.popleft()
            for char, child_node in current_node.items():
                if char == "output":
                    continue
                # 失敗遷移を探す
                fail_node = self.fail[id(current_node)]
                while fail_node is not None and char not in fail_node:
                    fail_node = self.fail.get(id(fail_node))
                # 適切な失敗遷移を設定
                self.fail[id(child_node)] = fail_node[char] if fail_node and char in fail_node else self.trie
                # 出力を継承
                if "output" in self.fail[id(child_node)]:
                    if "output" not in child_node:
                        child_node["output"] = []
                    child_node["output"].extend(self.fail[id(child_node)]["output"])
                queue.append(child_node)

    def search(self, text):
        """テキスト内のパターンを検索"""
        node = self.trie
        results = []
        for i, char in enumerate(text):
            # 現在のノードから遷移できない場合は失敗遷移を辿る
            while node is not None and char not in node:
                node = self.fail.get(id(node), self.trie)
            # 適切なノードに移動する
            if node is None:
                node = self.trie
                continue
            node = node[char]
            # 出力がある場合は結果を追加
            if "output" in node:
                for word in node["output"]:
                    results.append((i - len(word) + 1, word))
        return results


# サンプルコード
patterns = ["he", "she", "his", "hers"]
text = "ahishers"

ac = AhoCorasick()
for pattern in patterns:
    ac.add_word(pattern)
ac.build_automaton()
print("Search results:", ac.search(text))
