# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:00:20 2020

@author: Adam
"""
# import re
from dfclass import Node, Frontier
import copy

# Music Set Analysis
circle = ['B#/C', 'G', 'D', 'A', 'E/Fb', 'B/Cb', 'F#/Gb', 'E#/F', 
          'A#/Bb', 'D#/Eb', 'G#/Ab', 'C#/Db']
order = ['B#/C', 'C#/Db', 'D', 'D#/Eb', 'E/Fb', 'E#/F', 'F#/Gb',
             'G', 'G#/Ab', 'A', 'A#/Bb', 'B/Cb']
chrom_set = {'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#', 'Fb', 'F', 'F#',
             'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'B#', 'Cb'}
major_pattern = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
wholton_pattern = ['W', 'W', 'W', 'W', 'W', 'W']
octa1_pattern = ['H', 'W', 'H', 'W', 'H', 'W', 'H', 'W']
octa2_pattern = ['W', 'H', 'W', 'H', 'W', 'H', 'W', 'H']

scale_set = []
major_scales = dict()
scale_set.append((major_scales, major_pattern))
octa1_scales = dict()
scale_set.append((octa1_scales, octa1_pattern))
octa2_scales = dict()
scale_set.append((octa2_scales, octa2_pattern))
wholton_scales = dict()
scale_set.append((wholton_scales, wholton_pattern))

for scale in scale_set:
    for note in circle:
        scale[0][note] = {note}
        start = order.index(note) # need to rethink this or use regex
        for interval in scale[1]:
            if interval == 'W':
                scale[0][note].add(order[(start+2) % len(order)])
                start += 2
            elif interval == 'H':
                scale[0][note].add(order[(start+1) % len(order)])
                start += 1
        # Chooses flats to build scales if flat key
        # if re.search('b', note) or note == 'F':

# Finding a non-scale pitch set
# starting_pitch = input("Starting Pitch: ")

# Depth-first search finding all sets
# start = Node({starting_pitch}, None, None)
start = Node({'A', 'D', 'E/Fb', 'C#/Db'}, None, None)
frontier = Frontier()
frontier.add(start)
soln_set = []

while True:
    node = frontier.remove()
    # Defining pitches that could be added and adding them to frontier
    for note in order:
        if note not in node.state and len(node.state) < 5:
            pset = copy.copy(node.state)
            pset.add(note)
            frontier.add(Node(pset, None, None))
            
    # Checking if pitch set is unique, non-scale
    add = True
    for group in scale_set:
        for scale in group[0]:
            if node.state.issubset(group[0][scale]):
                add = False
    if add and len(node.state) == 5:
       soln_set.append(node.state)
    if frontier.empty():
        break

# for soln in soln_set:
#     if 'E/Fb' in soln:
#         print(soln)            
             
            
        
    























            
    
    