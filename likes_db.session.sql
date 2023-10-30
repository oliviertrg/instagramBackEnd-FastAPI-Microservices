CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    post_id text,
    user_id text,
    liked_at timestamp
);

SELECT * FROM likes  where post_id = '1234';

SELECT count(*) FROM likes  where post_id = '123';


INSERT INTO likes(post_id,user_id,liked_at) 
                   VALUES (
            '123',
            '1',
            '2023-10-30T17:03:33.088500') 
                   WHERE NOT EXISTS (post_id,user_id,liked_atpost_id,user_id,liked_at);


INSERT INTO likes
    (post_id,user_id,liked_at)
SELECT '1234',
            '1',
            '2023-10-30T17:03:33.088500'
WHERE
    NOT EXISTS (
        SELECT user_id FROM likes 
                   WHERE post_id = '1234'
    );



SELECT count(user_id) FROM likes WHERE post_id = '123';

SELECT user_id FROM likes WHERE 
                   user_id NOT IN (SELECT user_id FROM likes 
                   WHERE post_id = '123');






INSERT INTO customers (name, email)
VALUES ('John Doe', 'john.doe@example.com')
WHERE NOT EXISTS (SELECT email FROM customers 
WHERE email = 'john.doe@example.com');







CREATE TABLE customers (
    name text,
    email text
);

SELECT * FROM customers ;

INSERT INTO customers
    (name, email)
SELECT 'John Doe', 'john.doe@example.com'
WHERE
    NOT EXISTS (
        SELECT email FROM customers 
WHERE email = 'john.doe@example.com'
    );