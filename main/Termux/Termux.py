import time
import random
import os

n = ['1010100110111000010101011110110000011010100001110010100000101111010111110100101', 
	 '0011111010011010101010000111010001010011100111010111010101101010101000010101010', 
     '1111100000101000010001011000111000100000100111101010101010111000101011110010101', 
     '0101111111000100110010111110010111000111101101101001110000101010100111101001001', 
     '1000100100001011111010100001111010101010110000110000111101011111011011010101010', 
     '1111110001101010001110000101110101010101010111101010101001010100100100010011011', 
     '1101010101010101010101011110101010000111101011010101011100101010100111101010101', 
     '0101010101100101100010111111101001010010111011010111100010101010001111000010010', 
     '1101001111000100001111010010101000111010100100001011001001000010010011100000101', 
     '0010101110101000011111001010101011110001110101101010100100010100010111100101000', 
     '1000011111001010110000110101001010101101001011110010101010010101011100101111101']

def main():
     	os.system('clear')
	while True:
		randomn = random.choice(n)
		print(randomn)
		time.sleep(0.2)
main()
