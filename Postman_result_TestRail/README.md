# Reporting test results from Postman to TestRail.

Code to automatically report the results of tests performed in Postman to TestRail.
The test data comes from a csv file exported from TestRail.
This solution gives the possibility to edit test cases only in the documentation stored in TestRail tool.

For proper operation, you need to declare environment variables in Postman beforehand. The code from the files should be placed in the Postman *Pre-request Script* and *Tests* tabs.

***
### Pre-request Script
This code is designed to provide test case information and print it to the console. It includes the following details:

- Test Title
- Endpoint Name
- Test Case ID
- Expected Code
- Body Text

These details are extracted from the iteration data provided by Postman's collection runner and stored in collection variables for later use.

The code then defines a function named "print" that logs the above information to the console.

To use this code, you can simply copy and paste it into a *pre-request script* in Postman. Make sure that the iteration data in your collection runner includes values for `Title`, `Section`, `ID`, `Expected Result`, and `Steps`.

***
### Tests Script
This code is designed to test the response of an API request and post the result to TestRail. It includes the following functionality:

- Replacing environment and collection variables with their corresponding values
- Checking the status code of the API response and comparing it to an expected value
- Posting the test result to TestRail, including the test run ID, test case ID, version, status, and a message
- Unsetting collection variables after execution

The code first replaces collection and environment variables with their corresponding values. It then retrieves the status code of the API response and the expected code from collection variables. If the two values are equal, the test passes. If not, the test fails, and the response body is logged to the console.

The code then creates a request object to post the test result to TestRail. This object includes the test result status, version, and a message. The request object is sent to TestRail via a `pm.sendRequest` method.

After the test result is posted to TestRail, the collection variables are unset to prevent any conflicts with future tests.

To use this code, you can copy and paste it into the *Tests* tab in Postman. Make sure that your environment and collection variables are correctly set, including values for `title_of_test`, `env_version`, `testrail_url`, `clientAuthorization`, `test_run_id`, `test_case_id`, and `expected_code`. Once the test is run, the test result will be posted to TestRail and the collection variables will be unset after a delay of 2 seconds.

***
## Note
When the test is run, the information will also be printed on the console.

The code includes a setTimeout due to limitations on the number of requests that can be made to the TestRail API.

Please note that this code is not intended to be used as a standalone script and may need to be modified to suit your specific testing needs.
