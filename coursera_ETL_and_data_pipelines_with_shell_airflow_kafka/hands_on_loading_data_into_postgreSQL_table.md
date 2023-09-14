# Start PostgreSQL database
1. start PostgreSQL database
   > start_postgres
   
2. start interactive psql client connecting to the PostgreSQL server
   > psql --username=postgres --host=localhost

3. use a database called *template1*
   > \c template1

4. create a table
   > create table users(username varchar(50),userid int,homedirectory varchar(100));

5. quit the psql client
   > \q

# Loading local data into a PostgreSQL table using bash file
1. *csv2db.sh* file executing ETL 
    > echo "Extracting data" <br />
    > cut -d":" -f1,3,6 /etc/passwd > extract-data.txt <br />
    > echo "Transforming data" <br />
    > tr ":" "," < extract-data.txt > transformed-data.csv <br />
    > echo "Loading data" <br />
    > echo "\c template1;\COPY users FROM /home/project/transformed-data.csv DELIMITERS ',' CSV;" | psql --username=postgres --host=localhost <br />

**if CSV files have a header, then "CSV HEADER;" 

2. run bash file <br />
    > bash csv2db.sh
    
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/d681d0da-198e-4f62-b987-329d30291d22)

3. verify that the table users is populated with the data
    > echo '\c template1; \\SELECT * from users;' | psql --username=postgres --host=localhost

    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/0be125ba-148c-4204-a58a-b0b5af37dd62)


