CREATE PROCEDURE `sp_upsert_recipe` (
  sp_recipe_id INT,
  sp_name NVARCHAR(255),
  sp_category1 NVARCHAR(255),
  sp_category2 NVARCHAR(255),
  sp_category3 NVARCHAR(255),
  sp_author NVARCHAR(255),
  sp_rating DOUBLE,
  sp_reviews INT,
  sp_prep_time int,
  sp_cook_time int,
  sp_servings int,
  sp_yield NVARCHAR(255)
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
    sp_recipe_id,
    sp_name,
    sp_category1,
    sp_category2,
    sp_category3,
    sp_author,
    sp_rating,
    sp_reviews,
    sp_prep_time,
    sp_cook_time,
    sp_servings,
    sp_yield,
    CURRENT_TIMESTAMP(),
    CURRENT_USER(),
    CURRENT_TIMESTAMP(),
    CURRENT_USER()
  ) ON DUPLICATE KEY
UPDATE
  name = sp_name,
  category1 = sp_category1,
  category2 = sp_category2,
  category3 = sp_category3,
  author = sp_author,
  rating = sp_rating,
  reviews = sp_reviews,
  prep_time = sp_prep_time,
  cook_time = sp_cook_time,
  servings = sp_servings,
  yield = sp_yield,
  last_modified_date = CURRENT_TIMESTAMP(),
  last_modified_by = CURRENT_USER();