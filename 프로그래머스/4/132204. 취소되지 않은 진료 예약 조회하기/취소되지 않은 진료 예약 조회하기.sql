-- 코드를 입력하세요
select 
    a.apnt_no,
    p.pt_name,
    a.pt_no,
    a.mcdp_cd,
    d.dr_name,
    a.apnt_ymd
from appointment a 
    inner join doctor d on d.dr_id = a.mddr_id
    inner join patient p on a.pt_no = p.pt_no
where a.mcdp_cd = 'CS'
and apnt_cncl_yn = 'N'
and date_format(apnt_ymd, '%y-%m-%d') = '22-04-13'
order by apnt_ymd