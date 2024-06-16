create table samplers(
	idno serial not null,
	sampler_id varchar(64) primary key not null,
	fullname varchar(64) not null,
	gender varchar(64) not null,
	bdate varchar(64) not null,
	address text not null,
	modified_date timestamp without time zone default now() not null
);

create table methods(
	idno serial not null,
	name varchar(64) primary key not null,
	procedure text not null,
	modified_date timestamp without time zone default now() not null
);

create table collected_data(
	data_idno serial not null,
	sampler_id varchar(64) not null,
	container_code varchar(64) primary key not null,
	tray_code varchar(64) not null,
	method_param varchar(64) not null,
	result_value varchar(64) not null,
	coordinates varchar(64) not null,
	address text not null,
	sampling_desc text not null,
	date_collection timestamp without time zone default now() not null
);

create table containers(
	prep_idno serial not null,
	serial_number varchar(64) not null,
	code varchar(64) primary key not null,
	volume varchar(64) not null,
	material varchar(64) not null,
	date_prepared timestamp without time zone default now() not null
);

create table receiving(
	processno serial not null,
	container_code varchar(64) not null,
	sample_code text primary key not null,
	description text not null,
	date_received timestamp without time zone default now() not null
);

select * from methods
select * from collected_data
select * from samplers
select * from containers
select * from receiving