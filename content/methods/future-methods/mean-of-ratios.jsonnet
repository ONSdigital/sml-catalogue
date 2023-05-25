{
  title: 'Apple Counter',
  date: '2023-03-07',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Editing & Imputation',
    Theme: 'Imputation',
    Author: 'ONS',
    'Languages': 'Python/PySpark',
    "Release": "Not Released Yet"
  },
  additional_data: {
    "Release Status": "pending"
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/imputation/mean_of_ratios/technical_specification.md',
  description: |||
    Mean of Ratios imputation is a standard imputation method for business
    surveys. It can be used to impute value for unit (complete) non-response
    or item (partial) non-response. There is an option to use trimming as the
    method can be influenced by extreme values. The method imputes a single
    numeric variable. It uses the relationship between the variable being imputed
    and an appropriate predictive or auxiliary variable.

    As imputation can be carried out for multiple periods simultaneously, the method can apply forward, backward or
    construction imputation. The type of imputation used will vary for each non-respondent in each period depending on
    whether data is available in the predictive period.
  |||,
  additional_info: |||
    Links to the method code and specification are provided for further reading.
  |||,

}
