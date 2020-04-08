pg_host="192.168.7.38"
pg_user="ent.prd"
pg_pass="Viscovery-2019"
pg_db="vcms"
if [ "$1" = "insert_service_data" ]
  then
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "insert into system_recognition_services (service_name,service_type) values('"$2"','Embedding');"
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "select sn,service_name from system_recognition_services order by sn;"
fi
if [ "$1" = "check_service_data" ]
  then
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "
select company_services.sn as service_sn,
       companies.company_name,
       system_recognition_services.service_name 
from company_services 
left join companies on companies.sn=company_services.company_sn
left join system_recognition_services on system_recognition_services.sn=company_services.service_sn
order by company_services.sn;"
read -p "Select service_sn: " service_sn
echo "service_sn : "$service_sn
PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "select count(sn) as total from company_product_image_features where service_sn='"$service_sn"';"
fi
if [ "$1" = "backup" ]
  then
  apt-get update -y && apt-get install -y postgresql
  file_name=$(date +%Y%m%d)
  echo "backup is starting. file name : "$file_name
  PGPASSWORD=$pg_pass pg_dump -h $pg_host -U $pg_user -d $pg_db > "vcms_"$file_name".sql"
  echo "backup is done!"
fi
if [ "$1" = "clean_feature_data" ]
  then
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "
select company_services.sn as service_sn,
       companies.company_name,
       system_recognition_services.service_name
from company_services
left join companies on companies.sn=company_services.company_sn
left join system_recognition_services on system_recognition_services.sn=company_services.service_sn
order by company_services.sn;"
  read -p "Select service_sn for clean feature data: " service_sn
  echo "service_sn for clean : "$service_sn
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "select count(sn) as reset_image_total from company_product_images where service_sn='"$service_sn"';"
  echo "data is reseting...."
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "
update company_product_images 
set bbox_totals = 0,
    detection_send_mark = 0,
    detection_send_time = null,
    detection_finish_mark = 0,
    detection_finish_time = null,
    feature_extraction_send_mark = 0,
    feature_extraction_send_time = null,
    feature_extraction_finish_mark = 0,
    feature_extraction_finish_time = null
where service_sn='"$service_sn"';"
  echo "service data is reseted!"
  PGPASSWORD=$pg_pass psql -h $pg_host -U $pg_user -d $pg_db -c "delete from company_product_image_features where service_sn='"$service_sn"';"
  ecoh "feature is clear"
fi
if [ "$1" = "rebuild_feature_data" ]
  then
  echo "detection and feature_extraction is starting....."
  cd /opt/vcms && python3 crontabs.py batch_detection_feature 0
  echo "detection and feature_extraction is done!"
fi
