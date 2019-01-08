from datetime import datetime
import os
import hashlib
from PIL import Image

class ImageInfo:
	def __init__(self, img, imgname):
		self.name = img.filename
		self.name2 = imgname
		self.format = img.format
		self.size = img.size
		self.mode = img.mode
		self.hash = hashlib.md5(img.tobytes()).hexdigest()
		self.histogram = img.histogram()
	def getInfo(self):
		print(self.name, self.size, self.format, self.mode, self.hash)
	
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
		f = open('config.txt', 'r')
		self.directory = f.readline()
		f.close()

# Main Code
config = Configuration()
config.getConfig()
dir = config.directory
print(dir)
tmp = "D:\workspace\ImageOrganizar"
imgdir = os.listdir(dir)
imglist = []

result = open("colision.txt", "w")

for imgname in imgdir:
	# Get image from directory
	img = Image.open(dir+"\\"+imgname)
	# Save image as ImageInfo
	currimg = ImageInfo(img, imgname)
	#currimg.getInfo()
	imglist.append(currimg)
	# Compare to previous images
	for i in range(len(imglist)-2, 0, -1):
		if currimg.hash == imglist[i].hash:
			if currimg.size == imglist[i].size:
				if currimg.histogram == imglist[i].histogram:
					#print(currimg.name, imglist[i].name)
					#result.write(currimg.name+" "+imglist[i].name+"\n")
					if tmp is not None and os.path.isdir(tmp):
						if not os.path.isdir(tmp+"\\"+currimg.hash):
							os.mkdir(tmp+"\\"+currimg.hash)
							print("[LOG "+str(datetime.now())+"]: "+tmp+"\\"+currimg.hash+" created.")
						else:
							print("[LOG "+str(datetime.now())+"]: directory already exists")
						if os.path.exists(tmp+"\\"+currimg.hash):
							if os.path.exists(currimg.name):
								try:
									os.rename(currimg.name, tmp+"\\"+currimg.hash+"\\"+currimg.name2)
								except:
									print("[ERR "+str(datetime.now())+"]: currimg renaming")
							if os.path.exists(imglist[i].name):
								try:
									os.rename(imglist[i].name, tmp+"\\"+currimg.hash+"\\"+imglist[i].name2)
									del imglist[i]
									i = i-1
								except:
									print("[ERR "+str(datetime.now())+"]: imglist renaming")
								
			
# Close result file and print "end"
result.close()
print("end")