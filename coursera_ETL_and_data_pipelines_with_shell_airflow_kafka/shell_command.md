# basic shell command
- cat : verify that the file is created
  > cat extract-data.txt 
  
- cut : extract the first ~ four characters
  > ![image](https://github.com/youngmin-jin/exercise/assets/135728064/fd45d869-d49f-4484-9eea-831158c49556)

- d : delimeter
- f : columns divided by delimeter
  > ![image](https://github.com/youngmin-jin/exercise/assets/135728064/f9975037-31a8-464e-84ae-db4e02e00c9d)

- tr : transform the data
  > ![image](https://github.com/youngmin-jin/exercise/assets/135728064/c28b9701-efc3-471b-925b-af1e07598c4f)

  - tr -d : delete characters
    > ![image](https://github.com/youngmin-jin/exercise/assets/135728064/b2314d6c-cb87-4913-9226-47edb9431143)

- wget : downlaod files
  - -o : set file name
    > wget -O web-server-access-log.txt.gz "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz"
  
- gunzip : unzip the file
  > gunzip -f web-server-access-log.txt.gz
