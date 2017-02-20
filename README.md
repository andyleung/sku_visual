

1. Use virtualenv create directory srx-sales
2. source bin/activate
3. pip install -r requirements.txt
3. mkdir sku_visual 
4. mkdir data; 
5. sales-data to this directory, name file 2016sales.csv
6. (Macbook)%mongod 
7. (Ubunut)(If running on Ubuntu, skip. mongo should be default process on ubuntu)
8.  (srx-sales) andy@~/data% mongoimport -d 2016data -c 2016srx --type csv --headerline --file 2016sales.csv
9. %python app.py

Useful command to check the mongodb (mongo shell):
%mongo
>dbs
(show list 2016data)
>use 2016data
>show collections
(Should display 2016srx)

