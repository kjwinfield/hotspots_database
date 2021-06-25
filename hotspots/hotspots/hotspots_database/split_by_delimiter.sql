DELIMITER $$
DROP PROCEDURE IF EXISTS `test`.`SplitValueIntoMultipleRows` $$
CREATE
    PROCEDURE `test`.`SplitValueIntoMultipleRows`()
    BEGIN

	DECLARE r_len INTEGER;
        DECLARE r_id INTEGER;
        DECLARE r_name VARCHAR(50);
        DECLARE i INT DEFAULT 0;
	DECLARE splitted_name VARCHAR(50);
        DECLARE occurances INT DEFAULT 0;
        DECLARE done INT DEFAULT 0;
        DECLARE cur CURSOR FOR SELECT sometbl.id,sometbl.name FROM sometbl;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        DROP TEMPORARY TABLE IF EXISTS temp ;
        CREATE TEMPORARY TABLE temp(`id` INT(11),`name` VARCHAR(50));
	OPEN cur;
            read_loop: LOOP
		FETCH cur INTO r_id,r_name;
                IF done THEN
			LEAVE read_loop;
                END IF;
                SET occurances = (SELECT LENGTH(r_name) - LENGTH(REPLACE(r_name, '|', ''))+1);
		SET i = 1;
		WHILE i <= occurances DO
		  SET splitted_name = (SELECT REPLACE(SUBSTRING(SUBSTRING_INDEX(r_name, '|', i),
			LENGTH(SUBSTRING_INDEX(r_name, '|', i - 1)) + 1), '|', ''));
		  INSERT INTO temp VALUES (r_id, splitted_name);
		  SET i = i + 1;
		END WHILE;
            END LOOP;
        CLOSE cur;
        SELECT * FROM temp;
        DROP TEMPORARY TABLE temp;
        
    END$$

DELIMITER ;