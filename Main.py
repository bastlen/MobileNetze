import telnetlib
import sqlite3

tn = telnetlib.Telnet('localhost', port=4242, timeout=20)
print('Connection established!')

################
# main program #
################

# arguments
defCommand = b""
command1 = b"show subscriber id 1"

#TODO Build SMS command subscriber id 1 sms sender id 2 send Hello World
commandSMS = "subscriber id \i sms sender  "


# execute comands
def execCommand(command):
    # write command to nanoBTS
    tn.write(command + b"\n")
    # read callback from nanoBTS
    ret2 = tn.read_eager()
    ret2 = tn.read_until(b"_DNE", timeout=5)
    # handle callback
    print('Command executed!')
    return ret2

# default test (get connection)
execCommand(defCommand)

# execute commands
_s1 = execCommand(command1)
#s1 = str(_s1)
#s2 = "IMSI: "
_s2 = execCommand(command1)

#print(s1[s1.index(s2) + len(s2):])
#TODO parse infomration out of callbacks
print('command1')
print(_s1)
print('command2')
print(_s2)
