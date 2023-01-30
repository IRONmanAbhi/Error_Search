# Error_Search README

It searches the stack overflow for the error occured in the python code and opens few tabs in your browser of all the solution present for similar error on stack overflow. Stack over API is being used to fetch the questions and solutions.

## Features

Searches the stack overflow for the error generated in python program while running.
To understand how to use the extension read the "Extension Usage" below.

## Requirements

- certifi = ^2022.12.7
- charset-normalizer = ^3.0.1
- idna = ^3.4
- packaging = ^23.0
- pip = ^22.3.1
- python-dotenv = ^0.21.1
- requests = ^2.28.2
- setuptools = ^65.5.0
- tqdm = ^4.64.1
- urllib3 = ^1.26.14
- webdriver-manager = ^3.8.5

requirements.txt file inlcuded

## Extension Usage

To make the exrension work the user ahve to follow the following steps:

1. Press ctrl + shift + P
2. Now enter Run Python and hit Enter button

## Known Issues

1. Currently it is only fetching the errors out of the python program this can be implemented for all the available languages.
2. Instead of getting the result in terminal or the output window we get a pop up on right side of our VS code editor window.

## Release Notes

version 0.1.0 :-

- In this version extension creates a simple query to fect results from the stack overflow API which provides the extension with an JSON format result on the persent questions on stack overflow and other properties of question such as whether they are answered or not, what is the solution, no of solution etc.
