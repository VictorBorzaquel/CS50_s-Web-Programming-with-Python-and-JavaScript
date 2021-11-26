# SQL


## Init sql
```
touch flights.sql
sqlite3 flights.sql
```

### SQL3 commands
- .tables
- .mode columns
- .headers yes

## SQLite Types

- TEXT
- NUMERIC
- INTEGER
- REAL
- BLOB

## Create Table

### Types

- CHAR(size)
- VARCHAR(size)
- SMALLINT
- INT
- BIGINT
- FLOAT
- BOUBLE
- ...

### Constraints

- CHECK
- DEFAULT
- NOT NULL
- PRIMARY KEY
- UNIQUE

```
CREATE TABLE flights (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  origin TEXT NOT NULL,
  destination TEXT NOT NULL,
  deration INTEGER NOT NULL
);
```


## Update Table

```
UPDATE flights 
  SET duration = 430;
  WHERE origin = "New Work"
  AND destination = "London");
```

## Delete Table

```
DELETE flights WHERE destination = "Tokyo";
```

## Insert in table

```
INSERT INTO flights (
  origin, destination, deration
) VALUES (
  "New York", "London", 415
);
```

## Join

- JOIN / INNER JOIN
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL JOIN

```
SELECT first, origin, destination
  FROM flights JOIN passengers
  ON passengers.flight_id = flights.id
```

## Select in table

### Functions

- AVERAGE
- COUNT
- MAX
- MIN
- SUM
- ...

### Other Clauses

- LIMIT
- ORDER BY
- GROUP BY
- HAVING
- ...

### Index
```
CREATE INDEX name_index ON passengers (last);
```

### Examples

```
SELECT * FROM flights;
```
```
SELECT origin, destination FROM flights;
```
```
SELECT * FROM flights WHERE id = 3;
```
```
SELECT * FROM flights WHERE origin = "New York";
```
```
SELECT * FROM flights WHERE duration > 500;
```
```
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
```
```
SELECT * FROM flights WHERE duration > 500 OR destination = "Paris";
```
```
SELECT * FROM flights WHERE origin LIKE "%a%";
```

## SQL Inject

Comment = --

