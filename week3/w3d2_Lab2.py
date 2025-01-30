#Jayda Bowe
#W3D2 - Text File Handling 
#SE 126 - Intermediate Programming with Python
#1-23-2025 [W3D2]

#Program Prompt:Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#Variable Dictionary:
#total_rec - total records in the file
#file -  #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list/ matrix / table]
#comp - computer type
#manufacturer - the computer manufacturer
#processor - computer processor type
#ram_size - size  of the RAM
#hardDrive_1 - the first hard drive in the computer
#hardDrive_2 - second hard drive in some computers
#operating - operating system of computer
#year - year computer was made



#--------IMPORTS-----------------------------------------------------
import csv

#--------FUNCTIONS----------------------------------------------------


#--------MAIN EXECUTING CODE--------------------------------------------

#initialize needed counting vars

total_rec = 0


#-----------connected to file-------------------------------------------
with open("text_files/filehandling-1.csv") as csvfile: 
    #we must indent one level while connected to the file

    file = csv.reader(csvfile)

    print(f"\n\n{'COMPTYPE':10}{'BRAND':10}{'PROC':5}{'RAM':5} {'HD#1':6} {'No.HDD':11} {'HD#2':9} {'OS':8} {'YEAR':5}")
    print("--------------------------------------------------------------------------------------------------------------------------")

    for rec in file:
        #this loop will occur for every record in this file

        #Field 1 - rec[0] - computer type
        #from Lab #2
        if rec[0] == "D":
            comp = "Desktop"

        else:
            comp = "Laptop"

        #Field 2 - rec[1] - manufacturer type
        if rec[1] == "DL":
            manufacturer = "Dell"
        elif rec[1] == "GW":
            manufacturer = "Gateway"
        elif rec[1] == "HP":
            manufacturer = "HP"       
        else:
            manufacturer = "*ERROR*" #Optional 

        #Field 3 - rec[2] - processor
        processor = rec[2]

        #Field 4 - rec[3] - ram size
        ram_size = rec[3]

        #Field 5 - rec[4] - first hard drive size
        hardDrive_1 = rec[4]

        #Field 6 - rec[5] - number of hardrives
        no_of_hardDrives = int(rec[5])

        #Field 7,8,9 are based on int(rec[5])
        if no_of_hardDrives == 1:
            hardDrive_2 = "---"     #no second disk here since rec[5] is a 1
            operating = rec[6]      #next field is OS
            year = rec[7]           #final field is the year
        else:
            hardDrive_2 = rec[6]    #rec[5] != 1, so there is a second drive/extra record
            operating = rec[7]      #next field is the OS
            year = rec[8]           #final field is the year

        total_rec += 1    

        #one print for all of the records, regardless of size

        print(f"{comp:10}{manufacturer:10}{processor:5}{ram_size:5}{hardDrive_1:10}{str(no_of_hardDrives):10}{hardDrive_2:10}{operating:10}{year:5}")


#disconnected from file--------------------------------------------------
#displays final data (counting vars)
print()
print(f"Total records in the file: {total_rec}")
