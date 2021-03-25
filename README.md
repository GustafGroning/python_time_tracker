# python_time_tracker




## Fixes/issues
1. Right now, all saved data gets used when the user checks for reports. A choice should be available to allow viewing statistics from just the past day/week/month. This requires modifying timeLog.json to include a datetime timestamp.
2. AppKit stopped working during development, which made it impossible to track tasks automatically (which was the original goal). The problem might be with my installation of Python, this is the main thing to fix later on, which will be a complete overhaul of the app.

Categories.json and unused.txt includes components that were usefull when the app was built with automatic tracking through AppKit. I keep the code here so it's available when/if i get AppKit working again.