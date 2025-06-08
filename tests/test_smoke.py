from base.site_entry import Site
from helpers.allure import allure_description
from helpers.cookies import setup_cookies_from_file


class TestShoppingFlow:
    def test_successful_login(self, site: Site, credentials):
        allure_description(
            test_case_title="Успешный вход существующего пользователя",
            preconditions=["Пользователь May May или Ivan Ivanov существует"],
            steps=[
                {"action": "Открыть форму авторизации"},
                {
                    "action": "Ввести валидные логин/пароль",
                    "expected": "Пользователь авторизован",
                },
            ],
        )

        site.main_page.go_to_page()
        site.main_page.login_dropdown.click()
        site.main_page.login_button.click()

        site.main_page.login_form.login_field.clear_and_send_value(
            credentials["username"]
        )
        site.main_page.login_form.password_field.clear_and_send_value(
            credentials["password"]
        )
        site.main_page.login_form.submit_button.click()

        with site.main_page.expected.step(
            "Пользователь должен залогиниться как May May или Ivan Ivanov"
        ):
            site.main_page.expected.wait_for(
                lambda: any(
                    name in site.main_page.driver.page_source
                    for name in ("Ivan Ivanov", "May May")
                ),
                timeout=10,
            )

    def test_catalog_navigation_and_item_display(self, site: Site):
        allure_description(
            test_case_title="Навигация: Электроника → Планшеты → Digma",
            steps=[
                {"action": "Открыть каталог"},
                {"action": "Выбрать Digma в ветке Электроника/Планшеты"},
                {
                    "action": "Убедиться в наличии товара бренда Digma",
                    "expected": "Найден хотя бы один товар бренда «Digma»",
                },
            ],
        )

        site.main_page.go_to_page()
        site.main_page.catalog_button.click()
        site.main_page.catalog_dropdown.category_electronics.move_to_element()
        site.main_page.catalog_dropdown.subcategory_tablets.move_to_element()
        site.main_page.catalog_dropdown.brand_digma.click()

        with site.catalog_page.expected.step("Открыта страница бренда Digma"):
            site.catalog_page.is_opened()
            site.catalog_page.expected.wait_for(
                lambda: "Digma" in site.catalog_page.page_title.text(),
                timeout=5,
            )

        with site.catalog_page.expected.step(
            "Есть хотя бы один товар Digma на странице"
        ):
            titles = [el.text for el in site.catalog_page.product_titles.find_all()]
            site.catalog_page.expected.is_equal(any("Digma" in t for t in titles), True)

    def test_add_and_remove_item_from_cart(self, site: Site):
        allure_description(
            test_case_title="Добавление и удаление товара из корзины",
            steps=[
                {
                    "action": "Добавить товар в корзину",
                    "expected": "Товар появился в корзине",
                },
                {"action": "Удалить товар", "expected": "Корзина пуста"},
            ],
        )

        site.main_page.go_to_page()
        setup_cookies_from_file(site.driver)

        site.main_page.add_to_cart_button.move_to_element().click()
        chosen_title = site.main_page.cart_form.product_title.text()
        site.main_page.cart_form.go_to_cart_button.click()

        with site.cart_page.expected.step("Открыта страница оформления заказа"):
            site.cart_page.is_opened()
            site.cart_page.expected.wait_for(
                lambda: "Оформление заказа" in site.cart_page.page_title.text(),
                timeout=5,
            )

        with site.cart_page.expected.step(
            "Наименование продукта соответствует добавленному"
        ):
            actual_title = site.cart_page.product_titles.text()
            site.cart_page.expected.is_equal(actual_title, chosen_title)

        with site.cart_page.expected.step("В корзине конкретный добавленный продукт"):
            real_count = len(site.cart_page.added_items.find_all())
            site.cart_page.expected.is_equal(real_count, 1)

        with site.cart_page.expected.step("Количество добавленного продукта равно 1"):
            site.cart_page.expected.is_equal(
                site.cart_page.product_count.int_value(),
                1,
            )

        with site.cart_page.expected.step(
            "Удаление добавленного продукта через крестик"
        ):
            site.cart_page.remove_button.click()
            site.cart_page.expected.wait_for(
                lambda: len(site.cart_page.added_items.find_all()) == 0,
                timeout=5,
            )


class TestFavouriteFlow:
    def test_add_and_remove_item_from_favourite(self, site: Site):
        allure_description(
            test_case_title="Избранное: добавить и удалить товар",
            steps=[
                {
                    "action": "Добавить товар в избранное",
                    "expected": "Товар появился во вкладке «Избранное»",
                },
                {
                    "action": "Удалить товар из избранного",
                    "expected": "Список избранного пуст",
                },
            ],
        )

        site.main_page.go_to_page()
        setup_cookies_from_file(site.driver)

        chosen_product_title = site.main_page.product_card_title.text()
        site.main_page.add_to_favorite.move_to_element().click()

        site.main_page.go_to_favorite_page_button.move_to_element().click()

        with site.catalog_page.expected.step("Открыта страница 'Избранное'"):
            site.favorite_page.is_opened()
            site.catalog_page.expected.wait_for(
                lambda: "Избранное" in site.favorite_page.page_title.text(),
                timeout=5,
            )

        with site.favorite_page.expected.step(
            "В избранном ровно один добавленный продукт"
        ):
            fav_count = len(site.favorite_page.product_item.find_all())
            site.favorite_page.expected.is_equal(fav_count, 1)

        with site.favorite_page.expected.step(
            "Наименование продукта соответствует добавленному"
        ):
            actual_title = site.favorite_page.product_title.text()
            site.favorite_page.expected.is_equal(actual_title, chosen_product_title)

        with site.favorite_page.expected.step(
            "Удаление добавленного продукта из избранного"
        ):
            site.favorite_page.remove_from_favorite.click()
            site.favorite_page.expected.wait_for(
                lambda: len(site.favorite_page.product_item.find_all()) == 0,
                timeout=5,
            )
