-- # 185. Department Top Three Salaries   -MySQL-   HARD

/*
### Task:
--
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
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
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation: 
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees


### Testcase:
---
Employee =
| id | name  | salary | departmentId |
| -- | ----- | ------ | ------------ |
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |

Department =
| id | name  |
| -- | ----- |
| 1  | IT    |
| 2  | Sales |

*/
-- ### Solution:

-- Finding the top three highest salaries in each department

WITH DepartmentSalaryRank AS (
    -- Creating a CTE (Common Table Expression) to rank salaries within each department
    SELECT 
        e.name,
        e.salary,
        d.name AS departmentName,
        -- DENSE_RANK assigns a unique rank within each department, with no gaps in ranking for ties
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salaryRank
    FROM 
        Employee e
        INNER JOIN Department d ON e.departmentId = d.id -- Join Employee and Department tables
)
SELECT 
    departmentName AS Department, -- Selecting department name
    name AS Employee,             -- Selecting employee name
    salary AS Salary              -- Selecting employee salary
FROM 
    DepartmentSalaryRank          -- From the CTE
WHERE 
    salaryRank <= 3;              -- Filter to select only employees in top three salary ranks



-- ### Description:
/*
To find employees who are high earners (top three salaries) in each department, you can use a subquery to rank 
salaries within each department and then filter out those who are in the top three. This task can be accomplished 
using a common table expression (CTE) with window functions.

Explanation:

- The CTE `DepartmentSalaryRank` calculates a dense rank for each employee's salary within their respective departments, 
  ordered in descending order.
- The `DENSE_RANK()` function is used instead of `RANK()` to ensure that employees with the same salary get the same rank.
- The main query then selects the department name, employee name, and salary from this CTE.
- The `WHERE` clause filters out employees whose salary ranks are within the top three in their department.

This query will list the top three earning employees in each department, according to the unique salaries. 
If there are ties (same salary), they all will be included in the top three.

*/
