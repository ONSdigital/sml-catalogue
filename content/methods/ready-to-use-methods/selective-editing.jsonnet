{
  title: 'Selective Editing',
  date: '2022-06-29',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Editing & Imputation',
    Theme: 'Editing',
    Author: 'ONgggggS',
    'Languages': 'Python/Pandas',
    "Release": "v1.0.0"
  },
  additional_data: {
    "Release Status": "success",
    "Release Link": "https://github.com/ONSdigital/sml-python-small/releases/tag/1.0.0"
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/editing/selective_editing/methodological_specification.md',
  code_link: 'https://github.com/ONSdigital/sml-python-small/blob/main/sml_small/selective_editing.py',
  user_documentation_link: 'https://github.com/ONSdigital/sml-supporting-info/blob/main/method-info/selective-editing/selective_editing.md',
  description: |||
    Selective Editing is an internationally recognised editing method where potential errors are prioritised
    according to their expected effect on key outputs. Only respondents that are having an impact on published
    estimates will be recontacted.

    Selective Editing works by assigning a score to each important variable for a business where, the score
    reflects the impact that editing the respondent will have on the estimates. Only contributors with a high
    score are checked, low scoring contributors pass through unchecked.
  |||,
  additional_info: |||
    Links to the method code, specification and user documentation are provided for further reading.
  |||,
}
