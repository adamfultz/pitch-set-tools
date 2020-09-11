# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:27:03 2020

@author: Adam
"""

# Defining Classes to manage DFS algorithm
class Node:
    def __init__(self, state, previous, action):
        self.state = state
        self.previous = previous
        self.action = action
        
class Frontier:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node        
