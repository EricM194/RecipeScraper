CREATE PROCEDURE `sp_get_nutrition_by_id` (id int)
SELECT
  `nutrition`.`recipe_id` AS 'ID',
  `nutrition`.`amount` AS 'Amount',
  `nutrition`.`name` AS 'Name',
  `nutrition`.`daily_value` AS 'Daily Value'
FROM
  `recipes`.`nutrition`
WHERE
  recipe_id = id;