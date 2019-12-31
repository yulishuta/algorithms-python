#!/usr/bin/python
# -*- coding: UTF-8 -*-
class DWeightEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def start(self):
        return self.v

    def to(self):
        return self.w

    def getWeight(self):
        return self.weight

    def isSame(self, newEdge):
        return self.v == newEdge.v and self.w == newEdge.w and self.weight == newEdge.weight
