drop table if exists derived_columns_stage;
create table derived_columns_stage(
    State varchar(255),
    RecidivismRate varchar(255),
    PercentMale varchar(255),
    PercentFemale varchar(255),
    PercentAsian varchar(255),
    PercentWhite varchar(255),
    PercentBlack varchar(255),
    PercentNativeAmerican varchar(255),
    PercentOfPopInPrison varchar(255),
    TotalViolentCrimes varchar(255),
    TotalNonviolentCrimes varchar(255),
    OtherCrimes varchar(255),
    AverageQOLScore varchar(255),
    PopulationDensity varchar(255)
)