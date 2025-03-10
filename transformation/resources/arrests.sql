insert into arrests (State,
    Male,
    Female,
    Rape,
    Arson,
    Fraud,
    Larceny,
    Robbery,
    Runaway,
    Weapons,
    Burglary,
    Gambling,
    Vagrancy,
    Suspicion,
    Vandalism,
    Drunkenness,
    Embezzlement,
    Sex_Offenses,
    Rape_Legacy,
    Simple_Assault,
    Drug_Possession,
    Stolen_Property,
    Human_Trafficking,
    Aggravated_Assault,
    All_Other_Offenses,
    Disorderly_Conduct,
    Motor_Vehicle_Theft,
    Drug_Abuse_Violations,
    Liquor_Law_Violations,
    Counterfeiting_or_Forgery,
    Drug_Sale_or_Manufacturing,
    Drive_Under_the_Influence,
    Manslaughter_by_Negligence,
    Murder_and_Nonnegligent_Homicide,
    Curfew_and_Loitering_Law_Violations,
    Prostitution_and_Commercialized_Vice,
    Offenses_Against_the_Family_and_Children,
    Asian,
    White,
    Unknown,
    Multiple,
    NotSpecified,
    Black,
    NativeAmerican,
    NativeHawaiianOrPacificIslander
)
select '{state}',
    json_extract(json, '$.Arrestee Sex.Male'),
    json_extract(json, '$.Arrestee Sex.Female'),
    json_extract(json, '$.Offense Name.Rape'),
    json_extract(json, '$.Offense Name.Arson'),
    json_extract(json, '$.Offense Name.Fraud'),
    json_extract(json, '$.Offense Name.Larceny'),
    json_extract(json, '$.Offense Name.Robbery'),
    json_extract(json, '$.Offense Name.Runaway'),
    json_extract(json, '$.Offense Name.Weapons'),
    json_extract(json, '$.Offense Name.Burglary'),
    json_extract(json, '$.Offense Name.Gambling'),
    json_extract(json, '$.Offense Name.Vagrancy'),
    json_extract(json, '$.Offense Name.Suspicion'),
    json_extract(json, '$.Offense Name.Vandalism'),
    json_extract(json, '$.Offense Name.Drunkenness'),
    json_extract(json, '$.Offense Name.Embezzlement'),
    json_extract(json, '$.Offense Name.Sex Offenses'),
    json_extract(json, '$.Offense Name.Rape (Legacy)'),
    json_extract(json, '$.Offense Name.Simple Assault'),
    json_extract(json, '$.Offense Name.Drug Possession'),
    json_extract(json, '$.Offense Name.Stolen Property'),
    json_extract(json, '$.Offense Name.Human Trafficking'),
    json_extract(json, '$.Offense Name.Aggravated Assault'),
    json_extract(json, '$.Offense Name.All Other Offenses'),
    json_extract(json, '$.Offense Name.Disorderly Conduct'),
    json_extract(json, '$.Offense Name.Motor Vehicle Theft'),
    json_extract(json, '$.Offense Name.Drug Abuse Violations'),
    json_extract(json, '$.Offense Name.Liquor Law Violations'),
    json_extract(json, '$.Offense Name.Counterfeiting/Forgery'),
    json_extract(json, '$.Offense Name.Drug Sale/Manufacturing'),
    json_extract(json, '$.Offense Name.Drive Under the Influence'),
    json_extract(json, '$.Offense Name.Manslaughter by Negligence'),
    json_extract(json, '$.Offense Name.Murder and Nonnegligent Homicide'),
    json_extract(json, '$.Offense Name.Curfew and Loitering Law Violations'),
    json_extract(json, '$.Offense Name.Prostitution and Commercialized Vice'),
    json_extract(json, '$.Offense Name.Offenses Against the Family and Children'),
    json_extract(json, '$.Arrestee Race.Asian'),
    json_extract(json, '$.Arrestee Race.White'),
    json_extract(json, '$.Arrestee Race.Unknown'),
    json_extract(json, '$.Arrestee Race.Multiple'),
    json_extract(json, '$.Arrestee Race.Not Specified'),
    json_extract(json, '$.Arrestee Race.Black or African American'),
    json_extract(json, '$.Arrestee Race.American Indian or Alaska Native'),
    json_extract(json, '$.Arrestee Race.Native Hawaiian or Other Pacific Islander')
from stage_state;