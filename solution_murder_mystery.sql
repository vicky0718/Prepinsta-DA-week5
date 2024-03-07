# To list down all the tables from a murder_mystery database.

use murder_mystery;
show tables;


# Run a query to retrieve the crime scene report for the murder that occurred on Jan.15, 2018, in SQL City. Gather all available details from the report.
select * from crime_scene_report
where city = 'SQL City'
and type = 'murder'
and date = '20180115';



# Check the personal details of witnesses involved in the case. Retrieve their names, addresses, and any other relevant information.
select * from person
where address_street_name = 'Northwestern Dr'
order by address_number desc;

select * from person
where address_street_name = 'Franklin Ave'
and name like 'Annabel%';



# Access the recorded interviews of witnesses conducted after the murder. Gather insights into their statements and potential clues.
select * from interview
where person_id IN ('14887','16371');




# Investigate the gym database using details obtained from the crime scene report and witness interviews. Look for any gym-related information that might be relevant.
select * from get_fit_now_member
where id like '48Z%'
and membership_status = 'gold';



# Examine the car details associated with the crime scene. Retrieve information about the vehicles present during the incident.
select * from drivers_license
where plate_number like '%H42W%';



# Identify and collect personal details mentioned in the previous query. This includes names, addresses, and any additional details.
select * from person
where license_id IN ('183779', '423327', '664760');



# Determine who is identified in the previous query as a member of the gym. Utilize the gym database to confirm their membership status.
select * from get_fit_now_member
where person_id in ('51739', '67318', '78193');



# Interview the murderer to get the clues of true mastermind who is behind the murder.
select * from interview
where person_id = '67318';



# Working on the clues.
select * from income
order by annual_income desc;

select per.* , dl.hair_color, dl.gender, dl.car_make, dl.car_model, dl.height
from person as per
inner join drivers_license as dl 
on dl.id = per.license_id
inner join facebook_event_checkin as fb_event 
on fb_event.person_id = per.id
where dl.hair_color = 'red'
and dl.height between 65 and 67
and dl.gender = 'female'
and dl.car_make = 'Tesla'
and dl.car_model = 'Model S';