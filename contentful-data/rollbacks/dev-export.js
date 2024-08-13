function migrationFunction(migration, context) {
    const test = migration.createContentType("test");
    test
        .displayField("test")
        .name("test")
        .description("test")

    const testTest = test.createField("test");
    testTest
        .name("test")
        .type("Symbol")
        .localized(false)
        .required(false)
        .validations([])
        .disabled(false)
        .omitted(false)

    const testTest1 = test.createField("test1");
    testTest1
        .name("test1")
        .type("Symbol")
        .localized(false)
        .required(false)
        .validations([])
        .disabled(false)
        .omitted(false)
    test.changeFieldControl("test", "builtin", "singleLine")
    test.changeFieldControl("test1", "builtin", "singleLine")
}
module.exports = migrationFunction;
