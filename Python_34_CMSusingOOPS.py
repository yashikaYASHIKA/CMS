""
"""
Customer Management System using OOPS
"""



#BLL
import pickle
import pymysql
class Customer:
    cus_list=[]
    con = pymysql.connect(host="localhost", user="root", password="root123", database="cusdb")
    cur = con.cursor()
    def __init__(self): #self=1000
        self.id=0       #1000.id=0
        self.name=0     #1000.name=0
        self.age=0       #1000.age=0
        self.mob=0       #1000.mob=0
    def addCustomer(self):  #self=1000, 2000
        Customer.cus_list.append(self)  #cus_list=[1000,2000...
        Customer.cur.execute(f"insert into custb values('{self.id}','{self.name}','{self.age}','{self.mob}')")
        Customer.con.commit()
    def searchCustomer(self):   #self 9000, self.id=20, 9000.id=20, 9000.name=0, 9000.age=0
        # for e in Customer.cus_list: #e=1000, e=2000
        #     if(e.id==self.id):
        #         self.name=e.name    #self.name=Anil, 9000.name=Anil
        #         self.age=e.age
        #         self.mob=e.mob
        #         return
        qry=f"select * from custb where id='{self.id}'"
        Customer.cur.execute(qry)
        data=Customer.cur.fetchone()
        self.name=data[1]
        self.age=data[2]
        self.mob=data[3]


    def deleteCustomer(self):   #self=10000, self.id=20, self.name=0, self.age=0..
        qry=f"delete from custb where id='{self.id}'"
        Customer.cur.execute(qry)
        Customer.con.commit()
        # for e in Customer.cus_list: #e=1000, e=2000
        #     if(e.id==self.id):
        #         Customer.cus_list.remove(e)
        #         return
    def modifyCustomer(self):   #self=11000, self.id=30,self.name="Prashant",self.age=55..
        qry=f"update custb set name='{self.name}',age='{self.age}',mob='{self.mob}'where id='{self.id}'"
        Customer.cur.execute(qry)
        Customer.con.commit()
        # for e in Customer.cus_list: #e=1000
        #     if(e.id==self.id):
        #         e.name=self.name
        #         e.age=self.age
        #         e.mob=self.mob
        #         return


    @staticmethod
    def saveToPickle():
        f=open("D://temp/cmsdata.txt","wb")
        pickle.dump(Customer.cus_list,f)
        f.close()
    @staticmethod
    def loadFromPickle():
        f=open("D://temp/cmsdata.txt","rb")
        Customer.cus_list=pickle.load(f)
        f.close()

#PL
if(__name__=="__main__"):
    print("Welcome to CETPA's CMS")
    def showCustomer(cus):       #showCustomer(9000)
        print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)

    while(1):

        ch=input("""Enter Choice: 1 for Add Cust, 2 Search, 3 Delete, 4 Modify, 5 Display All, 6 Exit
        7: Save to Pickle, 8: Laod from Pickle:""")
        if(ch=="1"):    #Add Customer
            cus = Customer()  # cus 1000,#cus.id=0 #cus.name=0#cus.age=0#1000.mob=0
            cus.id=input("Enter Cust ID:")  #10, #20
            cus.name = input("Enter Cust Name:") #Vikas, #Anil
            cus.age = input("Enter Cust Age:")#39
            cus.mob = input("Enter Cust Mob:")  #1234
            cus.addCustomer()
            print("Customer Added Successfully")
        elif(ch=="2"):   #Search Customer
            cus=Customer()  #cus address 9000, #cus.id=0 #cus.name=0#cus.age=0#1000.mob=0
            cus.id=input("Enter Customer ID to search:")#9000.id=20    #cus.id=20
            cus.searchCustomer()    #self=cus
            showCustomer(cus)       #showCustomer(9000)
        elif(ch=="3"):  #Delete Customer
            cus=Customer()  #cus address 10000,#cus.id=0 #cus.name=0#cus.age=0#1000.mob=0
            cus.id=input("Enter Cust Id")# cus.id=20
            cus.deleteCustomer()
            print("Customer Deleted Successfully")
        elif(ch=="4"):  #Modify Customer
            cus=Customer()      #cus address 11000#cus.id=0 #cus.name=0#cus.age=0#1000.mob=0
            cus.id=input("Enter Cust ID:")  #cus.id=30
            cus.name=input("Enter Cust updated name:")#cus.name="Prashant"
            cus.age = input("Enter Cust updated age:")#cus.age=55
            cus.mob = input("Enter Cust updated mob:")#cus.mob=9999
            cus.modifyCustomer()
            print("Customer Modified Successfully")
        elif(ch=="5"):      #Display All Customers
            for e in Customer.cus_list:
                showCustomer(e)
        elif(ch=="6"):  #Exit
            print("Thanks for using CETPA's CMS")
        elif(ch=="7"):      #Save to Pickle
            Customer.saveToPickle()
        elif (ch == "8"):  # Load from Pickle
            Customer.loadFromPickle()
        else:
            print("Incorrect Choice")






