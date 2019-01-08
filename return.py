from datetime import datetime
import os

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
dir1 = config.directory
dir2 = "D:\workspace\ImageOrganizar"
dirlist = os.listdir(dir2)

print(dirlist)
for folder in dirlist:
	if 
	if os.path.isdir(dir2+"\\"+folder):
		tmplist = os.listdir(dir2+"\\"+folder)
		print(tmplist)
		#for tmp in tmplist:
			#if not os.path.isdir(dir2+"\\"+folder+"\\"+tmp):
				#os.rename(dir2+"\\"+folder+"\\"+tmp, dir1+"\\"+tmp, dir1+"\\"+tmp)