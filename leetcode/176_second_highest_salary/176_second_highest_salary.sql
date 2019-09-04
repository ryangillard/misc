# Write your MySQL query statement below
SELECT
    (SELECT
        Salary
    FROM
        Employee
    GROUP BY
        Salary
    ORDER BY
        Salary DESC
    LIMIT
        1 OFFSET 1) AS SecondHighestSalary