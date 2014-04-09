Insert some clever text here.\n

test of change


DEVELOPMENT NOTES

- Fabric tutorial
http://www.yaconiello.com/blog/deploying-django-site-fabric/

- To rename the apps in remote
. git pull
. dump sql of all exteriors tables
. delete all exteriors tables (disable foreignkey check http://gauravsohoni.wordpress.com/2009/03/09/mysql-disable-foreign-key-checks-or-constraints/)
. delete all exteriors migrations in table and in files in exteriors app
. schemamigration assemblees, consell, membres
. migrate assemblees, consell, membres

Migrate new Users structure:
- schemamigrate users (inital), xarxacat_site (auto)
- migrate users, xarxacat_site