# Personal Data Migrator
<img src="https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg" width="30" height="30">   Python script to migrate repo from MySql to MongoDB. 

# Story [![](https://img.shields.io/badge/language-python-brightgreen.svg)]() [![](https://img.shields.io/badge/source-MySQL-yellow.svg)]() [![](https://img.shields.io/badge/destination-mongoDB-green.svg)]()
> Time to migrate towards a Micro Services world!

The first version of [danieleautizi.com](https://github.com/dautizi/danieleautizi.com) was based on a single MySql datasource.
After a couple of years it has been decided to migrate to MongoDB in 2 steps:
* adding MongoDB intended to be the second datasource. Basically MongoDB was the first to contact and only in case of failure the app itself switches to the old MySql.
* MySQL has been shut down after 6 months of prod tests in a small Digital Ocean droplet.

The reason was basically the will to decouple data and consumer through a micro-service architecture:
* [Personal Data Service](https://github.com/dautizi/personal-data-service)
* [Consumer Website](https://github.com/dautizi/danieleautizi-website)

## Repositories   <img src="https://github.com/simple-icons/simple-icons/blob/develop/icons/mysql.svg" width="30" height="30"> <img src="https://github.com/simple-icons/simple-icons/blob/develop/icons/mongodb.svg" width="30" height="30">

- [MySQL](https://www.mysql.com/) - Source relational database.
- [MongoDB](https://www.mongodb.com/) - NoSQL Database as destination.

## How to run

```
python mongodb-migration-tool.py
```
