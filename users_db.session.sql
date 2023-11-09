
SELECT * from users  ;


CREATE TABLE tests (
  id SERIAL PRIMARY KEY,
  test text
);

SELECT * from tests ;

drop table test

INSERT INTO users (post)
VALUES (0)
WHERE EXISTS (
    SELECT 1
    FROM users
    WHERE user_id = 1
);

UPDATE users
SET post = 0
WHERE user_id = 1 ;

INSERT INTO users(user_id,post)
VALUES (1,'0')  ;



-- RETURNING id, name, email;

-- delete from users WHERE user_id = 5 ;

-- insert into users(usersname,email,passwords,is_active) 
--                 values ('asd','asd','asd',True) RETURNING user_id,usersname,email ;

-- CREATE FUNCTION get_user_info(id INT)
-- RETURNS INT
-- LANGUAGE plpgsql
-- AS $$
-- DECLARE
--   user RECORD;
-- BEGIN
--   SELECT * INTO user FROM users WHERE id = $1;
--   RETURN to_json(user);
-- END;
-- $$;