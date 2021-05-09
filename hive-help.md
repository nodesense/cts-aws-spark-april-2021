
remove meta data store

cd $HIVE_HOME


 rm -rf metastore_db/


Create a new one

$HIVE_HOME/bin/schematool -initSchema -dbType derby
