select pretty_name, justiceName, count(*) FROM decisions where datedecision > '1950-01-01' and majority = '1' GROUP BY justiceName, pretty_name ORDER BY count(*) desc limit 1;

select AVG(AGE(dateargument, datedecision)) from decisions where datedecision > '1960-01-01';

select AVG(AGE(finish_date, start_date)) from justices where is_active='false' and start_date > '1960-01-01';
