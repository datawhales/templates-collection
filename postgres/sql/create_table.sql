CREATE TABLE IF NOT EXISTS "iris_data" (
    id SERIAL PRIMARY KEY,
    sepal_length float8,
    sepal_width float8,
    petal_length float8,
    petal_width float8,
    target int
);
