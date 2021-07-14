CREATE TABLE nutrition (
  recipe_id int,
  amount NVARCHAR(255),
  name NVARCHAR(255),
  daily_value int,
  primary key (recipe_id, name),
  FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
);