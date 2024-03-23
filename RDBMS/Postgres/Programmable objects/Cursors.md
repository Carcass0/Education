In PostgreSQL, a cursor is a database object that allows you to traverse the result set of a query one row at a time.
![[PLPGSQL Cursor.png]]
1. First, declare a cursor.
2. Next, open the cursor.
3. Then, fetch rows from the result set into a record or a variable list.
4. After that, process the fetched row and exit the loop if no more row to fetch.
5. Finally, close the cursor.

### Step 1. Declaring a cursor

To declare a cursor, you use the `DECLARE` statement. Here’s the syntax for declaring a cursor:

`DECLARE cursor_name CURSOR FOR query;`
### Step 2. Opening the cursor

After declaring a cursor, you need to open it using the `OPEN` statement:

`OPEN cursor_name;`
### Step 3. Fetching rows from the cursor

Once the cursor is open, you can fetch rows from it using the `FETCH` statement. PostgreSQL offers different ways to fetch rows:

- FETCH NEXT: fetches the next row from the cursor.
- FETCH PRIOR: fetches the previous row from the cursor.
- FETCH FIRST: fetches the first row from the cursor.
- FETCH LAST: fetches the last row from the cursor.
- FETCH ALL: fetches all rows from the cursor.
### Step 4. Processing rows

After fetching a row, you can process it. Typically, you use a LOOP statement to process rows fetched from the cursor:

```SQL
LOOP         
-- Fetch the next row     
FETCH NEXT FROM cursor_name INTO variable_list;      
-- exit if not found     
EXIT WHEN NOT FOUND;      
-- Process the fetched row     
...  
END LOOP;
```
### Step 5. Closing the cursor

Once you’re done fetching rows, you need to close the cursor. To do it, you use the `CLOSE` statement:

`CLOSE cursor_name`Code language: SQL (Structured Query Language) (sql)

The `CLOSE` statement releases resources or frees up the cursor variable to allow it to be opened again using `OPEN` statement.

```SQL
CREATE OR REPLACE FUNCTION fetch_film_titles_and_years(
OUT p_title VARCHAR(255), 
OUT p_release_year INTEGER 
) 
RETURNS SETOF RECORD AS 
$$ 
DECLARE 
film_cursor CURSOR FOR 
SELECT title, release_year 
FROM film;
film_record RECORD; 
BEGIN 
-- Open cursor 
OPEN film_cursor; 
-- Fetch rows and return 
LOOP
FETCH NEXT FROM film_cursor INTO film_record; 
EXIT WHEN NOT FOUND; 
p_title := film_record.title;
p_release_year := film_record.release_year;
RETURN NEXT; 
END LOOP; 
-- Close cursor 
CLOSE film_cursor; 
END; 
$$ 
LANGUAGE PLPGSQL;
```
Output:
```
p_title           | p_release_year -----------------------------+----------------  Chamber Italian             |           2006  Grosse Wonderful            |           2006  Airport Pollock             |           2006  Bright Encounters           |           2006 ...
```
