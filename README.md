# VidToMu

Small pet project that is supposed to ultimately enable midi generation from a video stream.

## Using:
* Python
* OpenCV
* midiutil

## Current Problems:
* Need to determine which midi library is best for my purpose. Vishnubob, music21 or midiutil are viable options. Maybe I will write my own library. (for now I am sticking to midiutil) 
* Optimize pixel loops, currently the loops to detect color activations are not very efficient, I need to find a better way to do it. Viable options are cython or multithreading. Or both combined. Also look into OpenMP.

## Actual Problem 4/28/2019
* Now that everything somehow works, I need to determine the best model for my algorithm to get desirable results. The questions that I'm asking myself are:
1 How do certain colors translate into certain melodies, scales and modes?
2 What aspect does the color intensity play in this translation?
3 How is the amount of color present in a cell influencing the generated music?
4 Could I use crowdsourcing and machine learning to get data and enhance my algorithm? 
  
## Updates:
* Gricclass that splits frame into several subframes
* CellClass that enables us to draw a grid overlay
* Gridoverlay feature
* Color Activation function in the CellClass

  
## Future:
  * ~~Divide video frames into smaller cells~~
  * ~~Use these cell to detect an activation of color~~
  * ~~If activation positive, send a signal~~
  * ~~Assign cells to midi notes~~
  * ~~Quantize these notes~~
  * Return a midi stream
  * Figure out which midi library to use
  * fix bugs
  * Optimize the pixel loops in the cellClass
