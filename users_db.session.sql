
SELECT * from users  ;
-- INSERT INTO users (name, email)
-- VALUES ('John Doe', 'john.doe@example.com')
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