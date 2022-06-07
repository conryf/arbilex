DISENTING_JUSTICE_QUERY = "SELECT 1 AS id, pretty_name FROM decisions WHERE datedecision > ('1791-08-03'::DATE +  make_interval(0,0,0,%s)) AND majority = '1' GROUP BY pretty_name ORDER BY count(*) DESC limit 1";

DECISION_DURATION_QUERY = "SELECT 1 AS id, ROUND(AVG(EXTRACT(EPOCH FROM AGE(datedecision, dateargument))/(60*60*24))::NUMERIC,2) AS average_duration FROM decisions WHERE datedecision > ('1791-08-03'::DATE +  make_interval(0,0,0,%s))";

TERM_DURATION_QUERY = "SELECT 1 AS id, COALESCE(ROUND(AVG(EXTRACT(EPOCH FROM AGE(finish_date, start_date))/31557600)::NUMERIC,1)::TEXT, 'No Data')  AS average_duration FROM justices WHERE is_active='false' AND start_date > ('1791-08-03'::DATE +  make_interval(0,0,0,%s))";

