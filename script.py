import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 2:
    print("Usage: python your_script.py <selected_status>")
    sys.exit(1)

# Retrieve the selected status from the command-line argument
selected_status = sys.argv[1]

# Perform tasks based on the selected status
if selected_status == "Active":
    # Perform tasks for Active status
    print("Doing tasks for Active status...")
elif selected_status == "Inactive":
    # Perform tasks for Inactive status
    print("Doing tasks for Inactive status...")
else:
    # Handle other cases if necessary
    print("Invalid status")
