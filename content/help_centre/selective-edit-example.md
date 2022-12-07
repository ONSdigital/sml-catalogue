1. Go to the GitHub repository containing the Selective Edit method, linked on the methods page and navigate to releases (https://github.com/ONSdigital/sml-python-small/releases) and find the release that you want.
2. Download the `.whl` (wheel) file.
3. On the command line run `pip install PATH_TO/sml_small-{version}-py-none-any.whl` where the path represents the location your computer that you downloaded the file.
4. The wheel should now be installed and available for use.
5. Import selective edit into your current python project. Within a python file type `from sml_small.selective_editing import selective_editing`
6. The method itself is run from this single controlling method above. This takes a Pandas dataframe and several reference columns as input. Full details of the input parameters can be found on the code page. (https://github.com/ONSdigital/sml-python-small/blob/main/sml_small/selective_editing.py).
7. At minimum you will require a Pandas dataframe, and details of the reference columns, these are 'reference_col', 'design_weight_col', 'threshold_col' and 'question_list. These are strings and an array of strings in the case of question_list which hold the names of the relevant columns within your dataset. To use the method run:  
`return val  = selective_editing(input_dataframe, reference_col, design_weight_col, threshold_col, question_list`.
8. return_val will now contain the contents of the original dataset with the additional results columns appended to it.