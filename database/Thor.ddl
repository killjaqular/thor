USE Lightning_Data;

CREATE TABLE lightning_record(
    strike_time  datetime,
    nano_seconds int,
    lat          double,
    lon 		 double,
    rise_time    double,
    fall         double,
    peakcurrent  int,
    PRIMARY KEY (strike_time, nano_seconds)
    );

CREATE TABLE lightning_record(
    strike_time   datetime,
    nano_seconds  int,
    generated_key int,
    PRIMARY KEY (strike_time, nano_seconds)
    );
