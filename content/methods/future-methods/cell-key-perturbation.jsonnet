{
  title: 'Cell Key Perturbation',
  date: '2024-02-26',
  contact_details: 'smlhelp@ons.gov.uk',
  method_metadata: {
    'Expert group': 'Statistical Disclosure Control',
    Theme: 'Statistical Disclosure Control',
    Author: 'ONS Community Method',
    'Languages': 'Python & R',
    "Release": "Not Released Yet"
  },
  additional_data: {
    "Release Status": "pending"
  },
  description: |||
    Cell-key Perturbation adds small amounts of noise to frequency tables, to protect against disclosure. Noise is added to change the counts that appear in the frequency table by small amounts, for example a 14 is changed to a 15. This noise introduces uncertainty in the counts and makes it harder to identify individuals, especially when taking the ‘difference’ between two similar tables. An input file called a ‘ptable’ is needed which specifies the level of perturbation. These can also be used to apply rounding, and a threshold for small counts.
  |||,
}
