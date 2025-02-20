drop table if exists stage_state;
create table stage_state (state varchar(255), json varchar(255));
insert into stage_state(state, json) values('{state}', '{json}')