-- 183. Customers Who Never Order

/*
### Task:
---

Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+


### Testcase:
---
Customers =
| id | name  |
| -- | ----- |
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |

Orders =
| id | customerId |
| -- | ---------- |
| 1  | 3          |
| 2  | 1          |

*/
-- ### Solution:

-- Selecting customers who never placed an order

SELECT 
    Customers.name AS Customers  -- Selecting and renaming the name column to 'Customers'
FROM 
    Customers                    -- From the Customers table
    LEFT JOIN Orders ON Customers.id = Orders.customerId  -- Left joining with the Orders table on customerId
WHERE 
    Orders.id IS NULL;  -- Filtering for customers with no matching order (indicated by NULL in Orders.id)


-- ### Description
/*
To find all customers who never placed an order, you can write a SQL query that selects customers from the `Customers` table 
who do not have an entry in the `Orders` table. This can be achieved using a LEFT JOIN combined with a WHERE clause to check 
for NULLs in the joining field of the `Orders` table.

This query works by performing a left join of the `Customers` table with the `Orders` table on the `customerId` field. 
he `WHERE` clause then filters for those rows where there is no corresponding entry in the `Orders` table (i.e., where `Orders.id` 
is `NULL`), indicating that the customer has never placed an order. The result is the names of these customers.

*/
