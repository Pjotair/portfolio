package Pages;

import com.microsoft.playwright.*;
import static com.microsoft.playwright.Locator.*;


public class MainViewPage {
    public static String baseUrl = "https://fakestore.testelka.pl/";

    // Locators
    public static String LOGO = "div a[class='custom-logo-link']";
    public static String MENU_CONTAINER = "div[class='primary-navigation']";
    public static String MENU_ELEMENTS = "ul[id='menu-menu'] li";
    public static String HOME_PAGE_TITLE = "div[class='content-area'] header h1";
    public static String FIND_ELEMENTS = "div[class='content-area'] li h2";
    public static String SEARCH_INPUT = "input[id='woocommerce-product-search-field-0']";

    // Expected data
    public static String mainPageHeader = "Wybierz podróż dla siebie!";
    public static String[] expectedMenuList = {
            "Strona główna",
            "Sklep",
            "Zamówienie",
            "Koszyk",
            "Moje konto",
            "Lista życzeń"
    };
}
