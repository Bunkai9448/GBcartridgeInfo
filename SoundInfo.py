# file: SoundInfo.py
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.02
# Date: May 25th 2022

# File description: Use to easily seek (extract & insert) the bgm & sound values from a gameboy cartridge for later use

# Documentation sources https://gbdev.io/pandocs/Sound_Controller.html
# https://github.com/bwhitman/pushpin/blob/master/src/gbsound.txt


# The example game used for this code uses the ASM operations to initiate
# the sound channel values so this code will mainly translate those operations 
# to a hex string using python code so you can easily port the values 
# from/to the ASM.	You may update it with the values from your game

import binascii

print()
with open('initialD.gb','br') as f:

# --- Initialization

# S1: 80 BF F3 C1 BF
	sound1 = [hex(0x80), hex(0xBF), hex(0xF3), hex(0xC1), hex(0xBF)]
# S2: FF 00 00 00 B8
	sound2 = [hex(0xFF), hex(0x00), hex(0x00), hex(0x00), hex(0xB8)]
# S3: 7F 00 9F 00 B8
	sound3 = [hex(0x7F), hex(0x00), hex(0x9F), hex(0x00), hex(0xB8)]
# S4: FF C0 00 00 BF
	sound4 = [hex(0xFF), hex(0xC0), hex(0x00), hex(0x00), hex(0xBF)]
# Sound Control
	soundControl = [0x00] * 3
	
	
# Sound Control Registers
 # FF24 to FF26
 
	a = 0xFF			# 01:
	# FF00+26
	soundControl [2] = hex(a)	# 01:40F5 which is 0x80F5		
	a = 0x00 			# 01:40F7 which is 0x80F7
	# FF00+25
	soundControl [1] = hex(a)	# 01:		 		
	a = 0x77 			# 01:40FB which is 0x80FB
	# FF00+24		
	soundControl [0] = hex(a)	# 01:		


# Sound1:  Produces quadrangular waves with sweep and envelope functions.
 # FF10 to FF14 
# Sound2:  Produces quadrangular waves with an envelope.
 # FF15 to FF19 

	a = 0x80	# XOR a
	# FF00+10	
	sound1[0] = hex(a)		# 01:4100 which is 0x8100	
	# FF00+11
	sound1[1] = hex(a)		# 01:4104 which is 0x8104	
	# FF00+16
	sound2[1] = hex(a)		# 01:4106 which is 0x8106	
	a = 0x08 			# 01:4108 which is 0x8108
	# FF00+12	
	sound1[2] = hex(a)		# 01:410E which is 0x810E
	# FF00+17	
	sound2[2] = hex(a)		# 01:		
	a = 0x80			# 01:	 
	# FF00+14	
	sound1[4] = hex(a)		# 01:	
	# FF00+19	
	sound2[4] = hex(a)		# 01:			
		
# Sound3:  Outputs voluntary wave patterns from Wave RAM.
 # FF1A to FF1E 

	a = 0x80	# XOR a 	
	# FF00+1A
	sound3[0] = hex(a)		# 01:4124 which is 0x8124	
	a = 0x80	# XOR a
	# FF00+1B
	sound3[1] = hex(a)		# 01:		
	a = 0x20			# 01:412C which is 0x812C
	# FF00+1C
	sound3[2] = hex(a)		# 01:	
	
# Sound4:  Produces white noise with an envelope.
 # FF1F to FF23
	
	a = 0x80	# XOR a 	
	# FF00+20	
	sound4[1] = hex(a)		# 01:4115 which is 0x8115		
	a = 0x08			# 01:4117 which is 0x8117
	# FF00+21
	sound4[2] = hex(a)		# 01:				
	a = 0x30			# 01:411B which is 0x811B
	# FF00+22
	sound4[3] = hex(a)		# 01:		
	a = 0x80			# 01:411F which is 0x811F
	# FF00+23
	sound4[4] = hex(a)		# 01:		

 
# --- Updates
		
	a = 0x80				# 01:4130 which is 0x8130
	# FF00+1A 
	sound3[0] = hex(a)			# 01:			
	a = 0xC0 				# 01:4134 which is 0x8134
	# FF00+1E 
	sound3[4] = hex(a)			# 01:			
	a = 0xC7				# 01:4138 which is 0x8138 
	# FF00+12
	sound1[2] = hex(a)			# 01: 
	# FF00+17
	sound2[2] = hex(a)			# 01: 	

	
# --- Display the info on screen

	print('Sound Control: ', soundControl)
	print()	
	print('Proper1: 80 80 C7 B1 C8')		
	print('Sound1: ', sound1)
	print('Proper2: FF 80 C7 00 B8')	
	print('Sound2: ', sound2)	
	print('Proper3: FF 00 BF 00 F8')
	print('Sound3: ', sound3)
	print('Proper4: FF C0 08 30 BF')	
	print('Sound4: ', sound4)	

# Sound3:  FF30-FF3F - Wave Pattern RAM
	waveAddress = 0x83DD
	print('Wave Address: ', hex(waveAddress))	
	f.seek(waveAddress)
	waveValue = binascii.hexlify(f.read(16))
	print('Wave Pattern: ', waveValue)

	f.close()
