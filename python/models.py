class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.val == other.val and self.next == other.next
