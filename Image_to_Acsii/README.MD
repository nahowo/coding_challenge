# Image to Ascii Code
2024.11.17

### How to use
1. add Image file to Image_to_Ascii/data directory
- it only reads jpeg, if you want to use other formats you can change the format in image_to_ascii.py code.
2. create resized image and save the resized version
- to create and resize the image, add code to image_to_ascii.py:
    ```python
    createAndConvert({image name}, {image ratio})
    ```
- image name should be same as the name of the image you added at 1.
- size of the reduced image depends on the size of original image. try 5 ~ 10 first and adjust it.
3. run image_to_ascii.py file
4. check image_to_ascii.html
- you can drag and drop image_to_ascii.html file to web browser to check ascii image!