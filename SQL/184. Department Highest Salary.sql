-- 184. Department Highest Salary           -MySQL-  Medium

/*
### Task:
---
Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.

Example 1:
Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+

Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

### Testcase:
---
Employee =
| id | name  | salary | departmentId |
| -- | ----- | ------ | ------------ |
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |

Department =
| id | name  |
| -- | ----- |
| 1  | IT    |
| 2  | Sales |

*/
-- ### Solution:

-- Selecting employees with the highest salary in each department

SELECT 
    Department.name AS Department,  -- Selecting department name
    Employee.name AS Employee,      -- Selecting employee name
    Employee.salary AS Salary       -- Selecting employee salary
FROM 
    Employee
    INNER JOIN Department ON Employee.departmentId = Department.id  -- Joining Employee and Department tables
WHERE 
    (Employee.departmentId, Employee.salary) IN 
        (SELECT 
             departmentId, 
             MAX(salary)  -- Subquery to find the maximum salary for each department
         FROM 
             Employee 
         GROUP BY 
             departmentId
        );


-- ### Description:
/*
To find employees who have the highest salary in each of the departments, you need to perform the following steps:

1. Identify the maximum salary in each department.
2. Find the employees who earn that salary in each department.
3. Join this information with the `Department` table to include the department name.

Explanation:

- The subquery `(SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)` identifies the maximum salary for each department.
- The main query selects the names of departments and employees, along with the employees' salaries.
- The `INNER JOIN` combines the `Employee` and `Department` tables based on the `departmentId`.
- The `WHERE` clause filters employees who have a salary equal to the maximum salary for their department, as identified by the subquery.
- This query will output each department's name along with the employee (or employees, in case of a tie) who has the highest salary in that department.


*/