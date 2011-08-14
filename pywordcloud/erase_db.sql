create user 'pywordcloud'@'localhost' identified by 'pywordcloud';

drop database pywordcloud if exists;
create database pywordcloud;
grant all privileges on pywordcloud.* to 'pywordcloud'@'localhost';