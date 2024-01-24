import configparser

class Config:
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

    def requested_bar_stats(self):
        keys = [
            "MaxHealth"  ,
            "ShieldCap"  ,
            "ShieldRate" ,
            "ShieldDelay",
            "MeleeDamage",
            "GrenadeDmg" ,
            "GunAcc"     ,
            "GunDmg"     ,
            "FireRate"   ,
            "Recoil"     ,
            "Reload"     ,
            "ElemChance" ,
            "ElemDmg"    ,
            "Crit"       ,
        ]

        if "BarStats" not in self.config:
            return [None for k in keys]

        section = self.config["BarStats"]
        out = []
        for k in keys:
            if k in section:
                out.append(float(section[k]))
            else:
                out.append(None)

        return out

    def requested_golden_keys(self):
        if "GoldenKeys" not in self.config:
            return None

        if "count" not in self.config["GoldenKeys"]:
            return None

        return int(self.config["GoldenKeys"]["count"])

    def requested_bar_tokens(self):
        if "BarTokens" not in self.config:
            return None

        if "count" not in self.config["BarTokens"]:
            return None

        return int(self.config["BarTokens"]["count"])

    def requested_bar_rank(self):
        if "BarRank" not in self.config:
            return None

        if "value" not in self.config["BarRank"]:
            return None

        return int(self.config["BarRank"]["value"])

    def requested_fov(self):
        if "FOV" not in self.config:
            return None

        if "value" not in self.config["FOV"]:
            return None

        return int(self.config["FOV"]["value"])