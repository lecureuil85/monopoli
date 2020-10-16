class community:

    def __init__(self, id, params):
        self.id = id
        self.text = params["text"]
        self.bonus = params["bonus"]
        self.penalty = params["penalty"]
        self.players_pay_you = params["players_pay_you"]
        self.draw_chance = params["draw_chance"]