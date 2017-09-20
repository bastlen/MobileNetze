import os

# params for establishing connection to nanoBTS
con_arg1 = "cd"
con_arg2 = "cd ./openbsc/openbsc/src/osmo-nitb/"
con_arg3 = "./osmo-nitb -P"

# establish connection to nanoBTS
def estabConnection():
    os.system("gnome-terminal -e 'bash -c \"" + con_arg1 + ";" + con_arg2 + ";" + con_arg3 + "; exec bash\"'")

# connect
estabConnection()




