-- computes and store the average weighted score
DELIMITER $$

-- Drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers$$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables for processing
    DECLARE done INT DEFAULT 0;
    DECLARE current_user_id INT;

    -- Declare a cursor to loop through all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    
    -- Declare a handler to exit the loop when no more rows are found
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN user_cursor;

    -- Start looping through all users
    read_loop: LOOP
        -- Fetch user id from the cursor
        FETCH user_cursor INTO current_user_id;
        
        -- Exit the loop if there are no more users
        IF done = 1 THEN
            LEAVE read_loop;
        