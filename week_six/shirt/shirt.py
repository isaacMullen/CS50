from PIL import Image, ImageOps
import os, sys

accepted_files = [".png", ".jpg", ".jpeg"]

def main():
    for arg in sys.argv[1: ]:
        if os.path.splitext(arg)[1].lower() not in accepted_files:
            print(f"Please enter a .jpeg, .jpg or .png")
            sys.exit()
        else:
            resize_and_fit(sys.argv[1], sys.argv[2])


def resize_and_fit(i, i2):
    img = Image.open(i)
    img2 = Image.open(i2)
#cropping before image so shirt will extend to the bottom of the image
    crop = (0, 0, 1200, 1400)
    img = img.crop(crop)
#fitting the shirt to the size of the before image
    img2 = ImageOps.fit(img2, [1200, 1400])
#overlaying the shirt onto the before image
    img.paste(img2,(0, 0), img2)
#setting correct naming convention using the same number as the input files -- could have also just used a simple int variable but oh well
    for char in (str(i)):
        if char.isdigit():
            x = int(char)
    
    img.save(f"after{x}.jpg")


if __name__ == "__main__":
    main()







# with Image.open("shirt.png") as img:
#     ImageOps.fit(img, [1200, 1600]).show()