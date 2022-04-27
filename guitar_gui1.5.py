import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import os
import pygame
from pygame import mixer
import time

volume = float(0.5)

#commands for top menu options
def new_file():
    """
    Create a new area to save generated music

    Returns
    -------
    None.

    """
    print("New file")


def load_midi():
    """
    Load  a pre-saved midi file to work on

    Returns
    -------
    A Midi file from the local file area.

    """
    print("Load midi")
    
    file = askopenfilename()
    return (file)

def save_midi(midi):
    """
    

    Parameters
    ----------
    midi : Midi file that will be saved to the local file area.

    Returns
    -------
    None.

    """
    print("Save midi")
    
def upload_file():
    """
    Function to upload a file for the model to work with to the program

    Returns
    -------
    None.

    """
    #plot_notes(None)

def generate_music(midi):
    """
    

    Parameters
    ----------
    midi : Midi file to be used for the model.

    Returns
    -------
    New midi file.

    """
    print("Generate Music")

def get_sheet_music(midi):
    """
    

    Parameters
    ----------
    midi : Sheet music will be generated from the given Midi file.

    Returns
    -------
    Sheet Music.

    """
    print("Sheet Music")

def destroy():
    """

    Quits the application

    Parameters
    ----------
    None

    Returns
    -------
    None

    """

    
    window.quit()
    window.destroy()
    quit()

def load_music():
    file = askopenfilename(initialdir="C:/", title="Select a file")
    filename= file.split("/")[-1]
    
    #print(filename)
    global volume
    try:
        mixer.init()
        mixer.music.load(file)
        mixer.music.set_volume(volume)
        mixer.music.play()
        filename_label.config(fg="blue", text="Now Playing: " + str(filename))
        volume_label.config(fg="green", text="Current Volume: " + str(volume))
    except Exception as e:
        print(e)
        filename_label.config(fg="red", text="Cannot Play: " + str(filename))
        time.sleep(3)
        filename_label.config(fg="blue", text="Now Playing: " + str(filename))

def pause_music():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)


def play_music():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)


def volume_down():
    global volume
    if volume <= 0:
        volume_label.config(fg="red", text="Mute")
        return
    else:
        volume -=0.1
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        volume_label.config(fg="green", text="Current Volume: " + str(volume))

        
def volume_up():
    global volume
    if volume >= 1:
        return
    else:
        volume += 0.1
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        volume_label.config(fg="green", text="Current Volume: " + str(volume))



# #create a new window for the applciation
window = tk.Tk()
window.title('das82 Guitar Music Generator')
window.geometry('700x500')

#display area for genrated midi views etc

filename_label = tk.Label(window, fg="red", text='No song selected!')
filename_label.place(relx=0.43, rely=0.25, anchor='w')
volume_label = tk.Label(window, fg="green", text= "Current Volume: " + str(volume))
volume_label.place(relx=0.43, rely=0.3, anchor='w')

pause_b = tk.Button(window, text="Pause", command=lambda: pause_music())
play_b = tk.Button(window, text="Play", command=lambda: play_music())
pause_b.place(relx=0, rely=0.45, relwidth=0.5, anchor='w')
play_b.place(relx=0.5, rely=0.45, relwidth=0.5, anchor='w')
volume_up_b = tk.Button(window, text="+", command=lambda: volume_up())
volume_down_b = tk.Button(window, text="-", command=lambda: volume_down())
volume_up_b.place(relx=0.85, rely=0.39, relwidth=0.2, anchor='e')
volume_down_b.place(relx=0.15, rely=0.39, relwidth=0.2, anchor='w')

separator = ttk.Separator(window, orient='horizontal')
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

#button to upload music (midi file)
upload_b = tk.Button(window, text="Upload File", command=lambda: load_music())
upload_b.place(relx=0.12, rely=0.62, relwidth=0.2, relheight=0.2)

#button to generate music from midi
generate_b = tk.Button(window, text="Generate Music", command=lambda: generate_music(None))
generate_b.place(relx=0.41, rely=0.62, relwidth=0.2, relheight=0.2)

#button to generate tabliture from midi
sheet_b = tk.Button(window, text=" Generate Sheet Music", command=lambda: get_sheet_music(None))
sheet_b.place(relx=0.7, rely=0.62, relwidth=0.2, relheight=0.2)

#menu at the top
menubar = tk.Menu(window)

#File menu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Load Midi", command=lambda: load_midi())
file_menu.add_command(label="Save Midi", command=lambda: save_midi(None))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: destroy())

#Tools menu
tools_menu = tk.Menu(menubar)
menubar.add_cascade(label="Tools", menu=tools_menu)
#View menu
view_menu = tk.Menu(menubar)
menubar.add_cascade(label="View", menu=view_menu)
#Help menu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menubar)
window.mainloop()

