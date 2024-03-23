For user-defined functions, these syntaxes look as follows:
```SQL

CREATE FUNCTION [database_name.]function_name (parameters)
RETURNS data_type AS
BEGIN
    SQL statements
    RETURN value
END;
    
ALTER FUNCTION [database_name.]function_name (parameters)
RETURNS data_type AS
BEGIN
    SQL statements
    RETURN value
END;
    
DROP FUNCTION [database_name.]function_name;
```

Most things should be pretty obvious here. The function:

Takes parameters as input
Does something with these input values (SQL statements). Technically it will use values provided as parameters and combine them with other values (local variables) or database objects and then return the result of these combinations/calculations
Returns result of the calculation (RETURN value) with the previously defined type (RETURNS data_type)

Example of a function in postgresql:
```SQL
CREATE OR REPLACE FUNCTION get_employee_count_by_department(department_name TEXT)
RETURNS INT AS $$
DECLARE
    total_count INT;
BEGIN
    SELECT COUNT(*) INTO total_count
    FROM employees
    WHERE department = department_name;

    RETURN total_count;
END;
$$ LANGUAGE plpgsql;
```



