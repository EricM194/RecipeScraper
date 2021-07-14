CREATE PROCEDURE `sp_get_ingredients_by_id` (id int) BEGIN
SELECT
  `ingredient`.`recipe_id` AS 'ID',
  `ingredient`.`amount` AS 'Amount',
  `ingredient`.`measure` AS 'Measure',
  `ingredient`.`ingredient` AS 'Ingredient'
FROM
  `recipes`.`ingredient`
WHERE
  recipe_id = id;
END