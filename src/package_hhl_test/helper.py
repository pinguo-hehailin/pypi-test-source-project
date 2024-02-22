from package_hhl_test.sub_package.another_helper import SomeHelper


class Helper:
    def __init__(self):
        self.inner_helper = SomeHelper()
        pass

    def get_value(self, a: str):
        return self.inner_helper.say_hi(a)
