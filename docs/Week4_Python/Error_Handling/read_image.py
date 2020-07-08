# Manipulate operating system with Python
import os

# Imaging library to add support for opening, manipulating, saving image files
from PIL import Image


class ImageReader:

    # Initialising img_path
    def __init__(self, img_path):
        self.img_path = img_path

    # Checking file path
    def check_directory(self):
        print(os.getcwd())

    # Opening image
    def image_read(self):
        try:
            img = Image.open(self.img_path)
            img.show()
            print("Image of baby Anais found")

        # IOError Input/Output failure, when trying to open a file that does not exist
        except IOError:
            print("No image found")

    # Rotating image
    def rotate_image(self):
        try:
            img = Image.open(self.img_path)

            # Rotate image by 180 degrees
            img = img.rotate(180)
            img.show()

            # Save changes in relative location
            img.save('upsidedown_tang.JPG')
            print("Anais was rotated by 180 degrees!")

        # IOError Input/Output failure, when trying to open a file that does not exist
        except IOError:
            print("No image found")

    # Black and white image
    def grey_scale(self):
        try:
            img = Image.open(self.img_path)

            # Changing image to black and white
            # Dither mode adds white noise. Set to NONE
            # 'L' 8-bit pixels, black and white # 8 bit color graphics is method of storing img information in a computer's memory
            img = img.convert(mode='L', dither=Image.NONE)

            # Opens image
            img.show()

            # Saves image as new JPG
            img.save("black_white.JPG")
            print("Greyscale function successful!")
        except Exception:
            print("No image found")





img_path = "/Users/anaistang/DevOps_Training/docs/Week4_Python/Error_Handling/tang.JPG"
# img_path = "non_existent_image.JPG" # Raises error 'no image found'

i = ImageReader(img_path)
i.image_read()
i.rotate_image()
i.grey_scale()

"""
Bit depth refers to the colour information stored in an image, the higher the bit depth, the more colours it can store
8 - bit colour image, standard JPEG format
256 shades of blue, 256 shades of green, 256 shades of red
2 to the exponent of 8 which gives us 256
A total of 16.8 million possible colours (256*256*256)
Bit    7  6  5  4  3  2  1  0
Data   R  R  R  G  G  G  B  B
"""