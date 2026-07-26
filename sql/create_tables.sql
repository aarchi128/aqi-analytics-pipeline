CREATE DATABASE aqi_project;
USE aqi_project;

-- Table 1: stations — one row per unique station
CREATE TABLE stations (
    station_id INT AUTO_INCREMENT PRIMARY KEY,
    station_name VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    UNIQUE (station_name, city)
);

-- Table 2: readings — one row per pollutant reading per station per fetch
CREATE TABLE readings (
    reading_id INT AUTO_INCREMENT PRIMARY KEY,
    station_id INT,
    pollutant_id VARCHAR(50),
    min_value DECIMAL(10,2),
    max_value DECIMAL(10,2),
    avg_value DECIMAL(10,2),
    last_update DATETIME,
    fetched_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (station_id) REFERENCES stations(station_id)
);