import csv
csv_fileR=open(r"C:\Users\User\Desktop\Bido\Books.csv",'r+',newline='')
csv_reader= csv.reader(csv_fileR)
Book_ID=[]
Title=[]
Author=[]
Category=[]
Quantity=[]
Unit_price=[]
Total_price=[]

for line in csv_reader:
    Book_ID.append(int(line[0]))
    Title.append(line[1])
    Author.append(line[2])
    Category.append(line[3])
    Quantity.append(int(line[4]))
    Unit_price.append(float(line[5]))
    Total_price.append(float(line[6]))


def Credits():
    print("\n***********************************************")
    print("Welcome to FEPS Bookshop Inventory System")
    print("***********************************************\n")


def menu():
    print("\nPlease choose one of the following options")
    print("1. Read Data")
    print("2. List Data")
    print("3. Search by Title")
    print("4. Search by Author")
    print("5. Add a New Book")
    print("6. Delete a Book")
    print("7. Add to the Current Stock of a Book")
    print("8. Remove from the Current Stock of a Book")
    print("9. Show Total Value of the Books")
    print("10. Save Data")
    print("99. Exit")
    print("*************************************\n")
    user_input = input('Enter your choice: ')
    user_input = int(user_input)
    if user_input == 1:
        print("-- Your Option is : 1")
        Read_data()
    elif user_input == 2:
        print("-- Your Option is : 2")
        List_data()
    elif user_input == 3:
        print("-- Your Option is : 3")
        Search_By_Title() 
    elif user_input == 4:
        print("-- Your Option is : 4")
        Search_By_Author()
    elif user_input == 5:
        print("-- Your Option is : 5")
        Add_Book()
    elif user_input == 6:
        print("-- Your Option is : 6")
        Delete_Book()
    elif user_input == 7:
        print("-- Your Option is : 7")
        Add_To_Stock()
    elif user_input == 8:
        print("-- Your Option is : 8")
        Remove_From_Stock()
    elif user_input == 9:
        print("-- Your Option is : 9")
        Total_value()
    elif user_input == 10:
        print("-- Your Option is : 10")
        Save_Data()
    elif user_input == 99:
        print("-- Your Option is : 99")
        Exit()

def Read_data():
    csv_fileR=open(r"C:\Users\User\Desktop\Bido\Books.csv",'r+',newline='')
    csv_reader= csv.reader(csv_fileR)
    counter = 0
    for row in csv_reader:
        counter=counter + 1
    print("\nReading data ...")
    print("Reading data complete !")
    print("There are",counter, "books found in the data file\n")
    menu()
    

def List_data():
    print("\n-----------------------------------------------------------------------------------------------")
    print("Listing data ...\n")
    print("Book_ID"+"\tTitle"+"\t\t   Author"+"\t   Category"+"   Quantity"+"  Unit_price"+"      Total_price")
    for a,b,c,d,e,f,g in zip(Book_ID,Title,Author,Category,Quantity,Unit_price,Total_price):
        print("-----------------------------------------------------------------------------------------------")
        print(str(a)+"  \t"+str(b)+"\t   "+str(c)+"\t   "+str(d)+"\t"+str(e)+"\t"+str(f)+"\t\t"+str(g))
    print("\nListing data complete !\n")
    menu()


def Search_By_Title():
    print("\n*Searching by Title*")
    x=input("Enter the title of the book: ")
    print("Items Found:\n")
    for i in Title:
        i=i.rstrip()
        if i.startswith(x) or i.find(x) != -1:
            if i in Title:
                j=Title.index(i)
                print("-----------------------------------------------------------------------------------------------")
                print(f"{Book_ID[j]}\t{Title[j]}\t   {Author[j]}\t   {Category[j]}    {Quantity[j]} \t {Unit_price[j]}            {Total_price[j]}")
        # else:
        #     print("Not Found")  
    print("-----------------------------------------------------------------------------------------------\n")  
    menu()          



def Search_By_Author():
    print("\n*Searching by Author*")
    x=input("Enter the Author of the book: ")
    print("Items Found:\n")
    for i in Author:
        i=i.rstrip()
        if i.startswith(x) or i.find(x) != -1:
            if i in Author:
                j=Author.index(i)
                print("-----------------------------------------------------------------------------------------------")
                print(f"{Book_ID[j]}\t{Title[j]}\t   {Author[j]}\t   {Category[j]}    {Quantity[j]} \t {Unit_price[j]}            {Total_price[j]}")
        # else:
        #     print("Not Found")  
    print("-----------------------------------------------------------------------------------------------\n") 
    menu()   


def Add_Book():
    print("Adding a new book...")
    print("Please Enter Book Information:")
    print("--------------------------------------------\n")
    Book_ID.append(int(input("Enter Book ID : ")))
    Title.append(input("Enter Title : "))
    Author.append(input("Enter Auhtor : "))
    Category.append(input("Enter Category : "))
    QuantityVal=int(input("Enter Quantity : "))
    Quantity.append(QuantityVal)
    UnitVal=float(input("Enter Unit Price : "))
    Unit_price.append(UnitVal)
    TotalVal=float(QuantityVal*UnitVal)
    Total_price.append(TotalVal)
    menu()


def Delete_Book():
    print("Deleting a book...")
    print("--------------------------------------------\n")
    x=int(input("Enter the ID of the book you want to remove : "))-1
    del Book_ID[x]
    del Title[x]
    del Author[x]
    del Category[x]
    del Quantity[x]
    del Unit_price[x]
    del Total_price[x]
    menu()


def Add_To_Stock():
    print("\n---------------------------------------------")
    print("Adding to Current Stock of a book ...")
    print("Please enter book information :")
    x=int(input("Book ID : "))
    if x in Book_ID:
        Book_Index=Book_ID.index(x)
        UpdateQuantity=int(input("Quantity to add : "))
        Q = (Quantity[Book_Index])
        Q += UpdateQuantity
        Quantity[Book_Index]=Q
        Total_price[Book_Index]=Quantity[Book_Index]*Unit_price[Book_Index]
        print("Adding to Stock Complete!")
        print("---------------------------------------------\n")
        menu()


def Remove_From_Stock():
    print("\n---------------------------------------------")
    print("Removing from Current Stock of a book ...")
    print("Please enter book information :")
    x=int(input("Book ID : "))
    if x in Book_ID:
        Book_Index=Book_ID.index(x)
        UpdateQuantity=int(input("Quantity to remove from stock : "))
        Q = (Quantity[Book_Index])
        Q -= UpdateQuantity
        Quantity[Book_Index]=Q
        Total_price[Book_Index]=Quantity[Book_Index]*Unit_price[Book_Index]
        print("Removing from Stock Complete!")
        print("---------------------------------------------\n")
        menu()


def Total_value():
    print("\nTotal Value Of the Books ...")
    Total=0.0
    for i in Total_price:
        Total+=i
    print(f"Total Value = {Total} $\n")
    menu()


def Save_Data():
    csv_fileW=open(r"C:\Users\User\Desktop\Bido\Books.csv",'w',newline='')
    csv_writer = csv.writer(csv_fileW)
    NewList = list(zip(Book_ID,Title,Author,Category,Quantity,Unit_price,Total_price))
    for row in range(len(NewList)):
        csv_writer.writerow(NewList[row])
    csv_fileW.close()
    print("\nUpdate Data File Completed Successfully\n")
    menu()

def Exit():
    csv_fileR.close()

Credits()
menu()