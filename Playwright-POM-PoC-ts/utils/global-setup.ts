// global-setup.ts
import { chromium, FullConfig } from "@playwright/test";

async function globalSetup(config: FullConfig) {
  const { baseURL } = config.projects[0].use;
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(baseURL as string, { waitUntil: "domcontentloaded" });
  await page.waitForURL("**/", { waitUntil: "networkidle" }); // wait until loading all cookies
  await browser.close();
}

export default globalSetup;
