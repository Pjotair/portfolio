# 🎭 Playwright tests - Page Object Model structure - PoC

## Table od Contents
- [Playwright](#playwright)
- [Page Object Model](#page-object-model)
- [Installation](#installation)
- [Run Tests](#run-tests)
- [Resources](#resources)

## Playwright
Playwright is a versatile framework designed for Web Testing and Automation. With a single unified API, it empowers you to perform testing on [Chromium](https://www.chromium.org/Home), [Firefox](https://www.mozilla.org/en-US/firefox/new/), and [WebKit](https://webkit.org/) browsers. Playwright simplifies cross-browser web automation, providing a solution that is always up-to-date, highly capable, dependable, and exceptionally fast.

## Page Object Model
The Page Object Model (POM) is a design pattern used in software test automation to improve the maintainability and readability of test code. The main idea behind the POM is to represent each web page or user interface element as a separate class or object. POM is a widely adopted best practice in test automation because it enhances the maintainability, It makes it easier to manage and update test code as the application evolves, reducing maintenance overhead and ensuring that automated tests remain effective and reliable.

## Installation

To install and setup environment we need to to the following steps:

1. Install `Node.js` and `npm` [install npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), but I recommend to use [NVM](https://www.linode.com/docs/guides/how-to-install-use-node-version-manager-nvm/) (Node Version Manager) to do that to install needed version.
2. Install needed packages: [Install packages and Playwright](#install),

### Install

Put the following command into the `/Playwright-POM-Poc-ts` folder

```
npm install
```
to install all needed libraries and dependencies. The `node_modules` folder should be created when the installation process is complete. You can check Playwright version as sanity checks:
```
npx @playwright/test --version
```

You can optionally install only selected browsers, see [install browsers](https://playwright.dev/docs/cli#install-browsers) for more details.

* [Getting started](https://playwright.dev/docs/intro)
* [Installation configuration](https://playwright.dev/docs/installation)
* [API reference](https://playwright.dev/docs/api/class-playwright)

## Run Tests

You have the option to execute a single test, a group of tests, or the entire suite. These tests can be executed on a single browser or across multiple browsers. By default, tests are conducted in a headless mode, which means that no browser window will be displayed during the testing process, and you'll view the results in the terminal.

### Command Line
Running all tests
```
npx playwright test
```
Running a single test file
```
npx playwright test tests/test-home-page.spec.ts
```

## Resources

* [Documentation](https://playwright.dev/docs/intro)
* [Playwright Changelog](https://github.com/microsoft/playwright/releases)
