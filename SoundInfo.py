# file: SoundInfo.py
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.03
# Date: Aug 28th 2022

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

# Sound1:  Produces quadrangular waves with sweep and envelope functions.
 # FF10 to FF14 
# S1: 80 BF F3 C1 BF
	sound1 = [hex(0x80), hex(0xBF), hex(0xF3), hex(0xC1), hex(0xBF)]
# Sound2:  Produces quadrangular waves with an envelope.
 # FF15 to FF19 
# S2: FF 00 00 00 B8
	sound2 = [hex(0xFF), hex(0x00), hex(0x00), hex(0x00), hex(0xB8)]
# Sound3:  Outputs voluntary wave patterns from Wave RAM.
 # FF1A to FF1E 
# S3: 7F 00 9F 00 B8
	sound3 = [hex(0x7F), hex(0x00), hex(0x9F), hex(0x00), hex(0xB8)]
# Sound4:  Produces white noise with an envelope.
 # FF1F to FF23
# S4: FF C0 00 00 BF
	sound4 = [hex(0xFF), hex(0xC0), hex(0x00), hex(0x00), hex(0xBF)]
# Sound Control Registers
 # FF24 to FF26
	soundControl = [0x00] * 3

	
# ASM code to Python	


	# operation: ld a,80 			; address 02:40F3
	a = 0x80									
	# operation: ld (FF00+26), a	; address 02:40F5
	soundControl [2] = hex(a)		
	# operation: ld a,00 			; address 02:40F7
	a = 0x00 
	# operation: ld (FF00+25), a	; address 02:40F9 
	soundControl [1] = hex(a)		 		
	# operation: ld a,77 			; address 02:40FB
	a = 0x77
	# operation: ld (FF00+24), a	; address 02:40FD		
	soundControl [0] = hex(a)		

	# operation: XOR a	 			; address 02:40FF
	a = 0x00
	# operation: ld (FF00+10), a	; address 02:4100
	sound1[0] = hex(a)		
	# operation: ld a,80 			; address 02:4102
	a = 0x80
	# operation: ld (FF00+11), a	; address 02:4104
	sound1[1] = hex(a)			
	# operation: ld (FF00+16), a	; address 02:4106
	sound2[1] = hex(a)		
	# operation: ld a,08 			; address 02:4108
	a = 0x08 			
	# operation: ld (FF00+12), a	; address 02:410A
	sound1[2] = hex(a)
	# operation: ld (FF00+17), a	; address 02:410C
	sound2[2] = hex(a)	
	# operation: ld a,80 			; address 02:410E
	a = 0x80	 
	# operation: ld (FF00+14), a	; address 02:4110
	sound1[4] = hex(a)		# 01:	
	# operation: ld (FF00+19), a	; address 02:4112
	sound2[4] = hex(a)		# 01:			

	# operation: XOR a	 			; address 02:4114
	a = 0x00
	# operation: ld (FF00+20), a	; address 02:4115	
	sound4[1] = hex(a)
	# operation: ld a,08 			; address 02:4117
	a = 0x08 
	# operation: ld (FF00+21), a	; address 02:4119
	sound4[2] = hex(a)	
	# operation: ld a,30 			; address 02:411B
	a = 0x30 
	# operation: ld (FF00+22), a	; address 02:411D
	sound4[3] = hex(a)	
	# operation: ld a,80 			; address 02:411F
	a = 0x80
	# operation: ld (FF00+23), a	; address 02:4121
	sound4[4] = hex(a)		
	# operation: XOR a	 			; address 02:4123
	a = 0x00
	# operation: ld (FF00+1A), a	; address 02:4124
	sound3[0] = hex(a)	

# call 43BF   < sound3[0] fails here
	# operation: swap a	 			; address 02:43BF 
	# operation: ld hl,FF30			; address 02:
	# operation: ld de,43DD			; address 02:
	# operation: add e	 			; address 02:43BF
	# operation: ld e,a				; address 02:
	# operation: ld a,d				; address 02:
	# operation: adc a,00 			; address 02:43BF
	# operation: ld d,a				; address 02:
	# operation: xor a	 			; address 02:
	a = 0x00
	# operation: ld (ff00+1A),a		; address 02:43CE
	sound3[0] = hex(a)	

	# loop 43D0 to 43D6
	# operation: ld a,(de)			; address 02:43D0
	# operation: inc de 			; address 02:
	# operation: ldi (hl),a			; address 02:
	# operation: ld a,l				; address 02:
	# operation: cp a,40			; address 02:
	# operation: jr nz,43DO			; address 02:43D6
	# operation: ld a,80 			; address 02:43D8
	a = 0x80
	# operation: ld (FF00+1A), a	; address 02:43DA
	sound3[0] = hex(a)	
# ret

	# operation: xor a	 			; address 02:4129
	a = 0x00
	# operation: ld (FF00+1B), a	; address 02:412A
	sound3[1] = hex(a)				
	# operation: ld a,20 			; address 02:412C
	a = 0x20
	# operation: ld (FF00+1C), a	; address 02:412E
	sound3[2] = hex(a)				
	# operation: ld a,80 			; address 02:4130
	a = 0x80
	# operation: ld (FF00+1A), a	; address 02:4132
	sound3[0] = hex(a)						
	# operation: ld a,C0 			; address 02:4134
	a = 0xC0
	# operation: ld (FF00+1E), a	; address 02:4136
	sound3[4] = hex(a)						
	# operation: ld a,C7 			; address 02:4138
	a = 0xC7 
	# operation: ld (FF00+12), a	; address 02:413A
	sound1[2] = hex(a)			 
	# operation: ld (FF00+17), a	; address 02:413C
	sound2[2] = hex(a)				
	
# --- Display the info on screen

	print('Sound Control: ', soundControl)
	print()	
	print('Proper1: 80 80 C7 C1 B8')		
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
