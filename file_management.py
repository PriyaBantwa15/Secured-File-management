import os

class File:
    def __init__(self):
        self.path=os.getcwd()
        self.data={'user1':'1','user2':'xyz@456','user3':'lmn@123'}
        u_name=input("Enter username: ")
        self.u_name=u_name
        if u_name in self.data:
            passw=input("Enter password: ")
            if passw == self.data[u_name]:
                print("login successfull")
                print(f"User : {u_name}")

                ask=input("Do you have your file or not\n(write yes if file is existing or write no if file is not existing):").lower()
                if ask=='yes':
                    self.choice_file()
                elif ask=='no':
                    self.create_file()
                else:
                    print("Enter valid information")

            else:
                for i in range(4):
                    print("You have ",4-i,"tries")
                    passw=input("Incorrect password enter again:")
                    if passw == self.data[u_name]:
                        print("login successfull")
                        print(f"User : {u_name}")

                        ask=input("Do you have your file or not\n(write yes if file is existing or write no if file is not existing):").tolower()
                        if ask=='yes':
                            self.choice_file()
                        elif ask=='no':
                            self.create_file()
                        else:
                            print("Enter valid information")
                        
                    else:
                        print("Now you can login after 24 hours...")
        else:
            print("Invalid username")
        
    def create_file(self):
        lst_data=[]
        file=input("Enter the file name:")
        with open(file+".txt",'w')as c1:
            print("Your file is created successfully")

            while(True):
                data=input("Enter the data that you want to add in your file\n(write 'done' when you completed):\n")
                if data=='done':
                    break
                else:
                    lst_data.append(data+'\n')

            c1.writelines(lst_data)
        
        self.choice_file()

    def choice_file(self):
        #-------------choice--------------
        print("________________________________________________________________________________________")
        print("\n\t\t\t\t\tCHOICE FILLING")
        print("________________________________________________________________________________________")

        choice=int(input("\nEnter your choice \n1 for read only \n2 for write \n3 for appending \n4 create file \nany number for exit: "))
        if choice==1:
            self.read_file()
        elif choice==2:
            self.write_file()
        elif choice==3:
            self.append_file()
        elif choice==4:
            self.create_file()
        
        else:
            exit()
    def read_file(self):
        file=input("Enter the file name:")
        with open(file+".txt",'r') as self.r1:
            print("Your file data:\n\n\n")
            print(self.r1.read())
        self.choice_file()
    
    
    def write_file(self):
        lst_data=[]
        file=input("Enter the file name:")
        with open(file+".txt",'w') as self.r2:
            print("\nYour file data is removed now you can write:\n")

            while(True):

                data=input("Enter the data that you want to add in your file\n(write 'done' when you completed):\n")
                if data=='done':
                    break
                else:
                    lst_data.append(data+'\n')
            self.r2.writelines(lst_data)
            print("File is updated successfully")
        
        self.choice_file()


    def append_file(self):
        lst_data=[]
        self.file=input("Enter the file name:")
        with open(self.file+".txt",'a') as self.r3:
            while(True):

                data=input("Enter the data that you want to add in your file\n(write 'done' when you completed):\n")
                if data=='done':
                    break
                else:
                    lst_data.append(data+'\n')
            self.r3.writelines(lst_data)
            print("File is updated successfully")
        
        self.choice_file()
print("________________________________________________________________________________________")
print("\n\t\t\t\t\tLOGIN")
print("________________________________________________________________________________________")
try:
    obj=File()
except Exception as e:
    print(e)
