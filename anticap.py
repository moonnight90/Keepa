from anticaptchaofficial.recaptchav2proxyless import *
def get_key():
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("ad22efa6ba29897078afa89b89408073")
    solver.set_website_url("https://keepa.com")
    solver.set_website_key("6Lf6pwITAAAAAFzmtyDr1Vv629mD-I6QiibwemP1")

    captcha_text = solver.solve_and_return_solution()
    if captcha_text != 0:
        print("captcha text "+captcha_text)
    else:
        print("task finished with error "+solver.error_code)
    return captcha_text