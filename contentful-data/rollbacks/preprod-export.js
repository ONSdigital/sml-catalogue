function migrationFunction(migration, context) {
    const helpCentreInformation = migration.editContentType("helpCentreInformation");
    const helpCentreInformationHelpCentreCategory = helpCentreInformation.deleteField("help_centre_category");
}
module.exports = migrationFunction;
