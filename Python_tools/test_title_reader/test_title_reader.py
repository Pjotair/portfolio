"""
This is a reader tool that reads automated test tuts and associated test case numbers.
It collects this data and saves it in a CSV file
E.g.

| Test Title        | TC-id-1  | TC-id-2  |
|-------------------|----------|----------|
| This is Title One | C001111  | C123456  |
| Two is Title      | C002222  |          |
| [x] Three is Title| C003333  | C333000  |

To run go in terminal to the path with this file:
e.g. cd test_title_reader

then run use
'python3 test_title_reader.py ../tests --output output_data'

Where:
`python3` indicates that execution will occur using python
`test_title_reader.py` is the indication of the script file
`../tests` is the indication of the directory (located above) with the test files (with the extension .ts)
`--output file_name` is an optional argument in which you can specify the name of the file if it is not named “output.csv”

You can also get directions in the terminal assuming you are in the directory with the
python3 test_title_reader.py -h
"""

import os
import re
import csv
import argparse

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"


def extract_data_from_ts_file(file_path: str) -> list[list[str]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        scenario_pattern = r"(Scenario|xScenario)\('([^']*)'\)\s*\{(.*?)\}"
        matches = re.findall(scenario_pattern, content, re.DOTALL)

        results = []
        for match in matches:
            scenario_type = match[0]
            title = match[1]
            body = match[2]

            if scenario_type == 'xScenario':
                title = f"[x] {title}"

            tc_ids = re.findall(r"\.tag\('([^']*)'\)", body)

            results.append([title] + tc_ids)
        return results


def process_ts_files_in_directory(directory: str) -> list[list[str]]:
    all_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ts'):
                file_path = os.path.join(root, file)
                extracted_data = extract_data_from_ts_file(file_path)
                all_data.extend(extracted_data)
    return all_data


def save_to_csv(data: list[list[str]], csv_file: str):
    if not data:
        print(RED + "No data to write." + RESET)
        return

    max_tc_columns = max([len(row) - 1 for row in data])
    headers = ['TC-title'] + [f'TC-id-{i + 1}' for i in range(max_tc_columns)]

    output_directory = "output-data"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    csv_file_path = os.path.join(output_directory, csv_file)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row + [''] * (max_tc_columns - len(row) + 1))
    print(GREEN + f"The data was saved to a file: {csv_file}" + RESET)


def main():
    parser = argparse.ArgumentParser(description='Extract the title of scenarios and TC-ids from .ts files.')
    parser.add_argument('directory', type=str, help='The directory to search for .ts files.')
    parser.add_argument('--output', type=str, default='output.csv', help='Output CSV file name (default: output.csv)')
    args = parser.parse_args()

    if not args.output.endswith('.csv'):
        args.output += '.csv'

    data = process_ts_files_in_directory(args.directory)
    save_to_csv(data, args.output)


if __name__ == "__main__":
    main()
