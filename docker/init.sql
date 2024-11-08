DROP USER IF EXISTS 'mechsimvault-server'@'%';
CREATE USER 'mechsimvault-server'@'%' IDENTIFIED BY 'Ohm@42@42@42@';
GRANT ALL PRIVILEGES ON mech_sim_db.* TO 'mechsimvault-server'@'%';
FLUSH PRIVILEGES;
