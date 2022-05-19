# file: HeaderInfo.py
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.01
# Date: May 18th 2022

# File description: Used to quickly visualize the key values
# in a Gameboy cartridge header
# Theoretically in the future this file will be updated to modify and use 
# said values

# Documentation source https://gbdev.io/pandocs/The_Cartridge_Header.html

import binascii

print()
with open('initialD.gb','br') as f:
# 0143 - CGB Flag
 # 80h - Game supports CGB functions, but also works on old Game Boys.
 # C0h - Game works on CGB only (physically the same as $80).
	Pcgb_flag = 0x0143
	f.seek(Pcgb_flag) 
	print('Address for CGB flag > int:', Pcgb_flag,' ; hex:',hex(Pcgb_flag))
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
	print()
		
# 0146 - SGB Flag
 # $00: No SGB functions (Normal Game Boy or CGB only game)
 # $03: Game supports SGB functions
 # The SGB disables its SGB functions if this byte is set to a value other than $03
	Psgb_flag = 0x0146
	f.seek(Psgb_flag)
	print('Address for SGB flag > int:', Psgb_flag,' ; hex:',hex(Psgb_flag))
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
	print()
	
# 0148 - ROM Size
 # Specifies the ROM Size of the cartridge. 
	Prom_Size = 0x0148
	f.seek(Prom_Size)
	print('Address for ROM size > int:', Prom_Size,' ; hex:',hex(Prom_Size))
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
	print()
	
# 014A - Destination Code
 # Specifies if this version of the game is supposed to be sold in Japan, 
 # or anywhere else. Only two values are defined.
 # $00: Japanese
 # $01: Non-Japanese
	Pregion = 0x014A
	f.seek(Pregion)
	print('Address for ROM region > int:', Pregion,' ; hex:',hex(Pregion))
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
	print()
	
# 014D - Header Checksum
 # Contains an 8 bit checksum across the cartridge header bytes $0134-014C.
	pHeader_CS = 0x014D
	f.seek(pHeader_CS)
	print('Address for ROM header > int:', pHeader_CS,' ; hex:',hex(pHeader_CS))
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
# Calculate proper Header Checksum from the file
	checkSum = 0 
	cursor = 0x0134
	cEnd = 0x014C
	f.seek(cursor)
	while cursor <= cEnd:		
		readByte = f.read(1)
		readByteHex = binascii.hexlify(readByte)		
		val = int(readByteHex,16)
		checkSum = checkSum - (val + 1)
		checkSum = checkSum%256
		cursor = cursor + 1 		
	print('Proper checksum:', hex(checkSum))
	print()	
	
# 014E-014F - Global Checksum
 # Contains a 16 bit checksum (upper byte first) across the whole cartridge ROM. 
 # Produced by adding all bytes of the cartridge (except for the two checksum bytes). 
 # The Game Boy doesnt verify this checksum.
	pCartridge_CS1 = 0x014E
	pCartridge_CS2 = 0x014F
	f.seek(pCartridge_CS1)
	val = binascii.hexlify(f.read(1))
	print('Hex value on that location:',val)
	print()
	
	f.close()
