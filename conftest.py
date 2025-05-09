"""
This files includes configuration and methods for pytest to execute them as hooks
"""
import time

from tests.commons.functions import fill_test_case_detail_values
from tests.commons.csv import Csv
from tests.pom.main_page import MainPage
from tests.pom.login import Login
import pytest
import os


@pytest.fixture(scope='session')
def spreadsheet(request):
    """Find the file test data"""
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, 'test_data.csv')
    return Csv(file_path)


@pytest.fixture(scope='session')
def setup_server_url(spreadsheet, testing_environment):
    """Get the url in test cases"""
    return testing_environment(spreadsheet)


@pytest.fixture()
def test_data(request, spreadsheet):
    """Get the data"""
    fixture_name = request.param
    data = {
        'test_case': {
            'test_case_id': '',
            'build': '',
            'tester': '',
            'notes': '',
            'c_environment': ''},
        'data': []
    }

    # If fixture 'user_session' is being used
    if 'user_session' in request.keywords.node.funcargs:
        cookie = getattr(request.keywords.node.funcargs['user_session'], 'cookies', False)
        user_group = {'user_group': cookie['user_group']}
    else:
        user_group = {'user_group': []}
    data['test_case'].update(user_group)

    for row in (row for row in spreadsheet.rows() if row['TEST_TYPE'] == fixture_name):
        data = fill_test_case_detail_values(data, row)
        data['data'].append(row)
    return data


@pytest.fixture()
def ssot(global_driver, setup_server_url):
    """create the driver to run the tests"""
    driver = global_driver
    ssot = MainPage(driver)
    url = setup_server_url
    ssot.go_url(url)
    return ssot


@pytest.fixture()
def user_base(user_base_driver):
    """Create the driver to run the tests"""
    driver = user_base_driver
    user_base = MainPage(driver)
    return user_base


@pytest.fixture()
def login_page(user_base_driver, setup_server_url):
    def _login_page(user):
        driver = user_base_driver
        login = Login(driver)
        login.log_in(user['USER'], user['PASSWORD'])
        url = setup_server_url
        login.go_url(url)
    return _login_page

