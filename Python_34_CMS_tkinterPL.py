#PL
from CMSusingOOPS import *
from tkinter import *
from tkinter import messagebox
def add_handler():
    cus=Customer()      #1000, cus.id=0,cus.name=0
    cus.id=var_id.get()
    cus.name = var_name.get()
    cus.age = var_age.get()
    cus.mob = var_mob.get()
    cus.addCustomer()
    messagebox.showinfo("CMS","Customer Added Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")



def search_handler():
    cus=Customer()      #cus address 9000, cus.id=0,cus.name=0
    cus.id=var_id.get()     #cus.id=20
    cus.searchCustomer()    #cus.name="Anil",cus.age=41
    var_name.set(cus.name)
    var_age.set(cus.age)
    var_mob.set(cus.mob)


def delete_handler():
    cus=Customer()      #cus=10000
    cus.id=var_id.get() #cus.id=20
    cus.deleteCustomer()
    messagebox.showinfo("CMS", "Customer Deleted Successfully")
    var_id.set("")

def modify_handler():
    cus = Customer()  # 11000, cus.id=0,cus.name=0
    cus.id = var_id.get()       #20
    cus.name = var_name.get()   #Prashant
    cus.age = var_age.get()     #55
    cus.mob = var_mob.get()     #9999
    cus.modifyCustomer()
    messagebox.showinfo("CMS", "Customer Modified Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")


def display_all_handler():
    root_all_cust=Tk()
    lbl_id_all=Label(root_all_cust,text="CUST ID",font=1,bg="Orange",width=20,height=2)
    lbl_id_all.grid(row=0,column=0)
    lbl_name_all = Label(root_all_cust,text="CUST NAME", font=1, bg="Orange", width=20, height=2)
    lbl_name_all.grid(row=0, column=1)
    lbl_age_all = Label(root_all_cust,text="CUST AGE", font=1, bg="Orange", width=20, height=2)
    lbl_age_all.grid(row=0, column=2)
    lbl_mob_all = Label(root_all_cust,text="CUST MOB", font=1, bg="Orange", width=20, height=2)
    lbl_mob_all.grid(row=0, column=3)
    i=0
    qry="select * from custb"
    Customer.cur.execute(qry)
    data=Customer.cur.fetchall()
    for e in data:     #e=
        i+=1            #i=1, i=2
        lbl_id_cust=Label(root_all_cust,text=e[0], font=1, bg="Yellow", width=20, height=2)
        lbl_id_cust.grid(row=i,column=0)
        lbl_name_cust=Label(root_all_cust,text=e[1], font=1, bg="Yellow", width=20, height=2)
        lbl_name_cust.grid(row=i,column=1)
        lbl_age_cust=Label(root_all_cust,text=e[2], font=1, bg="Yellow", width=20, height=2)
        lbl_age_cust.grid(row=i,column=2)
        lbl_mob_cust=Label(root_all_cust,text=e[3], font=1, bg="Yellow", width=20, height=2)
        lbl_mob_cust.grid(row=i,column=3)


    # for e in Customer.cus_list:     #e=1000, 2000
    #     i+=1            #i=1, i=2
    #     lbl_id_cust=Label(root_all_cust,text=e.id, font=1, bg="Yellow", width=20, height=2)
    #     lbl_id_cust.grid(row=i,column=0)
    #     lbl_name_cust=Label(root_all_cust,text=e.name, font=1, bg="Yellow", width=20, height=2)
    #     lbl_name_cust.grid(row=i,column=1)
    #     lbl_age_cust=Label(root_all_cust,text=e.age, font=1, bg="Yellow", width=20, height=2)
    #     lbl_age_cust.grid(row=i,column=2)
    #     lbl_mob_cust=Label(root_all_cust,text=e.mob, font=1, bg="Yellow", width=20, height=2)
    #     lbl_mob_cust.grid(row=i,column=3)

def save_handler():
    Customer.saveToPickle()
    messagebox.showinfo("CMS", "Data Saved Successfully")
def load_handler():
    Customer.loadFromPickle()
    messagebox.showinfo("CMS", "Data Loaded Successfully")

root=Tk()
lbl_id=Label(root,text="Cust Id: ",font=1)
lbl_id.grid(row=0,column=0)
lbl_name=Label(root,text="Cust Name: ",font=1)
lbl_name.grid(row=1,column=0)
lbl_age=Label(root,text="Cust Age: ",font=1)
lbl_age.grid(row=2,column=0)
lbl_mob=Label(root,text="Cust Mob: ",font=1)
lbl_mob.grid(row=3,column=0)

var_id=StringVar()
entr_id=Entry(root,textvariable=var_id,font=1)
entr_id.grid(row=0,column=1)
var_name=StringVar()
entr_name=Entry(root,textvariable=var_name,font=1)
entr_name.grid(row=1,column=1)
var_age=StringVar()
entr_age=Entry(root,textvariable=var_age,font=1)
entr_age.grid(row=2,column=1)
var_mob=StringVar()
entr_mob=Entry(root,textvariable=var_mob,font=1)
entr_mob.grid(row=3,column=1)

btn_add=Button(root,text="Add Cust",font=1,command=add_handler,width=15,height=2)
btn_add.grid(row=4,column=0)
btn_search=Button(root,text="Search Cust",font=1,command=search_handler,width=15,height=2)
btn_search.grid(row=4,column=1)
btn_delete=Button(root,text="Delete Cust",font=1,command=delete_handler,width=15,height=2)
btn_delete.grid(row=4,column=2)
btn_modify=Button(root,text="Modify Cust",font=1,command=modify_handler,width=15,height=2)
btn_modify.grid(row=5,column=0)
btn_display_all=Button(root,text="Display All",font=1,command=display_all_handler,width=15,height=2)
btn_display_all.grid(row=5,column=1)
btn_save=Button(root,text="Save Data",font=1,command=save_handler,width=15,height=2)
btn_save.grid(row=5,column=2)
btn_load=Button(root,text="Load Data",font=1,command=load_handler,width=15,height=2)
btn_load.grid(row=6,column=0)




root.mainloop()

"""
This is called Perfect Layered Architecture, which we designed in CMS using OOPS and Tkinter.
Perfect Layered Architectures says, if we want to make some changes in PL then layered should
be perfectly separated that in our program to make change in PL, we should not touch the BLL.
vice versa also true/should be followed.

Here we have not small changes rather we have completely modified the PL from Console programming
to GUI programming still we have not touched the BLL.  
"""


