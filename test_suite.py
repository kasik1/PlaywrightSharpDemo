from tests.fixtures.users import create_login
from tests.commons.django_api_config import get_project_credentials

import pytest


@pytest.mark.parametrize('user_session', [*create_login()])
@pytest.mark.userbase
class TestMainHomePage:

    @pytest.mark.parametrize('test_data', ['test_count_element_for_section_ub'], indirect=True)
    def test_count_element_for_section_ub(self, user_base, test_data, user_session, login_page):
        """ count the elements for secction in the main page """
        user_base.log_out()
        login_page(user_session)
        user_base.get_sections_and_numbers()

    @pytest.mark.parametrize('test_data', ['test_options_user_ub'], indirect=True)
    def test_options_user_ub(self, user_base, test_data, user_session, login_page):
        """ check that the columns appear in the change log table"""
        user_base.log_out()
        login_page(user_session)
        user_base.open_user_menu()
        user_base.nav_user_click()

    @pytest.mark.parametrize('test_data', ['test_color_dashboard_ub'], indirect=True)
    def test_color_dashboard_ub(self, user_base, test_data, user_session, login_page):
        """ check that the columns appear in the change log table"""
        user_base.log_out()
        login_page(user_session)
        user_base.open_user_menu()
        first_color = user_base.check_color_view()
        assert first_color == "#ffffff"
        user_base.change_dark_color()
        change_color = user_base.check_color_view()
        assert change_color == "#212529"
        user_base.open_user_menu()
        user_base.change_light_color()

    @pytest.mark.parametrize('test_data', ['test_log_out_ub'], indirect=True)
    def test_log_out_ub(self, user_base, test_data, user_session, login_page):
        """ check that the columns appear in the change log table"""
        user_base.log_out()
        login_page(user_session)
        user_base.open_user_menu()
        user_base.log_out_home()


@pytest.mark.smoke
class TestMainPageFormValidation:

    @pytest.mark.parametrize('test_data', ['test_check_elements_home'], indirect=True)
    def test_check_elements_home(self, ssot, test_data):
        """ check if exist all titles in home page """
        titles = ["Organization", "Power", "IPAM", "Circuits", "Virtualization", "Change Log"]
        ssot.get_logo()
        for title in titles:
            assert ssot.is_title_present(title, type='strong')


@pytest.mark.parallel
@pytest.mark.functional
class TestMainPage:
    """Class for the tenant group module in ssot"""

    @pytest.mark.parametrize('test_data', ['test_count_element_for_section'], indirect=True)
    def test_count_element_for_section(self, ssot, test_data):
        """ count the elements for section in the main page """
        ssot.get_sections_and_numbers()

    @pytest.mark.skip
    @pytest.mark.parametrize('test_data', ['test_columns_change_log'], indirect=True)
    def test_columns_change_log(self, ssot, test_data):
        """ check that the columns appear in the change log table"""
        titles = ["Change Log"]
        for title in titles:
            assert ssot.is_title_present(title, type='strong')
        ssot.check_element_date_change_log()

    @pytest.mark.skip
    @pytest.mark.parametrize('test_data', ['test_change_log_link'], indirect=True)
    def test_change_log_link(self, ssot, test_data):
        """ check that the columns appear in the change log table"""
        titles = ["Change Log"]
        for title in titles:
            assert ssot.is_title_present(title, type='strong')
        ssot.check_link_log()

    @pytest.mark.parametrize('test_data', ['test_options_user'], indirect=True)
    def test_options_user(self, ssot, test_data, ):
        """ check that the options in menu the admin and profile"""
        ssot.open_user_menu()
        ssot.nav_user_click()

    @pytest.mark.parametrize('test_data', ['test_color_dashboard'], indirect=True)
    def test_color_dashboard(self, ssot, test_data, ):
        """ chack the change color in the dashboard"""
        first_color = ssot.check_color_view()
        assert first_color == "#f4f4f4"
        ssot.change_dark_color()
        change_color = ssot.check_color_view()
        assert change_color == "#c4ccd2"
        ssot.change_light_color()

    @pytest.mark.parametrize('test_data', ['test_log_out'], indirect=True)
    def test_log_out(self, ssot, test_data, setup_server_url):
        """ check that process for log out the page"""
        ssot.open_user_menu()
        ssot.log_out_home(setup_server_url)
        user, password = get_project_credentials()
        ssot.log_in(user, password)


