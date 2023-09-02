import { test, expect, Locator } from "@playwright/test";
import { HomePage } from "../pages/home-page/home-page";

import testParameters from "./data-for-test.json";

const TEST_PARAMETERS = testParameters["home"];

test.describe("Home Page Tests", () => {
  let homePage: HomePage;

  test.beforeEach(async ({ page }) => {
    homePage = new HomePage(page);
    // go to Home Page and wait until page is loaded
    await homePage.gotoHomePage();
  });

  test("Home Page - Page Header", async () => {
    /*
    The user sees the page header
    Given: the user has access to the page
    When: open the home page
    Then: the page contains the header
    */
    const homePageHeader: string = await homePage.pageTitle.innerText();
    const expectedPageHeader: string = TEST_PARAMETERS.pageTitle;
    expect(homePageHeader).toEqual(expectedPageHeader);
  });

  test("Home Page - Check [Get Started] Button", async ({context}) => {
    /*
    The user sees the page header
    Given: the user has access to the page
    When: open the home page
    Then: the page contains the header
    */
    const getStartedButton: Locator = homePage.getStartedButton
    await expect(getStartedButton).toBeVisible()
    await expect(getStartedButton).toBeEnabled()
  });
});
