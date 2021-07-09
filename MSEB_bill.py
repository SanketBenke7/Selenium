from selenium import webdriver
import os, time
import base64
# will convert the image to text string
import pytesseract
# adds image processing capabilities
from PIL import Image
cwd = os.getcwd()

#replace below value
consumer_number = "0000000000000"
Billing_Unit = "0000"
tesseract_file_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"
chrome_driver_path = f"{cwd}\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://wss.mahadiscom.in/wss/wss_view_pay_bill.aspx")
time.sleep(1)

consumerNo = driver.find_element_by_id("consumerNo")
consumerNo.send_keys(consumer_number)
time.sleep(1)

BillingUnit = driver.find_element_by_id("txtBUFilter")
BillingUnit.send_keys(Billing_Unit)
time.sleep(1)

canvas = driver.find_element_by_id("captcha")
# get the canvas as a PNG base64 string
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
# decode
canvas_png = base64.b64decode(canvas_base64)
# save to a file
with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)

 # opening an image from the source path
img = Image.open('canvas.png')
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd =tesseract_file_path
# converts the image to result and saves it into result variable
captch_code = pytesseract.image_to_string(img)
Captcha = driver.find_element_by_id("txtInput")
Captcha.send_keys(captch_code)
time.sleep(1)

driver.find_element_by_id("lblSubmit").click()

driver.find_element_by_id("Img1").click()

newURl = driver.window_handles[0]
driver.switch_to.window(newURl)
time.sleep(2)

before_date = driver.find_element_by_id("promptPaymentDate5")
last_date = driver.find_element_by_id("billDueDate7")
after_date = driver.find_element_by_id("billDueDate8")
before_date_bill = driver.find_element_by_id("netBillPPD3")
last_date_bill = driver.find_element_by_id("roundBill3")
after_date_bill = driver.find_element_by_id("netBillDPC")
print(f"before {before_date.text} = {before_date_bill.text}")
print(f"before {last_date.text} = {last_date_bill.text}")
print(f"after {after_date.text} = {after_date_bill.text}")
