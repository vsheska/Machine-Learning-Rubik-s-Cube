# Machine-Learning-Rubik-s-Cube
This repository contains the code used for my Rubik's Cube(2x2x2) machine learning project. The idea is to perform a weighted search through cube states until the solved cube is found. Currently a work in progress.

The CubeStructure.py file contains the structure of the cube, as well as methods to manipulate. Also included are function to generate a solved cube, as well as generate a scrambled cube given a number of turns from the solved state.

The Solver.py file contains a weighted search, where the weights are given by a neural network generated through tensorflow.
