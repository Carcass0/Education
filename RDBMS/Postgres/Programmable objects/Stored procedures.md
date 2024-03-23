```SQL
CREATE [ OR REPLACE ] PROCEDURE
    _`name`_ ( [ [ _`argmode`_ ] [ _`argname`_ ] _`argtype`_ [ { DEFAULT | = } _`default_expr`_ ] [, ...] ] )
  { LANGUAGE _`lang_name`_
    | TRANSFORM { FOR TYPE _`type_name`_ } [, ... ]
    | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
    | SET _`configuration_parameter`_ { TO _`value`_ | = _`value`_ | FROM CURRENT }
    | AS '_`definition`_'
    | AS '_`obj_file`_', '_`link_symbol`_'
    | _`sql_body`_
  } ...
```

To define a new stored procedure, you use the `create procedure` statement with the following syntax:

```SQL
create [or replace] procedure procedure_name(parameter_list)
language plpgsql
as $$ declare
-- variable declaration
begin
-- stored procedure body
end; $$
```

In this syntax:

- First, specify the name of the stored procedure after the `create procedure` keywords.
- Second, define parameters for the stored procedure. A stored procedure can accept zero or more parameters.
- Third, specify `plpgsql` as the procedural language for the stored procedure. Note that you can use other procedural languages for the stored procedure such as SQL, C, etc.
- Finally, use the dollar-quoted string constant syntax to define the body of the stored procedure.

Parameters in stored procedures can have the `in` and `inout` modes but cannot have the `out` mode.

A stored procedure does not return a value. You cannot use the `return` statement with a value inside a store procedure like this:

```SQL
return expression;
```

However, you can use the `return` statement without the `expression` to stop the stored procedure immediately:

```SQL
return;
```

If you want to return a value from a stored procedure, you can use parameters with the `inout` mode.

Examples:
```SQL
create or replace procedure transfer(
   sender int,
   receiver int, 
   amount dec
)
language plpgsql    
as $$
begin
    -- subtracting the amount from the sender's account 
    update accounts 
    set balance = balance - amount 
    where id = sender;

    -- adding the amount to the receiver's account
    update accounts 
    set balance = balance + amount 
    where id = receiver;

    commit;
end;$$;
```

## Inserting data using a procedure
```SQL
CREATE OR REPLACE PROCEDURE genre_insert_data("GenreId" integer, "Name" character varying) 
LANGUAGE SQL
AS $$ 
INSERT INTO public."Genre" VALUES ("GenreId", "Name"); 
$$; 
```

## Displaying a message on the screen
```SQL
CREATE OR REPLACE PROCEDURE display_message (INOUT msg TEXT) 
AS $$
BEGIN 
RAISE NOTICE 'Procedure Parameter: %', msg ;
END ; 
$$ 
LANGUAGE plpgsql ;
```

## Using transaction control
```SQL
CREATE OR REPLACE PROCEDURE control_transaction()
LANGUAGE plpgsql 
AS $$ 
DECLARE
BEGIN    
CREATE TABLE test1 (id int);  
INSERT INTO test1 VALUES (1);   
COMMIT;   
CREATE TABLE test2 (id int);    
INSERT INTO test2 VALUES (1);   
ROLLBACK;  
END $$;
```

## Using column data types
```SQL
CREATE OR REPLACE PROCEDURE genre_id_max()
LANGUAGE plpgsql AS $$
DECLARE 
id "Genre"."GenreId"%type; 
BEGIN  
select max("GenreId") into id from public."Genre";
RAISE NOTICE 'Maximum of GenreId is : %', id ;
END;
$$;
```

## Raising notices, warnings, and INFO messages
```SQL
CREATE OR REPLACE PROCEDURE raise_warning() AS $$ 
DECLARE
warn INT := 10; 
BEGIN 
RAISE NOTICE 'value of warn : % at %: ', warn, now(); 
warn := warn + 10; 
RAISE WARNING 'value of warn : % at %: ', warn, now(); 
warn := warn + 10; 
RAISE INFO 'value of warn : % at %: ', warn, now(); 
END;
$$ 
LANGUAGE plpgsql;
```

## Raising exceptions
```SQL
CREATE OR REPLACE PROCEDURE genre_id_exception() LANGUAGE plpgsql AS $$
DECLARE
id "Genre"."GenreId"%type;
BEGIN
select max("GenreId") into id from public."Genre";
RAISE EXCEPTION 'Maximum of GenreId is : %', id  USING HINT = 'Test For Raising exception.';
END;
$$ ;
```

## Traversing values in a table using a FOR loop
```SQL
CREATE OR REPLACE PROCEDURE genre_traverse() LANGUAGE plpgsql AS $$
DECLARE
genre_rec record;
BEGIN
for genre_rec in (select "GenreId","Name" from public."Genre" order by "GenreId")
loop
RAISE NOTICE 'Genre Id is : % , Name is : %', genre_rec."GenreId",genre_rec."Name";
end loop;
END;
$$ ;
```

## Using SECURITY INVOKER
SECURITY INVOKER indicates that the procedure is to be executed with the privileges of the user that calls it. That is the default.
```SQL
CREATE OR REPLACE PROCEDURE genre_traverse() LANGUAGE plpgsql SECURITY INVOKER
AS $$
DECLARE
genre_rec record;
BEGIN
for genre_rec in (select "GenreId","Name" from public."Genre" order by "GenreId")
loop
RAISE NOTICE 'Genre Id is : % , Name is : %', genre_rec."GenreId",genre_rec."Name";
end loop;
END;
$$;
```

## Using SECURITY DEFINER
SECURITY DEFINER specifies that the procedure is to be executed with the privileges of the user that owns it. A SECURITY DEFINER procedure cannot execute transaction control statements (for example, COMMIT and ROLLBACK, depending on the language).
```SQL
CREATE OR REPLACE PROCEDURE genre_traverse() LANGUAGE plpgsql SECURITY DEFINER
AS $$
DECLARE
genre_rec record;
BEGIN
for genre_rec in (select "GenreId","Name" from public."Genre" order by "GenreId")
loop
RAISE NOTICE 'Genre Id is : % , Name is : %', genre_rec."GenreId", genre_rec."Name";
end loop;
END;
$$;
```

## Setting configuration parameters
The effects of a SET LOCAL command for a variable are restricted to the procedure inside which the command is executed; the configuration parameter's prior value is restored after exiting the procedure. However, a simple SET command (without LOCAL) overrides the SET clause, much as it would do for a previous SET LOCAL command. The effects of the configuration will persist after procedure exit, unless the current transaction is rolled back.
```SQL
CREATE OR REPLACE PROCEDURE datestyle_change() LANGUAGE plpgsql SET datestyle TO postgres, dmy
AS $$
BEGIN
RAISE NOTICE 'Current Date is : % ', now();
END;
$$;
```

