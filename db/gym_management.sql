DROP TABLE IF EXISTS fitness_class_member_bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS fitness_classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE,
    membership_num INT
);

CREATE TABLE fitness_classes(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    type VARCHAR(255)   
);

CREATE TABLE fitness_class_member_bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    fitness_class_id INT REFERENCES fitness_classes(id)
);