package Tests;

import com.microsoft.playwright.*;
import com.microsoft.playwright.options.LoadState;
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
    void checkLogo() {
        /*
        The user sees the page logo
        Given: the user has access to the page
        When: open the home page
        Then: the page contains the logo
        */
        Locator logo = page.locator(LOGO);
        assertThat(logo).isVisible();
        logo.click();
        assertThat(page).hasURL(baseUrl);
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
    void checkSearch() {
        /*
        The user can search for products
        Given: There are products in the store
        When: Provides the search phrase
        Then: the page displays the search results
        */
        Locator searchInput = page.locator(SEARCH_INPUT);
        String searchedPhrase = "windsurfing";
        searchInput.type(searchedPhrase);
        page.press(SEARCH_INPUT, "Enter");
        page.waitForLoadState(LoadState.NETWORKIDLE);

        ElementHandle[] elements = page.querySelectorAll(FIND_ELEMENTS).toArray(new ElementHandle[0]);
        page.waitForTimeout(500);
        if (0 < elements.length) {
            for (ElementHandle element : elements) {
                String currentText = element.innerText();
                String lowerText = currentText.toLowerCase();
                assert lowerText.contains(searchedPhrase);
            }
        }
    }
}
