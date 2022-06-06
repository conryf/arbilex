INSERT INTO justices(
    name,
    name_2,
    start_date,
    is_active,
    finish_date,
    nominating_party,
    military_service,
    law_school,
    state_of_birth
) SELECT 
    data->>'name',
    data->>'name_2',
    (data->>'start_date')::DATE,
    data->>'is_active',
    (data->>'finish_date')::DATE,
    data->>'nominating_party',
    data->>'military_service',
    data->>'law_school',
    data->>'state_of_birth'
FROM temp;

--DROP TABLE temp;
