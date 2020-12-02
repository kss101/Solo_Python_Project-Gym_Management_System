DROP TABLE IF EXISTS fitness_class_member_bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE fitness_class_types;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE,
    membership_num INT,
    membership_type VARCHAR(255),
    is_active BOOLEAN
);

CREATE TABLE fitness_classes(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    duration INT,
    type VARCHAR(255),
    discription TEXT 
);

CREATE TABLE fitness_class_types(
    id SERIAL PRIMARY KEY,
    class_type VARCHAR(255)
);

CREATE TABLE fitness_class_member_bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitness_class_id INT REFERENCES fitness_classes(id) ON DELETE CASCADE
);