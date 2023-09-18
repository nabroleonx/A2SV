# Write your MySQL query statement below
select department.name as department, employee.name as employee, employee.salary from employee join department
on employee.departmentId = department.id
where (employee.departmentId, employee.salary) in (select departmentId, max(salary) from employee group by departmentId)
