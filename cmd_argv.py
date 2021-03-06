# Command Line Arguments
import sys

# Print Arguments
print("Number of arguments:", len(sys.argv), "arguments.")  # C-Style
print("Arguments:", sys.argv)

print()

# Sum up the Arguments
sum = 0
for arg in sys.argv[1:]:
    try:
        sum += int(arg)
    except Exception as e:
        print(str(type(e)) + ": " + str(e))

print(sum)
