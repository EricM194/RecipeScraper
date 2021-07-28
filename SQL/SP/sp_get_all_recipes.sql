CREATE PROCEDURE `sp_get_all_recipes` () 
SELECT
  `recipe`.`recipe_id` AS 'ID',
  `recipe`.`name` AS 'Name',
  `recipe`.`category1` AS 'Category 1',
  `recipe`.`category2` AS 'Category 2',
  `recipe`.`category3` As 'Category 3',
  `recipe`.`author` AS 'Author',
  `recipe`.`rating` AS 'Rating',
  `recipe`.`reviews` AS 'Reviews',
  `recipe`.`prep_time` AS 'Prep time',
  `recipe`.`cook_time` AS 'Cook Time',
  `recipe`.`servings` AS 'Servings',
  `recipe`.`yield` AS 'Yield',
  `recipe`.`created_date` AS ' Created Date',
  `recipe`.`created_by` AS 'Created By',
  `recipe`.`last_modified_date` AS 'Last Modified Date',
  `recipe`.`last_modified_by` AS 'Last Modified By'
FROM
  `recipes`.`recipe`;