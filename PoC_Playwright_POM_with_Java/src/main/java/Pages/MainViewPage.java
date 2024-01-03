package Pages;

public class MainViewPage {
    public static String baseUrl = "https://fakestore.testelka.pl/";

    // Locators
    public static String HOME_PAGE_TITLE = "div[class='content-area'] header h1";
    public static String MENU_CONTAINER = "div[class='primary-navigation']";
    public static String MENU_ELEMENTS = "ul[id='menu-menu'] li";

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
