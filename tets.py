# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = r"C:\Users\SANJEEV KUMAR\OneDrive\Pictures\Screenshots\Screenshot (2400).png"
image = cv2.imread(image_path)

def four_point_neighbors(image, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < image.shape[0] - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < image.shape[1] - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

# Define function to find 8-point neighbors
def eight_point_neighbors(image, row, col):
    neighbors = four_point_neighbors(image, row, col)
    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))  # Top-left
    if row > 0 and col < image.shape[1] - 1:
        neighbors.append((row - 1, col + 1))  # Top-right
    if row < image.shape[0] - 1 and col > 0:
        neighbors.append((row + 1, col - 1))  # Bottom-left
    if row < image.shape[0] - 1 and col < image.shape[1] - 1:
        neighbors.append((row + 1, col + 1))  # Bottom-right
    return neighbors

# Define function to find diagonal neighbors
def diagonal_neighbors(image, row, col):
    neighbors = []
    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))  # Top-left
    if row > 0 and col < image.shape[1] - 1:
        neighbors.append((row - 1, col + 1))  # Top-right
    if row < image.shape[0] - 1 and col > 0:
        neighbors.append((row + 1, col - 1))  # Bottom-left
    if row < image.shape[0] - 1 and col < image.shape[1] - 1:
        neighbors.append((row + 1, col + 1))  # Bottom-right
    return neighbors

row = 10
col = 10

print("4-Point Neighbors:", four_point_neighbors(image, row, col))
print("8-Point Neighbors:", eight_point_neighbors(image, row, col))
print("Diagonal Neighbors:", diagonal_neighbors(image, row, col))

