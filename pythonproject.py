information = []
data = []
count = 0
j = 1
"""
Initialize the class object 
"""
class Application():
    
    def details(self):
        for i in range(count):
            print("\n{5} The name of the book is {0}, written by {1}.\nthe version {2} published in the year {3} at the price of {4}".format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],i+1))
    def sort_price(self):
        # Filtering the data accourding to prize
        print("\n list based on prize")
        p=[]
        for i in range(count):
            o = data[i][4]
            p.append(o)
        p.sort()
        for i in p:
            for k in range (count):
                if(i == data[k][4]):
                    print(data[k])
    def application_input(self):
        global information
        global data
        global count
        global j
        print("Enter the software application details :")
        count = int(input('Enter the total number of books :'))
        for i in range(count):
            # Getting input from the user 
            name = input("\nEnter the " +str(i+j)+" book name : ")
            information.append(name)
            author = input("Enter the " +str(i+j)+" author : ")
            information.append(author)
            version = input("Enter the " +str(i+j)+" version : ")
            information.append(version)
            year = int(input("Enter the "+str(i+j)+" published year: "))
            information.append(year)
            price = int(input("Enter the "+str(i+j)+"  book price : "))
            information.append(price)
            data.append(information)
            information = []
                 
    def sort_year(self):
        print("\n list based on published year")  
        year=[]
        for i in range(count):
            b = data[i][3]
            year.append(b)
        year.sort()
        for i in year:
            for j in range(count):
                if(i == data[j][3]):
                    print(data[j])
    # search option program
    def search(self):
        print("\n\nsearching")
        while(True):
            choice=int(input(("Enter  1 to search \nOR\nEnter 0 to stop ")))
            # If any records found then return the filter result otherwise warning message
            if(choice==1):
                s=input("Enter the AUTHOR name : ")
                q=int(input("Enter the published year : "))
                flag=0
                for i in range(count):
                    if(q == data[i][3]):
                        if(s == data[i][1]):
                            print("The searched book is  ",data[i])
                            flag=flag+1
                if(flag == 0):
                    print("No such book is found by {1} in {0}".format(q, s))
            elif(choice==0):
                return print("THANK YOU!!")
            #sorting by year
    
obj = Application()
obj.application_input()
obj.details()
obj.sort_price()
obj.sort_year()
obj.search()

