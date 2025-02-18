create table staging as select * from
    population as p
        inner join recidivism as r on p.state = r.state
        inner join qol as q on q.state = p.state;