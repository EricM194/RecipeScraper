CREATE PROCEDURE `sp_insert_recipe` (
  recipe_id INT,
  name NVARCHAR(255),
  category1 NVARCHAR(255),
  category2 NVARCHAR(255),
  category3 NVARCHAR(255),
  author NVARCHAR(255),
  rating DOUBLE,
  reviews INT,
  prep_time int,
  cook_time int,
  servings int,
  yield NVARCHAR(255)
)
INSERT INTO
  `recipes`.`recipe` (
    `recipe_id`,
    `name`,
    `category1`,
    `category2`,
    `category3`,
    `author`,
    `rating`,
    `reviews`,
    `prep_time`,
    `cook_time`,
    `servings`,
    `yield`,
    `created_date`,
    `created_by`,
    `last_modified_date`,
    `last_modified_by`
  )
VALUES
  (
    recipe_id,
    name,
    category1,
    category2,
    category3,
    author,
    rating,
    reviews,
    prep_time,
    cook_time,
    servings,
    yield,
    CURRENT_TIMESTAMP(),
    CURRENT_USER(),
    CURRENT_TIMESTAMP(),
    CURRENT_USER()
  );