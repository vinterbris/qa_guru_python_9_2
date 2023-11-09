import pytest
from selene.support.shared import browser, config
from selene import be, have


@pytest.fixture()
def site():
    config.window_width = 1920
    config.window_height = 900
    browser.open('https://google.com')



def test_google_search(site):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_no_result(site):
    browser.element('[name="q"]').should(be.blank).type('a;lsdkfjal;skjdfaskjdhfjklahsdfklj').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('По запросу a;lsdkfjal;skjdfaskjdhfjklahsdfklj ничего не найдено.'))
