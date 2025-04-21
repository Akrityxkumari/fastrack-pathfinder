import random
import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import string

# Initialize global variables
cities = []
city_names = []
N = 0

# Predefined city names list
predefined_city_names = [
    "Tokyo", "New York", "Paris", "London", "Mumbai", "Sydney",
    "Cairo", "Moscow", "Rio", "Toronto", "Rome", "Dubai", "Beijing",
    "Seoul", "Istanbul", "Madrid", "Chicago", "Bangkok", "Berlin",
    "Los Angeles", "Barcelona", "Singapore", "Vienna", "Osaka",
    "San Francisco", "Amsterdam"
]

def distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def total_distance(tour):
    dist = 0
    for i in range(len(tour)):
        dist += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return dist

def swap_two_cities(tour):
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def hill_climbing():
    current_solution = list(range(len(cities)))
    random.shuffle(current_solution)
    current_cost = total_distance(current_solution)

    improvement = True
    while improvement:
        improvement = False
        for _ in range(100):
            neighbor = swap_two_cities(current_solution)
            neighbor_cost = total_distance(neighbor)
            if neighbor_cost < current_cost:
                current_solution = neighbor
                current_cost = neighbor_cost
                improvement = True
                break
    return current_solution, current_cost

def plot_tour(tour, title="Travel Path"):
    x = [cities[i][0] for i in tour] + [cities[tour[0]][0]]
    y = [cities[i][1] for i in tour] + [cities[tour[0]][1]]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o-r', label='Path')

    for idx, city_idx in enumerate(tour):
        city_x, city_y = cities[city_idx]
        if idx == 0:
            plt.plot(city_x, city_y, 'go', markersize=10)  # Start city in green
            plt.text(city_x+0.5, city_y+0.5, f"Start: {city_names[city_idx]}", fontsize=9, color='green')
        elif idx == len(tour) - 1:
            plt.plot(city_x, city_y, 'ro', markersize=10)  # Last city in red
            plt.text(city_x+0.5, city_y+0.5, f"End: {city_names[city_idx]}", fontsize=9, color='red')
        else:
            plt.plot(city_x, city_y, 'bo', markersize=8)  # Other cities in blue
            plt.text(city_x+0.5, city_y+0.5, f"{city_names[city_idx]}", fontsize=8)

    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def generate_cities():
    global cities, city_names, N
    try:
        N = int(city_count_entry.get())
        if N <= 0:
            raise ValueError
        cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(N)]
        city_names = generate_city_names(N)
        messagebox.showinfo("Success", f"{N} cities generated!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive number.")

def generate_city_names(n):
    names = []
    for i in range(n):
        if i < len(predefined_city_names):
            names.append(predefined_city_names[i])
        else:
            alphabet = list(string.ascii_uppercase)
            idx = i - len(predefined_city_names)
            names.append(f"City {alphabet[idx // 26 % 26]}{alphabet[idx % 26]}")
    return names

def clear_cities():
    global cities, city_names
    cities = []
    city_names = []
    result_label.config(text="")
    messagebox.showinfo("Clear", "Cities cleared! You can now generate new cities.")

def run_hill_climbing():
    if not cities:
        messagebox.showerror("Error", "Please generate cities first!")
        return
    solution, cost = hill_climbing()
    result_label.config(text=f"Optimized Distance: {cost:.2f}")
    plot_tour(solution, f"Optimized Tour (Distance: {cost:.2f})")

# GUI Window
window = tk.Tk()
window.title("TSP Hill Climbing Optimizer")
window.geometry("420x330")
window.configure(bg="#F0F0F0")

title_label = tk.Label(window, text="Travelling Salesman Problem", font=("Helvetica", 16, "bold"), bg="#F0F0F0")
title_label.pack(pady=12)

city_count_label = tk.Label(window, text="Enter Number of Cities:", font=("Helvetica", 12), bg="#F0F0F0")
city_count_label.pack()

city_count_entry = tk.Entry(window, font=("Helvetica", 12))
city_count_entry.pack(pady=6)
city_count_entry.insert(0, "10")

# Buttons
generate_btn = tk.Button(window, text="Generate Cities", command=generate_cities, bg="#98FB98", font=("Helvetica", 11))
generate_btn.pack(pady=5)

clear_btn = tk.Button(window, text="Clear Cities", command=clear_cities, bg="#FF7F7F", font=("Helvetica", 11))
clear_btn.pack(pady=5)

solve_btn = tk.Button(window, text="Optimize Route", command=run_hill_climbing, bg="#FFA500", font=("Helvetica", 11))
solve_btn.pack(pady=5)

# Result display
result_label = tk.Label(window, text="", font=("Helvetica", 13, "bold"), fg="#333333", bg="#F0F0F0")
result_label.pack(pady=12)

window.mainloop()
