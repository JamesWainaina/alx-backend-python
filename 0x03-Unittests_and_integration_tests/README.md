# 0x03. Unittests and Integration Tests

## Overview
This project covers the fundamentals of Unit and Integration Testing in Python. It emphasizes the importance of testing individual functions and the interaction between various parts of the codebase. 

## Unit Testing
Unit testing is the process of testing individual functions to ensure they return expected results for a variety of inputs, including standard inputs and edge cases. A unit test should focus solely on the logic within the function being tested. External dependencies, especially those involving network or database calls, should be mocked.

The primary goal of a unit test is to verify that a function works as expected under the assumption that everything outside the function is functioning correctly.

## Integration Testing
Integration tests are designed to test the complete code path end-to-end. Unlike unit tests, integration tests focus on the interactions between different parts of the code. While low-level functions that make external calls (e.g., HTTP requests, file I/O, database I/O) are mocked, the goal is to ensure that the various components work together as intended.

## Execution
To execute your tests, use the following command:
```bash
$ python -m unittest path/to/test_file.py

