# VidToMu

Small pet project that is supposed to ultimately enable midi generation from a video stream.

## Using:
* Python
* OpenCV
* Midiutil
* Refer to this [tutorial](https://github.com/AhmadMoussa/Python-Midi-Ableton) to set up python and ableton

## Current Problems:
* 05/08/2019 Need to find an efficient way to translate pixels into music. 
* ~~~Need to determine which midi library is best for my purpose. Vishnubob, music21 or midiutil are viable options. Maybe I will write my own library. (for now I am sticking to midiutil)~~~ Not needed anymore, figured out how to send signals in realtime to ableton. Hence for now I don't require to handle midi files. Otherwise, midiutil works just fine.
* Optimize pixel loops, currently the loops to detect color activations are not very efficient, I need to find a better way to do it. Viable options are cython or multithreading. Or both combined. Also look into OpenMP. 05/08/2019 This is still a problem. I discovered that it is even worse now with high resolution videos. There has to be a much faster way than what I am doing.
* ~~~4/29/2019  need to send realtime midi signals to ableton live from python~~~

## Actual Problem 4/28/2019
Now that everything somehow works, I need to determine the best model for my algorithm to get desirable results. The questions that I'm asking myself are:
1. How do certain colors translate into certain melodies, scales and modes?
  * maybe take into consideration the positional data of color triggers, https://www.youtube.com/watch?v=sxtUjeYJU7A comments on this video give relevant ideas
2. What aspect does the color intensity play in this translation? 05/08/2019 intensity could play some sort of threshholding value, such that certain notes only trigger if a certain value is surpassed. 
3. How is the amount of color present in a cell influencing the generated music?
4. Could I use crowdsourcing and machine learning to get data and enhance my algorithm? 
5. explore histogram comparison to compare the amount of change of color between frames
  
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
  * ~~Figure out which midi library to use~~ for now I am using MidiUtil which is doing just fine, but I don't know if I actually require it since I'm don't really need to create midi files to disk and back, I need realtime transmission
  * fix bugs
  * Optimize the pixel loops in the cellClass
  * need it to be able to detect a range of colors not just one specific color
  * figure out how the output music is being modeled and what role the video/color elements play in this generation
  * send midi signals to ableton live from python in realtime [This is a start on how to do so](https://wiki.python.org/moin/PythonInMusic#MIDI_Mania)
