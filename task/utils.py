
import pandas as pd
from paymob import settings
from functools import reduce
from itertools import chain, combinations


class FileReader:

    def __init__(self, path=None):
        if not path:
            self.path = settings.CSV_FILE_PATH
        else:
            self.path = path

    def read(self):
        dataframe = pd.read_csv(self.path, usecols = ['Key','Values'])
        return dataframe

    def read_keys(self):
        dataframe = pd.read_csv(self.path, usecols = ['Key'])
        return list(map(lambda x: x.strip(), dataframe['Key'].values.tolist()))

    def read_values(self):
        dataframe = pd.read_csv(self.path, usecols = ['Values'])
        return list(map(lambda x: str(x), dataframe['Values'].values.tolist()))


class TextMatch:

    def search(self, token, txt):
        token_length = len(token)
        txt_length = len(txt)
        for i in range(txt_length - token_length + 1):
            j = 0
            while (j < token_length):
                if (txt[i + j] != token[j]):
                    break
                j += 1
            if (j == token_length):
                return True
        return False

    def token_matching(self, token, values):
        print("---> ", token)
        return list(filter(lambda x: self.search(token=token, txt=x), values))

    def powerset(self, iterable):
        s = list(iterable)  # allows duplicate elements
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    def matching(self, key,values):
        matches = {}
        for i, token in enumerate(self.powerset(key.split(" ")), 1):
            token = ' '.join(token)
            choices = self.token_matching(token, values)
            percentage = (len(token.strip())/(len(key.strip())-1)) * 100
            if percentage >= 50:
                matches.update({k: percentage for k in choices})
        matches.pop(key)
        return matches
