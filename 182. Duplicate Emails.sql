-- ### 182. Duplicate Emails.          MySQL


/*
### Task:
---

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.


### Testcase:
---

| id | email   |
| -- | ------- |
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |

*/
-- Solution MySQL:

-- Selecting duplicate emails from the Person table

SELECT 
    email AS Email  -- Selecting and renaming the email column to 'Email'
FROM 
    Person          -- From the Person table
GROUP BY 
    email           -- Grouping the records by email
HAVING 
    COUNT(email) > 1;  -- The HAVING clause filters groups having more than one occurrence, indicating duplicates

/*
### Description:
---

To find duplicate emails in the `Person` table, you can use a SQL query that groups the records by email and then
filters to keep only those groups having more than one record.

Explanation:

- `GROUP BY email` groups the records based on the `email` field.
- `HAVING COUNT(email) > 1` filters out the groups to include only those where the count of emails in 
   the group is greater than 1, which indicates a duplicate.
- The query selects the `email` field, and we alias it as `Email` to match the desired output format.

*/
