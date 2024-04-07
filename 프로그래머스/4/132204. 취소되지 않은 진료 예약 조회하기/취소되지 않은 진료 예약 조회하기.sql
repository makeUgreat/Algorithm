select
    a.apnt_no,
    p.pt_name,
    a.pt_no,
    a.mcdp_cd,
    d.dr_name,
    a.apnt_ymd
from
    appointment a
    inner join patient p on a.pt_no = p.pt_no
    inner join doctor d on a.mddr_id = d.dr_id
where
    to_char(apnt_ymd,'yyyy-mm-dd') = '2022-04-13'
    and d.mcdp_cd = 'CS'
    and a.apnt_cncl_yn ='N'
order by a.apnt_ymd;