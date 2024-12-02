from PIL import Image
import os

density = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', '&nbsp', '&nbsp', '&nbsp', '&nbsp', '&nbsp', '&nbsp', '&nbsp']
densitylist = []
level = len(density) - 1
block = 255 / level

def stringToArr(densityString):
    arr = []
    for i in densityString:
        arr.append(i)
    return arr

def reduceSize(t, resizeSize):
    t = list(t)
    for i in range(len(t)):
        t[i] //= resizeSize
    return tuple(t)

def convertToAscii(image, width, height):
    ascii_image = ""
    for i in range(height - 1):
        tmp_image = ""
        for j in range(width - 1):
            tmp_image += getDensity(image.getpixel((j, i)), "black")
        tmp_image += " <br>"
        ascii_image += tmp_image
    return ascii_image

def getDensity(pixel, method):
    try:
        if method == "black":
            return density[level - int(round(pixel // block, 0))]
        elif method == "white":
            return density[int(round(pixel // block, 0))]
    except IndexError:
        print("인덱스 오류 발생:", int(round(pixel // block, 0)))

def save_as_html(ascii_art, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(
f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet", href="./Image_to_Acsii/style.css">
    </head>
    <body>{ascii_art}
    </body>
</html>""")

# make a new reduced image and convert it to html file
def createAndConvert(imageName, ratio):
    # image = Image.open(os.getcwd() + "/Image_to_Ascii/data/" + imageName + ".jpeg")
    image = Image.open("Image_to_Acsii/data/" + imageName + ".jpeg")
    originalSize = image.size
    reducedSize = reduceSize(originalSize, ratio)
    reducedName = "reduced" + imageName[0].upper() + imageName[1:]
    if os.path.isfile('Image_to_Acsii/data/' + reducedName) == False: # if reduced version already exists, it doesn't make a new one
        reducedImage = image.resize(reducedSize).convert("L").save("Image_to_Acsii/data/" + reducedName + ".jpeg", format = "jpeg")
    reducedImage = Image.open("Image_to_Acsii/data/" + reducedName + ".jpeg")

    ascii_art = convertToAscii(reducedImage, reducedSize[0], reducedSize[1])
    save_as_html(ascii_art, "image_to_ascii.html")


# convert existing image to html file
def convert(imageName):
    reducedName = "reduced" + imageName[0].upper() + imageName[1:]
    reducedImage = Image.open("Image_to_Acsii/data/" + reducedName + ".jpeg")
    reducedSize = reducedImage.size
    ascii_art = convertToAscii(reducedImage, reducedSize[0], reducedSize[1])
    save_as_html(ascii_art, "image_to_ascii.html")

createAndConvert("your_image_name", 5) # change image name and ratio