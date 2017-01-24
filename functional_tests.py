#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Thejojo'

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time




class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 女孩去看了网站首页
        self.browser.get('http://localhost:8000')
        # browser.get('http://sina.com')

        # 女孩注意到网站标题含有To-Do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # 应用邀请她输入一个待办
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        # 她输入了一个，买个本子
        inputbox.send_keys('Buy peacock feathers')

        # 她输入后，页面更新了，显示了她输入的项目
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(10)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # 页面又显示了一个文本框，可以输入其他待办
        # 女孩输入了另一个待办

        # 页面再次更新

        # 显示了2个待办
        self.fail('Finish the test!')

        # 她想知道这个网站是否会记住她的清单

        # 她看到网站为她生成了一个唯一的url

        # 而且页面里有文字解说这个功能

        # 她访问这个URL，发现她的待办还存在

        # 她很满意，去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')
