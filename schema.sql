CREATE TABLE universities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    state_province TEXT,
    alpha_two_code TEXT
);

CREATE TABLE university_domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    university_id INTEGER,
    domain TEXT,
    FOREIGN KEY (university_id) REFERENCES universities(id)
);

CREATE TABLE university_webpages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    university_id INTEGER,
    web_page TEXT,
    FOREIGN KEY (university_id) REFERENCES universities(id)
);

-- Índices para melhorar desempenho em JOINs e buscas por universidade
CREATE INDEX idx_university_domains_university_id ON university_domains(university_id);
CREATE INDEX idx_university_webpages_university_id ON university_webpages(university_id);