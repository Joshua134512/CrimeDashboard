create table stage as select p.state,
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
        outer left join recidivism as r on p.state = r.state
        outer left join qol as q on p.state = q.state
        outer left join utility as u on p.state = u.state
        outer left join arrests as a on u.abbreviation = a.state;