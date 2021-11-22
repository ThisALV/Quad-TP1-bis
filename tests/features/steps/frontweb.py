import behave
from selenium import webdriver
from selenium.webdriver.firefox import options as firefoxoptions
from selenium.webdriver.support.ui import Select


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
    context.driver.quit()


@behave.given("La calculatrice ouverte dans un navigateur")
def step_impl(context):
    options = firefoxoptions.Options()
    options.headless = True

    context.driver = webdriver.Firefox(options=options)
    context.driver.get("http://localhost:8080/index.html")


@behave.when("On rempli le formulaire avec {a:d}, {b:d} et on sélectionne l'opération {op}")
def step_impl(context, a, b, op):
    context.driver.find_element(value="entree-a").send_keys(str(a))
    context.driver.find_element(value="entree-b").send_keys(str(b))

    choix_operation = Select(context.driver.find_element(value="operation"))
    choix_operation.select_by_visible_text(op)

    context.driver.find_element(value="valider").click()


@behave.then("Elle affiche le calcul {calcul}")
def step_impl(context, calcul):
    try:
        assert context.driver.page_source == f"<html><head></head><body>{calcul}</body></html>"
    finally:
        context.driver.quit()
