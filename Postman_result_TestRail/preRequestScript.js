// Title of test
const downloadTestTitle = pm.iterationData.get("Title");
pm.collectionVariables.set("title_of_test", downloadTestTitle);

// Endpoint name
const nameEndpoint = pm.iterationData.get("Section");
pm.collectionVariables.set("name_endpoint", nameEndpoint);
let iterationNumber = (pm.info.iteration + 1);

// Test Case ID
const testCaseId = pm.iterationData.get("ID");
let catCaseId = testCaseId.substr(1);
pm.collectionVariables.set("test_case_id", catCaseId);

// Expected Code
const expectedCode = pm.iterationData.get("Expected Result");
pm.collectionVariables.set("expected_code", expectedCode);

// body_text
let bodyText = pm.iterationData.get("Steps");
pm.collectionVariables.set("body_text", bodyText);

function print () {
    console.log(`iteration: ${iterationNumber} | Expected code: ${expectedCode} |
    Start testing: ${nameEndpoint.slice(0,-12)}${bodyText}`);
}

setTimeout(print, 2000);
