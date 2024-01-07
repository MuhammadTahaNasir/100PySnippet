# Get user input
input_seconds = int(input("Enter the duration in seconds: "))

# Calculate hours, minutes, and remaining seconds
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
remaining_seconds = input_seconds % 60

# Display the result
print(f"Equivalent time: {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
