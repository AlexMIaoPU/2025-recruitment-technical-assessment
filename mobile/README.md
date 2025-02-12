# DevSoc Subcommittee Recruitment: Freerooms Mobile Development 

## **⚠️ IMPORTANT ⚠️**

This assessment is optional when applying for Freerooms. You may complete the project-agnostic frontend/backend assessment instead, particularly if you are also interested in applying for other projects.

If you aren't appplying for any other projects, and you are specifically interested in mobile development with Freerooms, we recommend completing this assessment. In this case you do not need to complete any other assessment.

## Overview
This assessment contains unit tests for the `BuildingLoader` in the Freerooms iOS application. This object fetches an array of `Building` from a hypothetical backend.

The aim is to implement the `BuildingLoader` in a Test Driven Development (TDD) flow, ensuring that it correctly handles network requests, errors, and data processing when fetching building information to use within the app.

## Requirements

It is highly recommended to complete this task using Xcode on a Mac. Code can be written on Windows but running the tests will require a Mac - in particular, you will need to have at least version 16.0 of Xcode to run tests.

## Instructions

We've provided you with an incomplete `BuildingLoader` implementation, which should use an `HttpClient` to make the request for buildings from the backend. A `MockHttpClient` in the tests performs the request and returns the data for an array of `RemoteBuilding`. This is the type of the payload returned from the hypothetical backend for this assessment. Do **not** change anything in `RemoteBuilding`.

Appropriate tests to guide and validate your implementation have been provided in FreeroomsAssessmentTests. You need to make all the tests pass, one by one, by implementing the `fetchBuildings` method in the existing `BuildingLoader` class. These tests must **all pass** for the recruitment task to be considered complete.


1) Fork the latest version of the assessment repo. Here's <a href="https://guides.github.com/activities/forking" target="_blank">how forking works</a>.

2) Open the `FreeroomAssessment.xcodeproj` project on Xcode 16.0 or later.
	- Older Xcode versions will not support running the tests.

3) There are two main folders in the project:
	- The `FreeroomsAssessment` folder contains the production types, including the `BuildingLoader` and dependencies for requesting and loading the feed remotely.
		- ⚠️ Important ⚠️: **You can create new files, but from the starting files you can only change the `BuildLoader.swift` file to implement the `fetchBuildings` method. Do not change the signature of the `fetchBuildings` method.**
		- Do not change any other files in the folder.
	- The `FreeroomsAssessmentTests` folder contains the test cases.
		- ⚠️ Important ⚠️: **You should only be uncommenting tests in the `FreeroomsBuildingAPITests.swift` file to implement all test cases. Do not change or delete any tests.**
		- Do not change any other files in the test folder.
	- Do not change any project settings, including scheme settings.
	- Do not change the indentation in the project.
	- Do not rename the existing classes and files.

4) Use `FreeroomsAssessmentTests/FreeroomsBuildingAPITests.swift` to validate your implementation.
	- Uncomment (CMD+/) and implement one test at a time following the TDD process:
		- Make the test pass, commit, refactor if required, commit, and move to the next one.
	- While developing your solutions, you can run all tests either in Xcode or from the command line:
        - In Xcode use the shortcut CMD+U or run the tests from Product > Test in the menu bar up top. Make sure that the FreeroomsAssessmentTests scheme is selected like so:
        ![](xcode-test-scheme.jpg)
        - In the `/freerooms mobile` folder run the command `xcodebuild test -scheme FreeroomsAssessmentTests` (note that this method may be slower due to code signing)

5) Errors should be handled accordingly.
	- There shouldn't be *any* force-unwrap `!` or `fatalError` in your implementation (this excludes all the testing code).
	- There shouldn't be empty `catch` blocks.
	- There shouldn't be any `print` statements, such as `print(error)`.

6) The `Building` struct should *not* implement `Decodable` - even in extensions.
	- That's because the `CodingKeys` to decode the JSON are API-specific details defined in the backend. So declaring the `CodingKeys` in the `Building` will couple it with API implementation details. And since other modules depend on the `Building`, they'll also be coupled with API implementation details.
	- We suggest mapping from a `RemoteBuilding` to `Building`

7) Make careful and proper use of access control (e.g. marking as `private` any implementation details that aren’t referenced from other external components).

8) When all tests are passing and you're done implementing your solution:
	- Review your code and make sure it follows **all** the instructions above.
		- If it doesn't, make the appropriate changes, push, and review your code again.
	- If it does, you are good for submission!

## Marking Guidelines
There are no exact marks associated with getting specific tests to pass. Your implementation will be judged based on the following guidelines:

1) Aim to commit your changes every time you add/alter the behavior of your system or refactor your code. A general rule you can follow in this task is to make the test pass, commit, refactor if required, commit, and move to the next test.

2) Aim for descriptive commit messages that clarify the intent of your contribution; they should help with understanding your train of thought and the purpose of changes.

3) The system should always be in a green state, meaning that in each commit all uncommented tests should be passing.

4) The project should build without warnings.

5) The code should be carefully organized and easy to read (e.g. indentation must be consistent).

6) Comments are acceptable but you should firstly aim to write self-documenting code by providing context and detail when naming your components. Avoid any lengthy explanations in comments.
 
## Submission

To submit, push your solutions to your forked repo and submit a link to the fork in the application form.

## Additional comment

As there are limited opportunities to gain mobile development experience outside of self-study or work, we are open to candidates of varying experiences and abilities. The most important attributes are curiosity and willingness to self-teach/learn. We will provide the training and guidance to make meaningful contributions to the codebase. Therefore, if you find this exercise difficult, do not be disheartened - please make an attempt.