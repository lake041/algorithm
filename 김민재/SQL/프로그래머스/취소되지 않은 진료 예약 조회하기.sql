SELECT
    a.apnt_no,
    p.pt_name,
    p.pt_no,
    a.mcdp_cd,
    d.dr_name,
    a.apnt_ymd
FROM appointment AS a
JOIN patient As p
ON a.pt_no = p.pt_no
JOIN doctor AS d
ON a.mddr_id = d.dr_id
WHERE
    a.mcdp_cd = 'CS'
    AND date_format(a.apnt_ymd, '%Y%m%d') = "20220413"
    AND a.apnt_cncl_yn = "N"
ORDER BY a.apnt_ymd ASC