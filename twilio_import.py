import serial
import requests
import time

from twilio.rest import Client 

account_sid = 'Your Twilio account id'
auth_token = 'Your Twilio account token'
client = Client(account_sid, auth_token)

count=1
# Open the serial connection
ser = serial.Serial('COM8', 9600)  # Replace 'COM8' with your Arduino's serial port

# Create an empty list to store the values
values_list = []

# Read values from Arduino
while True:
    # Read the line from serial
    count=count+1
    line = ser.readline()

    # Convert the line to float and append it to the list
    try:
        value = float(line.strip())
        values_list.append(value)
    except ValueError:
        pass

    # Check if the desired number of values is reached
    if len(values_list) >= 5:  # Adjust this condition according to your array size
        # Print the received values
        sum1=0
        print(values_list)
        for i in range(5):
            sum1+=values_list[i]
       
        # Send data to ThingSpeak
        api_key = 'Your API key'  # Put your ThingSpeak API key here
        url = f'https://api.thingspeak.com/update?api_key=Your API key&field1=0'
        

        # Prepare the data payload
        data = {"api_key": api_key}
        
        for i, value in enumerate(values_list):
            field_name = f"field{i+1}"
            data[field_name] = value
    
        # Send the data using HTTP GET request
        response = requests.get(url, params=data)

        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print("Data sent to ThingSpeak successfully.")
        else:
            print("Failed to send data to ThingSpeak.")
            print("Response:", response.text)
        
        # Clear the values list
        values_list = []


        #twilio code

        # print(sum1/5)

        if (sum1/5)>100:
            print("Warning!!!!!!!!!!!!Average Smoke reading greater than  normal")
            message = client.messages.create(
            from_='+Dummy number',
            body='warning!!!!! Average Smoke reading greater than  normal !!',
            to='+91Your Number'
            )
            print(message.sid)

    # send to website code


# Close the serial connection
ser.close()
