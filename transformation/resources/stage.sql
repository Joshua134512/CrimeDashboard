create table stage as select p.state,
    r.recidivismrate,
    r.prisonpopulation,
    r.imprisonmentrate,
    p.population,
    q.qualityoflifequalityoflife as qualityoflifetotalscore,
    q.qualityoflifeaffordability,
    q.qualityoflifeeconomy,
    q.qualityoflifeeducationandhealth,
    q.qualityoflifesafety,
    a.Male,
    a.Female,
    a.Rape,
    a.Arson,
    a.Fraud,
    a.Larceny,
    a.Robbery,
    a.Runaway,
    a.Weapons,
    a.Burglary,
    a.Gambling,
    a.Vagrancy,
    a.Suspicion,
    a.Vandalism,
    a.Drunkenness,
    a.Embezzlement,
    a.Sex_Offenses,
    a.Rape_Legacy,
    a.Simple_Assault,
    a.Drug_Possession,
    a.Stolen_Property,
    a.Human_Trafficking,
    a.Aggravated_Assault,
    a.All_Other_Offenses,
    a.Disorderly_Conduct,
    a.Motor_Vehicle_Theft,
    a.Drug_Abuse_Violations,
    a.Liquor_Law_Violations,
    a.Counterfeiting_or_Forgery,
    a.Drug_Sale_or_Manufacturing,
    a.Drive_Under_the_Influence,
    a.Manslaughter_by_Negligence,
    a.Murder_and_Nonnegligent_Homicide,
    a.Curfew_and_Loitering_Law_Violations,
    a.Prostitution_and_Commercialized_Vice,
    a.Offenses_Against_the_Family_and_Children
 from
    population as p
        inner join recidivism as r on p.state = r.state
        inner join qol as q on p.state = q.state
        inner join utility as u on p.state = u.state
        inner join arrests as a on u.abbreviation = a.state;