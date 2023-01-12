(☞ﾟヮﾟ)☞ 

## BEFORE FIRST USE

Before you first run the program you need to remove a few things:
<br>- in **default.json** remove the first tree line ("sim":"", "tag":"","name":"") 
<br>- uncomment the three lines in main.py (line 20,21,22), and delete their content.


### TODO
- ~~make so all values with the same BLOCK_TYPE are written under same line~~ DONE
- ~~use different json object based on the BLOCK_TYPE [ eg: if BLOCK_TYPE is "AI" then use "AI:{}" ]~~ DONE
- ~~the above thing should be working now...but the values are not getting written to the file~~ DONE
- ~~add text bellow the list of titles [ dont know what it is ]~~  DONE
- ~~fix the position of values [ eg: values in table get infront of the valus in .json >> can lead to conversion errors ]~~ DONE
- add updated values for "lower_title" based on BLOCK_TYPE
