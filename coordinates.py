import pyautogui
import time

print("Move your mouse to the desired location.")
print("Coordinates will be displayed every second. Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()  # Get current mouse coordinates
        position_str = f"X: {x} Y: {y}"
        print(position_str)  # Print in the same line
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopped.")
