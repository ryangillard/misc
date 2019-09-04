# Write your MySQL query statement below
SELECT
    A.Id
FROM
    Weather AS A
INNER JOIN
    Weather AS B
ON
    DATEDIFF(A.RecordDate, B.RecordDate) = 1
WHERE
    A.Temperature > B.Temperature