{
  title: 'Thousand Pound Correction',
  date: '2022-06-29',
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
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/editing/thousand_pounds_correction/thousand_pounds_correction.md',
  code_link: 'https://github.com/ONSdigital/sml-python-small/blob/main/sml_small/editing/thousand_pounds/thousand_pounds.py',
  user_documentation_link: 'https://github.com/ONSdigital/sml-supporting-info/blob/main/method-info/thousand-pound-correction/thousand_pound_correction.md',
  description: |||
    The automatic editing method for thousand pounds correction is
    commonly used across ONS business surveys. It is a generic rule
    that uses user defined thresholds to automatically detect and correct
    thousand pounds errors. This is when the respondent should have
    reported values in thousands of pounds but has reported in actual
    pounds e.g., returned a value of £56,000 instead of correctly
    submitting 56.

    The method checks the ratio of a principal variable
    against a suitable predictor variable and makes an automatic correction
    if the calculated ratio is around 1000. The automatic correction is
    applied to all relevant variables for the respondent.
   |||,
  additional_info: |||
    Links to the method code, specification and user documentation are provided for further reading.
  |||,
}
