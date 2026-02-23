# Write your MySQL query statement below
SELECT 
    a.deptname AS Department,
    a.name     AS Employee,
    a.salary
FROM (
    SELECT 
        e.name,
        e.salary,
        d.name AS deptname,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentid 
            ORDER BY salary DESC
        ) AS rnk
    FROM employee e
    JOIN Department d
        ON e.departmentid = d.id
) AS a
WHERE a.rnk = 1;