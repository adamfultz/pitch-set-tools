# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:00:20 2020

@author: Adam
"""
# import re
from dfclass import Node, Frontier
import copy
from sys import argv

'''
generate_scales:
    produces set of diatonic, whole tone, octatonic, and harmonic minor scales
    for analysis and generation of pitch sets
'''
def generate_scales():
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
    harm_minor_pattern = ['W', 'H', 'W', 'W', 'H', 'AUG', 'H']
    
    scale_set = []
    major_scales = dict()
    scale_set.append((major_scales, major_pattern))
    octa1_scales = dict()
    scale_set.append((octa1_scales, octa1_pattern))
    octa2_scales = dict()
    scale_set.append((octa2_scales, octa2_pattern))
    wholton_scales = dict()
    scale_set.append((wholton_scales, wholton_pattern))
    harm_min_scales = dict()
    scale_set.append((harm_min_scales, harm_minor_pattern))
    
    for scale in scale_set:
        for note in circle:
            scale[0][note] = {note}
            start = order.index(note)
            for interval in scale[1]:
                if interval == 'W':
                    scale[0][note].add(order[(start+2) % len(order)])
                    start += 2
                elif interval == 'H':
                    scale[0][note].add(order[(start+1) % len(order)])
                    start += 1
                elif interval == 'AUG':
                    scale[0][note].add(order[(start+3) % len(order)])
            
            return (order, scale_set)



'''
make_pset:
    generates a set of pitches that do not form a subset of any scale produced
    by generate_scales. User specifies starting pitch(es) and the number of
    pitches in the set (length). Recommend 5-7
'''
def make_pset(notes, length):
    if type(notes) != set or len(notes) > length:
        print("Correct usage: make_pset(notes[set of strings], length[int]),\
              length must be greater than number of notes")
        return 1
    # This section uses "off the shelf" DFS-searching objects to find solutions
    start = Node(notes, None, None)
    frontier = Frontier()
    frontier.add(start)
    soln_set = []
    
    order, scale_set = generate_scales()
    
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
    return soln_set

# for soln in soln_set:
#     if 'E/Fb' in soln:
#         print(soln)            
'''
build_chord:
    taking the user's input note and quality (e.g. major, minor, etc.),
    produces all possible applicable chords
'''             

def build_chord(note, quality):
    order, scale_set = generate_scales()
    # maps interval names to number of half-steps in each
    intervals = {
        'm2' : 1,
        'M2' : 2,
        'm3' : 3,
        'M3' : 4,
        'P4' : 5,
        'tt' : 6,
        'P5' : 7,
        'm6' : 8,
        'M6' : 9,
        'm7' : 10,
        'M7' : 11}
    
    if quality == "major":
        root = ['M3', 'P5']
        third = ['m3', 'm6']
        fifth = ['P4', 'M6']
        chord_set = [root, third, fifth]
        
    
    elif quality == "minor":
        root = ['m3', 'P5']
        third = ['M3', 'M6']
        fifth = ['P4', 'm6']
        chord_set = [root, third, fifth]
        
    elif quality == "promethian":
        root = ['tt', 'm7', 'M3', 'M6', 'M2']
        two = ['M3', 'm7', 'm3', 'm6', 'tt']
        three = ['tt', 'M7', 'M3', 'M2', 'm6']
        four = ['P4', 'm7', 'm6', 'M2', 'tt']
        chord_set = [root, two, three, four]
    
    
    
    soln_set = []
    start = order.index(note)
    # iterate through group of chords
    for sequence in chord_set:
        chord = [note]
        # iterate through the intervals in each of the chords
        for interval in sequence:
            next_note = order[(intervals[interval] + start) % len(order)]
            chord.append(next_note)
        soln_set.append(chord)
    return soln_set
    
    
    
    
    
    
    
    # quality options: major, minor, tritone, quartal, quintal, whole-tone, 
    # input one note and quality, no choice over other notes but choose chord quality- implement filter function



soln_set = build_chord('A', 'minor')            
# soln_set = make_pset({'A', 'D', 'E/Fb'}, 5)       
    























            
    
    