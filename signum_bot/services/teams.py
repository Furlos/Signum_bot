class TeamLeader(User):
    def accept_request(self):
        """ Принять запрос на добавлние в команду """
        pass

    def reject_request(self):
        """ Отказать в запросе на добавление в команду """
        pass

    def rename_team(self):
        pass

    def kicked_off_team(self):
        """ Выгнать из состава команды """
        pass


class Team(_TeamModel):
    def get_info(self):
        pass
