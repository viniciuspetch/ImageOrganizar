from datetime import datetime
import os
import hashlib
from PIL import Image


class ImageInfo:
    def __init__(self, img, image_name):
        self.name = img.filename
        self.name2 = image_name
        self.format = img.format
        self.size = img.size
        self.mode = img.mode
        self.hash = hashlib.md5(img.tobytes()).hexdigest()
        self.histogram = img.histogram()

    def getInfo(self):
        print(self.name, self.size, self.format, self.mode, self.hash)


# Need to reimplement
def move_images():
	tmp = None
    if tmp is not None and os.path.isdir(tmp):
        if not os.path.isdir(tmp+"\\"+curr_image.hash):
            os.mkdir(tmp+"\\"+curr_image.hash)
            print("[LOG "+str(datetime.now())+"]: " +
                  tmp+"\\"+curr_image.hash+" created.")
        else:
            print("[LOG "+str(datetime.now())+"]: directory already exists")
        if os.path.exists(tmp+"\\"+curr_image.hash):
            if os.path.exists(curr_image.name):
                try:
                    os.rename(curr_image.name, tmp+"\\" +
                              curr_image.hash+"\\"+curr_image.name2)
                except:
                    print("[ERR "+str(datetime.now())+"]: curr_image renaming")
            if os.path.exists(image_list[i].name):
                try:
                    os.rename(image_list[i].name, tmp+"\\" +
                              curr_image.hash+"\\"+image_list[i].name2)
                    del image_list[i]
                    i = i-1
                except:
                    print("[ERR "+str(datetime.now())+"]: image_list renaming")


# Main code
def main():
    dir = "C:\\workspace\\images"
    image_dir = os.listdir(dir)
    image_list = []
    for image_name in image_dir:
        # Get image from directory, and save as ImageInfo
        curr_image = ImageInfo(Image.open(dir+"\\"+image_name), image_name)
        curr_image.getInfo()
        image_list.append(curr_image)

        # Compare to previous images
        for i in range(len(image_list)-2, 0, -1):
            if curr_image.hash == image_list[i].hash:
                if curr_image.size == image_list[i].size:
                    if curr_image.histogram == image_list[i].histogram:
                        print(curr_image.name+"\n"+image_list[i].name+"\n\n")

    # Close result file and print "end"
    result.close()
    print("end")


if __name__ == "__main__":
    main()
