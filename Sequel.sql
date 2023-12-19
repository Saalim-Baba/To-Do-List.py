CREATE DATABASE IF NOT EXISTS todo_list;

-- Verwende die erstellte Datenbank
USE todo_list;

-- Erstelle eine Tabelle für die To-Do-Liste
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY,
    task_description TEXT,
    task_status TEXT
);