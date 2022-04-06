import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import os



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
    print("Upload File")

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

# #create a new window for the applciation
window = tk.Tk()
window.title('das82 Guitar Music Generator')
window.geometry('700x500')

#display area for genrated midi views etc
display_area = tk.Label(window, text="DISPLAY AREA GOES HERE")
display_area.place(relx=0.1, rely=0.05, relheight=0.4, relwidth=0.8)

separator = ttk.Separator(window, orient='horizontal')
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

#button to upload music (midi file)
upload_b = tk.Button(window, text="Upload File", command=lambda: upload_file())
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
file_menu.add_command(label="Exit", command=window.destroy)

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
