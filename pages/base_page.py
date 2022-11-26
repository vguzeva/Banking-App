class BasePage:

    user = 'Demo-User'
    user_password = 'Demo-Access1'
    admin = 'Bank-Admin'
    admin_password = 'Demo-Access1'
    timeout = 10

    def __init__(self, driver) -> None:
        self.driver = driver