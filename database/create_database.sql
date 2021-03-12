DROP DATABASE IF EXISTS openfoodfacts;
CREATE DATABASE openfoodfacts;
USE openfoodfacts;


DROP TABLE IF EXISTS category;
CREATE TABLE category (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(200) UNIQUE,
  PRIMARY KEY (id)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS nutriscore;
CREATE TABLE nutriscore (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(1) UNIQUE,
  PRIMARY KEY (id)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS product;
CREATE TABLE product (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) UNIQUE,
  url VARCHAR(200) UNIQUE,
  nutriscore_id INT UNSIGNED,
  store VARCHAR(50),
  PRIMARY KEY (id),
  CONSTRAINT fk_product_nutriscore_id FOREIGN KEY (nutriscore_id) REFERENCES nutriscore(id)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS product_category;
CREATE TABLE product_category (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  product_id INT UNSIGNED,
  category_id INT UNSIGNED,
  PRIMARY KEY (id),
  CONSTRAINT fk_product_category_product_id FOREIGN KEY (product_id) REFERENCES product(id),
  CONSTRAINT fk_product_category_category_id FOREIGN KEY (category_id) REFERENCES category(id)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS substitute;
CREATE TABLE substitute (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  base_id INT UNSIGNED,
  substitute_id INT UNSIGNED,
  PRIMARY KEY (id),
  CONSTRAINT fk_substitute_base_id FOREIGN KEY (base_id) REFERENCES product(id),
  CONSTRAINT fk_substitute_substitute_id FOREIGN KEY (substitute_id) REFERENCES product(id)
) ENGINE=InnoDB;
