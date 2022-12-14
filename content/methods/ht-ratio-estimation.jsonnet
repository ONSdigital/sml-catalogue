{
  title: 'HT/Ratio Estimation',
  date: '2022-05-18',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Access type': 'Internal',
    'Expert group': 'Sample Design & Estimation',
    Theme: 'Sample Design & Estimation',
    Author: 'ONS',
    Status: 'In development',
    'Programming language': 'Python/PySpark',
    'Code available?': 'Yes',
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/sample_design_and_estimation/estimation/ht_estimation.rst',
  code_link: 'https://github.com/ONSdigital/statistical-methods-library/blob/main/statistical_methods_library/estimation/ht_ratio.py',
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
    Below are some links that will help you further understand the method. 
    
    The code link takes you to the repo while the specification link take you to some further reading.
  |||,

}
