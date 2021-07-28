CREATE PROCEDURE `sp_insert_direction` (
  recipe_id int,
  step INT,
  instruction text
)
INSERT INTO
  `recipes`.`direction` (
    `recipe_id`,
    `step`,
    `instruction`
  )
VALUES
  (recipe_id, step, instruction);