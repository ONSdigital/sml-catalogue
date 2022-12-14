{
  title: 'Thousand pound correction',
  date: '2022-06-29',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Access type': 'Internal',
    'Expert group': 'Editing & Imputation',
    Theme: 'Editing',
    Author: 'ONS',
    Status: 'Approved for development',
    'Programming language': 'Python/Pandas',
    'Code available?': 'No',
  },
  specification_link: null,
  code_link: null,
  readme_link: null,
  description: 'The automatic editing method for thousand pounds correction is commonly used across ONS business surveys. It is a generic rule that uses user defined thresholds to automatically detect and correct thousand pounds errors. This is when the respondent should have reported values in thousands of pounds but has reported in actual pounds e.g., returned a value of £56,000 instead of correctly submitting 56. \n\n The method checks the ratio of a principal variable against a suitable predictor variable and make an automatic correction if the calculated ratio is around 1000. The automatic correction is applied to all relevant variables for the respondent.',
  additional_info: |||
    No resources are currently available.
  |||,
}
