CREATE PROCEDURE `sp_insert_nutrition` (
  recipe_id int,
  amount float,
  name NVARCHAR(255),
  daily_value int
)
INSERT INTO
  `recipes`.`nutrition` (
    `recipe_id`,
    `amount`,
    `name`,
    `daily_value`
  )
VALUES
  (recipe_id, amount, name, daily_value);