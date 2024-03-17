An SQL **stored procedure** is a group of pre-compiled SQL statements (prepared SQL code) that can be reused by simply calling it whenever needed.

The basic syntax to create an SQL stored procedure:
```SQL
DELIMITER //
CREATE PROCEDURE procedure_name(parameter1 datatype, parameter2 datatype, ...)
BEGIN 
-- SQL statements to be executed
END
DELIMITER ;
```

Procedures are executed by using the CALL keyword
Stored procedure parameter types:

| S.No. | Parameter & Description                                                                                                       |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1     | **Input parameters**<br><br>These parameters are used to pass values from the calling statement to the stored procedure.      |
| 2     | **Output parameters**<br><br>These parameters are used to return values from the stored procedure.                            |
| 3     | **Input/Output parameters**<br><br>These parameters allow a stored procedure to accept input values and return output values. |
Usage of an Out parameter:
```sql
DELIMITER //
CREATE PROCEDURE GetDetail(OUT total INT)
BEGIN 
SELECT COUNT(AGE) INTO total FROM CUSTOMERS WHERE AGE = 25;
END // 
DELIMITER;
```
Calling the procedure and getting the result:
```sql
CALL GetDetail(@total);
```
Using the result:
```SQL
SELECT @total;
```

To assign a value to a parameter, use the SET keyword

To verify weather the procedure is created:
```SQL
SHOW CREATE PROCEDURE GetDetails;
```

## Advantages of Stored Procedures

Following are the advantages of stored procedures −

- **Improved Performance:** Stored procedures are pre-compiled and stored on the server, so they can be executed more quickly than SQL statements that are sent from client applications.
    
- **Code Reuse:** Stored procedures can be called from different client applications, which means that the same code can be reused across different applications. This reduces development time and maintenance costs.
    
- **Reduced Network Traffic:** Because stored procedures are executed on the server, only the results are returned to the client, which reduces network traffic and improves application performance.
    
- **Better Security:** Stored procedures can be used to enforce security rules and prevent unauthorized access to sensitive data. They can also limit the actions that can be performed by users, making it easier to maintain data integrity and consistency.
    
- **Simplified Maintenance:** By storing SQL code in a single location, it becomes easier to maintain and update the code. This makes it easier to fix bugs, add new functionality, and optimize performance.
    

## Drawbacks of Stored Procedures

Following are the disadvantages of stored procedures −

- **Increased Overhead:** Stored procedures can consume more server resources than simple SQL statements, particularly when they are used frequently or for complex operations.
    
- **Limited Portability:** Stored procedures are often specific to a particular database management system (DBMS), which means they may not be easily portable to other DBMSs.
    
- **Debugging Challenges:** Debugging stored procedures can be more challenging than debugging simple SQL statements, particularly when there are multiple layers of code involved.
    
- **Security Risks:** If stored procedures are not written correctly, they can pose a security risk, particularly if they are used to access sensitive data or to perform actions that could compromise the integrity of the database.