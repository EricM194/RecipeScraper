CREATE PROCEDURE `sp_update_recipe`(
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
BEGIN
UPDATE
  recipes.recipe
SET
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
  last_modified_by = CURRENT_USER()
WHERE
  recipe_id = sp_recipe_id;
END