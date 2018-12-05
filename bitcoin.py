"""
YOU ARE FREE TO USE THIS FILE AS U WISH
THIS FILE DOESNT COME WITH ANY KIND OF WARRANTY, THIS FILE WORKS AS LONG AS COIN DESK API IS ONLINE
YOU ARE FREE DOWNLOAD, DISTRIBUTE, USE
"""

import json,requests,csv # imports the dependencies
from twilio.rest import Client # imports the twilio account
account_sid = input("add sid") # add your acoount_sid (found in the twilio console)
auth_token  = input("auth")# add your auth_token (found in consle)
res=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") # downloads the required data in json
res.raise_for_status() # checks for anomalies while downloading
print("download success")
data=json.loads(res.text) # converts the json data to pythonic dictionary
time=((data["time"]["updated"])) # takes the time
USD=(data["bpi"]["USD"]["rate_float"]) # reads the usd value of bitcoin right now
GBP=(data["bpi"]["GBP"]["rate_float"]) # reads the gbp value of bitcoin right now
EUR=(data["bpi"]["EUR"]["rate_float"]) # reads the eur value of bitcoin right now
file=open("bit_coin_value.csv","a",newline="") # creates new csv file in current directory, the file only gets appended
print("appending to the file")
writer=csv.writer(file,delimiter="\t") # starts writing with tab space in between the cells
print("data written")
writer.writerow([time,str(USD)+" USD",str(GBP)+" GBP",str(EUR)+" EUR"]) # appends new row to the exixting row
file.close() # closes the file 
"""
This part will make necessary requests to send
messages, 
"""
client = Client(account_sid, auth_token)
message = client.messages.create(
    to=input("your number"), 
    from_=input("destination number"),
    body="the current value of bit coin in USD is "+str(USD)+"$")

print(message.sid)