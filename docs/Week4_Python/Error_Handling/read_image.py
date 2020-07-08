import os

from PIL import Image


class ImageReader:

    def __init__(self, img_path):
        self.img_path = img_path

    def check_directory(self):
        print(os.getcwd())

    def image_read(self):
        try:
            img = Image.open(self.img_path)
            img.show()
            print("Image of baby Anais found")

        # IOError Input/Output failure, when trying to open a file that does not exist
        except IOError:
            print("No image found")

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



img_path = "/Users/anaistang/DevOps_Training/docs/Week4_Python/Error_Handling/tang.JPG"

i = ImageReader(img_path)
i.image_read()
i.rotate_image()

