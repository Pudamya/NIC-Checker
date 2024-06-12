#Importing the NIC
import NIC

#Variable initialization
nic_num=0

#Get the inputs from the user
nic_num=str(input("Type your NIC number : "))

#Check whether the NIC is old or new
if len(nic_num)==12 or (nic_num[-1]).isnumeric=="True":

    print("NIC type : new")
    #Call the function
    NIC.new_NIC(nic_num)

elif len(nic_num)==10 or (nic_num[-1]).isnumeric=="False":
    print("NIC type : old")
    #Call the function
    NIC.old_NIC(nic_num)
    
else:
    print("Invalid NIC")
