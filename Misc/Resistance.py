A_string=raw_input("please enter the Area: (in m2): \n")
L_string=raw_input("please enter the Length: (in m): \n")
k_string=raw_input("please enter the conductivity: (in W/(m.K)): \n")
print( "\n Hey! you just told me that "+" A = "+(A_string)+" L = "+(L_string)+" k ="+k_string) 
R=float(L_string)/(float(k_string)*float(A_string))
print("\n Well the resistance will be "+ str(R)+"\n")
print("The Rice to be seen" +str(R)+ "degC/W")