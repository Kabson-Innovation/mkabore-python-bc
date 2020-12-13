
class Person:
    def __init__(self, json_data):
        self.education = dict()
        self.marriage = dict()
        self.online_info = dict()
        self.personal = dict()
        self.work = dict()
        self.create_instance(json_data)

    def create_instance(self, json_data):
        p = json_data['person']
        self.education = p['education']
        self.marriage = p['marriage']
        self.online_info = p['online_info']
        self.personal = p['personal']
        self.work = p['work']



