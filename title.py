import items

class Title:
    def __init__(self,title):
        self.title = title

    def is_achieved(self, inventory, stats):
        raise NotImplementedError()

class Mage(Title):
    def __init__(self):
        super().__init__(title = ' the Mage')

    def calc_status_level(self,stats):
        return stats['mga'].level

    def is_achieved(self,inventory, stats):
        magic_affinity = self.calc_status_level(stats)
        required_magic_affinity = 5
        above_required_level = False
        has_magic_stuff = False
        for i in inventory:
            if isinstance(i, items.Magical):
                has_magic_stuff = True
                break

        if magic_affinity >= required_magic_affinity:
            above_required_level = True

        if above_required_level and has_magic_stuff:
            return self.title
        return ''

class ShieldWarrior(Title):
    def __init__(self):
        super().__init__(title = ' the Shield warrior')

    def calc_status_level(self,stats):
        return stats['def'].level

    def is_achieved(self,inventory, stats):
        defence = self.calc_status_level(stats)
        required_defence = 5
        above_required_level = False
        has_shield = False
        for i in inventory:
            if i.name == 'Shield':
                has_shield = True
                break

        if defence >= required_defence:
            above_required_level = True

        if above_required_level and has_shield:
            return self.title
        return ''

class Archer(Title):
    def __init__(self):
        super().__init__(title = ' the Archer')
    def calc_status_level(self,stats):
        return stats['agi'].level
    def is_achieved(self,inventory, stats):
        agility = self.calc_status_level(stats)
        required_agility = 5
        above_required_level = False
        has_bow = False
        for i in inventory:
            if i.name == 'Bow':
                has_bow = True
                break

        if agility >= required_agility:
            above_required_level = True

        if above_required_level and has_bow:
            return self.title
        return ''

class GoldCollector(Title):
    def __init__(self):
        #t = ' the Gold collector'
        t = ' the Rich'
        super().__init__(title = t)

    def count_gold(self,inventory):
        gold = 0
        for i in inventory:
            if isinstance(i, items.Gold):
                gold += i.value
        return gold

    def is_achieved(self,inventory,stats):
        gold_amt = self.count_gold(inventory)
        required_amt = 200
        if gold_amt >= required_amt:
            return self.title
        return ''

# class MageKiller(Title):
#     def __init__(self):
#         super().__init__(title = ' the Mage killer')
#     def is_achieved(self):
#         pass

class ScorpionKiller(Title):
    def __init__(self):
        super().__init__(title = ' the Scorpion killer')

    def is_achieved(self,inventory,stats):
        required_number = 3
        cnt = 0
        for i in inventory:
            if i.name == 'Scorpion sting':
                cnt+=1

        if cnt >= required_number:
            return self.title
        return ''

titles = [Mage(),ShieldWarrior(),Archer(), GoldCollector(), ScorpionKiller()]
no cr
