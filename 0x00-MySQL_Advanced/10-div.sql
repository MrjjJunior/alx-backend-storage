-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number
DELIMITER //

-- Create SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- If the second number is 0, return 0, otherwise return a / b
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END//

DELIMITER ;
