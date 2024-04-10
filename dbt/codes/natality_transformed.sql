select r1.race child
        , r2.race mother
        , r3.race father
        , round(avg(weight_pounds),2) avg_weight_pounds
--        , round(avg(apgar_5min),2) avg_apgar_5min
        , round(avg(mother_age),2) avg_mother_age
--        , round(avg(gestation_weeks),2) avg_gestation_weeks
        , round(avg(weight_gain_pounds),2) avg_weight_gain_pounds
        , round(avg(father_age),2) avg_father_age
from {{ ref('natality_original') }} o
    join {{ ref('natality_race') }} r1 on o.child_race = r1.id
    join {{ ref('natality_race') }} r2 on o.mother_race = r2.id
    join {{ ref('natality_race') }} r3 on o.father_race = r3.id
group by child
        , mother
        , father
order by avg_weight_pounds desc
