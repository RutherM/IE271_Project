import apps.dbconnect as db
from datetime import datetime

def add_collected_data(si, cc, tc, mp, rv, co, ad, sa):
    sqlcode = """ INSERT INTO collected_data (
        sampler_id,
        container_code,
        tray_code,
        method_param,
        result_value,
        coordinates,
        address,
        sampling_desc,
        date_collection
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    md = datetime.now()
    db.modifydatabase(sqlcode, [si, cc, tc, mp, rv, co, ad, sa, md])

def add_methods(mn, mp):
    sqlcode = """ INSERT INTO methods (
        name,
        procedure,
        modified_date
    )
    VALUES (%s, %s, %s)"""
    md = datetime.now()
    db.modifydatabase(sqlcode, [mn, mp, md])

def add_containers(sn, co, vo, ma):
    sqlcode = """ INSERT INTO containers (
        serial_number,
        code,
        volume,
        material,
        date_prepared
    )
    VALUES (%s, %s, %s, %s, %s)"""
    dp = datetime.now()
    db.modifydatabase(sqlcode, [sn, co, vo, ma, dp])

def add_samplers(si, sn, sg, sb, sa):
    sqlcode = """ INSERT INTO samplers (
        sampler_id,
        fullname,
        gender,
        bdate,
        address,
        modified_date
    )
    VALUES (%s, %s, %s, %s, %s, %s)"""
    md = datetime.now()
    db.modifydatabase(sqlcode, [si, sn, sg, sb, sa, md])

def add_receiving(cc, sc, de):
    sqlcode = """ INSERT INTO receiving (
        container_code,
        sample_code,
        description,
        date_received
    )
    VALUES (%s, %s, %s, %s)"""
    md = datetime.now()
    db.modifydatabase(sqlcode, [cc, sc, de, md])

def get_methods():
    sql = 'SELECT * FROM methods'
    values = []
    colnames = ['id','name', 'procedure','date_modified']
    return db.querydatafromdatabase(sql, values, colnames);

def get_containers():
    sql = 'SELECT * FROM containers'
    values = []
    colnames = ['prepno','serial','code', 'volume', 'material','date_prepared']
    return db.querydatafromdatabase(sql, values, colnames);

def get_samplers():
    sql = 'SELECT * FROM samplers'
    values = []
    colnames = ['idno','id','name', 'gender','bdate','address','date_modified']
    return db.querydatafromdatabase(sql, values, colnames);

def get_data():
    sql = 'SELECT * FROM collected_data'
    values = []
    colnames = ['id','sampler_id','container_code', 'tray_code', 'parameter','value','coordinates','address','sampling_desc', 'date_collected']
    return db.querydatafromdatabase(sql, values, colnames);

def get_receiving():
    sql = 'SELECT * FROM receiving'
    values = []
    colnames = ['processno','container_code','sample_code', 'description','date_received']
    return db.querydatafromdatabase(sql, values, colnames);

