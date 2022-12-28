# Tests and test areas

## What tests exist?

### 1. Sml-catalogue portal has no test as it stands
### 2. Sml python small and the statistical methods library has tests written in pytest, unittest and has csv for mock data
   * Selective editing - Test fails with type error if no input.
   * Selective editing - Test type validation on the input dataframe(s).
   * Selective editing - Test type validation on the target column lists(s).
   * Selective editing - Test if cols missing from input dataframe(s).
   * Selective editing - Test if output is a dataframe (or the expected type)---
   * Selective editing - Test if output contents is as expected, both new columns and data content.
   * Selective editing - Test any other error based outputs
   * Selective editing - Test the question list validation.
   * Selective editing - Test the combination type validation.
   * Selective editing - Test column name params validation.
   * Selective editing - Test if cols missing from input dataframe.
   * Selective editing - Test if output is a dataframe.
   * Selective editing - Test if output contents is as expected, both new columns and data content.
   * Date adjustment - Test fails with type error if no input.
   * Date adjustment - Test type validation on the input dataframe(s).
   * Date adjustment - Test type validation on the target column lists(s).
   * Date adjustment - Test if cols missing from input dataframe(s).
   * Date adjustment - Test if output is a dataframe (or the expected type)---
   * Date adjustment - Test if output contents is as expected, both new columns and data content.
   * Date adjustment - Test any other error based outputs
   * Date adjustment - Test type validation on the input strings.
   * Date adjustment - Test fails with type error if no input.
   * Date adjustment - test type validation on the target column lists(s).
   * Date adjustment - test if output is a List.
   * Date adjustment - test if output contents is as expected.
   * Date adjustment - test fails with type error if no input.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test type validation on the target column list(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - test if output contents is as expected, both new columns and data content.
   * Date adjustment - test any other error based outputs.
   * Date adjustment - test fails with type error if no input.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test type validation on the target column lists(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - Test if output is as expected, both new columns being created and data content --
   * Date adjustment - test any other error based outputs.
   * Date adjustment - test fails with type error if no input.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - test if output contents is as expected, both new columns and data content.
   * Date adjustment - test any other error based outputs.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test type validation on the target column lists(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - test if output contents is as expected, both new columns and data content.
   * Date adjustment - test any other error based outputs.
   * Date adjustment - test fails with type error if no input.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test type validation on the target column lists(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - test if output contents is as expected, both new columns and data content.
   * Date adjustment - test any other error based outputs.
   * Date adjustment - test fails with type error if no input.
   * Date adjustment - test type validation on the input dataframe(s).
   * Date adjustment - test type validation on the target column lists(s).
   * Date adjustment - test if cols missing from input dataframe(s).
   * Date adjustment - test if output is a dataframe.
   * Date adjustment - test if output contents is as expected, both new columns and data content.
   * Date adjustment - test any other error based outputs.
   * Tests estimation - test type validation on the input dataframe(s).
   * Tests estimation - test validation fail if mismatched death cols.
   * Tests estimation - test validation fail if mismatched calibration cols.
   * Tests estimation - test if params not strings.
   * Tests estimation - test if params null.
   * Tests estimation - test validation fail if nulls in data.
   * Tests estimation - test if cols missing from input dataframe(s).
   * Tests estimation - test if references are duplicated in the input dataframe.
   * Tests estimation - test validation fail if mixed h values in a strata.
   * Tests estimation - test output is correct type.
   * Tests estimation - test no extra columns are copied to the output.
   * Tests estimation - test expected columns are in the output.
   * Tests estimation - test expected columns are in the output when default names aren't used.
   * Tests estimation - test valid scenarios.
   * Test Imputation - tests type validation on the input dataframe(s).
   * Test Imputation - tests type validation on the back_data dataframe(s).
   * Test Imputation - tests if cols missing from input dataframe(s).
   * Test Imputation - tests if dataframe has duplicate rows.
   * Test Imputation - tests if target missing from input dataframe(s).
   * Test Imputation - tests if params null.
   * Test Imputation - tests if output contents are as expected, both new columns and data.
   * Test Imputation - tests that when provided back data does not match input schema then fails.
   * Test Imputation - tests if when the back data input has link cols and the main data input does not then the columns are ignored.
   * Test Imputation - tests when main data input has link cols and the back data input does not then columns aren't lost.
   * Test Imputation - tests if columns of the incorrect type are caught.
   * Test Imputation - tests expected columns are in the output.
   * Test Imputation - tests Scenarios.
   * Test outliering - type validation on the input dataframe(s).
   * Test outliering - if params not strings.
   * Test outliering - if params null.
   * Test outliering - validation fail if mismatched calibration cols.
   * Test outliering - validation fail if nulls in data.
   * Test outliering - if cols missing from input dataframe(s).
   * Test outliering - if output contents are as expected, both new columns and data.
   * Test outliering - expected columns are in the output.

## What do we want to test (foundation suite of tests)?
### 1. Pytest testing behaviour tests
   * Help center tests
user guidance, code and specification link tests
   * Method links
   * Filter tests
   * Dropdown tests
   * Home button and banner links
   * Error pages and codes
### 2. Snapshot testing
   * Home page snapshot
   * Methods list and methods pages snapshot
   * Help center pages snapshot
### 3. Unit testing 
 This is difficult to pin down as there are a lot of tests already existing in sml-python-small and the statistical-methods-library which cover a wide range.

 Therefore, I believe it will be more worthwhile adding unit test tickets for future work development tickets, as and when we see the need instead of backdating tests or looking for tests that are missing.

 With regards to the sml-catalogue repo I think pytest BDD tests would be a better goal.

 For example, we can now approach a TDD process when developing tickets or we can make developer an test tickets when a business need is raised. I leave it to the team and ADM to decide which.


## How do we do this (test tools, methods and test results)?
   * Pytest
   * Unittest
   * Python
   * Generic sml-catalogue pytest BDD tests for UI frontend testing e.g method links and help center links 