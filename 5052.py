import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data, isFinish=False):
        self.data = data
        self.isFinish = isFinish
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current = self.head
        
        for i in range(len(string)):
            char = string[i]
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

            if current.isFinish:
                return False

            if i == len(string) - 1:
                current.isFinish = True

        return True

t = int(input())

for _ in range(t):
    n = int(input())

    isTrue = True
    trie = Trie()

    numbers = [str(input().rstrip()) for _ in range(n)]
    numbers.sort()

    for number in numbers:
        if not trie.insert(number):
            isTrue = False

    if isTrue:
        print("YES")
    else:
        print("NO")