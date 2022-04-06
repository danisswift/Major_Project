# -*- coding: utf-8 -*-
"""


@author: Daniel Swift (das82@aber.ac.uk)
"""

#library to interpret midi files
from mido import MidiFile


class MidiInfo:
    """
    Get information from a midi file
    """
    def __init__(self, midi):
        #initialse
        self.midi = midi
    
    def get_file_info(self):
        return self.midi
    
    def get_track_messages(self, track):
        """
        Return the messages for one or more tracks

        Parameters
        ----------
        track : int type to represent which track we want information about

        Returns
        -------
        None.

        """
        
        for message in self.midi.tracks[track]:
            print(message)
    
    def get_num_messages(self, track):
        """
        

        Parameters
        ----------
        track : int type to represent which track we want information about

        Returns
        -------
        count : int type for amount of messages

        """
        count = 0
        for message in self.midi.tracks[track]:
            count+=1
        return count    
    
    
def test_midi_info():
    mid = MidiFile("Beatles_Blackbird.mid", clip=True)
    info = MidiInfo(mid)
    print(info.get_file_info)
    print(info.get_num_messages(0))
    print(info.get_track_messages(0))

#print("running")
test_midi_info()    
    
    
    
    
    
    
    
    
    
    
    
