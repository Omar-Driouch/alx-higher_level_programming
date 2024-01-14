# 0x0F. Python - Object-relational mapping

## Project Overview

+ Project Name: Object-relational mapping
+ Language: Python, MySQL
 

## Project Description
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

**Without ORM:**
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
**With an ORM:**
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Key learning objectives include distinguishing between a binary tree and a Binary Search Tree, understanding the potential time complexity benefits compared to linked lists, and grasping concepts like depth, height, and size of a binary tree. 

Additionally, you will explore different traversal methods and become familiar with the characteristics of complete, full, perfect, and balanced binary trees. 

Upon completion, you should be able to articulate these concepts confidently without relying on external resources like Google.

## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```
sudo apt-get install python3.8-venv
python3 -m venv venv
source venv/bin/activate
```


**Install MySQLdb module version 2.0.x**
    For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04
```
    $ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

**Install SQLAlchemy module version 1.4.x**
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

  
## Usage
+ Clone the project to your local machine

```
git clone https://github.com/alamy2711/binary_trees.git

```


+ Run this command to compile the project
 
```
gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 1-main.c 1-binary_tree_insert_left.c 0-binary_tree_node.c -o Output
```

## Project Data structures
```
/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

```

**Binary Search Tree**
```
typedef struct binary_tree_s bst_t;

```
**AVL Tree**
```
typedef struct binary_tree_s avl_t;

```
**Max Binary Heap**
```
typedef struct binary_tree_s heap_t;


```

## Contributors
+ Mustapha El Alamy - [Github Profile](https://github.com/alamy2711/)
+ Omar Driouch - [LinkedIn Profile](https://www.linkedin.com/in/omar-driouch/)

