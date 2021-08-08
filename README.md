# Fetch-Reciept-Generator

## How to install (with from source)

- 1.) Open commmand prompt in the directory with the source code. 
- 2.) Use the command `pip install -r requirements.txt` to install all dependencies.
- 3.) Run main.py and use the console window that appears to customize your receipt.
- 4.) Open the output directory and find the reciept.pdf. Open the file and enjoy!

## How to install (from without python)

- 1.) Download the .zip file found in the releases page on Github.
- 2.) Unzip the file and make sure a main.exe file and other folders such as /output, /storeimg, /barcode, and /fonts are found in the root directory.
- 3.) Run main.exe and enjoy! Remember to go to the /output folder and open the reciept.pdf file.

## Adding more images to the reciept generator

- 1.) Make sure all images you would like to add follow the following requirements.
      _ Image file format ends with `.jpg`
      _ Images need to have a white or transparent background
      _ Images need to be resized to exactly 200x70 resolution for optimal results
      _ The image name is the name you will enter when you are asked for the store name in the program

- 2.) Move your image file to the /storeimg folder.

- 3.) Make sure the image follows all the requirements in step 1.

- 4.) Your new store should work and you will be able to make reciepts for that store.
