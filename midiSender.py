import rtmidi
import time

class MidiSender:
    def __init__(self):
        self.midiout = rtmidi.MidiOut()
        self.available_ports = self.midiout.get_ports()
        print(self.available_ports)

        if self.available_ports:
            self.midiout.open_port(1)
        else:
            self.midiout.open_virtual_port("My virtual output")

    # the frequency with which it is sending notes is too high, I need to reduce it, maybe send every other note
    def sendNote(self, note):
        note_on = [0x90, 65+note]

        self.midiout.send_message(note_on)

    def endTransmission(self):
        del self.midiout
