create table if not exists project(id char(32) primary key not null, project_type char(32), project_name nvarchar(256) not null, display_name nvarchar(256), create_time datetime not null,resource_path nvarchar(512) not null, thumbnail_path nvarchar(512) not null)

create table if not exists stuff(id char(32) primary key not null, project_id char(32) not null, stuff_name nvarchar(256) not null, display_name nvarchar(256), width int, height int, ext_name varchar(8), stuff_path nvarchar(512) not null, thumbnail_path nvarchar(512) not null) 

create table if not exists tag(stuff_id char(32) not null, tag_name nvarchar(32) not null)

create table if not exists log(id integer primary key not null, project_id char(32) not null, stuff_id char(32) not null, username nvarchar(32), user_ip varchar(36) not null, action_type char(8) not null, action_content nvarchar(512) not null, action_time datatime not null)

create table if not exists piclib(sys_name nvarchar(32), create_time datetime, resource_time datetime, refresh_time datetime)

insert into piclib (create_time) values (datetime('now','localtime'))
