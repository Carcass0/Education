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

An updatable view may contain both updatable and non-updatable columns. If you attempt to modify a non-updatable column, PostgreSQL will raise an error.

When you execute a modification statement such as INSERT, UPDATE, or DELETE to an updatable view, PostgreSQL will convert this statement into the corresponding statement of the underlying table.

If you have a `WHERE` condition in the defining query of a view, you still can update or delete the rows that are not visible through the view. However, if you want to avoid this, you can use the `WITH CHECK OPTION` to define the view.



When you create a view `WITH CHECK OPTION`, PostgreSQL will ensure that you can only modify data of the view that satisfies the condition in the view’s defining query.

In PostgreSQL, you can specify a scope of check:

- `LOCAL`
- `CASCADED`

The `LOCAL` scope restricts the check option enforcement to the current view only. It does not enforce the check to the views that the current view is based on.


PostgreSQL extends the view concept to the next level which allows views to store data physically. These views are called **materialized views**.

Materialized views cache the result set of an expensive query and allow you to refresh data periodically.

```SQL
CREATE MATERIALIZED VIEW [IF NOT EXISTS] view_name
AS
query
WITH [NO] DATA;
```

- First, specify the `view_name` after the `CREATE MATERIALIZED VIEW` clause
- Second, add the query that retrieves data from the underlying tables after the `AS` keyword.
- Third, if you want to load data into the materialized view at the creation time, use the `WITH DATA` option; otherwise, you use `WITH NO DATA` option. If you use the `WITH NO DATA` option, the view is flagged as unreadable. It means that you cannot query data from the view until you load data into it.
- Finally, use the IF NOT EXISTS option to conditionally create a view only if it does not exist.

To load data into a materialized view, you use the  `REFRESH MATERIALIZED VIEW` statement

When you refresh data for a materialized view, PostgreSQL locks the underlying tables. Consequently, you will not be able to retrieve data from underlying tables while data is loading into the view.

To avoid this, you can use the `CONCURRENTLY` option.

With the `CONCURRENTLY` option, PostgreSQL creates a temporary updated version of the materialized view, compares two versions, and performs INSERT and UPDATE only the differences.

PostgreSQL allows you to retrieve data from a materialized view while it is being updated. One requirement for using `CONCURRENTLY` option is that the materialized view must have a `UNIQUE` index.


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


\\dv to display all views in db