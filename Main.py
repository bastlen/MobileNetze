import telnetlib

## establish connection BCS(PC) BTS(nanoBTS)
tn = telnetlib.Telnet('localhost', port=4242, timeout=20)
print('Connection established!')

##vars
# admin subscriber id
adminSubID = 9

## arguments
# inital command
defCommand = b""
# show subscriber
command1 = b"show subscriber id 1"
#TODO Build SMS command subscriber id 1 sms sender id 2 send Hello World
commandSMS = "subscriber id \i sms sender  "

## execute comands
def execCommand(command):
    # write command to nanoBTS
    tn.write(command + b"\n")
    # read callback from nanoBTS
    ret2 = tn.read_eager()
    ret2 = tn.read_until(b"_DNE", timeout=5)
    # handle callback
    print('Command executed!')
    return ret2


## send SMS as Admin to receiver
def adminSMS(receiverID, message):
    arg = "subscriber id " + str(receiverID) + " sms sender id " + str(adminSubID) + " send ADMIN: " + message + "."
    print(str.encode(arg,'ascii'))
    execCommand(str.encode(arg,'ascii'))


## send broadcast SMS as Admin to multible receivers
def broadcastSMS(receiverIDs, message):
    for x in receiverIDs:
        adminSMS(x, message)


## TESTS

## default test (get connection)
execCommand(defCommand)

## admin singel SMS
adminSMS(2, "Testmessage")

## broaadcast SMS
# list with subscriber ID
idList = [2, 5, 8]
broadcastSMS(idList,"Turn Off Phone!")

