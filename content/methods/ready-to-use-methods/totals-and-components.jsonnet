{
  title: 'Totals and Components',
  date: '2023-03-07',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Editing & Imputation',
    Theme: 'Editing',
    Author: 'ONS',
    'Languages': 'Python/Pandas',
    "Release": "v1.1.0"
  },
  additional_data: {
    "Release Status": "success",
    "Release Link": "https://github.com/ONSdigital/sml-python-small/releases/tag/1.1.0"
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/totals_components/editing_and_imputation/totals_components.md',
  code_link: 'https://github.com/ONSdigital/sml-python-small/tree/main/sml_small/editing/totals_and_components',
  user_documentation_link: 'https://github.com/ONSdigital/sml-supporting-info/blob/main/method-info/totals-and-components/totals-and-components.md',
  description: |||
    The automatic editing method for totals and components correction is currently used in ONS business surveys to ensure fixed relationships between variables are satisfied. For example, when a total (e.g., total employment) is collected along with the component breakdown (e.g., full-time male, full-time female, part-time male, part-time female).
    The primary use of the method is to automatically detect and correct errors in respondent data where fixed relationships have not been satisfied to improve the efficiency of the editing process, reduce the burden on respondents and survey validators and improve overall data quality.
    This method can also be used to ensure fixed relationships between variables are satisfied in other data types such as imputed data to improve overall data quality.
  |||,
  additional_info: |||
    Links to the method code and specification are provided for further reading.
  |||,
}
