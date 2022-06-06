INSERT INTO summary(day)
SELECT generate_series(1,83975);
 
UPDATE summary SET most_disenting_justice = (SELECT pretty_name FROM decisions WHERE datedecision > ('1791-08-02'::DATE + make_interval(0,0,0,0,summary.day)) AND majority = '1' GROUP BY justiceName, pretty_name ORDER BY count(*) DESC LIMIT 1);

UPDATE summary SET average_decision_duration = (SELECT AVG(AGE(dateargument, datedecision)) FROM decisions WHERE datedecision > 
('1791-08-02'::DATE + make_interval(0,0,0,0,summary.day));

UPDATE summary SET average_term_duration = (SELECT AVG(AGE(finish_date, start_date)) FROM justices WHERE is_active='false' AND start_date >('1791-08-02'::DATE + make_interval(0,0,0,0,summary.day)); 
