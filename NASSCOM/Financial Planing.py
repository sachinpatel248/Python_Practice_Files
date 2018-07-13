import json
import csv
import pandas
import ast
import datetime
import os


# To be incremented or stored and retrived from file
Unique_ID = 0

Expense_File_Path = r'Farmers_Expense.csv';
Income_File_Path = r'Farmers_Income.csv';
Unique_ID_File_Path = r'Unique_ID.txt'


#################################  For UNIQUE ID START    #########################

def Write_Unique_ID(Unique_ID):
    global Unique_ID_File_Path
    file = open(Unique_ID_File_Path, 'w')
    file.write(str(Unique_ID))
    file.close()


def Read_Unique_ID():
    global Unique_ID_File_Path
    
    if not (os.path.exists(Unique_ID_File_Path)):
        Unique_ID = 0
        Write_Unique_ID(str(Unique_ID))
        
    file = open(Unique_ID_File_Path, 'r') 
    Unique_ID = str(file.read())
    file.close()
    return Unique_ID

def Get_Unique_ID():
    global Unique_ID;
    Unique_ID = int(Read_Unique_ID());
    Unique_ID = Unique_ID + 1;
    Write_Unique_ID(Unique_ID);    
    #print (Unique_ID)
    return Unique_ID

#################################  For UNIQUE ID   END   #########################


#################################  Expense Object  START  #########################

class Expense(object):
    
    ID = 0   
    FarmerID = 0    
    
    # Labour
    Labour = False
    
    Male = 0
    Female = 0
    
    # Job
    Job = False
    Ploughing = 0
    Planting = 0
    Weeding = 0
    Weeding = 0
    
    # Material
    Material = False
    
    Fertilizers = 0
    Seeds = 0
    Saplings = 0
    Pesticides = 0
    Utility = 0
    Water = 0
    Electricity = 0
    
    # Machinery
    Machinery = False
    
    Tractor = 0
    Pump = 0
    DateTime = 0
    
    
    def __init__(self, ID, farmerID ,labour, male, female, job, ploughing, planting, weeding, material, fertilizers, seeds, saplings, pesticides, utility, water, electricity, machinery, tractor, pump, datetime):
        
        self.ID = ID
        
        self.FarmerID = farmerID
        
        
        self.labour = labour
        self.male = male 
        self.female = female
        
        self.job = job
        self.ploughing = ploughing
        self.planting = planting
        self.weeding = weeding
        
        self.material = material
        
        self.fertilizers = fertilizers
        self.seeds = seeds
        self.saplings = saplings
        self.pesticides = pesticides
        self.utility = utility
        self.water = water
        self.electricity = electricity
        
        self.machinery = machinery
        self.tractor = tractor
        self.pump = pump
        self.datetime = datetime
        
    def __str__(self):
        return (str(self.__dict__))

#################################  Expense Object  END  #########################


#################################  INCOME Object  START  #########################

class Income(object):
    
    ID = 0
    Farmer_ID = 0
    
    # Rent
    Rent = False
    
    Warehouse = 0
    Land = 0
    Tractor = 0
    Pump = 0
    Labour = 0
    
    # Sell
    Sell = False
    
    # Cotton
    Cotton = 0
    
    Rate  = 0
    Quantity = 0
    Amount = 0
    
    
    # Cottonseed
    Cottonseed = False
    
    Rate  = 0
    Quantity = 0
    Amount = 0
    
    DateTime = 0
    
    
    
    def __init__(self, ID ,farmerID, rent, warehouse, land, tractor, pump, labour, sell, cotton, cottonrate, cottonquantity, cottonamount, cottonseed, cottonseedrate, cottonseedquantity, cottonseedamount, datetime):
        
        self.ID = ID
        self.farmerID = farmerID
        
        self.rent = rent
        
        self.warehouse = warehouse
        self.land = land
        self.tractor = tractor
        self.pump = pump
        self.labour = labour
        
        self.sell = sell
        
        self.cotton = cotton
        self.cottonrate  = cottonrate
        self.cottonquantity = cottonquantity
        self.cottonamount = cottonamount
        
        self.cottonseed = cottonseed
        
        self.cottonseedrate  = cottonseedrate
        self.cottonseedquantity = cottonseedquantity
        self.cottonseedamount = cottonseedamount
        
        self.datetime = str(datetime)
                
        
    def __str__(self):
        return (str(self.__dict__))

#################################  INCOME OBJECT END  #########################



#################################  INCOME Object CREATION Function START  #########################


def Create_Income_Object(list_Income_Object):
    ID  = list_Income_Object[0]
    farmerID = list_Income_Object[1]
    rent = list_Income_Object[2]
    warehouse = list_Income_Object[3]
    land = list_Income_Object[4]
    tractor = list_Income_Object[5]
    pump = list_Income_Object[6]
    labour = list_Income_Object[7]
    sell = list_Income_Object[8]
    cotton = list_Income_Object[9]
    cottonrate = list_Income_Object[10]
    cottonquantity = list_Income_Object[11]
    cottonamount = list_Income_Object[12]
    cottonseed = list_Income_Object[13]
    cottonseedrate = list_Income_Object[14]
    cottonseedquantity = list_Income_Object[15]
    cottonseedamount = list_Income_Object[16]
    datetime = str(list_Income_Object[17])
    
    new_Income_Object = Income(ID ,farmerID, rent, warehouse, land, tractor, pump, labour, sell, cotton, cottonrate, cottonquantity, cottonamount, cottonseed, cottonseedrate, cottonseedquantity, cottonseedamount, datetime)
    
    return new_Income_Object

#################################  INCOME Object CREATION Function END  #########################



#################################  EXPENSE Object Create Function START  #########################


def Create_Expense_Object(list_Expense_Object):
    ID = list_Expense_Object[0]
    farmerID  = list_Expense_Object[1]
    labour = list_Expense_Object[2]
    male = list_Expense_Object[3]
    female = list_Expense_Object[4]
    job = list_Expense_Object[5]
    ploughing = list_Expense_Object[6]
    planting = list_Expense_Object[7]
    weeding = list_Expense_Object[8]
    material = list_Expense_Object[9]
    fertilizers = list_Expense_Object[10]
    seeds = list_Expense_Object[11]
    saplings = list_Expense_Object[12]
    pesticides = list_Expense_Object[13]
    utility = list_Expense_Object[14]
    water = list_Expense_Object[15]
    electricity = list_Expense_Object[16]
    machinery = list_Expense_Object[17]
    tractor = list_Expense_Object[18]
    pump = list_Expense_Object[19]
    datetime = list_Expense_Object[20]

    
    new_Expense_Object = Expense(ID ,farmerID, warehouse, land, tractor, pump, labour, sell, cotton, cottonrate, cottonquantity, cottonamount, cottonseed, cottonseedrate, cottonseedquantity, cottonseedamount, datetime)

    return new_Expense_Object


#################################  EXPENSE Object Create Function END  #########################



#################################  To Write List Object to CSV START  #########################


def Write_List_In_File(CSV_File_Path, List_To_Write):

    with open(CSV_File_Path, 'a',newline='') as myfile:
        wr = csv.writer(myfile)
        for list_Object in List_To_Write:
            dict_income_Object = ast.literal_eval(str(list_Object))
            list_Object_Value = []
            for key in dict_income_Object:
                list_Object_Value.append((dict_income_Object[key]))
            wr.writerow(list_Object_Value)



#################################  Get Farmers INCOME data via FARMER_ID #########################


def Get_Farmers_Income(Farmer_ID):
    list_Income_Object = []
    with open(Income_File_Path, 'r',newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if (Farmer_ID == ''):
                income_Object = Create_Income_Object(row)
                list_Income_Object.append(income_Object)
            if (row[1] == Farmer_ID):
                income_Object = Create_Income_Object(row)
                list_Income_Object.append(income_Object)

    json_Income_Object = json.dumps(list_Expense_Object, default=lambda o: o.__dict__)
    
    return list_Income_Object


#################################  ADD Farmers INCOME data #########################


def Add_Income_Data(string_Json_Data):
    global Income_File_Path
    json_Object = json.loads(string_Json_Data)
    list_Income_Object = []
    
    for key in json_Object:
        if (key == 'ID'):
            list_Income_Object.append( Get_Unique_ID())
        elif (key == 'datetime'):
            list_Income_Object.append(str(datetime.datetime.now()))
            s=1
        else:
            list_Income_Object.append(json_Object[key])
    
    print (list_Income_Object)
            
    income_Object = Create_Income_Object(list_Income_Object)
    
    list_Income_Object = []
    list_Income_Object.append(income_Object)
    print (type(income_Object))
    
    Write_List_In_File(Income_File_Path , list_Income_Object)

    return True



#################################  Get Farmers EXPENSE data via FARMER_ID #########################


def Get_Farmers_Expense(Farmer_ID):
    list_Expense_Object = []
    global Expense_File_Path
    with open(Expense_File_Path, 'r',newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if (Farmer_ID == ''):
                expense_Object = Create_Expense_Object(row)
                list_Expense_Object.append(expense_Object)
            if (row[1] == Farmer_ID):
                expense_Object = Create_Expense_Object(row)
                list_Expense_Object.append(expense_Object)
                
    json_Expense_Object = json.dumps(list_Expense_Object, default=lambda o: o.__dict__)
    
    return json_Expense_Object


#################################  Add Farmers EXPENSE data #########################


def Add_Expense_Data(string_Json_Data):
    global Expense_File_Path
    json_Object = json.loads(string_Json_Data)
    list_Expense_Object = []
    
    for key in json_Object:
        if (key == 'ID'):
            list_Expense_Object.append( Get_Unique_ID())
        elif (key == 'datetime'):
            list_Expense_Object.append(str(datetime.datetime.now()))
        else:
            list_Expense_Object.append(json_Object[key])
    
    #print (list_Income_Object)
            
    expense_Object = Create_Expense_Object(list_Expense_Object)
    
    list_Expense_Object = []
    list_Expense_Object.append(expense_Object)
    #print (type(income_Object))
    
    Write_List_In_File(Expense_File_Path , list_Expense_Object)

    return True;











