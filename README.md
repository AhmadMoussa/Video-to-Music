# VidToMu

Small pet project that is supposed to ultimately enable midi generation from a video stream.

## Using:
* Python
* OpenCV

## Current Problems:
* Need to determine which midi library is best for my purpose. Vishnubob, music21 or midiutil are viable options. Maybe I will write my own library.
* Optimize pixel loops, currently the loops to detect color activations are not very efficient, I need to find a better way to do it. Viable options are cython or multithreading. Or both combined. Also look into OpenMP.
  
## Updates:
* Gricclass that splits frame into several subframes
* CellClass that enables us to draw a grid overlay
* Gridoverlay feature
* Color Activation function in the CellClass

  
## Future:
  * ~~Divide video frames into smaller cells
  * ~~Use these cell to detect an activation of color
  * ~~If activation positive, send a signal
  * ~~Assign cells to midi notes
  * ~~Quantize these notes
  * Return a midi stream
  * Figure out which midi library to use
  * fix bugs
  * Optimize the pixel loops in the cellClass
