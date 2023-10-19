CREATE TABLE IF NOT EXISTS domain (
  id SERIAL PRIMARY KEY,
  code VARCHAR(50) NOT NULL,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS industry_class (
  id SERIAL PRIMARY KEY,
  code VARCHAR(50) NOT NULL,
  name VARCHAR(100) NOT NULL,
  type VARCHAR(50) NOT NULL,
  domain_id INT,
  FOREIGN KEY (domain_id) REFERENCES domain(id)
);

CREATE TABLE IF NOT EXISTS flowmap (
  id SERIAL PRIMARY KEY,
  node JSONB NOT NULL,
  edge JSONB NOT NULL,
  industry_class_id INT REFERENCES industry_class(id),
  domain_id INT REFERENCES domain(id)
);
