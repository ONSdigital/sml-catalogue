{
  title: 'Selective Editing',
  date: '2022-06-29',
  contact_details: 'Editing.and.Imputation.expert.group@ons.gov.uk',
  method_metadata: {
    'Access type': 'Internal',
    'Expert group': 'Editing & Imputation',
    Theme: 'Editing',
    Author: 'ONS',
    Status: 'Complete',
    'Programming language': 'Python/Pandas',
    'Code available?': 'Yes',
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/editing/selective_editing/methodological_specification.md',
  code_link: 'https://github.com/ONSdigital/sml-python-small/blob/main/sml_small/selective_editing.py',
  description: |||
    Selective Editing is an internationally recognised editing method where potential errors are prioritised
    according to their expected effect on key outputs. Only respondents that are having an impact on published
    estimates will be recontacted.

    Selective Editing works by assigning a score to each important variable for a business where, the score
    reflects the impact that editing the respondent will have on the estimates. Only contributors with a high
    score are checked, low scoring contributors pass through unchecked.
  |||,

}
