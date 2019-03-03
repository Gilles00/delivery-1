from django.urls import reverse

from random import randint

from menu.models import MenuItem
from menu.tests_selenium import FirefoxTests
from time import sleep


class OrdersFirefoxTests(FirefoxTests):

    def fill_session_cart(self):
        expected_contents = []
        for i in range(3):
            new_menu_item = MenuItem.objects.create(
                name=f'Dish{i}', price=randint(10, 300))
            add_url = reverse('menu:update_cart', args=(new_menu_item.id,))
            amount = randint(1, 10)
            self.client.post(add_url, {'amount': amount})
            expected_contents.append({
                'id': new_menu_item.id,
                'name': new_menu_item.name,
                'price': new_menu_item.price,
                'amount': amount,
                'cost': new_menu_item.price * amount
            })
        return expected_contents


class ShoppingCartTests(OrdersFirefoxTests):

    def test_shopping_cart_is_empty(self):
        """
        Empty shopping cart is displayed correctly.
        """
        self.login_browser_user()
        url = self.live_server_url + reverse('orders:shopping_cart')

        self.browser.get(url)
        self.assertEqual(
            self.browser.find_element_by_tag_name('p').text,
            "Your shopping cart is empty."
        )

    def test_shopping_cart_has_items(self):
        """
        Added to cart items are displayed correctly.
        """
        self.login_browser_user()
        expected_contents = self.fill_session_cart()
        url = self.live_server_url + reverse('orders:shopping_cart')
        self.browser.get(url)

        list_items = self.browser.find_elements_by_tag_name('li')

        self.assertTrue(len(expected_contents) == len(list_items))

        for item, list_item in zip(expected_contents, list_items):
            text = list_item.text
            self.assertIn(item['name'], text)
            self.assertIn(str(item['price']), text)
            self.assertIn(str(item['cost']), text)
            amount = list_item.find_element_by_id('amount')
            self.assertEqual(item['amount'], int(amount.get_property('value')))
        self.assertIn(
            str(self.client.session['cart_cost']),
            self.browser.find_element_by_id('food_cost').text
        )

    def test_update_shopping_cart(self):
        """
        Amount of items in cart can be changed.
        """

    def test_remove_item_from_cart(self):
        """
        Items in cart can be removed.
        """

    def test_link_to_checkout(self):
        """
        Link at the bottom leads to checkout page.
        """
        self.login_browser_user()
        self.fill_session_cart()
        url = self.live_server_url + reverse('orders:shopping_cart')
        self.browser.get(url)
        self.browser.find_element_by_link_text('Checkout').click()
        div = self.browser.find_element_by_tag_name('div')
        self.assertIn(
            "This is a checkout page.",
            div.text
        )


class CheckoutTests(OrdersFirefoxTests):

    def test_process_order(self):
        """
        Clicking on the button processes order.
        """
        self.login_browser_user()
        self.fill_session_cart()
        url = self.live_server_url + reverse('orders:checkout')
        self.browser.get(url)
        self.browser.find_element_by_id('nothing').submit()
        sleep(1)
        div = self.browser.find_element_by_tag_name('div')
        self.assertIn(
            "Your order was placed.",
            div.text
        )
        self.assertTrue(len(self.client.session['cart']) == 0)