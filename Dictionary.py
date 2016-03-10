from bitarray import bitarray
import hashlib

class BloomFilter:
	
	def __init__(self, size, hash_count):
		self.size = size 
		self.hash_count = hash_count
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
	
	def add(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			self.bit_array[result] = 1
			
	def lookup(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			if self.bit_array[result] == 0:
				print "--" , word, "--" ,
				return ""
				break
	                else:
				return word
     		
				
			
			 
bf = BloomFilter(500000, 7)

lines = open("/usr/share/dict/american-english").read().splitlines()
for line in lines:
	bf.add(line)

	
with open("Thema10.txt") as f:
	lines = f.readlines()
	for line in lines:
		words = line.split()
		for word in words:
			print (word),
		
			
print "\nThe mistakes are shown below ,within --"

for word in words:
    print bf.lookup(word),	
