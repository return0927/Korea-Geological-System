CREATE TABLE busan (
    uid character varying(17),
    name character varying(100),
    subname character varying(100),
    upground_floors integer,
    underground_floors integer,
    height double precision,
    built_date character varying(8),
    updated_date character varying(8),
    zip integer,
    shp character varying(30)
);
CREATE TABLE daegu (
  LIKE busan
);
CREATE TABLE daejeon (
LIKE busan
);
CREATE TABLE incheon (
LIKE busan
);
CREATE TABLE seoul (
LIKE busan
);