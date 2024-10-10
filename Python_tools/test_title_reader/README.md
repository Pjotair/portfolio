# Test Title Reader

This is a reader tool that reads automated test tuts and associated test case numbers.
It collects this data and saves it in a CSV file.
<br>E.g.

| Test Title        | TC-id-1  | TC-id-2  |
|-------------------|----------|----------|
| This is Title One | C001111  | C123456  |
| Two is Title      | C002222  |          |
| [x] Three is Title| C003333  | C333000  |


To run go in terminal to the path with this file:
e.g.
```zsh
cd test_title_reader
```

then run
```zsh
python3 test_title_reader.py ../tests --output output_data
```

Where:<br>
`python3` indicates that execution will occur using python
`test_title_reader.py` is the indication of the script file
`../tests` is the indication of the directory (located above) with the test files (with the extension .ts)
`--output file_name` is an optional argument in which you can specify the name of the file if it is not named “output.csv”

You can also get directions in the terminal assuming you are in the directory with the 
```zsh
python3 test_title_reader.py -h
```
