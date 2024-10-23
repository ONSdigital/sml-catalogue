function migrationFunction(migration, context) {
    const helpCentreInformation = migration.editContentType("helpCentreInformation");
    const helpCentreInformationHelpCentreCategory = helpCentreInformation.createField("help_centre_category");
    helpCentreInformationHelpCentreCategory
        .name("Category")
        .type("Symbol")
        .localized(false)
        .required(true)
        .validations([{ "in": ["Information", "Access (and usage)", "Feedback", "Support"], "message": "Please select a category from the drop down menu" }])
        .disabled(false)
        .omitted(false)
    helpCentreInformation.changeFieldControl("help_centre_category", "builtin", "dropdown", {})
}
module.exports = migrationFunction;
