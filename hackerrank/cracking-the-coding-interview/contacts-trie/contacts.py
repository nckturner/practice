#!/usr/bin/env python3

inp = """add boo
add b
add book
add boo
add boy
add bla
add dog
find bo"""

class Node:
    def __init__(self):
        self.children = {}
        self.num = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def trie_add(self, contact):
        node = self.root
        for letter in contact:
            node = node.children.setdefault(letter, Node())
            node.num += 1
        node.children.setdefault("end")

    def trie_find(self, contact):
        node = self.root
        for letter in contact:
            node = node.children.get(letter, None)
            if not node:
                return 0
        return node.num

trie = Trie()

for line in inp.split('\n'):
    op, contact = line.split(' ')

    if op == "add":
        trie.trie_add(contact)
    elif op == "find":
        print(trie.trie_find(contact))



