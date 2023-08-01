import json, requests

base_url = 'https://api.openweathermap.org/data/2.5/weather'
appid = '0a4b273894e6d9eed8be5b4349e626a8'

##City
def city():
  local = input('Please enter your city name\n')
  url = f"{base_url}?q={local}&units=imperial&APPID={appid}"
  print(url)
  print()
  respon = requests.get(url)
  unf_data = respon.json()
  ##print (unformated_data)
  temp = unf_data["main"]["temp"]
  print(f'The temperature is {temp}')
  temp_max = unf_data["main"]["temp_max"]
  print(f'The high today is {temp_max}')
  spiral()

##Zip
def zip():
  local = input('Please enter your zip code\n')
  url = f"{base_url}?q={local}&units=imperial&APPID={appid}"
  print(url)
  print()
  respon = requests.get(url)
  unf_data = respon.json()
  ##print (unformated_data)
  temp = unf_data["main"]["temp"]
  print(f'The temperature is {temp}')
  temp_max = unf_data["main"]["temp_max"]
  print(f'The high today is {temp_max}')
  spiral()

##Start
def greet():
  print('Welcome to the Python Weather Service!')
  lookup()
  


##Look up method
def lookup():
  q = input('Press 1 to look up weather by city\nPress 2 to look up weather by zip\n')
  if q == '1':
    city()
  elif q == '2':
    zip()
  else:
    print('Error. Try again\n')
    lookup()

##Round
def spiral():
  s = input('Enter 1 to see another report\nEnter 2 to exit\n')
  if s == '1':
    print("I've got nowhere to be.")
    lookup()
  elif s == '2':
    print('Thank you. Have a great day!\n')
  else:
    print('1 or 2. just put one\n')
    spiral()  
  
    
greet()