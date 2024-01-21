-- ###  181. Employees Earning More Than Their Managers.  -- MySQL --

-- ## Topic: Database

/*
### Task:
---

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.


### Testcase:
---
| id | name  | salary | managerId |
| -- | ----- | ------ | --------- |
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | null      |
| 4  | Max   | 90000  | null      |

*/

--### Write your MySQL query statement below:

-- Select names of employees who earn more than their managers
SELECT 
    e1.name AS Employee
FROM 
    Employee e1
    JOIN Employee e2 ON e1.managerId = e2.id  -- Join Employee table with itself to link employees with their managers
WHERE 
    e1.salary > e2.salary;  -- Filter to get employees whose salary is greater than their manager's


--### Description:
/*
To solve this problem, you need to write a SQL query that finds employees who earn more than their managers. You can accomplish this by joining the `Employee` table with itself. In this self-join, one instance of the table represents the employees and the other instance represents their managers. Then, compare the salaries of the employees and their managers. Here's the SQL query to do this:

Explanation:
- `e1` and `e2` are aliases for the `Employee` table, where `e1` represents employees and `e2` represents managers.
- The `JOIN` operation is performed on the condition `e1.managerId = e2.id`, which links each employee to their manager.
- The `WHERE` clause filters out the rows where an employee's salary (`e1.salary`) is greater than their manager's salary (`e2.salary`).
- Finally, select the `name` column from the `e1` table (employees), which will list the names of the employees who earn more than their managers.

*/