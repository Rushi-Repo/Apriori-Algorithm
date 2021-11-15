# Apriori-Algorithm

CS 634 Data Mining 
Midterm Project
By: Rushikesh Kshirsagar 
UCID: rsk54
Implementation of the Apriori Algorithm.
The programming language used for the following project is Python.
Databases:
1.	The main_db.csv contains all the 30 items usually seen in Amazon, K-mart, or any other supermarkets.

 
2.	Database 1: 1.csv contains 20 transactions of the items in main_db.csv.

 

3.	Database 2: 2.csv contains 20 transactions of the items in main_db.csv.
 
4.	Database 3: 3.csv contains 20 transactions of the items in main_db.csv.
 
5.	Database 4: 4.csv contains 20 transactions of the items in main_db.csv.

 
6.	Database 5: 5.csv contains 20 transactions of the items in main_db.csv.
 
The databases directory is the same folder as apriori.py which contains code for the Apriori algorithm. 

Program Execution:
1.	The user is prompted to enter the path of the transactional database on which the algorithm is to be applied on.
2.	Once the user enters the path of the file, the program will then ask the user to add the minimum support and minimum confidence.
3.	After getting all the values from the user i.e., Transaction file path, minimum support & minimum confidence it will start processing the code to get the output.
4.	Once the code is executed it will give the associations rules, support, and confidence of all the transactions above the minimum support and minimum confidence provided by the user.
5.	It will also give the time taken by the program to execute itself at the end of the output.
Please find the screenshots of execution below (Tested the code on 2 cases below)


































CASE 1: I tested 1.csv, 2.csv, 3.csv, 4.csv and 5.csv with minimum support of 0.1 and minimum confidence of 0.1 for both the parts of the files.

Transaction 1:

Transactional Inputs:

 

Association Rules:

 


Transaction 2:

Transactional Inputs:

 

Association Rules:

 



Transaction 3:

Transactional Inputs:

 

Association Rules:

 



Transaction 4: 

Transactional Inputs:

 

Association Rules:

 



Transaction 5:

Transactional Inputs:

 

Association Rules:

 


CASE 2: I tested 1.csv, 2.csv,.csv, 4.csv and 5.csv with minimum support of 0.1 and minimum confidence of 0.5 for both the parts of the files.

Transaction 1: 

Transactional Inputs:

 

Association Rules:

 
Transaction 2:

Transactional Inputs:
 
 

Association Rules:

 





Transaction 3:

Transactional Inputs:

 

Association Rules:

 



Transaction 4:

Transactional Inputs:

 

Association Rules:

 



Transaction 5:

Transactional Inputs:
 
Association Rules:
 



Conclusion:
As displayed above, all the Apriori algorithm was tested in multiple conditions on all the 5 databases. The association rules and the time required to complete the task can be seen fluctuating. 
Algorithm	Transaction Databases	Minimum Support = 0.1 & Minimum Confidence = 0.1	Minimum Support = 0.1 & Minimum Confidence = 0.5	Minimum Support = 0.1 & Minimum Confidence = 0.8
APRIORI ALGORITHM	1.csv	0.0030	0.0018	0.0039
	2.csv	0.0039	0.0039	0.0038
	3.csv	7.7024	5.4695	6.3425
	4.csv	0.0196	0.0437	0.0162
	5.csv	0.0439	0.0356	0.0204
Summary Table
