import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import sys
import pygame
from pygame import mixer
import time
from tayuya import MIDIParser #guitar tab
from generator import Generator

#global variables
volume = float(0.5)
file = None
filename = ""


#commands for top menu options
def save_midi(midi):
    """
    

    Parameters
    ----------
    midi : Midi file that will be saved to the local file area.

    Returns
    -------
    None.

    """
    global file
    if file == None:
        return
    else:
        try:
            initial_path = file.split("/")
            save_path=[]
            for i in range(len(initial_path)-1):
                save_path.append(initial_path[i])
                
            print(save_path)
        except Exception as e:
            print(e)
        
    
def upload_file():
    """
    Function to upload a file for the model to work with to the program

    Returns
    -------
    None.

    """
    global file
    global filename
    file = askopenfilename(initialdir="C:/", title="Select a file")
    filename = file.split("/")[-1]
    load_music()
    print(file)
    print(filename)
    

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
    
    if midi == None:
        return
    
    global file
    
    #default values    
    temperature = float(1.0)
    gen_length = 100
    seq_length = 50

    gen_win = tk.Toplevel(window)
    gen_win.title("Generation Settings")
    gen_win.geometry("300x120")
    
    temp_label = tk.Label(gen_win, text="Temperature")
    temp_entry = tk.Entry(gen_win, width=4)
    gen_length_label = tk.Label(gen_win, text="Length of generation (notes)")
    gen_length_entry = tk.Entry(gen_win, width=4)
    seq_length_label = tk.Label(gen_win, text="Length of each sequence")
    seq_length_entry = tk.Entry(gen_win, width=4)

    gen_length_entry.insert(0, str(gen_length))
    temp_entry.insert(0, str(temperature))
    seq_length_entry.insert(0, str(seq_length))
    
    gen_length_label.place(relx=0, rely=0.22)
    temp_entry.place(relx=0.3, rely=0)
    seq_length_label.place(relx=0, rely=0.48)
    seq_length_entry.place(relx= 0.47, rely=0.48)
    temp_label.place(relx=0, rely=0)
    gen_length_entry.place(relx=0.55, rely=0.22)
    conf_button = tk.Button(gen_win, text="Confirm Values", command=lambda: set_variables(midi)).place(relx=0.05, rely=0.7)

    def set_variables(midi):
        global file
        temperature = float(temp_entry.get())
        gen_length = int(gen_length_entry.get())
        seq_length = int(seq_length_entry.get())
        new_generator = Generator(midi, seq_length, gen_length)
        new_mid = new_generator.generate()
        file = new_mid
        load_music()
    
    
        
        

def get_sheet_music(midi_file):
    """
    

    Parameters
    ----------
    midi : Sheet music will be generated from the given Midi file.

    Returns
    -------
    Sheet Music.

    """
    print("Sheet Music")
    global lim
    try:
        mid = MIDIParser(midi_file, track=0) #set up a parsed midi to generate tabs from
        lim = len(mid.get_tracks())
        print(lim)
    except Exception as e:
        print(e)
    try:        
        for i in range(lim): #for each track on the midi (could represent a different instrument
            try:
                midi = MIDIParser(file, track=i)
                try:   #attempt to write tab to a text file, currently not working as midi.render_tabs() doesn't return a string             
                    tab = ["Tab for track %d:" %i, "========================================================================", midi.render_tabs()]
                    with open("new_tab.txt", "w+") as f:
                        for line in tab:
                            f.write(line)
                            f.write('\n')
                            print("Successfully uploaded File")
                except Exception as e:
                    print(e)
                print("Tab for track %d:" %i)
                print("========================================================================")
                midi.render_tabs() #Generate each tab in the shell               
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
                

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

    pygame.quit()
    window.quit()
    window.destroy()
    sys.exit()

def load_music():
    """

    Load a sound file (normally a midi file) to be played back

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    
    
    #print(filename)
    global volume
    global file
    global filename
    print(file)
    if file == None or filename == "": #check if a file is loaded
        return
    else:
        try: #intialise mixer
            mixer.init()
            mixer.music.load(file)
            mixer.music.set_volume(volume)
            mixer.music.play()
            pause_music() #stop music from playing immediately after being loaded
            filename_label.config(fg="blue", text="Now Playing: " + str(filename))
            volume_label.config(fg="green", text="Current Volume: " + str(volume))
        except Exception as e:
            print(e)
            filename_label.config(fg="red", text="Cannot Play: " + str(filename))
        

def pause_music():
    #pause loaded audio file
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)


def play_music():
    try:
        if mixer.music.get_busy(): #if music is playing then it will rewind, doesn't work for midi files
            mixer.music.rewind()
            #mixer.music.set_pos(0)
            print('rewinding')
        else: #play loaded audio file
            print('not busy')
            mixer.music.unpause()
    except Exception as e:
        print(e)


#small functions to adjust volume up and down
def volume_down():
    global volume
    if volume <= 0:
        volume_label.config(fg="red", text="Mute")
        return
    else:
        #error thrown if mixer has not been intiated yet
        try:
            volume -=0.1
            volume = round(volume, 1)
            mixer.music.set_volume(volume)
            volume_label.config(fg="green", text="Current Volume: " + str(volume))
        except Exception as e:
            print(e)
            

        
def volume_up():
    global volume
    if volume >= 1:
        return
    else:
        #error thrown if mixer has not been intiated yet
        try:            
            volume += 0.1
            volume = round(volume, 1)
            mixer.music.set_volume(volume)
            volume_label.config(fg="green", text="Current Volume: " + str(volume))
        except Exception as e:
            print(e)



# #create a new window for the application
window = tk.Tk()
window.title('MidiGen by das82')
window.geometry('700x500')

#display area for genrated midi views etc
title_label = tk.Label(window, text="MidiGen", font=("Arial", 25))
title_label.place(relx=0.43, rely=0.05)
filename_label = tk.Label(window, fg="red", text='No song selected!')
filename_label.place(relx=0.43, rely=0.25, anchor='w')
volume_label = tk.Label(window, fg="green", text= "Current Volume: " + str(volume))
volume_label.place(relx=0.43, rely=0.3, anchor='w')

#Pause/Play Buttons
pause_b = tk.Button(window, text="Pause", command=lambda: pause_music())
play_b = tk.Button(window, text="Play/Rewind", command=lambda: play_music())
pause_b.place(relx=0, rely=0.45, relwidth=0.5, anchor='w')
play_b.place(relx=0.5, rely=0.45, relwidth=0.5, anchor='w')

#Volume Buttons
volume_up_b = tk.Button(window, text="+", command=lambda: volume_up())
volume_down_b = tk.Button(window, text="-", command=lambda: volume_down())
volume_up_b.place(relx=0.85, rely=0.39, relwidth=0.2, anchor='e')
volume_down_b.place(relx=0.15, rely=0.39, relwidth=0.2, anchor='w')

separator = ttk.Separator(window, orient='horizontal')
separator.place(relx=0, rely=0.5, relwidth=1, relheight=1)

#button to upload music (midi file or mp3)
upload_b = tk.Button(window, text="Upload File", command=lambda: upload_file())
upload_b.place(relx=0.12, rely=0.62, relwidth=0.2, relheight=0.2)

#button to generate music from midi
generate_b = tk.Button(window, text="Generate Music", command=lambda: generate_music(file))
generate_b.place(relx=0.41, rely=0.62, relwidth=0.2, relheight=0.2)

#button to generate tabliture from midi
sheet_b = tk.Button(window, text=" Generate Sheet Music", command=lambda: get_sheet_music(file))
sheet_b.place(relx=0.7, rely=0.62, relwidth=0.2, relheight=0.2)

#menu at the top
menubar = tk.Menu(window)

#File menu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: upload_file())
file_menu.add_command(label="Load Midi", command=lambda: upload_file())
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

