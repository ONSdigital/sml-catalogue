function migrationFunction(migration, context) {
    migration.deleteContentType("test")
}
module.exports = migrationFunction;
