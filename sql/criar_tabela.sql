DROP TABLE IF EXISTS TB_IMIGRANTES;

CREATE TABLE IF NOT EXISTS TB_IMIGRANTES (
    ID INT GENERATED BY DEFAULT AS IDENTITY,
    status_migratorio VARCHAR(100),
    pais VARCHAR(100),
    total_de_imigrantes INT
);