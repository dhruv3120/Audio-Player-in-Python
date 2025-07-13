import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog, messagebox
from pygame import mixer
import os

mixer.init()

playlist = []
current_song_index = 0
is_playing = False

def load_song():
    global playlist
    files = filedialog.askopenfilenames(filetypes=[("MP3 FILES", "*.mp3")])
    for f in files:
        playlist.append(f)
        song_listbox.insert("end", os.path.basename(f))

def play_song():
    global is_playing
    if not playlist:
        messagebox.showwarning("No Songs", "Please add songs to play.")
        return
    mixer.music.load(playlist[current_song_index])
    mixer.music.play()
    is_playing = True

def pause_song():
    global is_playing
    if is_playing:
        mixer.music.pause()
        is_playing = False
    else:
        mixer.music.unpause()
        is_playing = True

def stop_song():
    global is_playing
    mixer.music.stop()
    is_playing = False

def next_song():
    global current_song_index
    if not playlist:
        return
    current_song_index = (current_song_index + 1) % len(playlist)
    mixer.music.load(playlist[current_song_index])
    mixer.music.play()

# GUI setup
app = tk.Tk()
app.geometry("700x400")
app.title("Spotify")
app.config(background="#121212")
app.resizable(False,False)

# Set Icon
icon_image = ImageTk.PhotoImage(file="spotify.jpg")
app.iconphoto(False, icon_image)

# Title Label
title_label = tk.Label(app, text="Spotify Clone", font=("Arial", 24), bg="#121212", fg="white")
title_label.pack(pady=10)

# Playlist Box
song_listbox = tk.Listbox(app, height=10, width=60, bg="#1e1e1e", fg="white")
song_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(app, bg="#121212")
button_frame.pack(pady=10)

# Buttons
play_btn = tk.Button(button_frame, text="Play", width=10, command=play_song)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(button_frame, text="Pause", width=10, command=pause_song)
pause_btn.grid(row=0, column=1, padx=5)

stop_btn = tk.Button(button_frame, text="Stop", width=10, command=stop_song)
stop_btn.grid(row=0, column=2, padx=5)

next_btn = tk.Button(button_frame, text="Next", width=10, command=next_song)
next_btn.grid(row=0, column=3, padx=5)

# Add song button
add_btn = tk.Button(app, text="Add Songs", width=20, command=load_song)
add_btn.pack(pady=10)

app.mainloop()
