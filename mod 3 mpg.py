# Missing authorship comments
# Also, watch out for code plagiarism - read this article https://www.turnitin.com/blog/plagiarism-and-programming-how-to-code-without-plagiarizing-2
# Especially if this is something that you use as your own sample code later.

# Calculate Miles Per Gallon
print("This program calculates mpg.")
 
# Get miles driven from the user
miles_driven = input("Enter miles driven:") # Could simplify the next couple lines by wrtiting miles_driven = float(input("Enter miles driven:"))
# Convert text entered to a
# floating point number
miles_driven = float(miles_driven)
 
# Get gallons used from the user
gallons_used = input("Enter gallons used:")
# Convert text entered to a
# floating point number
gallons_used = float(gallons_used)
 
# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)
