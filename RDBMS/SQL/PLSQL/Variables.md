Naming conventions:

| Prefix | Data type |
| ------ | --------- |
| v_     | VARCHAR2  |
| n_     | NUMBER    |
| t_     | TABLE     |
| r_     | ROW       |
| d_     | DATE      |
| b_     | BOOLEAN   |
Assignment is handled by the walrus operator :=

In order to declare a variable with the same type as the data in a column, do TABLENAME.COLUMNNAME%TYPE

%TYPE is called a variable anchor
