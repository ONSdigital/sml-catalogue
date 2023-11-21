{
  title: 'Horvitz-Thompson Ratio Estimator',
  date: '2022-05-18',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Sample Design & Estimation',
    Theme: 'Sample Design & Estimation',
    Author: 'ONS',
    'Languages': 'Python/PySpark',
    "Release": "Not Released Yet",
  },
  additional_data: {
    "Release Status": "pending"
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/sample_design_and_estimation/estimation/ht_estimation.rst',
  description: |||
    Sampling in business surveys is often done using stratified simple random sampling
    without replacement. The largest businesses are usually selected with certainty.
    This SML method uses two approaches for estimating totals in such cases.
    The Horvitz-Thompson estimator in this case is known as a stratified expansion estimator,
    which is the simplest method used. We also use a combined ratio estimator. This is
    appropriate where there is a linear relationship through the origin between the target
    variable and an auxiliary variable we know for all units, and the scatter about the line
    increases with the size of the auxiliary variable.
  |||,
  additional_info: |||
    Links to the method code and specification are provided for further reading.
  |||,

}
