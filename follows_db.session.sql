CREATE TABLE followers (
  id SERIAL PRIMARY KEY,
  user_id TEXT,
  following_id TEXT,
  create_at TIMESTAMP
);

SELECT * FROM followers ;