import pyautogui
import time

print("Move the mouse to the desired position, then press 'Enter' to record the position.")
input()  # Wait for the user to press Enter

# Get the current mouse position
click_position = pyautogui.position()
print(f"Position recorded: {click_position}")
while True:
    # Perform a click at the recorded position
    print(f"Clicking at position: {click_position}")
    pyautogui.click(click_position)
    time.sleep(1)
