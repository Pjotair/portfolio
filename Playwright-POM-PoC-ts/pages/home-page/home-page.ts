import { Locator, Page } from "@playwright/test";
import { BasePage } from "../base-page";
import { HomePageLocators as Selectors } from "./home-page-locators";

export class HomePage extends BasePage {
  readonly url: string;
  readonly pageTitle: Locator;

  constructor(page: Page) {
    super(page);
    this.url = "/";

    this.pageTitle = this.page.locator(Selectors.HOME_PAGE_TITLE);
  }

  async gotoHomePage() {
    await this.page.goto(this.url);
    await this.page.waitForURL(`**${this.url}`, { waitUntil: "networkidle" });
  }
}
