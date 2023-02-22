const testTitle = pm.collectionVariables.replaceIn("{{title_of_test}}");
const envVersion = pm.collectionVariables.replaceIn("{{env_version}}");
const testRailUrl = pm.collectionVariables.replaceIn("{{testrail_url}}/add_result/{{test_case_id}}");
var statusCode = pm.response.code;
const expectedCode = pm.collectionVariables.replaceIn("{{expected_code}}");
const robotAuthorization = pm.environment.replaceIn("{{clientAuthorization}}");

console.log(testRailUrl)

pm.test(`${testTitle} and Verify status code: ${statusCode}`, () => {
    pm.expect(pm.response.code).to.eql(parseInt(expectedCode));
})

function ExecuteResult() {
    if (statusCode == expectedCode) {
    var testResult = 1;
    var message = "Test passed";
    } else {
    pm.expect(responseBody);
    console.log(responseBody);
    var odp = responseBody;
    var testResult = 5;
    var message = `Test failed, expected code: ${expectedCode}, \n but got status code: ${statusCode}.
    \n Response Body:" \n (${String(odp)})`;
    }

    const result = {
        url: testRailUrl,
        method: 'POST',
        header: {
            'Authorization': clientAuthorization,
            'Content-Type': 'application/json',
            'accept': '*/*',
            },

        body: {
            mode: 'raw',
            raw: JSON.stringify({"status_id": testResult, "version": envVersion, "comment": message}),
        }

    };
    pm.sendRequest(result, (error, response) => {
    console.log(error ? error : response.json());
    });
}
setTimeout(ExecuteResult, 2000);

function ClearVariables() {
    pm.collectionVariables.unset("title_of_test");
    pm.collectionVariables.unset("name_endpoint");
    pm.collectionVariables.unset("test_run_id");
    pm.collectionVariables.unset("test_case_id");
    pm.collectionVariables.unset("expected_code");
    pm.collectionVariables.unset("body_text");
}
setTimeout(ClearVariables, 2000);
