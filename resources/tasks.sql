-- Table: tasks

-- DROP TABLE tasks;

CREATE TABLE tasks
(
  id serial NOT NULL,
  command character varying,
  year character varying,
  month character varying,
  day character varying,
  hour character varying,
  minute character varying,
  CONSTRAINT tasks_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tasks
  OWNER TO postgres;