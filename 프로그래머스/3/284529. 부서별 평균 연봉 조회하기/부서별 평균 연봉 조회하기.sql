select
    a.dept_id,
    b.DEPT_NAME_EN,
    round(avg(sal),0) as AVG_SAL
from
    hr_employees a 
    inner join hr_department b on a.dept_id = b.dept_id
group by
    dept_id
order by
    AVG_SAL desc;