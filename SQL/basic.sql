/*database creation*/
CREATE DATABASE basics;
USE basics;

/*drop the table if it already exits in the database*/
DROP TABLE EmployeeDemographics;

DROP TABLE  EmployeeSalary;

/*table creation*/
CREATE TABLE EmployeeDemographics (EmployeeID INT,FirstName VARCHAR(50),LastName VARCHAR(50),Age INT,Gender VARCHAR(50));

CREATE TABLE EmployeeSalary(EmployeeID INT,JobTitle VARCHAR(50),Salary INT)


/*insert values into the tables*/
INSERT INTO EmployeeDemographics (EmployeeID,FirstName,LastName,Age,Gender) VALUES
(1001,'Jim','Halpert',30,'Male'),
(1002,'Pam','Beasly',30,'Female'),
(1003,'Dwight','Schrute',29,'Male'),
(1004,'Anglea','Martin',31,'Female'),
(1005,'Toby','Flenderson',32,'Male'),
(1006,'Michael','Scott',35,'Male'),
(1007,'Meredith','Palmer',32,'Female'),
(1008,'Stanley','Hudson',38,'Male'),
(1009,'Kevin','Malone',31,'Male');

SELECT * FROM EmployeeDemographics;

INSERT INTO EmployeeSalary(EmployeeID,JobTitle,Salary) VALUES
(1001,'Salesman',45000),
(1002,'Receptionist',36000),
(1003,'Salesman',63000),
(1004,'Accountant',47000),
(1005,'HR',50000),
(1006,'Regional Manager',65000),
(1007,'Supplier Relations',41000),
(1008,'Salesman',48000),
(1009,'Accountant',42000);

SELECT * FROM EmployeeSalary;

/*view only the first 5 rows*/
/*top->SQL Server, limit->MYSQL*/
SELECT *  FROM EmployeeDemographics LIMIT 5;


/*selecting only 5 rows from top skipping the first 2 rows*/
SELECT *  FROM EmployeeDemographics LIMIT 5 OFFSET 2;

/*display unique values*/
SELECT DISTINCT(EmployeeID) FROM EmployeeDemographics;

SELECT DISTINCT(Gender) FROM EmployeeDemographics;

SELECT COUNT(LastName) AS LastNameCount FROM EmployeeDemographics;

SELECT MAX(Salary),MIN(salary),AVG(salary) FROM EmployeeSalary;

SELECT * FROM EmployeeDemographics WHERE FirstName='Jim';

SELECT * FROM EmployeeDemographics WHERE FirstName<>'Jim';

SELECT * FROM EmployeeDemographics WHERE Age<=32;

SELECT * FROM EmployeeDemographics WHERE Age<=32 AND Gender='Female';

SELECT * FROM EmployeeDemographics WHERE Age<=32 OR Gender='Female';

SELECT * FROM EmployeeDemographics WHERE FirstName LIKE "M%";

SELECT * FROM EmployeeDemographics WHERE FirstName LIKE "M%h%";
 
SELECT * FROM EmployeeDemographics WHERE FirstName LIKE "M%h%l";

SELECT * FROM EmployeeDemographics WHERE FirstName IS NOT NULL ;

SELECT * FROM EmployeeDemographics WHERE FirstName IS NULL ;

SELECT * FROM EmployeeDemographics WHERE FirstName IN ("Jim","Michael");


/*distinct->returns the very first occurence the particular things*/
SELECT DISTINCT(Gender) FROM EmployeeDemographics ;

/*group by->return all the distinct values rolled up*/
SELECT Gender,COUNT(Gender) FROM EmployeeDemographics GROUP BY gender;

SELECT Gender,Age,COUNT(Gender) FROM EmployeeDemographics GROUP BY gender,age;


/*below query return in ascending order of age and gender , first it checks for age arrange in ascending order */

/* if two rows have same age then order by gender*/
SELECT * FROM EmployeeDemographics ORDER BY age, gender;

/* if two rows have same age then order by gender in descending*/
SELECT * FROM EmployeeDemographics ORDER BY age, gender DESC;

/*both age and gender in descending*/
SELECT * FROM EmployeeDemographics ORDER BY age DESC, gender DESC;

/*EmployeeId->1*/
/*FirstName->2*/
/*LastName->3*/
/*Age->4*/
/*Gender->5*/
SELECT * FROM EmployeeDemographics ORDER BY 4 DESC, 5 DESC;

