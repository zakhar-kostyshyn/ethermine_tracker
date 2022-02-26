create table if not exists ethermine
(
    id                  varchar(36) primary key,
    time                integer,
    lastSeen            integer,
    reportedHashrate    integer,
    currentHashrate     integer,
    validShares         smallint,
    invalidShares       smallint,
    staleShares         smallint,
    activeWorkers       smallint,
    averageHashrate     float,
    coinsPerMin         float
);
