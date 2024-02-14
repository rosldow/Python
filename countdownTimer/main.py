import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1) # 1 second delay
        seconds -=1
    print("Time's up!")

try:
    seconds = int(input("Enter the countdown time in second: "))
    countdown_timer(seconds)
except ValueError:
    print("Invalid input.")
