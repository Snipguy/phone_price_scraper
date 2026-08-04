from main import wait_for_connection
from main import check_internet_connection
from unittest.mock import patch

@patch("main.urllib.request.urlopen")
def test_internet_connection_success(mock_urlopen):
    result = check_internet_connection()

    assert result is True
    mock_urlopen.assert_called_once()


@patch("main.urllib.request.urlopen")
def test_internet_connection_failure(mock_urlopen):
    mock_urlopen.side_effect = Exception()

    result = check_internet_connection()

    assert result is False


@patch("main.check_internet_connection")
def test_wait_for_connection_success(mock_connection):
    mock_connection.return_value = True

    result = wait_for_connection(
        max_retries=3,
        retry_delay=0
    )

    assert result is True
    assert mock_connection.call_count == 1

@patch("main.check_internet_connection")
def test_wait_for_connection_failure(mock_connection):
    mock_connection.return_value = False

    result = wait_for_connection(
        max_retries=3,
        retry_delay=0
    )

    assert result is False
    assert mock_connection.call_count == 3