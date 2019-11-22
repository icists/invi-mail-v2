class Invitation():
    def __init__(self, row):
        LANG, MAIL, NAME, SENDER, FIELD, ONE_SEN, DATE, DESC, DONE, ETC = range(10)
        self.lang = row[LANG]
        self.mail = row[MAIL]
        self.name = row[NAME]
        self.sender = row[SENDER]
        self.field = row[FIELD]
        self.one_sen = row[ONE_SEN]
        self.date = row[DATE]
        self.desc = row[DESC]
        self.done = row[DONE] == 'O'
        self.etc = row[ETC]

    def is_eng(self):
        return self.lang == '영'

    def finalResonance(self, name):
        last_char = list(name).pop()
        chk = (ord(last_char) - ord('가')) % 28
        return bool(chk)
    
    def postposition_yi(self, chk):
        if chk:
            return '이'
        else:
            return ''

    def postposition_leul(self, chk):
        if chk:
            return '을'
        else:
            return '를'

    def __str__(self):
        return "{:30} {}".format(self.name, self.mail)