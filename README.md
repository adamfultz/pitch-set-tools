# pitch-set-tools
Tools for studying pitch sets for advanced music composition

This repository contains code that can be used to study and produce computer-informed music. This is NOT the same as electronic music. Rather, this code enables composers to create sequences of notes that satisfy particular musical constraints of interest- e.g. not belonging to certain scales, pitch sets, etc. 

1st iteration: 11 Sept. 2020
The user can enter a series of notes into the script (line 52) which will be used to generate a list of all related 5-note sequences that are not part of any major/minor/modal, whole tone, or octatonic scale. 

2nd iteration: 22 Sept. 2020
Broke the functionality apart into individual functions and began formalizing the script. Added the build_chord function, which can produce sets of viable chords from a user-specified starting pitch and chord type/quality.
