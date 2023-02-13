class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, str_list):
        current = self.head

        for string in str_list:
            # children에 string이 있는지 찾기
            idx = -1
            isTrue = False
            for i in range(len(current.children)):
                if current.children[i].data == string:
                    idx = i
                    isTrue = True
                    break
            
            # children에 없다면 생성
            if not isTrue:
                current.children.append(Node(string))

            # 해당 child로 이동
            current = current.children[idx]

    def print_trie(self, current, depth):
        # 사전 순으로 출력하기 위한 정렬
        current.children.sort(key=lambda x:x.data)

        # 루트 노드를 제외하고 재귀적으로 출력
        if depth != -1:
            print("--" * depth + current.data)
        for child in current.children:
            self.print_trie(child, depth + 1)

n = int(input())
trie = Trie()

for _ in range(n):
    x = list(map(str, input().split()))[1:]
    trie.insert(x)

trie.print_trie(trie.head, -1)