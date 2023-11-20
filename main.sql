--------------------------------------------------
-- Section USERS
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id                     TEXT    UNIQUE NOT NULL,
    user_created_at             TEXT    NOT NULL,  
    user_firstname              TEXT    NOT NULL, 
    user_lastname               TEXT    DEFAULT "",
    user_email                  TEXT    UNIQUE NOT NULL,
    user_password               TEXT    NOT NULL,
    user_tasks_created          TEXT    DEFAULT 0,
    user_tasks_assigned         TEXT    DEFAULT 0,
    user_role                   TEXT    DEFAULT 1,
    user_birthdate              TEXT,
    user_verification_key       TEXT    NOT NULL,
    user_verified_at            TEXT    DEFAULT 0,
    user_inactivation_key       TEXT    DEFAULT 0,
    user_inactive               TEXT    DEFAULT 0,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;

--------------------------------------------------
--- Section TASKS

DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks(
    task_id                     TEXT    UNIQUE NOT NULL,
    task_created_at             TEXT    NOT NULL,
    task_title                  TEXT    NOT NULL,
    task_description            TEXT    NOT NULL,
    task_due_date               TEXT    NOT NULL,
    task_visibility             TEXT    INTEGER DEFAULT 0,
    task_image                  TEXT    NULL,
    task_assigned_users         TEXT    INTEGER DEFAULT 0,
    PRIMARY KEY(task_id) 
)WITHOUT ROWID;


-- --------------------------------------------------
-- -- Section TASKS_ASSIGNMENTS

DROP TABLE IF EXISTS tasks_assignments;
CREATE TABLE tasks_assignments(
    task_assignment_user_fk     TEXT,
    task_assignment_task_fk     TEXT,
    PRIMARY KEY(task_assignment_user_fk, task_assignment_task_fk)
)WITHOUT ROWID;