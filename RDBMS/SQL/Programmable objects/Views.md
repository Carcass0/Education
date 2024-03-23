View = basically named stored query

After creating a view, you can query data from it as you would from a regular table. Behind the scenes, the DB will rewrite the query against the view and its defining query, executing it to retrieve data from the base tables.

Views do not store data except the materialized views.  Materialized views store data physically and periodically refresh it from the base tables.

The materialized views are handy in various scenarios, providing faster data access to a remote server and serving as an effective caching mechanism.
## Advantages of SQL views

Views offer many advantages:

### 1) Simplifying complex queries

Views help simplify complex queries. Instead of dealing with joins, aggregations, or filtering conditions, you can query from views as if they were regular tables.

Typically, first, you create views based on complex queries and store them in the database. Then, you can use simple queries based on views instead of using complex queries.

### 2) Security and access control

Views enable fine-grained control over data access. You can create views that expose subsets of data in the base tables, hiding sensitive information.

This is particularly useful when you have applications that require access to distinct portions of the data.

### 3) Logical data independence

If your applications use views, you can freely modify the structure of the base tables. In other words, views enable you to create a layer of abstraction over the underlying tables.

```SQL
CREATE VIEW view_name AS query;
```

\\d+ can be used to view information on a view, including columns and types, and the view definition.
\\dv to display all views in db

```SQL
DROP VIEW [IF EXISTS] view_name 
[CASCADE | RESTRICT];
```

Use `CASCADE` option to remove dependent objects along with the view or the `RESTRICT` option to reject the removal of the view if other objects depend on the view. The `RESTRICT` option is the default.


A view can be updatable if it meets certain conditions. This means that you can insert, update, or delete data from the underlying tables via the view.

A view is updatable when it meets the following conditions:

First, the defining query of the view must have exactly one entry in the `FROM` clause, which can be a table or another updatable view.

Second, the defining query must not contain one of the following clauses at the top level:

- GROUP BY
- HAVING
- LIMIT
- OFFSET FETCH
- DISTINCT
- WITH
- UNION
- INTERSECT
- EXCEPT

Third, the selection list of the defining query must not contain any:

- Window functions
- Set-returning function
- Aggregate functions

An updatable view may contain both updatable and non-updatable columns. If you attempt to modify a non-updatable column, SQL will raise an error.

When you execute a modification statement such as INSERT, UPDATE, or DELETE to an updatable view, PostgreSQL will convert this statement into the corresponding statement of the underlying table.

If you have a `WHERE` condition in the defining query of a view, you still can update or delete the rows that are not visible through the view. However, if you want to avoid this, you can use the `WITH CHECK OPTION` to define the view.


 A recursive view is a view whose defining query references the view name itself.
 
 A recursive view can be useful in performing hierarchical or recursive queries on hierarchical data structures stored in the database.

The `CREATE RECURSIVE VIEW` statement is syntax sugar for a standard recursive query.

The `CREATE RECURSIVE VIEW` statement is equivalent to the following statement:

```SQL
CREATE VIEW view_name
AS
WITH RECURSIVE cte_name (columns) AS (
SELECT ...)   
SELECT columns FROM cte_name;
```