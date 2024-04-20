select
    concat('/home/grep/src/',a.board_id,'/',a.file_id,a.file_name,a.file_ext) as FILE_PATH
from
    used_goods_file a 
    inner join (
        select
            board_id
        from
            used_goods_board
        order by
            views desc
        limit 1
    ) b on a.board_id = b.board_id 
order by
    a.file_id desc;