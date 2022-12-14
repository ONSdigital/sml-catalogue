{
  title: 'Ratio of Means',
  date: '2022-06-07',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Access type': 'Internal',
    'Expert group': 'Editing & Imputation',
    Theme: 'Imputation',
    Author: 'ONS',
    Status: 'In development',
    'Programming language': 'Python/PySpark',
    'Code available?': 'Yes',
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/imputation/ratio_of_means/methodological_specification.md',
  code_link: 'https://github.com/ONSdigital/statistical-methods-library/blob/main/statistical_methods_library/imputation/ratio_of_means.py',
  description: |||
    Ratio of means is a standard imputation method used for business surveys. The method imputes for each non-responding
    contributor a single numeric target variable within the dataset for multiple periods simultaneously. It uses the
    relationship between the target variable of interest and a predictive value and/or auxiliary variable to inform the
    imputed value. Due to its robust nature, it does not use any form of trimming or outliering.

    As imputation can be carried out for multiple periods simultaneously, the method can apply forward, backward or
    construction imputation. The type of imputation used will vary for each non-respondent in each period depending on
    whether data is available in the predictive period.
  |||,
  additional_info: |||
    Links to the method code and specification are provided for further reading.
  |||,

}
