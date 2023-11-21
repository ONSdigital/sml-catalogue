{
  title: 'Winsorisation',
  date: '2022-05-18',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Sample Design & Estimation',
    Theme: 'Sample Design & Estimation',
    Author: 'ONS',
    'Languages': 'Python/PySpark',
    "Release": "Not Released Yet"
  },
  additional_data: {
    "Release Status": "pending"
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/specs_from_current_sml_pages/sample_design_and_estimation/Winsorisation/SML_Winsorization_Specification.docx.rst',
  description: |||
    In business surveys, some responses can be very large, and can distort estimates when such a
    business is selected.  Consequently, it is sometimes desirable to reduce the effect of these
    businesses.  This is known as outlier treatment.  This SML method applies a technique known
    as one-sided winsorisation.  The objective of the method is to introduce a small bias, while
    reducing the variance.  This is intended to reduce the mean squared error of the total, a
    measure of overall accuracy.  The method works for stratified expansion estimation and
    combined ratio estimation, which are commonly used in business surveys.
  |||,
  additional_info: |||
    Links to the method code and specification are provided for further reading.
  |||,
}
