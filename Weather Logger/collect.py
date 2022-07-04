from sense_hat import * 
from time import sleep

sense = sense_hat()

while True:
    sleep(5)
    myfile = open('weather.txt','a')
    myfile.write(sense.temp)
    myfile.write('\n')
    myfile.close()