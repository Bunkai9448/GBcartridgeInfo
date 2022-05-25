# file: SoundInfo.py
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.01
# Date: May 25th 2022

# File description: Use to easily seek (extract & insert) the bgm & sound values from a gameboy cartridge for later use

# Documentation sources https://gbdev.io/pandocs/Sound_Controller.html
# https://github.com/bwhitman/pushpin/blob/master/src/gbsound.txt

# Change pointers (Address values according to your game)


import binascii

print()
with open('initialD.gb','br') as f:

# Sound1:  Produces quadrangular waves with sweep and envelope functions.
 # FF10 - NR10 - Channel 1 Sweep register (R/W)
 # FF11 - NR11 - Channel 1 Sound length/Wave pattern duty (R/W)
 # FF12 - NR12 - Channel 1 Volume Envelope (R/W)
 # FF13 - NR13 - Channel 1 Frequency lo (Write Only)
 # FF14 - NR14 - Channel 1 Frequency hi (R/W)

# Sound2:  Produces quadrangular waves with an envelope.
 # FF16 - NR21 - Channel 2 Sound Length/Wave Pattern Duty (R/W)
 # FF17 - NR22 - Channel 2 Volume Envelope (R/W)
 # FF18 - NR23 - Channel 2 Frequency lo data (W)
 # FF19 - NR24 - Channel 2 Frequency hi data (R/W)

# Sound3:  Outputs voluntary wave patterns from Wave RAM.
 # FF1A - NR30 - Channel 3 Sound on/off (R/W)
 # FF1B - NR31 - Channel 3 Sound Length (W)
 # FF1C - NR32 - Channel 3 Select output level (R/W)
 # FF1D - NR33 - Channel 3 Frequency s lower data (W)
 # FF1E - NR34 - Channel 3 Frequency s higher data (R/W)
 # FF30-FF3F - Wave Pattern RAM
	waveAddress = 0x83DD
	print('Sound3 Wave Address: ', hex(waveAddress))	
	f.seek(waveAddress)
	waveValue = binascii.hexlify(f.read(16))
	print('Sound3 Wave Pattern: ', waveValue)

# Sound4:  Produces white noise with an envelope.
 # FF20 - NR41 - Channel 4 Sound Length (W)
 # FF21 - NR42 - Channel 4 Volume Envelope (R/W)
 # FF22 - NR43 - Channel 4 Polynomial Counter (R/W)
 # FF23 - NR44 - Channel 4 Counter/consecutive; Inital (R/W)

# Sound Control Registers
 # FF24 - NR50 - Channel control / ON-OFF / Volume (R/W)
 # FF25 - NR51 - Selection of Sound output terminal (R/W)
 # FF26 - NR52 - Sound on/off
 
	f.close()
