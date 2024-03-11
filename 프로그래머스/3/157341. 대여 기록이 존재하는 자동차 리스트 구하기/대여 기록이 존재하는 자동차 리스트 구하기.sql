select
    distinct(car.car_id)
from
    car_rental_company_car as car
    inner join
    car_rental_company_rental_history as history
    on car.car_id = history.car_id
where
    date_format(history.start_date,'%m') = '10'
    and
    car_type = '세단'
order by
    car.car_id desc;
    
