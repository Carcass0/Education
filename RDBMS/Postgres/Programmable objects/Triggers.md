A PostgreSQL trigger is a function invoked automatically whenever an event associated with a table occurs. An event could be any of the following: INSERT, UPDATE, DELETE or TRUNCATE.

A trigger is a special user-defined function associated with a table. To create a new trigger, you define a trigger function first, and then bind this trigger function to a table.

The difference between a trigger and a user-defined function is that a trigger is automatically invoked when a triggering event occurs.

## PostgreSQL trigger types

PostgreSQL provides two main types of triggers:

- Row-level triggers
- Statement-level triggers.

The differences between the two kinds are how many times the trigger is invoked and at what time.

For example, if you issue an `UPDATE` statement that modifies 20 rows, the row-level trigger will be invoked 20 times, while the statement-level trigger will be invoked 1 time.

You can specify whether the trigger is invoked before or after an event. If the trigger is invoked before an event, it can skip the operation for the current row or even change the row being updated or inserted. In case the trigger is invoked after the event, all changes are available to the trigger.

## When to use triggers

Triggers are useful in case the database is accessed by various applications, and you want to keep the cross-functionality within the database that runs automatically whenever the data of the table is modified. For example, if you want to keep the history of data without requiring the application to have logic to check for every event such as `INSERT` or `UDPATE`.

Also, you can use triggers to maintain complex data integrity rules which cannot implement elsewhere except at the database level. For example, when a new row is added into the `customer` table, other rows must be also created in tables of banks and credits.

The main drawback of using a trigger is that you must know the trigger exists and understand its logic to figure out the effects when data changes.

## PostgreSQL triggers vs SQL standard triggers

Even though PostgreSQL implements SQL standard, triggers in PostgreSQL has some specific features:

- PostgreSQL fires trigger for the TRUNCATE event.
- PostgreSQL allows you to define the statement-level trigger on views.
- PostgreSQL requires you to define a user-defined function as the action of the trigger, while the SQL standard allows you to use any SQL commands.

To create a new trigger in PostgreSQL, you follow these steps:

- First, create a trigger function using CREATE FUNCTION statement.
- Second, bind the trigger function to a table by using `CREATE TRIGGER` statement.

## Create trigger function syntax

A trigger function is similar to a regular [user-defined function](https://www.postgresqltutorial.com/postgresql-plpgsql/postgresql-create-function/). However, a trigger function does not take any arguments and has a return value with the type `trigger`.

The following illustrates the syntax of creating a trigger function:

```SQL
CREATE FUNCTION trigger_function()
RETURNS TRIGGER
LANGUAGE PLPGSQL AS $$ 
BEGIN    
-- trigger logic 
END; 
$$
```
Notice that you can create a trigger function using any language supported by PostgreSQL.
A trigger function receives data about its calling environment through a special structure called `TriggerData` which contains a set of local variables.
For example, `OLD` and `NEW` represent the states of the row in the table before or after the triggering event.

PostgreSQL also provides other local variables preceded by `TG_` such as `TG_WHEN`, and `TG_TABLE_NAME`.

After creating a trigger function, you can bind it to one or more trigger events such as INSERT, UPDATE, and DELETE.

## Creating a trigger
The `CREATE TRIGGER` statement allows you to create a new trigger.

The following illustrates the basic syntax of the `CREATE TRIGGER` statement:

```SQL
CREATE TRIGGER trigger_name     
{BEFORE | AFTER} { event }
ON table_name
[FOR [EACH] { ROW | STATEMENT }]
EXECUTE PROCEDURE trigger_function
```

In this syntax:

First, provide the name of the trigger after the `TRIGGER` keywords.

Second, indicate the timing that causes the trigger to fire. It can be `BEFORE` or `AFTER` an event occurs.

Third, specify the event that invokes the trigger. The event can be `INSERT` , `DELETE`, `UPDATE` or `TRUNCATE`.

Fourth, specify the name of the table associated with the trigger after the `ON` keyword.

Fifth, define the type of triggers, which can be:

- The row-level trigger that is specified by the `FOR EACH ROW` clause.
- The statement-level trigger that is specified by the `FOR EACH STATEMENT` clause.

A row-level trigger is fired for each row while a statement-level trigger is fired for each transaction.

Suppose a table has 100 rows and two triggers that will be fired when a `DELETE` event occurs.

If the `DELETE` statement deletes 100 rows, the row-level trigger will fire 100 times, once for each deleted row. On the other hand, a statement-level trigger will be fired for one time regardless of how many rows are deleted.

Finally, give the name of the trigger function after the `EXECUTE PROCEDURE`keywords.

Example:
Trigger function:
```SQL
CREATE OR REPLACE FUNCTION log_last_name_changes()
RETURNS TRIGGER 
LANGUAGE PLPGSQL 
AS 
$$ 
BEGIN 
IF NEW.last_name <> OLD.last_name THEN
INSERT INTO employee_audits(employee_id,last_name,changed_on) VALUES(OLD.id,OLD.last_name,now());
END IF;
RETURN NEW;
END; 
$$
```

Trigger:
```SQL
CREATE TRIGGER last_name_changes
BEFORE UPDATE
ON employees
FOR EACH ROW 
EXECUTE PROCEDURE log_last_name_changes();
```