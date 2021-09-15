# ArduinoSerialTimeFinder
 Finds your serial data speed of Arduino for regularly data communication.
## **How do you use?**
&emsp;**1)** Import the project. <br>
```python 
from ArduinoSerialTimeFinder import ArduinoSerialTimeFinder
```
&emsp;**2)** Assign the class object to your variable.<br>
```python
yourVariable = ArduinoSerialTimeFinder(arduino)
```
&emsp;or
```python
yourVariable = ArduinoSerialTimeFinder(port, baudrate)
```
>`arduino`: *If you use the Arduino port already, you can assign the serial object here. If you use this variable, port and baudrate are not needed. (arduino=<class 'serial.serialwin32.Serial'>)*<br>
>`port`: *Arduino port as string. (port="COM6")*<br>
>`baudrate`: *Arduino baudrate as int. (baudrate=115200)*<br>

&emsp;**3)** Find the correct time.<br>
```python
yourVariable.findTime(len_serial_data, limit, starting_time, dt)
```
>`len_serial_data`: *Length of sended serial data by Arduino as char. (len_serial_data=256)* 
>>*If your data length in range of 2 values, you can also use list for accept all variables in values range. (len_serial_data=[250, 260]: Accepts correct all values in range(250, 260), 250 and 260 included.)*<br>

>`limit`: *Break the test() loop after how many times correct values repeated. (limit=300)* <br>
>>*Default=-1, this means never break the loop.*<br> 

>`starting_time`: *Starting time.* <br>
>>*Default=0* <br>

>`dt`: *Time difference for new time if time doesn't correct. (sleeptime=0.00001)*<br>
>>*Default=0.00001*

&emsp;**4)** Get the correct time.<br>
```python
yourVariable.getTime()
```
>Returns correct time. Use after `findTime` method.
<br> 

## **How it works?**
&emsp;**1)** You need to know your Arduino will send how many chars. <br>
&emsp;**2)** When you input this value to `test()` method, program will calculate the waiting time of wanted data for getting them correctly from Arduino. Until Arduino output data and Python input data are equal, the program will add/subtract dt to the time.<br>
&emsp;**Notice 1)** If you say "Why I need this? I can calculate communication time with my baudrate!", this will not work if you use so much `delay` on your Arduino also if you use libraries for robotic tools (even LiquidCrystal) you can not guess your Arduino delay how much times. I wrote this code for complicated and unpredictable scenarios like this.
&emsp;**Notice 2)** You need this when you need to get data regularly. If you are not getting data regularly this code is not needed so much. When you get regularly data from Arduino if you set too much sleep in Python you get next data too, if you don't set enough time you can't get even current data, it comes divided to parts.

