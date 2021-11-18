import behave
from selenium import webdriver
from selenium.webdriver.firefox import options as firefoxoptions


@behave.given("Un navigateur ouvert")
def step_impl(context):
    options = firefoxoptions.Options()
    options.headless = True
    context.driver = webdriver.Firefox(options=options)


titre_attendu = {
    "https://www.google.com/": "Google",
    "http://www.chezmoicamarche.org/": "Chez moi ça marche"
}


@behave.when('On charge une page web "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.titre_attendu = titre_attendu[url]


@behave.then("Elle s'affiche")
def step_impl(context):
    assert context.driver.title == context.titre_attendu
