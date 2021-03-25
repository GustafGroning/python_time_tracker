# python_time_tracker
A small python script for logging your time spent between different tasks. Mostly made for my own education in Python.

Whenever a task is completed, it's saved in timeLog.json. The program starts with 20 minutes logged in each category for the sake of being able to test the statistics.

## Fixes/issues
1. Right now, all saved data gets used when the user checks for reports. A choice should be available to allow viewing statistics from just the past day/week/month. This requires modifying timeLog.json to include a datetime timestamp.
2. Currently only three categories (work, fun, waste) exist. Later on the plan is to allow the user to create custom categories.
3. AppKit stopped working during development, which made it impossible to track tasks automatically (which was the original goal). The problem might be with my installation of Python, this is the main thing to fix later on, which will be a complete overhaul of the app. The goal is for the user to be able to create custom categories, save which websites or apps belong to which category, and for the program to run in the background, without requiring input for switching tasks or saving the data.


Categories.json and unused.txt includes components that were usefull when the app was built with automatic tracking through AppKit. I keep the code here so it's available when/if i get AppKit working again.