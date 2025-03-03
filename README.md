

# Getting information about SUI blockchain. 


More precisely about its assets. 
The code is written for sharing, an example of using API queries, since Blockberry API has difficulties with getting the necessary information some of the queries will be replaced by getting data using selenium. 

Parses by API data on the coin, also on it receives data on the top wallets, the task is to collect the maximum information about the coin itself also data on it in pools, large holders and also to deduce the sites that are engaged in its trading. 

As long as I write the code in my spare time, not so often there will be updates, in the following I will describe in detail what I used to get what information from the site. Do not judge strictly)))) 

All the obtained information is stored in a PostgreSQL database, using sqlalchemy and sqlmodel 








at the moment it is realized to get data on the coin itself and top wallets

