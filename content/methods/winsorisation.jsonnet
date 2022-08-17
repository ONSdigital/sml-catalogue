{
  title: 'Winsorisation',
  date: '2022-05-18',
  contact_details: 'Sample.Design.Estimation.Business@ons.gov.uk',
  method_metadata: {
    'Access type': 'Internal',
    'Expert group': 'Sample Design & Estimation',
    Theme: 'Sample Design & Estimation',
    Author: 'ONS',
    Status: 'Complete',
    'Programming language': 'Python/PySpark',
    'Code available?': 'Yes',
  },
  specification_link: 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/specs_from_current_sml_pages/sample_design_and_estimation/Winsorisation/SML_Winsorization_Specification.docx.rst',
  code_link: 'https://github.com/ONSdigital/statistical-methods-library/blob/main/statistical_methods_library/outliering.py',
  description: |||
    Winsorisation (sometimes known as Winsorization) can be one-sided or two-sided. Usually one-sided Winsorisation,
    where large extreme values are outliered, is used for surveys in the ONS. This specification explains one-sided
    Winsorisation. Two sided Winsorisation is not recommended because it is not optimal in any way; the choice of
    L-value is subjective, thus two-sided Winsorisation equates to trimming.

    The method uses a pre-calculated parameter, ‘L-value’ (supplied by Methodology), to calculate a threshold for
    each return using one of two methods; the decision is founded on whether expansion estimation or (combined)
    ratio estimation is being used for the variable.

    If a return is deemed influential by the method (greater or lower than the calculated threshold), a new outlier
    weight, ‘o-weight’, is calculated which will reduce the value of the return, to the most extreme retained value,
    when subsequently grossed.

    An observation is considered influential if its value is correct, but its weighted contribution has an
    excessive effect on the estimated total or period-to-period change. Although influential values occur infrequently
    in economic surveys, if one appears and is not “treated,” it may introduce substantial over- or under-estimation
    of survey totals or period-to-period change. If the sample contains no influential values, the procedure is
    anti-conservative in that it adjusts values not considered influential to minimize the MSE (by reducing the
    variance). In contrast, the procedure can become very conservative depending on the degree of difference of the
    weighted influential value from the others in the sample. When the sample contains two or more influential values,
    Winsorisation detects and adjusts only the influential values and does not trim any values that are not influential.
  |||,

}
