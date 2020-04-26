Are you finding yourself writing long strings to build up a SQL query in python
to communicate with your SQL database? Then **sql_query** is what you are looking for.
This package provides you with tools to build simple SQL queries from the ground up,
without having to type everything out over and over again. 
With this module, you'll no longer need codeblocks like this to write your queries :

```python
field = 'x'
table = 'a'
cond = 10

query = 'SELECT {} FROM {} WHERE {} = {}'.format(field, table, field, cond)
```

The **sql_query** equivalent of the above looks like this:

```python
from sql_query import sql_select

query = sql_select('x', 'a')
query.where(attr='x', cond=10)
```

A simple *SELECT-FROM-WHERE* example has been demonstrated above with the **sql_select** object.
This object also supports *GROUP BY*, *HAVING*, *ORDER BY*, *LIMIT* and *JOIN* statements.
There is also the **sql_update** object, which supports *UPDATE*, *SET* and *WHERE* statements.
Review the documentation to get a better understanding of how to implement these statements.

Convert a **sql_query** (sub)object to a string using the build-in str() function to get your 
SQL query as text. The result can be used directly in for example pandas' *pd.read_sql_query()*
or sqlalchemy's *engine.execute(text())* methods.