import math
import random

##   Customize reciepts   ##
print("Fetch Reciept Generator")
print("Created by BengaliTech")
print("""This program is meant to be used to generate custom reciepts as pdf files to be
scanned into the Fetch Rewards app. The purpose is to make the items reflect the 
current promotions that are going on to provide you maximium points \n \n""")

#Store
storename = input("Enter the name of the store: ")
storeaddress = input("Enter the store address in this format '11111 Street Rd, City, State, Zip Code': ")

#Date/Time
date = input("Enter date in this format 'mm/dd/yyyy': ")
time = input("Enter time in this format '12:00 AM/PM': ")

#Price
salestax = input("Enter your sales tax in this format '0.06': ")

item1name = input("Enter the name of your first product: ")
item1qty = input("Enter how much of this item you want to buy: ")
item1price = input("Enter the price of your first item in this format '11.11': ")

item2name = input("Enter the name of your second product: ")
item2qty = input("Enter how much of this item you want to buy: ")
item2price = input("Enter the price of your second item in this format '11.11': ")

item3name = input("Enter the name of your third product: ")
item3qty = input("Enter how much of this item you want to buy: ")
item3price = input("Enter the price of your third item in this format '11.11': ")

#barcode
barid = random.randrange(0000000000000, 9999999999999)

tax = (float(item1price) * float(item1qty) + float(item2price) * float(item2qty) + float(item3price) * float(item3qty)) * float(salestax)
roundtax = round(tax, 2)
result = float(item1price) * float(item1qty) + float(item2price) * float(item2qty) + float(item3price) * float(item3qty) + tax
total = round(result, 2)
print(total)

extramoney = random.randrange(5, 30)

##   Pdf generation   ##
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors, fonts
from barcode import EAN13
from barcode import writer
from PIL import Image

filename = 'reciept.pdf'
storeImg = f'storeimg/{storename}.jpg'

reciept_barcode = EAN13(str(barid), writer.ImageWriter('PNG'))
reciept_barcode.save('barcode/barcode')

barcode_old = Image.open('barcode/barcode.png')
barcode_new = barcode_old.resize((150, 50))
barcode_new.save('barcode/barcode.png')

reciept = canvas.Canvas(f'output/{filename}', pagesize = (250, 445))
reciept.setTitle('Reciept')

reciept.drawImage(storeImg, 25, 375, anchor='c')
reciept.drawImage('barcode/barcode.png', 50, 0)

#Set up fonts
pdfmetrics.registerFont(TTFont('MerchantCopy', 'fonts/MerchantCopy.ttf'))
pdfmetrics.registerFont(TTFont('Helvetica-Light', 'fonts/Helvetica-Light.ttf'))

reciept.setFont('MerchantCopy', 16)
reciept.drawString(20, 365, storeaddress)
reciept.drawCentredString(125, 380, storename)
reciept.drawCentredString(125, 350, f"{date} {time}")


reciept.setFont('MerchantCopy', 14)

if (float(item1price) != 0 and float(item1qty) != 0):
    reciept.drawString(20, 300, f"{item1qty}   {item1name}: ${item1price}")

if (float(item3price) != 0 and float(item2qty) != 0):
    reciept.drawString(20, 280, f"{item2qty}   {item2name}: ${item2price}")

if (float(item3price) != 0 and float(item3qty) != 0):
    reciept.drawString(20, 260, f"{item3qty}   {item3name}: ${item3price}")


reciept.setFont('MerchantCopy', 16)
reciept.drawRightString(125, 210, f"Subtotal: {float(item1price) * float(item1qty) + float(item2price) * float(item2qty) + float(item3price) * float(item3qty)}")
reciept.drawRightString(125, 190, f"Tax: {roundtax}")
reciept.drawRightString(125, 170, f"Cash: {round(total + float(extramoney), 2)}")
reciept.drawRightString(125, 150, f"Change: {round((total + float(extramoney)) - total, 2)}")

reciept.setFont('MerchantCopy', 20)
reciept.drawRightString(125, 100, f"Total: {total}")


reciept.setFont('MerchantCopy', 18)
reciept.drawString(10, 70, f"Thank you for shopping at {storename}!")
reciept.save()