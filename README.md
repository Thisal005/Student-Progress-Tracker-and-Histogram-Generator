# Student-Progress-Tracker-and-Histogram-Generator

This Python program helps track and visualize student progress based on their credit data. It allows users to input credits for "Pass," "Defer," and "Fail" categories, calculates the student's progress (e.g., "Progress," "Progress (Module trailer)," etc.), and generates a histogram to display the distribution of outcomes.

Features:

Credit Validation: Ensures input credits are within the valid range and total up to 120.

Progress Calculation: Based on the provided credits, determines the student's outcome (e.g., Progress, Trailer, Retriever, Exclude).

Data Logging: Saves entered data to a file for later review.

Histogram Generation: Uses the graphics.py library to create a bar chart showing the distribution of progress outcomes.




How It Works:



The user selects between student or staff login.

The program prompts the user to input their credits for "Pass," "Defer," and "Fail."

The student's progress status is determined based on their credit input.

The outcomes are visualized through a histogram displaying the number of students in each outcome category.

Data is saved to a file and displayed in the console.



Requirements:

Python 3.x

graphics.py library for histogram generation (can be installed via pip if necessary)
