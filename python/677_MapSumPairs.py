from collections import defaultdict


class MapSum:
    class Node:
        def __init__(self):
            self.count = 0
            self.children = defaultdict(self.__class__)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dep = {}
        self.roots = defaultdict(self.Node)

    def insert(self, key: str, val: int) -> None:
        if key not in self.dep:
            self.dep[key] = val
        else:
            self.dep[key], val = val, val - self.dep[key]
        nodes = self.roots
        for v in key:
            nodes[v].count += val
            nodes = nodes[v].children

    def sum(self, prefix: str) -> int:
        nodes = self.roots
        for v in prefix[:-1]:
            nodes = nodes[v].children
        return nodes[prefix[-1]].count
