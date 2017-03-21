BEGIN;
--
-- Create model Choice
--
CREATE TABLE "exams_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL);
--
-- Create model Question
--
CREATE TABLE "exams_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Tag
--
CREATE TABLE "exams_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tag_text" varchar(200) NOT NULL, "question_id" integer NOT NULL REFERENCES "exams_question" ("id"));
--
-- Add field question to choice
--
ALTER TABLE "exams_choice" RENAME TO "exams_choice__old";
CREATE TABLE "exams_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "question_id" integer NOT NULL REFERENCES "exams_question" ("id"));
INSERT INTO "exams_choice" ("id", "choice_text", "question_id") SELECT "id", "choice_text", NULL FROM "exams_choice__old";
DROP TABLE "exams_choice__old";
CREATE INDEX "exams_tag_7aa0f6ee" ON "exams_tag" ("question_id");
CREATE INDEX "exams_choice_7aa0f6ee" ON "exams_choice" ("question_id");
COMMIT;
