import pyodbc
import pandas as pd
import json
import csv
import pandas
import ast
import datetime
import os


connection = 0;
cursor = 0;
sql_Query = ''


def Set_Connection():
    global connection
    global cursor
    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=IN-MH1LPW101089;"
                      "Database=FarmerDB;"
                      "Trusted_Connection=yes;")
    cursor = connection.cursor()



class Farmer():
    FarmerID = 0;
    FarmerName = 0;
    MobileNumber = ''
    
    def __str__(self):
        return (str(self.__dict__))


class ExpenseLabour():
    Id = 0;
    FarmerID = 0;
    Male = 0;
    Female = 0;
    Ploughing = 0;
    Planting = 0;
    Weeding = 0;
    Harvesting = 0;
    
    def __init__(self, ID, FarmerID ,Male, Female, Ploughing, Planting, Weeding, Harvesting):
        self.Id = ID;
        self.FarmerID = FarmerID
        self.Male = Male
        self.Female = Female
        self.Ploughing = Ploughing
        self.Planting = Planting
        self.Weeding = Weeding
        self.Harvesting = Harvesting
    
    def __str__(self):
        return (str(self.__dict__))




class ExpenseMaterial():
    Id = 0;
    FarmerID = 0;
    Fertilizers = 0;
    Seeds = 0;
    Saplings = 0;
    Pesticides = 0;
    
    def __init__(self, ID, FarmerID ,Fertilizers, Seeds, Saplings, Pesticides):
        self.Id = ID;
        self.FarmerID = FarmerID
        self.Fertilizers = Fertilizers
        self.Seeds = Seeds 
        self.Saplings = Saplings
        self.Pesticides = Pesticides 
    
    def __str__(self):
        return (str(self.__dict__))


class ExpenseMachinery():
    Id = 0;
    FarmerID = '';
    Tractor = 0;
    Pump = 0;
    
    def __init__(self, ID ,FarmerID, Tractor, Pump):
        self.Id = ID;
        self.FarmerID = FarmerID
        self.Tractor = Tractor
        self.Pump = Pump  
    
    def __str__(self):
        return (str(self.__dict__))


class IncomeRent():
    Id = 0;
    FarmerID = 0;
    Warehouse = 0;
    Land = 0;
    Tractor = 0;
    Pump = 0;
    Labour = 0;
    
    def __init__(self, ID, FarmerID, Warehouse, Land, Tractor, Pump, Labour):
        self.Id = ID;
        self.FarmerID = FarmerID
        self.Warehouse = Warehouse
        self.Land = Land 
        self.Tractor = Tractor
        self.Pump = Pump
        self.Labour = Labour
    
    def __str__(self):
        return (str(self.__dict__))


class IncomeSell:
    Id = 0;
    FarmerID = 0;
    Type = 0;
    Rate = 0;
    Quantity = 0;
    Amount = 0;
    
    def __init__(self,ID, FarmerID, Type, Rate, Quantity, Amount):
        self.Id = ID;
        self.FarmerID = FarmerID
        self.Type = Type
        self.Rate = Rate 
        self.Quantity = Quantity
        self.Amount = Amount
    
    def __str__(self):
        return (str(self.__dict__))



#############################################



def Run_Insert_Query(sql_Query):
    global cursor
    global connection
    
    #Set_Connection();
    cursor.execute(sql_Query);
    connection.commit()
    #cursor.close();
    #connection.close();



###########################################    API    #########################




def AddExpenseUtility(json_String):
    
    json_Object = json.loads(json_String)
    
    sql_Query = "insert into ExpenseUtility (FarmerID, Water, Electricity)  values (%d,%d,%d); " % (json_Object["FarmerID"],json_Object["Water"],json_Object["Electricity"]);
    Run_Insert_Query(sql_Query);



def AddExpenseMachinery(json_String):
    
    json_Object = json.loads(json_String)
    
    sql_Query = "insert into ExpenseMachinery (FarmerID, Tractor, Pump)  values (%d,%d,%d); " % (json_Object["FarmerID"],json_Object["Tractor"],json_Object["Pump"]);
    Run_Insert_Query(sql_Query);



def AddExpenseLabour(json_String):
    
    json_Object = json.loads(json_String)
    
    sql_Query = "insert into ExpenseLabour (FarmerID, Male, Female, Ploughing, Planting, Weeding, Harvesting)  values (%d,%d,%d,%d,%d,%d,%d); " % (json_Object["FarmerID"],json_Object["Male"],json_Object["Female"],json_Object["Ploughing"],json_Object["Planting"],json_Object["Weeding"],json_Object["Harvesting"]);
    Run_Insert_Query(sql_Query);




def AddExpenseMaterial(json_String):
    
    json_Object = json.loads(json_String)
    
    sql_Query = "insert into ExpenseMaterial (FarmerID ,Fertilizers, Seeds, Saplings, Pesticides)  values (%d,%d,%d,%d,%d); " % (json_Object["FarmerID"],json_Object["Fertilizers"],json_Object["Seeds"],json_Object["Saplings"],json_Object["Pesticides"]);
    Run_Insert_Query(sql_Query);




def AddIncomeRent(json_String):

    json_Object = json.loads(json_String)
    
    sql_Query = "insert into IncomeRent (FarmerID, Warehouse, Land, Tractor, Pump, Labour)  values (%d,%d,%d,%d,%d,%d); " % (json_Object["FarmerID"],json_Object["Warehouse"],json_Object["Land"],json_Object["Tractor"],json_Object["Pump"],json_Object["Labour"]);
    Run_Insert_Query(sql_Query);



def AddIncomeSell(json_String):
    
    json_Object = json.loads(json_String)
    
    sql_Query = "insert into IncomeSell (FarmerID, Type, Rate, Quantity, Amount)  values (%d,%s,%d,%d,%d); " % (json_Object["FarmerID"], str("'" + json_Object["Type"] + "'") ,json_Object["Rate"],json_Object["Quantity"],json_Object["Amount"]);
    Run_Insert_Query(sql_Query);













    
