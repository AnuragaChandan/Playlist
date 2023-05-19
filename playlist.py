import os
import random
import pygame
import tkinter as tk
from tkinter import ttk

# Directory path where the songs are located (current directory)
songs_directory = os.getcwd()

# List to store the song file names
song_files = []

# Find all the song files in the directory
for file in os.listdir(songs_directory):
    if file.endswith(".mp3"):
        song_files.append(file)

# Randomly shuffle the song list
random.shuffle(song_files)

# Initialize pygame
pygame.init()
pygame.mixer.init()



# Function to play the next song
def play_next_song():
    # Stop the current song
    pygame.mixer.music.stop()

    # Get the index of the current song
    current_index = song_files.index(current_song.get())

    # Get the index of the next song
    next_index = (current_index + 1) % len(song_files)

    # Set the next song as the current song
    current_song.set(song_files[next_index])

    # Load and play the next song
    pygame.mixer.music.load(os.path.join(songs_directory, current_song.get()))
    pygame.mixer.music.play()

def play_previous_song():
    # Stop the current song
    pygame.mixer.music.stop()

    # Get the index of the current song
    current_index = song_files.index(current_song.get())

    # Get the index of the previous song
    previous_index = (current_index - 1) % len(song_files)

    # Set the previous song as the current song
    current_song.set(song_files[previous_index])

    # Load and play the previous song
    pygame.mixer.music.load(os.path.join(songs_directory, current_song.get()))
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
def play_music():
    # Load and play the current song
    pygame.mixer.music.load(os.path.join(songs_directory, current_song.get()))
    pygame.mixer.music.play()
def pause_music():
    pygame.mixer.music.pause()
def resume_music():
    pygame.mixer.music.unpause()
# Create the main window
window = tk.Tk()
window.title("Music Player")

# Variable to hold the current song
current_song = tk.StringVar()

# Create a label to display the current song
song_label = ttk.Label(window, textvariable=current_song)
song_label.pack(pady=10)

button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

# Create a button to go to the next song
previous_button = ttk.Button(button_frame, text="Previous", command=play_previous_song)
previous_button.pack(side="left")
play_button = ttk.Button(button_frame, text="play again", command=play_music)
play_button.pack(side="left")
next_button = ttk.Button(button_frame, text="Next", command=play_next_song)
next_button.pack(side="left")
#resume_button = ttk.Button(button_frame, text="Resume", command=resume_music)
#resume_button.pack(side="left")
#pause_button = ttk.Button(button_frame, text="Pause", command=pause_music)
#pause_button.pack(side="left")
stop_button = ttk.Button(window, text="stop", command=stop_music)
stop_button.pack(pady=10)

# Set the initial current song
current_song.set(song_files[0])

# Load and play the first song
pygame.mixer.music.load(os.path.join(songs_directory, current_song.get()))
pygame.mixer.music.play()

def check_music_status():
    if not pygame.mixer.music.get_busy():
        play_next_song()
    
    # Check the music status every 500 milliseconds (0.5 seconds)
    window.after(500, check_music_status)

# Start checking the music status
check_music_status()



# Start the GUI event loop
window.mainloop()

# Stop the music player when the GUI is closed
pygame.mixer.music.stop()

print("Music player stopped.")

