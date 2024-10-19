-- script create a procedure that computes and updates average score
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- caluculate average score for user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- update the users table with the new average score
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$

DELIMITER;