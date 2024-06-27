This folder stores data regarding environment management in Contentful. 

**Note that the data in this folder is auto-generated, and should not be edited manually.**

migration-log.txt contains a log of previously run commands involving content migration.

Using the scripts contentful_migrate.sh and contentful_rollback.sh, content can be moved between environments in Contentful via the command line.

During this process, the migration script will store an snapshot JSON of the source environment under the content-exports folder, and a backup JSON of the target environment in the rollbacks folder.
In order to perform the content migration, the migration script also generates a JavaScript file under the migrations folder. This file contains the required actions which update the target environment to the same content models as the source environment. Similarly, a JavaScript file is stored under the rollbacks folder which contains the required actions to revert the target environment back to its original state should a rollback be required.

When a migration is performed, the **content models** in the target environment are updated (**using the JavaScript file**) first to ensure they are consistent with the source environment.
Next, the **content entries** in the target environment are updated (**using the JSON file**) to match the source environment. 

A rollback is performed in the same way using the respective JavaScript and JSON file in the rollbacks folder.

Manual intervention may be required when a migration involves deleting a content type. This is because the Contentful CLI can't delete content entries. If you attempt to perform a migration (or rollback) that will require the deletion of a content type and its entries, you will be prompted to manually delete all the content entries relating to that content model in the relevant environment. The migration (or rollback) can then continue normally.
**Content models can only be deleted by the migration scripts when they contain no entries.**