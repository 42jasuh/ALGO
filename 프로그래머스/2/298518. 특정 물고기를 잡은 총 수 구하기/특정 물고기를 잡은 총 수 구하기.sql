SELECT count(*) as FISH_COUNT
FROM fish_info AS fi
inner join fish_name_info as fni
on fi.fish_type = fni.fish_type
where fni.fish_name in ('BASS', 'SNAPPER');