from sub_module.another_helper import SomeHelper


class Helper:
    def __init__(self):
        self.inner_helper = SomeHelper()
        pass

    @staticmethod
    def get_value(a: str):
        return f', {a}'
