tests = {'id': 'selective-editing', 'name': 'Selective Editing', 'theme': 'Editing', 'expert_group': 'Editing & Imputation', 'language': 'Python/ Pandas', 'access': 'Internal', 'author': 'ONS', 'description': 'Selective Editing is an internationally recognised editing method where potential errors are prioritised according to their expected effect on key outputs. Only respondents that are having an impact on published estimates will be recontacted.\n\nSelective Editing works by assigning a score to each important variable for a business where, the score reflects the impact that editing the respondent will have on the estimates. Only contributors with a high score are checked, low scoring contributors pass through unchecked.', 'contact_details': 'smlhelp@ons.gov.uk', 'code_available': True, 'status': ['Complete'], 'additional_information': 'Links to the method code, specification and user documentation are provided for further reading.', 'code_link': 'https://github.com/ONSdigital/sml-python-small/blob/main/sml_small/selective_editing.py', 'specification_link': 'https://github.com/ONSdigital/Statistical-Method-Specifications/blob/main/editing_and_imputation/editing/selective_editing/methodological_specification.md', 'user_documentation_link': 'https://github.com/ONSdigital/sml-python-small/blob/main/docs/selective_editing.md'}
for k, v in tests.items():
    if isinstance(tests[k], list):
        print("List hit", v[0])
        tests[k] = v[0]

print(tests)
    # print(k, v)
# status = tests["status"]
# print(isinstance(status, list))