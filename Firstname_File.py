#Create a new file to store names

first_name = open("firstName.txt","x")

#write to firstName.txt file
first_name=open("firstName.txt","a")
first_name.write("Bob")
first_name.write("\nRia")
first_name.write("\nVeronica")
first_name.write("\nPeter")
first_name.write("\nHazel")
first_name.write("\nJosie")
first_name.write("\nHollie")
first_name.write("\nMae")
first_name.write("\nKate")
first_name.write("\nSana")

#open and read the firstName.txt file
first_name=open("firstName.txt","r")
print(first_name.read())

#close the firstName.txt file
first_name.close()

