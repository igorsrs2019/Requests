import requests
import time

contador = 1
status = True

#As long as the status code is 200 the repeat loop will be executed.
while status:
    r = requests.get('http://www.google.com')
    if (r.status_code == 200):
         
         time.sleep(0)
         contador = contador + 1
         print(contador)
    else:
        print("status code is not 200, operation canceled")
        status = False