import os
import hashlib
from PIL import Image

# ImageData class
# Stores image name, image full path, hash, 
class ImageData:
	def __init__(self, img, name):
		self.img = img
		self.name = name
		self.bytes = None		
		self.hash = None
	def printall(self):
		print(self.name, self.hash)
	def getHash(self):
		if hash == None:
			self.hash = hashlib.md5(getBytes(self)).hexdigest()
		return self.hash
	def getBytes(self):
		if bytes == Nome:
			self.bytes = img.tobytes()
		return self.bytes

		
# Configuration class
# Stores config stuff
class Configuration:
	def __init__(self):
		directory = None
		useHash = True
		useHistogram = True
		usePixel = True
		useDimension = True
	def getConfig(self):
		f = open('config.txt', r)
		directory = f.readline()
		f.close()
			

# Main Code
config = Configuration()
dir = config.getConfig().directory
imglist = os.listdir(dir)
iclist = []
for imgname in imglist:
	img = Image.open(dir+"\\"+imgname)
	print(imgname)
	print(type(img))
	imghash = hashlib.md5(img.tobytes()).hexdigest()
	
	# Create ImageData object
	imgobj = ImageData(img, imgname)
	#imgobj.printall()
	iclist.append(imgobj)

	#for i in range(len(iclist)-2, 0, -1):
	#	if imgobj.hash == iclist[i].hash:
	#		print(imgobj.name, iclist[i].name)
	#		if imgobj.img == iclist[i].img
	#			print("confirmed")