import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random
import math
import os

# Initialize pygame mixer
pygame.mixer.init()

# Get the current directory
current_directory = os.path.dirname(__file__)

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Function to create the Toplevel window for displaying the GIF
def create_error_window():
    # Create a Toplevel window for displaying the GIF
    error_window = tk.Toplevel()
    error_window.title("You are an idiot!")  # Change the title
    error_window.geometry("400x300")  # Set initial dimensions (width: 400, height: 300)

    # Load GIF image
    gif_path = os.path.join(current_directory, "Offiz_resources\\you-are-an-idiot.gif")
    gif_image = Image.open(gif_path)
    tk_image = ImageTk.PhotoImage(gif_image)

    # Create a label to display the GIF image
    image_label = tk.Label(error_window, image=tk_image)
    image_label.image = tk_image  # Keep a reference to prevent garbage collection
    image_label.pack()

    # Define parameters for movement
    speed = 30  # Double the speed
    move_interval = 20  # Update interval in milliseconds

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Choose a random angle between down and right
    angle = random.uniform(-math.pi / 4, math.pi / 4)  # Angle between -45 and 45 degrees

    # Calculate direction components using trigonometry
    direction_x = math.cos(angle)
    direction_y = math.sin(angle)

    # Function to move the window around the screen
    def move_error_window():
        nonlocal direction_x, direction_y
        current_x = error_window.winfo_x()
        current_y = error_window.winfo_y()

        # Calculate new position
        new_x = current_x + direction_x * speed
        new_y = current_y + direction_y * speed

        # Check if the window hits the edges of the screen
        if new_x <= 0 or new_x >= screen_width - error_window.winfo_width():
            direction_x *= -1
        if new_y <= 0 or new_y >= screen_height - error_window.winfo_height():
            direction_y *= -1

        # Convert new position to integers
        new_x = int(new_x)
        new_y = int(new_y)

        # Move the window
        error_window.geometry(f"+{new_x}+{new_y}")

        # Schedule next movement
        error_window.after(move_interval, move_error_window)

    # Start moving the window
    move_error_window()

    # Load and play the sound in a loop
    sound_path = os.path.join(current_directory, "Offiz_resources\\you-are-an-idiot.wav")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # Play in a loop

    # Bind a function to the window's close event
    def on_close():
        # When the window is closed, create two more error windows
        for _ in range(2):
            create_error_window()
        error_window.destroy()

    error_window.protocol("WM_DELETE_WINDOW", on_close)

# Create the initial error window
create_error_window()

# Run the tkinter event loop
root.mainloop()
