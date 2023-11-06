CREATE TABLE followers (
  id SERIAL PRIMARY KEY,
  user_id TEXT,
  following_id TEXT,
  create_at TIMESTAMP
);

SELECT create_at FROM followers ;

DELETE FROM followers
WHERE user_id = '12x12' and following_id = 'asdasd'; 


EXISTS (
  SELECT 1
  FROM followers AS c
  WHERE user_id = '3'
  and following_id = 'vic'
);