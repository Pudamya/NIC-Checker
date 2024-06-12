#Defining a function for the new NIC
def new_NIC(nic_num):
    "This is to extract the details from the NIC number"
    #Print the birth year
    print("You were born on ", nic_num[0:4])

    #Identify the gender
    if  nic_num[2:5]<=366:
        print("You are a male")
    elif nic_num[2:5]>=501 and nic_num<=866:
        print("You are a female")
    else:
        print("Incorrect NIC number")

    #Identify as a voter or none-voter
    if nic_num[-1]=="V":
        print("You are a voter")
    elif nic_num[-1]=="X":
        print("You are a none voter")
    else:
        print("Invalid NIC number")
    return 
    

#Defining a function for the old NIC
def old_NIC(nic_num):
    "This is to extract the details from the NIC number"
    #Print the birth year
    print("You were born on ", nic_num[0:2])

    #Identify the gender
    if  nic_num[2:5]<=366:
        print("You are a male")
    elif nic_num[2:5]>=501 and nic_num<=866:
        print("You are a female")
    else:
        print("Incorrect NIC number")

    #Identify as a voter or none-voter
    if nic_num[-1]=="V":
        print("You are a voter")
    elif nic_num[-1]=="X":
        print("You are a none voter")
    else:
        print("Invalid NIC number")
    return
    
