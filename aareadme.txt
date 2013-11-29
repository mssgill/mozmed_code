-- Nov 21, 2013

---- Calling mySql from cmd line:

Have to use this version to be able to read from the infile:

  mysql --local-infile

see: http://dev.mysql.com/doc/refman/4.1/en/load-data-local.html


---- Once inside mySql

Execute script as so:

\. provider_data_loader.sql

Note that this code has varchar(10) for all the fields, which isn't
enough for some of them, but if i put in a varchar(100), i get an
error about it being too many columns or somesuch, and when i looked
this up, it appears there are actual limits mySql imposes on number of
columns, or total number of chars per entry, which is columns x how
long each is.  Backing it

Another error was title of the column, and there were 2 that were
extremely long, so i changed them to "pbmacc" and then it works.

After doing this, the script executes and various columns can be
probed with syntax such as:

  select  `Provider Organization Name (Legal Business Name)` from t;

showing that columns contents for all entries.


------------------------- Python code

- makebarchart.py

- is_md_or_do.py


