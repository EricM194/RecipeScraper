CREATE PROCEDURE `sp_insert_ingredient` (
  recipe_id int,
  amount float,
  measure NVARCHAR(255),
  ingredient NVARCHAR(255)
)
INSERT INTO
  `recipes`.`ingredient` (
    `recipe_id`,
    `amount`,
    `measure`,
    `ingredient`
  )
VALUES
  (recipe_id, amount, measure, ingredient);