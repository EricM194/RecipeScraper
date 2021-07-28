CREATE PROCEDURE `sp_get_directions_by_id` (id int)
SELECT
  `direction`.`recipe_id` AS 'ID',
  `direction`.`step` AS 'Step',
  `direction`.`instruction` AS ' Instruction'
FROM
  `recipes`.`direction`
WHERE
  recipe_id = id
ORDER BY
  `direction`.`step`;