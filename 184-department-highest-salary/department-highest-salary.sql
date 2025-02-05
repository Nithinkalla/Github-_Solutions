# Write your MySQL query statement below
SELECT DEPARTMENT.NAME Department,EMPLOYEE.NAME Employee,Salary
FROM EMPLOYEE INNER JOIN DEPARTMENT
ON EMPLOYEE.DEPARTMENTID = DEPARTMENT.ID
WHERE EMPLOYEE.SALARY = (SELECT MAX(SALARY) FROM EMPLOYEE WHERE EMPLOYEE.DEPARTMENTID = DEPARTMENT.ID );