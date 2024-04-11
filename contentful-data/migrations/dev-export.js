function migrationFunction(migration, context) {
    const test = migration.createContentType("test");
    test
        .displayField("test")
        .name("test")
        .description("")

    const testTest = test.createField("test");
    testTest
        .name("test")
        .type("Symbol")
        .localized(false)
        .required(false)
        .validations([])
        .disabled(false)
        .omitted(false)
    test.changeFieldControl("test", "builtin", "singleLine")
}
module.exports = migrationFunction;
