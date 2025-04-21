# TSP Hill Climbing Optimizer

This Python application solves the **Travelling Salesman Problem (TSP)** using a **Hill Climbing optimization algorithm**. It provides a graphical interface (GUI) using **Tkinter** to generate cities, optimize the tour, and visualize the result using **Matplotlib**.

## Features

- Generate a custom number of cities randomly placed on a 2D map.
- Automatically assigns city names using a predefined list and custom naming.
- Uses Hill Climbing to find a short route visiting all cities once and returning to the starting point.
- Visualizes the optimized path with clear markers for start, end, and intermediate cities.
- Intuitive and clean GUI interface.

## Requirements

- Python 3.x
- `matplotlib`
- `tkinter` (comes pre-installed with most Python distributions)

### Install dependencies

Use pip to install Matplotlib if it's not already installed:

```bash
pip install matplotlib
