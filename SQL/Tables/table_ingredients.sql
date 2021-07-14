CREATE TABLE ingredient (
  recipe_id int,
  amount float,
  measure NVARCHAR(255),
  ingredient NVARCHAR(255),
  FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
);