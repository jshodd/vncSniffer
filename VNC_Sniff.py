from scapy.all import *
import binascii

charmap = {}

def process(packet):
	if len(packet) < 75:
		packet = str(bytes(packet)).split('\\')
		seg = packet[-1]
		if "00" in seg:
			char = seg[-2]
			if char in charmap:
				charmap[char]+=1
			else:
				charmap[char] = 1
			if charmap[char]%4==0:
				print(char)
def main():
	print("sniffing...\n")
	sniff(filter="host 10.71.3.8 and portrange 5951-5962",prn=process)

if __name__ == "__main__":
	main()
