create table staging as select p.state,
    r.recidivismrate,
    r.prisonpopulation,
    r.imprisonmentrate,
    p.population,
    q.qualityoflifetotalscore,
    q.qualityoflifequalityoflife,
    q.qualityoflifeaffordability,
    q.qualityoflifeeconomy,
    q.qualityoflifeeducationandhealth,
    q.qualityoflifesafety
 from
    population as p
        inner join recidivism as r on p.state = r.state
        inner join qol as q on q.state = p.state;