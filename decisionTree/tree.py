from turtle import right


class node:
    def __init__(self, left, right, feature, split, is_leaf):
        self.left = left
        self.right = right
        self.feature = feature
        self.split = split
        self.is_leaf = is_leaf