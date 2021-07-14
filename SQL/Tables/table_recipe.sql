CREATE TABLE recipe (
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
  yield NVARCHAR(255),
  created_date DATETIME,
  created_by NVARCHAR(255),
  last_modified_date DATETIME,
  last_modified_by NVARCHAR(255),
  primary key (recipe_id)
);