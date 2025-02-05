# Write your MySQL query statement below
select e1.name as Employee from employee e2 inner join employee e1
on e2.id = e1.managerid 
where e2.salary < e1.salary;