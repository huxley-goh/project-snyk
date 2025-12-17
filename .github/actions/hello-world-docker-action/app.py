# hello_arg.py
import sys

if __name__ == "__main__":
    # Check if at least one argument was provided (sys.argv[0] is the script name)
    if len(sys.argv) > 1:
        user_argument = sys.argv[1]
        print(f"Hello, {user_argument}!")
    else:
        print("Hello, world! (No argument provided)")
