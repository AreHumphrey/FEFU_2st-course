CREATE TABLE Notes (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Note TEXT UNIQUE NOT NULL,
  TimeOfCreation DATETIME NOT NULL,
  ProgressMade REAL DEFAULT 0 CHECK (ProgressMade >= 0 AND ProgressMade <= 1),
  Status TEXT DEFAULT 'started' CHECK (Status IN ('started', 'accepted', 'canceled'))
);
