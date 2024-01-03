package Tests;

import com.microsoft.playwright.*;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.Test;

import static Pages.MainViewPage.*;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static com.microsoft.playwright.assertions.PlaywrightAssertions.assertThat;

public class TestMainView {
    static Playwright playwright;
    static Browser browser;

    BrowserContext context;
    Page page;

    @BeforeAll
    static void launchBrowser() {
        playwright = Playwright.create();
        browser = playwright.chromium().launch();
    }

    @AfterAll
    static void closeBrowser() {
        playwright.close();
    }

    @BeforeEach
    void createContextAndPage() {
        context = browser.newContext();
        page = context.newPage();
        page.navigate(baseUrl);
    }

    @AfterEach
    void closeContext() {
        context.close();
    }

    @Test
    void checkPageHeader() {
        /*
        The user sees the page header
        Given: the user has access to the page
        When: open the home page
        Then: the page contains the header
        */
        Locator pageHeader = page.locator(HOME_PAGE_TITLE);
        assertThat(pageHeader).containsText(mainPageHeader);
        }
    @Test
    void checkNavigateList() {
        /*
        The user sees the navigation menu
        Given: the user has access to the page
        When: open the home page
        Then: the page contains the menu elements
        */
        Locator menuContainer = page.locator(MENU_CONTAINER);
        assertThat(menuContainer).isVisible();

        ElementHandle[] listItems = page.querySelectorAll(MENU_ELEMENTS).toArray(new ElementHandle[0]);
        String[] actualList = new String[listItems.length];
        for (int i = 0; i < listItems.length; i++) {
            actualList[i] = listItems[i].innerText();
        }
        assertArrayEquals(expectedMenuList, actualList);
    }
}
