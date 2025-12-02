class Rule:
    def __init__(self,id,cat,name,description,bad_typo,good_typo):
        self.id= id
        self.cat = cat
        self.name = name
        self.description = description
        self.bad_typo = bad_typo
        self.good_typo = good_typo
        

    def get_id(self):
        return f"{self.id}"
    def get_name(self):
        return f"{self.name}"
    def get_description(self):
        return f"{self.description}"
    def get_bad_typo(self):
        return f"{self.bad_typo}"
    def get_good_typo(self):
        return f"{self.good_typo}"
    def get_cat(self):
        return f"{self.cat}"


    def set_name(self,name_changed):
        self.name = name_changed
    def set_description(self,description_changed):
        self.description = description_changed
    def set_bad_typo(self,bad_typo_changed):
        self.bad_typo = bad_typo_changed
    def set_good_typo(self,good_typo_changed):
        self.good_typo = good_typo_changed

    def set_cat(self,cat_changed):
        self.cat = cat_changed

