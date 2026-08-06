import pytest
from unittest.mock import Mock
from selenium.common.exceptions import StaleElementReferenceException
from phone_price_scraper import main

def test_locate_element_with_retry_success():
    driver = Mock()
    element = Mock()

    driver.find_element.return_value = element

    result = main.locate_element_with_retry(driver, "id", "test")

    assert result is element
    driver.find_element.assert_called_once_with("id", "test")


def test_locate_element_with_retry_after_stale():
    driver = Mock()
    element = Mock()

    driver.find_element.side_effect = [
        StaleElementReferenceException(),
        element
    ]

    result = main.locate_element_with_retry(driver, "id", "test", retries=3)

    assert result is element
    assert driver.find_element.call_count == 2


def test_locate_element_with_retry_failure():
    driver = Mock()

    driver.find_element.side_effect = StaleElementReferenceException()

    with pytest.raises(StaleElementReferenceException):
        main.locate_element_with_retry(driver, "id", "test", retries=3)

    assert driver.find_element.call_count == 3


