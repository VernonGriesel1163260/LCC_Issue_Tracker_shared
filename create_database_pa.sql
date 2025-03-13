USE `VernonGriesel116$LCC_Issue_Tracker_db`;

-- -----------------------------------------------------
-- Table `users`
-- -----------------------------------------------------
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `users` ;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password_hash` CHAR(60) NOT NULL,
  `email` VARCHAR(320) NOT NULL,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `location` VARCHAR(50) NOT NULL,
  `profile_image` VARCHAR(255),
  `role` ENUM('visitor', 'helper', 'admin') NOT NULL,
  `status` ENUM('active', 'inactive') NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `issues`
-- -----------------------------------------------------
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `issues` ;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE IF NOT EXISTS `issues` (
  `issue_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `summary` VARCHAR(255) NOT NULL,
  `description` TEXT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `status` ENUM('new', 'open', 'stalled', 'resolved') NOT NULL,
  PRIMARY KEY (`issue_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_issues_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comments`
-- -----------------------------------------------------
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `comments` ;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE IF NOT EXISTS `comments` (
  `comment_id` INT NOT NULL AUTO_INCREMENT,
  `issue_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `content` TEXT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`comment_id`),
  INDEX `issue_id_idx` (`issue_id` ASC) VISIBLE,
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_issue_id`
    FOREIGN KEY (`issue_id`)
    REFERENCES `issues` (`issue_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
