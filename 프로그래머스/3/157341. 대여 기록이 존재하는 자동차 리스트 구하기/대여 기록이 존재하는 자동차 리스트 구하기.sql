select
    distinct(car.car_id)
from
    car_rental_company_car car
    inner join
    car_rental_company_rental_history history
    on car.car_id = history.car_id
where
    to_char(history.start_date,'mm') = '10'
    and
    car.car_type = '세단'
order by
    car.car_id desc;
    