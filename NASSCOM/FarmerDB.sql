Create Database FarmerDB;

Use FarmerDB;

Create Table Farmer
(
FarmerID int IDENTITY(1,1) PRIMARY KEY,
FarmerName varchar(30),
MobileNumber varchar(10)
)

/*
insert into Farmer(FarmerName, MobileNumber) values ('Ravindra Shinde', '9820090436');
insert into Farmer(FarmerName, MobileNumber) values ('Kanchan Shinde', '9820090436');
insert into Farmer(FarmerName, MobileNumber) values ('Dipak Kathekar', '7703165238');
*/

select * from Farmer;

drop table ExpenseLabour
Create Table ExpenseLabour
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Male int ,
Female int,
Ploughing int,
Planting int,
Weeding int,
Harvesting int,
CurrentDateTime DateTime
)

Create Table ExpenseMaterial
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Fertilizers int,
Seeds int,
Saplings int,
Pesticides int
)

Create Table ExpenseUtility
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Water int,
Electricity int,
)

Create Table ExpenseMachinery
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Tractor int,
Pump int,
)

*/


select * from ExpenseMaterial;

insert into AddExpenseLabour (FarmerID, Male, Female, Ploughing, Planting, Weeding, Harvesting)  values (1,1000,3000,344,190,150,200); 












Create Table IncomeRent
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Warehouse int ,
Land int,
Tractor int,
Pump int,
Labour int
)

select * from IncomeRent;

Create Table IncomeSell
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Type varchar (30) ,
Rate  int,
Quantity int,
Amount int
)


select * from IncomeSell ;






create table Finance
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
IsExpense int ,
Type varchar(100),
SubType varchar(100),
JobType varchar(100),
Amount Decimal,
Comment varchar(100),
CurrentDate DateTime
);


select * from Finance where FarmerID 

insert into Finance (FarmerID, IsExpense, Type, SubType, JobType, Amount, Comment, CurrentDate)  
values (1,1,'Labour','Job','Harvesting',500,'For Farm Labour',CAST('2018-04-05 19:43:15' AS DATETIME)); 

create table Notification
(
Id int IDENTITY(1,1) PRIMARY KEY,
FarmerID int FOREIGN KEY REFERENCES Farmer(FarmerID),
Farmer_Mobile_Number varchar(10),
Resource_Type varchar(100),
Sub_Resource_Type varchar(100),
Job_Type varchar(100),
No_Of_Resources int,
Latitude Decimal,
Longitude Decimal,
Comment varchar(100),
Start_Date DateTime,
End_Date DateTime,
Published_Date DateTime,
);

drop table Notification;

select * from Notification where FarmerID = 1 ; 

insert into Notification (farmerID ,farmer_Mobile_Number, resource_Type, sub_Resource_Type, job_Type, no_Of_Resources, latitude, longitude, start_Date, end_Date, published_Date) 
values (1,'7703165238','Labour','Male','Harvesting',10,72,19,CAST('2018-04-07 15:07:51' AS DATETIME),CAST('2018-06-06 15:07:51' AS DATETIME),CAST('2018-04-07 15:07:51' AS DATETIME));


select Cast('4/17/2018' as datetime)

select * from Finance;

select 
            (select AVG(Amount) from Finance where FarmerID = 1 and Type = 'Labour' and IsExpense = 1 ) as 'Farmer_Labour_Average', 
            (select AVG(Amount) from Finance where FarmerID = 1 and Type = 'Material') as 'Farmer_Material_Average',
            (select AVG(Amount) from Finance where FarmerID = 1 and Type = 'Utilities') as 'Farmer_Utilities_Average',
            (select AVG(Amount) from Finance where Type = 'Labour') as 'Labour_Average',
            (select AVG(Amount) from Finance where Type = 'Material') as 'Material_Average',
            (select AVG(Amount) from Finance where Type = 'Utilities') as 'Utilities_Average';






