Tryton - Data Warehouse
=======================

This module provides the foundation for other modules to build data
warehouse tables over it.

Key Features
------------

1. Date Dimension
`````````````````

The date dimension is almost always present in every data mart. For
example, every sale happens on a given date. While most attributes of a
date can be easily obtained with SQL functions (``to_month``, ``to_day``
etc.), data analysis often involves other information if it is a holiday,
the fiscal period the date belongs.

This module introduces a new model ``dw.date`` which stores a row per date
and company in the table. The additional columns introduced include if the
day is a ``holiday`` (yes/no), ``season_name`` (Christmas, Thanksgiving,
Easter, Valentines Day and everything else you could think of).

Benefits
........

For those designers wondering why an explicit date dimension table is
needed: If a business wishes to slice and dice data beyond the
non-standard date attributes, this seems to be the more effective model.
The idea is inspired by the book on Data Warehouse Toolkit by Ralph
Kimball. (Read Chapter two if you want to know more.)

Another side effect of having such a table is the ability to measure what
did not happen. Grouping by date would only show the result on what
happened on days when transactions existed, while a join on the date
dimension would cearly yield the dates during which no transaction occured
with an explicit value.
