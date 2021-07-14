CREATE TABLE direction (
  recipe_id int,
  step INT,
  instruction text,
  primary key (recipe_id, step),
  FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
);