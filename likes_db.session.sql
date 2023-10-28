CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    post_id text,
    user_id text,
    liked_at timestamp
);

SELECT * FROM likes ;
