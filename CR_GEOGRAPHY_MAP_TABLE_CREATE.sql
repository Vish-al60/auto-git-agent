CREATE TABLE CR_GEOGRAPHY_MAP (
    ID INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique auto-increment ID for each location point',
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Timestamp when the data was recorded',
    lat DECIMAL(9,6) COMMENT 'Latitude coordinate to plot the point on the map',
    lon DECIMAL(9,6) COMMENT 'Longitude coordinate to plot the point on the map',
    fuelLevel DECIMAL(5,2) COMMENT 'Current fuel level of the vehicle or asset',
    speed DECIMAL(6,2) COMMENT 'Current speed of the vehicle or asset in km/h',
    NAME VARCHAR(100) COMMENT 'Name or identifier of the vehicle or asset',
    UUID VARCHAR(50) COMMENT 'Unique universal identifier for tracking the vehicle or asset'
)
