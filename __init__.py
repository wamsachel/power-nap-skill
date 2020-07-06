from mycroft import MycroftSkill, intent_file_handler


class PowerNap(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nap.power.intent')
    def handle_nap_power(self, message):
        self.speak_dialog('nap.power')


def create_skill():
    return PowerNap()

