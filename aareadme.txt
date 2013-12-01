-- start: Nov 21, 2013
-- cur:   Nov 30, 2013

[Modified version of mssg-data-sci blog notes ]

------------------------------ mySQL code

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

---- makebarchart.py  

Sorts states by number of MDs in them and makes a barchart of this.

Run as so: py makebarchart.py [limnumber] 

 Where the optional arg
 limnumber (defaults to zero) is the lower limit on the number of MDs
 that must be in a given state for that state to be shown in the
 barchart.  e.g. for the 1e5 file, 1000 works well.

Other than this, it's quite well commented within the file itself how
it works, and i also uploaded a barchart from it to a new Dropbox
folder where i'll keep stuff like that in the future.

----    is_md_or_do.py

is pretty similar, just picks the column that lists the
professional title, and i found there are plenty of dentists etc. in
here too, not just MDs or DOs.



