import math


class ShootingPhase:  # change this name to shooting_phase? and make the same for the close_combat_phase, instance them

    shooting_phase = """
   _____ _                 _   _               _____  _                    
  / ____| |               | | (_)             |  __ \| |                   
 | (___ | |__   ___   ___ | |_ _ _ __   __ _  | |__) | |__   __ _ ___  ___ 
  \___ \| '_ \ / _ \ / _ \| __| | '_ \ / _` | |  ___/| '_ \ / _` / __|/ _ \\
  ____) | | | | (_) | (_) | |_| | | | | (_| | | |    | | | | (_| \__ |  __/
 |_____/|_| |_|\___/ \___/ \__|_|_| |_|\__, | |_|    |_| |_|\__,_|___/\___|
                                        __/ |                              
                                       |___/     
    """

    x = ["Rolling event", "roll required", "% chances", "Asserted", "Failed", "Notes"]
    re_roll_types = ["all 1s", "1 roll of 1", "fail rolls", "1 fail roll"]

    def __init__(self, shots, Bs, w_str, AP, D, T, save, wounds=1, inv=None, in_cover=False, fnp=None, hits_reroll=None,
                 wound_reroll=None, damage_reroll=None, save_reroll=None, target_composition=5, w_name=None,
                 target_name=None, print_on=False):

        self.data_list = []

        self.shots_holder = shots
        if type(self.shots_holder) == str:
            self.initial_shots = self.set_shots()
        else:
            self.initial_shots = shots

        self.Bs = Bs
        self.w_str = w_str  # todo: random w_str
        self.AP = AP
        self.D = D
        self.T = T
        self.save = save

        self.hits_reroll = hits_reroll
        self.wound_reroll = wound_reroll
        self.damage_reroll = damage_reroll
        self.save_reroll = save_reroll

        self.inv = inv
        self.in_cover = in_cover
        self.wounds = wounds
        self.fnp = fnp
        self.target_comp = target_composition
        self.w_name = w_name
        self.target_name = target_name

        self.wounds_pool = self.target_comp * self.wounds

        # all events
        self.stat_shots = self.set_shots()  # check the initial_attacks allow to roll
        # print("stat_shots", self.stat_shots)
        self.stat_hits = self.to_hit()  # check how many hits valid
        # print("stat_hits", self.stat_hits)
        self.fail_hits = self.initial_shots - self.stat_hits  # check how many failed to hit
        # print("fail_hits", self.fail_hits)
        self.req_to_wound = self.set_req_to_wound()  # check required roll to wound
        # print("req_to_wound", self.req_to_wound)
        self.stat_w_str = self.set_w_str()
        self.stat_wounds = self.to_wound()  # check how many hits could damage
        # print("stat_wounds", self.stat_wounds)
        self.saving = self.set_save()
        # print("saving", self.saving)
        self.stat_saved = self.to_save()  # check armour saves from defender_page
        # print("stat_not_saved", self.stat_saved)

        self.stat_failed_saves = self.stat_wounds - self.stat_saved
        # print("stat_failed_saves", self.stat_failed_saves)
        self.stat_damage = self.set_damage()  # --> OK
        # print("stat_damage", self.stat_damage)
        self.intake_damage = self.stat_failed_saves * self.stat_damage
        # print("intake_damage", self.intake_damage)
        if self.fnp:
            self.fnp_saved = self.feel_no_pain()
        else:
            self.fnp = 0
            self.fnp_saved = 0
            # print("fnp_saved", self.fnp_saved)
            # print("fnp x damage", self.fnp_saved * self.stat_damage)
        self.wounds_taken, self.killed_models = self.wound_allocation()
        self.print_on = print_on
        if self.print_on:
            # self.heading_printed = False
            self.message = f"\n*** {self.initial_shots} x {self.w_name}s: S-{self.w_str}, AP-{self.AP}, D-{self.D}" \
                           f" vs {target_composition} x {target_name}s: T-{self.T}, Save-{self.save}+ ***"
            self.__repr__()

    # -> OK
    def __repr__(self):
        """
        prints the table of the shooting phase wih the statistic calculation
        :return:
        """
        print(f"\n{self.stat_shots}x {self.w_name} damge {self.D} vs {self.target_comp}x {self.target_name}")
        heading = "Action      Dice  Event       Required    Chances     Asserted    Failed      Notes"
        extra_spaces = len("after re-rolling all fails")
        print(heading)
        print("-" * (len(heading) + extra_spaces))
        for element in self.data_list:
            total_len = 12
            for item in element:
                word_len = len(str(item))
                spaces = " " * (total_len - word_len)

                print(item, end=spaces)
            print("")
        print("-" * (len(heading) + extra_spaces))

    # -> OK
    def create_table_line(self, action="Rolling", event=None, rolls=None, required=None, percent=None, asserted=None,
                          failed=None, notes=None):
        """
        inserts each parameter in the line format and appends the line to the printing list
        """
        total_len = 12
        if not notes:
            notes = ""
        action_spaces = ' ' * (total_len - len(action))
        dice_space = ' ' * (6 - len(f"{rolls:.1f}"))
        line = [f"{action}{action_spaces}{rolls:.1f}{dice_space}", f"{event}", f"at {required}+", f"{percent:.1f}%",
                f"{asserted:.1f}", f"{failed:.1f}", f"{notes}"]
        self.data_list.append(line)

    def create_results(self, wounds_taken, killed_models, models_in_unit):

        wounds_left = self.wounds_pool - wounds_taken

        line = [f"Out of {self.wounds_pool} wounds in the unit: {wounds_taken:.1f} wound(s) taken"
                f"\nOut of {self.target_comp} models in unit, the number of kills: {killed_models:.1f} model(s)"
                f"\nUnit still holds: {models_in_unit} model(s)"
                f"\nTo eliminate the target is needed to take out: {wounds_left:.1f} more wound(s)"]
        self.data_list.append(line)

    def create_bottom_line(self, wounds_taken, killed_models):
        """
        how effective this shooting choice is?
        :param wounds_taken:
        :param killed_models:
        :return:
        """
        percent = 0
        sep_line = "-" * 111
        if self.target_comp > 1 and self.wounds == 1:  # case of 1wound-objects_models objects_models
            percent = self.percentage_calc(total=self.target_comp, part=killed_models)
        elif self.target_comp == 1 and self.wounds > 1:  # case one model multi wound
            percent = self.percentage_calc(total=self.wounds, part=wounds_taken)
        elif self.target_comp > 1 and self.wounds > 1:  # multi wound objects_models
            percent = self.percentage_calc(total=self.wounds_pool, part=wounds_taken)

        bottom_line = [sep_line, f"""\nFinal Effectiveness: {percent:.2f}%"""]
        self.data_list.append(bottom_line)

    # -> OK
    # def percent_of_getting_just_certain_number(self, n_shots):
    #     percent_chances_of_rolling_an_specific_side = (n_shots / 6) * (100 / 6)
    #     n_dice_represents = self.initial_shots * percent_chances_of_rolling_an_specific_side / 100
    #     return percent_chances_of_rolling_an_specific_side, n_dice_represents

    # -> OK ✔
    @staticmethod
    def percentage_calc(total=None, part=None, percent=None, print_on=False):
        """
         %     part
        ---- = ----
        100    total

        :param print_on:
        :param percent:
        :param total:
        :param part:
        :return:
        """
        result = 0
        if percent and total:
            part = total * (percent / 100)
            result = part
        elif part and percent:
            total = 100 / percent * part
            result = total
        elif part and total:
            percent = part / total * 100
            result = percent

        if print_on:
            print(f"\nPERCENT CALC:\t\ttotal: {total:.1f}\tpart: {part:.1f}\tpercent: {percent:.1f}\n")
        return result

    # -> OK ✔
    @staticmethod
    def percent_of_die_roll(req_roll):
        """
        how much a die's side value or higher represent of the whole die.
        :param req_roll: minimum required in a die roll to be successful
        :return: string of percent of the chances to get the min req or more in a roll
        """
        if req_roll == 4:
            return 50.0

        return ShootingPhase.percentage_calc(total=6, part=(7 - req_roll), print_on=False)

    # -> OK ✔
    @staticmethod
    def roll(n, req_roll, print_on=False):
        """
        calculates statistically the possibility of n dice rolls in relation with the required roll
        :param print_on: printing on
        :param n: amount of dice to roll
        :param req_roll: min required roll
        :return: asserted rolls as float number out of n, eg 3.6 hits
        """

        if req_roll == str:  # some sort of debugging?
            return n
        if req_roll == 0 or req_roll is None or req_roll > 6:
            print("no roll allowed")
            return 0

        accuracy = n / 100 * ((7 - req_roll) * (100 / 6))

        if print_on:
            print(f"\t{accuracy:.1f}/{n}\t\t{n - accuracy:.1f}/{n}")

        return accuracy

    # -> OK ✔
    def how_many_ones_in_a_bunch(self):
        part = self.percentage_calc(total=self.initial_shots, percent=(100 / 6))
        return part

    # -> OK ✔
    def set_re_rolling(self, fails, req):
        """
        determines what type of formula to use according to the re rolling type

        accuracy is die asserts

        :param fails: n of dice to roll
        :param req: value minimum to assert
        :return: how many dice are good
        """

        extra_accuracy = 0

        # reroll all 1s
        if self.hits_reroll == "all 1s":
            percent_chances_of_rolling_1 = self.how_many_ones_in_a_bunch()
            extra_accuracy = self.roll(percent_chances_of_rolling_1, req)

        # reroll 1 single roll of 1
        elif self.hits_reroll == "1 roll of 1":
            percent_chances_of_rolling_1 = self.how_many_ones_in_a_bunch()
            if 0 < percent_chances_of_rolling_1 < 1:
                extra_accuracy = self.roll(percent_chances_of_rolling_1, req)
            elif percent_chances_of_rolling_1 >= 1:
                extra_accuracy = self.roll(1, req)
            else:
                extra_accuracy = 0

        # reroll all fail rolls
        elif self.hits_reroll == "fail rolls":

            extra_accuracy = self.roll(fails, req)

        # reroll 1 single all fail
        elif self.hits_reroll == "1 fail roll":
            if 1 > fails > 0:
                extra_accuracy = self.roll(fails, req)
            else:
                extra_accuracy = self.roll(1, req)
        else:
            print("unknown case")

        return extra_accuracy

    # -> OK ✔
    def set_shots(self):
        """
        decodes the type of shot from WH code in to statistic calculable int.
        :return: statistic amount of initial_attacks
        """

        initial_shots = self.shots_holder

        if type(initial_shots) == str:

            if initial_shots.isnumeric():  # case is just a str number ok
                return int(initial_shots)

            initial_shots = initial_shots.split("d")
            if "+" in initial_shots[1]:
                holder = initial_shots[1].split("+")
                initial_shots.remove(initial_shots[1])
                initial_shots.insert(1, holder[0])
                initial_shots.append(holder[1])
                dice_amount, shot_random_amount, extra = initial_shots
                extra = int(extra)
                shot_random_amount = int(shot_random_amount)
                if dice_amount:
                    dice_amount = int(dice_amount)
                    if shot_random_amount == 3:  # 4d3+2
                        initial_shots = dice_amount * (shot_random_amount / 2) + extra
                    elif shot_random_amount == 6:  # 2d6+2
                        initial_shots = dice_amount * 3.5 + extra

                else:
                    if shot_random_amount == 3:  # d3+2
                        initial_shots = shot_random_amount / 2 + extra
                    elif shot_random_amount == 6:  # d6+2
                        initial_shots = 3.5 + extra

                return initial_shots

            else:  # not extra shots
                dice_amount, shot_random_amount = initial_shots
                shot_random_amount = int(shot_random_amount)
                if dice_amount:
                    dice_amount = int(dice_amount)
                    if shot_random_amount == 3:  # 4d3
                        initial_shots = dice_amount * (shot_random_amount / 2)

                    elif shot_random_amount == 6:  # 2d6
                        initial_shots = dice_amount * 3.5

                    return initial_shots

                else:

                    if shot_random_amount == 3:  # d3
                        initial_shots = shot_random_amount / 2
                    elif shot_random_amount == 6:  # d6
                        initial_shots = 3.5

                    return initial_shots

        # case is just an int
        return initial_shots

    # -> OK
    def to_hit(self):
        Bs = self.Bs
        initial_shots = self.initial_shots
        w_name = self.w_name
        hits_reroll = self.hits_reroll
        """
        for each shot of the profile/group a die is rolled to check hits
        :return: statistic amount of successful initial_attacks
        """
        # auto hit # ok
        if type(Bs) == str:

            if Bs == "1":
                return 0

            percent = 100
            accuracy = initial_shots
            failed = 0
            action = "Solving"
            notes = f"auto hits, {w_name}"
            self.create_table_line(action=action, event="autohits", rolls=initial_shots, required="_", percent=percent,
                                   asserted=accuracy, failed=failed, notes=notes)
            return accuracy

        if self.Bs <= 1:
            return 0

        # normal case, no reroll
        event = "to hit"
        action = "Rolling"
        initial_rolls = initial_shots
        required = self.Bs
        percent = self.percent_of_die_roll(required)
        asserted = self.roll(initial_rolls, required)
        failed = initial_rolls - asserted

        self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required, percent=percent,
                               asserted=asserted, failed=failed, notes=None)
        if hits_reroll:
            action = "re-rolling"
            re_roll_type = hits_reroll
            extra_asserted = self.roll(failed, required)
            extra_percent = self.percentage_calc(total=initial_rolls, part=extra_asserted)
            failed_to_re_rolls = failed
            notes = f"re-rolled {re_roll_type}"

            re_failed = failed_to_re_rolls - extra_asserted
            if re_failed < 0:
                re_failed = 0
            self.create_table_line(action=action, event=event, rolls=failed_to_re_rolls, required=self.Bs,
                                   percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)

            action = "Resulting"
            asserted += extra_asserted
            if asserted > initial_rolls:
                asserted = initial_rolls
            if asserted < 0:
                asserted = 0
            percent += extra_percent
            if percent < 0:
                percent = 0
            notes = f"after re-rolling {hits_reroll}"
            self.create_table_line(action=action, event=event, rolls=initial_rolls, required=self.Bs, percent=percent,
                                   asserted=asserted, failed=re_failed, notes=notes)

        return asserted

    def set_w_str(self):
        """
        decodes the type of strength from WH code in to statistic calculable int.
        :return: statistic amount of initial_attacks
        """

        holder = self.w_str  # self.initial_attacks

        if type(holder) == str:
            if "d" in holder:
                dice_amount, shot_random_amount = holder.split("d")

                shot_random_amount = int(shot_random_amount)
                if dice_amount:
                    # print("yes", end=" ")
                    dice_amount = int(dice_amount)
                    # print(dice_amount, type(dice_amount))
                    if shot_random_amount == 3:
                        # print("yes", end=" ")
                        self.initial_shots = dice_amount * shot_random_amount / 2 + 0.4
                        # print(self.initial_attacks, type(initial_attacks))
                    elif shot_random_amount == 6:
                        # print("yes", end=" ")
                        self.initial_shots = dice_amount * 3.5
                        # print(self.initial_attacks, type(self.initial_attacks))

                    else:
                        print("unknown case")
                else:
                    if shot_random_amount == 3:
                        # print("yes", end=" ")
                        self.initial_shots = shot_random_amount / 2 + 0.4
                        # print(shot_random_amount, type(shot_random_amount))
                    elif shot_random_amount == 6:
                        # print("yes", end=" ")
                        self.initial_shots = shot_random_amount / 2 + 0.5
                        # print(shot_random_amount, type(shot_random_amount))
                return self.initial_shots
        return holder  # works pretty well

    # -> OK
    def set_req_to_wound(self):
        """
        decodes the WH codes for wounding by calculating toughness  vs  strength.
        :return:
        """

        if self.w_str > self.T:
            req_wound_roll = 3
            if self.w_str >= self.T * 2:
                req_wound_roll = 2
        elif self.w_str < self.T:
            req_wound_roll = 5
            if self.w_str <= self.T / 2:
                req_wound_roll = 6
        else:
            req_wound_roll = 4

        return req_wound_roll

    # -> OK
    def to_wound(self):
        """
        for each successful hit of the profile/group a die is rolled to check wounds
        :return: statistic amount of successful wounds inflicted
        """

        event = "to wound"
        initial_rolls = self.stat_hits
        percent = self.percent_of_die_roll(self.req_to_wound)
        asserted = self.roll(self.stat_hits, self.req_to_wound)
        required = self.set_req_to_wound()
        failed = self.stat_hits - asserted

        self.create_table_line(event=event, rolls=initial_rolls, required=required, percent=percent, asserted=asserted,
                               failed=failed)

        if self.wound_reroll:
            action = "Re-rolling"
            extra_asserted = self.roll(failed, required)
            extra_percent = self.percentage_calc(total=self.stat_hits, part=extra_asserted)
            initial_rolls = failed
            re_failed = initial_rolls - extra_asserted
            notes = f"re-rolled {self.wound_reroll}"

            self.create_table_line(action=action, event=event, rolls=initial_rolls, required=self.req_to_wound,
                                   percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)

            action = "Resulting"
            asserted += extra_asserted
            if asserted < 0:
                asserted = 0
            percent += extra_percent
            notes = f"after re-rolling {self.hits_reroll}"
            self.create_table_line(action=action, event=event, rolls=self.stat_hits, required=self.req_to_wound,
                                   percent=percent, asserted=asserted, failed=re_failed, notes=notes)

        return asserted

    # -> OK
    def set_save(self):

        if self.in_cover:
            self.save -= 1
            if self.save < 2:
                self.save = 2
        if self.inv and self.save + self.AP > self.inv:
            # print(f"inv save {self.inv}+")
            return self.inv
        if self.save + self.AP > 6:
            # print("no save\t 0", end="")
            return None

        return self.save + self.AP

    # -> OK
    def to_save(self):

        action = "Rolling"
        event = "to save"
        required = self.saving
        initial_rolls = self.stat_wounds

        asserted = self.roll(initial_rolls, required)
        percent = self.percentage_calc(total=initial_rolls, part=asserted)
        failed = initial_rolls - asserted
        damage = self.D
        notes = f"weapon damage: {damage}"

        self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required, percent=percent,
                               asserted=asserted, failed=failed, notes=notes)
        if self.save_reroll:
            action = "Re-rolling"
            re_roll_type = self.save_reroll
            re_rolls = failed
            extra_asserted = self.roll(re_rolls, required)
            extra_percent = self.percentage_calc(total=initial_rolls, part=extra_asserted)
            re_failed = re_rolls - extra_asserted
            notes = f"re-rolled {re_roll_type}"

            self.create_table_line(action=action, event=event, rolls=failed, required=required,
                                   percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)

            action = "Resulting"
            asserted += extra_asserted
            if asserted < 0:
                asserted = 0
            percent += extra_percent
            notes = f"after re-rolling {re_roll_type}"
            self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required,
                                   percent=percent, asserted=asserted, failed=re_failed, notes=notes)

        return asserted

    # -> OK
    def set_damage(self):
        """
        decode the WH codes for damage to be calculated
        :return: a int amount of damage per shot
        """

        holder = self.D

        damage_final = 0
        extra = 0

        if type(holder) == str:
            holder = holder.split("d")  # is working tho, holder became a list

            amount = holder[0]
            randomy = holder[1]

            if "+" in randomy:
                randomy, extra = randomy.split("+")
                randomy = int(randomy)
                extra = int(extra)

            if not amount:
                amount = 1
            else:
                int(amount)

            if int(randomy) == 3:
                damage_final = math.ceil(int(randomy) / 2) * int(amount)
            elif int(randomy) == 6:
                damage_final = math.ceil(int(randomy) / 2 + 0.4) * int(amount)

            damage_final += int(extra)
            # print("damage_final", damage_final)

        elif type(holder) is int:
            return holder

        else:
            damage_final = self.D

        return damage_final

    def feel_no_pain(self):

        fail_to_save = self.stat_failed_saves
        damage = self.set_damage()

        to_fnp = fail_to_save * damage
        action = "Rolling"
        event = "to FNP"
        rolls = to_fnp
        required = self.fnp
        asserted = self.roll(rolls, required)
        percent = self.percentage_calc(total=rolls, part=asserted)
        failed = rolls - asserted
        notes = "feel no pain per weapon damage"

        self.create_table_line(action=action, event=event, rolls=rolls, required=required, percent=percent,
                               asserted=asserted, failed=failed, notes=notes)

        return asserted

    # todo: from a class objects_models that hods many class objects_models in it
    def wound_allocation(self):

        original_wounds_per_model = self.wounds  # holder
        models_in_unit = self.target_comp
        original_weapon_damage = self.stat_damage
        weapon_damage = original_weapon_damage
        dice_counter = self.stat_failed_saves
        wounds_left = original_wounds_per_model
        killed_models = 0
        wasted_wounds = 0
        wounds_taken = 0

        if self.fnp:
            percent_of_fnp = self.percent_of_die_roll(self.fnp)
            weapon_damage = weapon_damage - self.percentage_calc(percent=percent_of_fnp, total=weapon_damage)
            # print("weapon_damage", weapon_damage)
        while dice_counter > 0 and models_in_unit > 0:

            if self.target_comp > 1:
                wounds_left = original_wounds_per_model  # starting with a new model
            # wounds_holder = 0

            while wounds_left > 0 and dice_counter > 0:
                dice_counter -= 1
                wounds_left -= weapon_damage
                if wounds_left == 0:
                    wounds_taken += weapon_damage
                    models_in_unit -= 1
                    killed_models += 1
                if wounds_left < 0:
                    wounds_taken += wounds_left
                    models_in_unit -= 1
                    killed_models += 1
                    wasted_wounds += abs(wounds_left)
                if wounds_left > 0:
                    wounds_taken += weapon_damage
                    if models_in_unit <= 0:
                        if dice_counter > 0:
                            wasted_wounds += dice_counter * weapon_damage

        # print("wounds_taken in wound_allocation", wounds_taken)
        "we are resolving the initial attacks vs the final results"
        self.create_bottom_line(wounds_taken, killed_models)
        self.create_results(wounds_taken, killed_models, models_in_unit)
        return wounds_taken, killed_models


# class FightingPhase:
#     fighting_phase = """
#   ______ _       _     _   _               _____  _
#  |  ____(_)     | |   | | (_)             |  __ \| |
#  | |__   _  __ _| |__ | |_ _ _ __   __ _  | |__) | |__   __ _ ___  ___
#  |  __| | |/ _` | '_ \| __| | '_ \ / _` | |  ___/| '_ \ / _` / __|/ _ \\
#  | |    | | (_| | | | | |_| | | | | (_| | | |    | | | | (_| \__ \  __/
#  |_|    |_|\__, |_| |_|\__|_|_| |_|\__, | |_|    |_| |_|\__,_|___/\___|
#             __/ |                   __/ |
#            |___/                   |___/
#     """
#
#     x = ["Rolling event", "roll required", "% chances", "Asserted", "Failed", "Notes"]
#     re_roll_types = ["all 1s", "1 roll of 1", "fail rolls", "1 fail roll"]
#
#     def __init__(self, attacks, Ws, model_str, w_str, AP, D, T, save, wounds=1, inv=None, in_cover=False, fnp=None,
#                  hits_reroll=None,
#                  wound_reroll=None, damage_reroll=None, save_reroll=None, target_composition=5, w_name=None,
#                  target_name=None, print_on=False):
#
#         self.data_list = []
#
#         self.attacks_holder = attacks
#         if self.attacks_holder == str:
#             self.initial_attacks = self.set_attacks()
#         else:
#             self.initial_attacks = attacks
#
#         self.Ws = Ws
#         self.model_str = model_str
#         self.w_str = w_str
#
#         self.AP = AP
#         self.D = D
#         self.T = T
#         self.save = save
#
#         self.hits_reroll = hits_reroll
#         self.wound_reroll = wound_reroll
#         self.damage_reroll = damage_reroll
#         self.save_reroll = save_reroll
#
#         self.inv = inv
#         self.in_cover = in_cover
#         self.wounds = wounds
#         self.fnp = fnp
#         self.target_comp = target_composition
#         self.w_name = w_name
#         self.target_name = target_name
#
#         self.wounds_pool = self.target_comp * self.wounds
#
#         # all events
#         self.stat_shots = self.set_attacks()  # check the initial_attacks allow to roll
#         # print("stat_shots", self.stat_shots)
#         self.stat_hits = self.to_hit()  # check how many hits valid
#         # print("stat_hits", self.stat_hits)
#         self.fail_hits = self.initial_attacks - self.stat_hits  # check how many failed to hit
#         # print("fail_hits", self.fail_hits)
#         self.stat_w_str = self.set_w_str()
#         print("stat_w_str", self.stat_w_str)
#         self.req_to_wound = self.set_req_to_wound()  # check required roll to wound
#         # print("req_to_wound", self.req_to_wound)
#         self.stat_wounds = self.to_wound()  # check how many hits could damage
#         # print("stat_wounds", self.stat_wounds)
#         self.saving = self.set_save()
#         # print("saving", self.saving)
#         self.stat_saved = self.to_save()  # check armour saves from defender_page
#         # print("stat_not_saved", self.stat_saved)
#         self.stat_failed_saves = self.stat_wounds - self.stat_saved
#         # print("stat_failed_saves", self.stat_failed_saves)
#         self.stat_damage = self.set_damage()  # --> OK
#         # print("stat_damage", self.stat_damage)
#         self.intake_damage = self.stat_failed_saves * self.stat_damage
#         # print("intake_damage", self.intake_damage)
#         if self.fnp:
#             self.fnp_saved = self.feel_no_pain()
#         else:
#             self.fnp = 0
#             self.fnp_saved = 0
#             # print("fnp_saved", self.fnp_saved)
#             # print("fnp x damage", self.fnp_saved * self.stat_damage)
#         self.wounds_taken, self.killed_models = self.wound_allocation()
#         self.print_on = print_on
#         if self.print_on:
#             # self.heading_printed = False
#             self.message = f"\n*** {self.initial_attacks} x {self.w_name}s: S-{self.w_str}, AP-{self.AP}, D-{self.D}"/
#                            f" vs {target_composition} x {target_name}s: T-{self.T}, Save-{self.save}+ ***"
#             self.__repr__()
#
#         """
#         self.effectiveness = 33.33%
#         self.wound_rate = 4.0/12
#         self.kill_rate = 1.0/3"""
#
#     # -> OK
#     def __repr__(self):
#         """
#         prints the table of the shooting phase wih the statistic calculation
#         :return:
#         """
#         print(f"\n{self.stat_shots}x {self.w_name} damage {self.D} vs {self.target_comp}x {self.target_name}")
#         heading = "Action      Dice  Event       Required    Chances     Asserted    Failed      Notes"
#         extra_spaces = len("after re-rolling all fails")
#         print(heading)
#         print("-" * (len(heading) + extras_paces))
#         for element in self.data_list:
#             total_len = 12
#             for item_ in element:
#                 word_len = len(str(item_))
#                 spaces = " " * (total_len - word_len)
#
#                 print(item_, end=spaces)
#             print("")
#         print("-" * (len(heading) + extra_spaces))
#
#     # -> OK
#     def create_table_line(self, action="Rolling", event=None, rolls=None, required=None, percent=None, asserted=None,
#                           failed=None, notes=None):
#         """
#         inserts each parameter in the line format and appends the line to the printing list
#         """
#         total_len = 12
#         if not notes:
#             notes = ""
#         action_spaces = ' ' * (total_len - len(action))
#         dice_space = ' ' * (6 - len(f"{rolls:.1f}"))
#         line = [f"{action}{action_spaces}{rolls:.1f}{dice_space}", f"{event}", f"at {required}+", f"{percent:.1f}%",
#                 f"{asserted:.1f}", f"{failed:.1f}", f"{notes}"]
#         self.data_list.append(line)
#
#     def create_results(self, wounds_taken, killed_models, wasted_wounds, models_in_unit):
#
#         wounds_left = self.wounds_pool - wounds_taken
#
#         line = [f"Out of {self.wounds_pool} wounds in the objects_models: {wounds_taken:.1f} wound(s) taken"
#                 f"\nOut of {self.target_comp} objects_models in objects_models, the number of kills:
#                 {killed_models:.1f} model(s)"
#                 f"\nUnit still holds: {models_in_unit} model(s)"
#                 f"\nTo eliminate the target is needed to take out: {wounds_left:.1f} more wound(s)"]
#         # f"\nWasted weapon damage that din't inflict any wounds: {wasted_wounds:.1f}"
#         self.data_list.append(line)
#
#     def create_bottom_line(self, wounds_taken, killed_models):
#         """
#         how effective this shooting choice is?
#         :param wounds_taken:
#         :param killed_models:
#         :return:
#         """
#         percent = 0
#         sep_line = "-" * 111
#         if self.target_comp > 1 and self.wounds == 1:  # case of 1wound-objects_models objects_models
#             percent = self.percentage_calc(total=self.target_comp, part=killed_models)
#         elif self.target_comp == 1 and self.wounds > 1:  # case one model multi wound
#             percent = self.percentage_calc(total=self.wounds, part=wounds_taken)
#         elif self.target_comp > 1 and self.wounds > 1:  # multi wound objects_models
#             percent = self.percentage_calc(total=self.wounds_pool, part=wounds_taken)
#
#         bottom_line = [sep_line, f"""\nFinal Effectiveness: {percent:.2f}%"""]
#         self.data_list.append(bottom_line)
#
#     # -> OK
#     def percent_of_getting_just_certain_number(self, n_shots):
#         percent_chances_of_rolling_an_specific_side = (n_shots / 6) * (100 / 6)
#         n_dice_represents = self.initial_attacks * percent_chances_of_rolling_an_specific_side / 100
#         return percent_chances_of_rolling_an_specific_side, n_dice_represents
#
#     # -> OK
#     @staticmethod
#     def percentage_calc(total=None, part=None, percent=None, print_on=False):
#         """
#          %     part
#         ---- = ----
#         100    total
#
#         :param print_on:
#         :param percent:
#         :param total:
#         :param part:
#         :return:
#         """
#         result = 0
#         if percent and total:
#             part = total * (percent / 100)
#             result = part
#         elif part and percent:
#             total = 100 / percent * part
#             result = total
#         elif part and total:
#             percent = part / total * 100
#             result = percent
#
#         if print_on:
#             print(f"\nPERCENT CALC:\t\t total: {total:.1f}\t part: {part:.1f}\t percent: {percent:.1f}\n")
#         return result
#
#     # -> OK
#     @staticmethod
#     def percent_of_die_roll(req_roll):
#         """
#         how much a die's side value or higher represent of the whole die.
#         :param req_roll: minimum required in a die roll to be successful
#         :return: string of percent of the chances to get the min req or more in a roll
#         """
#         if req_roll == 4:
#             return 50.0
#
#         return ShootingPhase.percentage_calc(6, (7 - req_roll), print_on=False)
#
#     # -> OK
#     @staticmethod
#     def roll(n, req_roll, print_on=False):
#         """
#         calculates statistically the possibility of n dice rolls in relation with the required roll
#         :param print_on: printing on
#         :param n: amount of dice to roll
#         :param req_roll: min required roll
#         :return: asserted rolls as float number out of n, eg 3.6 hits
#         """
#
#         if req_roll == str:  # some sort of debugging?
#             return n
#         if req_roll == 0 or req_roll is None or req_roll > 6:
#             print("no roll allowed")
#             return 0
#
#         accuracy = n / 100 * ((7 - req_roll) * (100 / 6))
#
#         if print_on:
#             print(f"\t{accuracy:.1f}/{n}\t\t{n - accuracy:.1f}/{n}")
#
#         return accuracy
#
#     # -> OK
#     def percent_chances_of_rolling_1(self):
#         return (self.initial_attacks / 6) * (100 / 6)
#
#     # -> OK
#     def re_rolling(self, fails, req):
#
#         extra_accuracy = 0
#
#         # reroll all 1s
#         if self.hits_reroll == "all 1s":
#             percent_chances_of_rolling_1 = self.percent_chances_of_rolling_1()
#             n_dice_represents = self.initial_attacks * percent_chances_of_rolling_1 / 100
#             extra_accuracy = self.roll(n_dice_represents, req)
#
#         # reroll 1 single roll of 1
#         elif self.hits_reroll == "1 roll of 1":
#             percent_chances_of_rolling_1 = self.percent_chances_of_rolling_1()
#             if 0 < percent_chances_of_rolling_1 <= 1:
#                 extra_accuracy = self.roll(percent_chances_of_rolling_1, req)
#             else:
#                 extra_accuracy = self.roll(1, req)
#
#         # reroll all fail rolls§
#         elif self.hits_reroll == "fail rolls":
#             extra_accuracy = self.roll(fails, req)
#
#         # reroll 1 single all fail
#         elif self.hits_reroll == "1 fail roll":
#             if 1 > fails > 0:
#                 extra_accuracy = self.roll(fails, req)
#
#             else:
#                 print("unknown case")
#
#         return extra_accuracy
#
#     # -> OK but points some possible errors TODO: get rid off the conflict
#     def set_attacks(self):
#         """
#         decodes the type of shot from WH code in to statistic calculable int.
#         :return: statistic amount of initial_attacks
#         """
#
#         holder = self.initial_attacks  # self.initial_attacks
#
#         if type(holder) == str:
#             # print("yes", end=" ")
#             # if holder.isnumeric():
#             #     return int(holder)
#             dice_amount, shot_random_amount = holder.split("d")
#             # print(dice_amount, type(dice_amount), shot_random_amount, type(shot_random_amount))
#             shot_random_amount = int(shot_random_amount)
#             # print(dice_amount, type(dice_amount))
#             # print(shot_random_amount, type(shot_random_amount))
#             if dice_amount:
#                 # print("yes", end=" ")
#                 dice_amount = int(dice_amount)
#                 # print(dice_amount, type(dice_amount))
#                 if shot_random_amount == 3:
#                     # print("yes", end=" ")
#                     self.initial_attacks = dice_amount * math.ceil(shot_random_amount / 2 + 0.4)
#                     # print(self.initial_attacks, type(initial_attacks))
#                 elif shot_random_amount == 6:
#                     # print("yes", end=" ")
#                     self.initial_attacks = dice_amount * 3.5  # shot_random_amount / 2, cause the average of d6 is
#                     # 6+, 50%
#                     # print(self.initial_attacks, type(self.initial_attacks))
#
#                 else:
#                     print("unknown case")  # todo: extra attacks
#             else:
#                 if shot_random_amount == 3:
#                     # print("yes", end=" ")
#                     self.initial_attacks = math.ceil(shot_random_amount / 2 + 0.4)
#                     # print(shot_random_amount, type(shot_random_amount))
#                 elif shot_random_amount == 6:
#                     # print("yes", end=" ")
#                     self.initial_attacks = shot_random_amount / 2 + 0.5
#                     # print(shot_random_amount, type(shot_random_amount))
#             return self.initial_attacks
#         return holder  # works pretty well
#
#     # -> OK
#     def to_hit(self):
#         """
#         for each shot of the profile/group a die is rolled to check hits
#         :return: statistic amount of successful initial_attacks
#         """
#
#         # auto hit # ok
#         if type(self.Ws) == str:
#             percent = 100
#             accuracy = self.initial_attacks
#             failed = 0
#             action = "Solving"
#             notes = f"auto hits, {self.w_name}"
#             self.create_table_line(action=action, event="autohits", rolls=self.initial_attacks, required="_",
#                                    percent=percent, asserted=accuracy, failed=failed, notes=notes)
#             return self.stat_shots
#
#         # normal case, no reroll
#         event = "to hit"
#         action = "Rolling"
#         initial_rolls = self.initial_attacks
#         required = self.Ws
#         percent = ShootingPhase.percent_of_die_roll(required)
#         asserted = self.roll(initial_rolls, required)
#         failed = initial_rolls - asserted
#
#         self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required, percent=percent,
#                                asserted=asserted, failed=failed, notes=None)
#         if self.hits_reroll:
#             action = "re-rolling"
#             re_roll_type = self.hits_reroll
#             extra_asserted = self.roll(failed, required)
#             extra_percent = self.percentage_calc(total=initial_rolls, part=extra_asserted)
#             failed_to_re_rolls = failed
#             notes = f"re-rolled {re_roll_type}"
#
#             re_failed = failed_to_re_rolls - extra_asserted
#             if re_failed < 0:
#                 re_failed = 0
#             self.create_table_line(action=action, event=event, rolls=failed_to_re_rolls, required=self.Ws,
#                                    percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)
#
#             action = "Resulting"
#             asserted += extra_asserted
#             if asserted > initial_rolls:
#                 asserted = initial_rolls
#             if asserted < 0:
#                 asserted = 0
#             percent += extra_percent
#             if percent < 0:
#                 percent = 0
#             notes = f"after re-rolling {self.hits_reroll}"
#             self.create_table_line(action=action, event=event, rolls=initial_rolls, required=self.Ws, percent=percent,
#                                    asserted=asserted, failed=re_failed, notes=notes)
#
#         return asserted
#
#     # -> OK
#     def set_req_to_wound(self):
#         """
#         decodes the WH codes for wounding by calculating toughness  vs  strength.
#         :return:
#         """
#
#         if self.w_str > self.T:
#             req_wound_roll = 3
#             if self.w_str >= self.T * 2:
#                 req_wound_roll = 2
#         elif self.w_str < self.T:
#             req_wound_roll = 5
#             if self.w_str <= self.T / 2:
#                 req_wound_roll = 6
#         else:
#             req_wound_roll = 4
#
#         return req_wound_roll
#
#     def set_w_str(self):
#         """
#         decodes the type of strength from WH code in to statistic calculable int.
#         :return: statistic amount of initial_attacks
#         """
#
#         holder = self.w_str  # self.initial_attacks
#
#         if type(holder) == str:
#             if "d" in holder:
#                 dice_amount, attacks_random_amount = holder.split("d")
#                 # print(dice_amount, type(dice_amount), attacks_random_amount, type(attacks_random_amount))
#                 attacks_random_amount = int(attacks_random_amount)
#                 # print(dice_amount, type(dice_amount))
#                 # print(attacks_random_amount, type(attacks_random_amount))
#                 if dice_amount:
#                     # print("yes", end=" ")
#                     dice_amount = int(dice_amount)
#                     # print(dice_amount, type(dice_amount))
#                     if attacks_random_amount == 3:
#                         # print("yes", end=" ")
#                         self.initial_attacks = dice_amount * math.ceil(attacks_random_amount / 2 + 0.4)
#                         # print(self.initial_attacks, type(initial_attacks))
#                     elif attacks_random_amount == 6:
#                         # print("yes", end=" ")
#                         self.initial_attacks = dice_amount * 3.5
#                         # print(self.initial_attacks, type(self.initial_attacks))
#
#                     else:
#                         print("unknown case")
#                 else:
#                     if attacks_random_amount == 3:
#                         # print("yes", end=" ")
#                         self.initial_attacks = math.ceil(attacks_random_amount / 2 + 0.4)
#                         # print(attacks_random_amount, type(attacks_random_amount))
#                     elif attacks_random_amount == 6:
#                         # print("yes", end=" ")
#                         self.initial_attacks = attacks_random_amount / 2 + 0.5
#                         # print(attacks_random_amount, type(attacks_random_amount))
#                 return self.initial_attacks
#         return holder  # works pretty well
#
#     # -> OK
#     def to_wound(self):
#         """
#         for each successful hit of the profile/group a die is rolled to check wounds
#         :return: statistic amount of successful wounds inflicted
#         """
#
#         event = "to wound"
#         initial_rolls = self.stat_hits
#         percent = self.percent_of_die_roll(self.req_to_wound)
#         asserted = self.roll(self.stat_hits, self.req_to_wound)
#         required = self.set_req_to_wound()
#         failed = self.stat_hits - asserted
#
#         self.create_table_line(event=event, rolls=initial_rolls, required=required, percent=percent,
#                               asserted=asserted, failed=failed)
#
#         if self.wound_reroll:
#             action = "Re-rolling"
#             extra_asserted = self.roll(failed, required)
#             extra_percent = self.percentage_calc(total=self.stat_hits, part=extra_asserted)
#             initial_rolls = failed
#             re_failed = initial_rolls - extra_asserted
#             notes = f"re-rolled {self.wound_reroll}"
#
#             self.create_table_line(action=action, event=event, rolls=initial_rolls, required=self.req_to_wound,
#                                    percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)
#
#             action = "Resulting"
#             asserted += extra_asserted
#             if asserted < 0:
#                 asserted = 0
#             percent += extra_percent
#             notes = f"after re-rolling {self.hits_reroll}"
#             self.create_table_line(action=action, event=event, rolls=self.stat_hits, required=self.req_to_wound,
#                                    percent=percent, asserted=asserted, failed=re_failed, notes=notes)
#
#         return asserted
#
#     # -> OK
#     def set_save(self):
#
#         if self.in_cover:
#             self.save -= 1
#             if self.save < 2:
#                 self.save = 2
#         if self.inv and self.save + self.AP > self.inv:
#             # print(f"inv save {self.inv}+")
#             return self.inv
#         if self.save + self.AP > 6:
#             # print("no save\t 0", end="")
#             return None
#
#         return self.save + self.AP
#
#     # -> OK
#     def to_save(self):
#
#         action = "Rolling"
#         event = "to save"
#         required = self.saving
#         initial_rolls = self.stat_wounds
#
#         asserted = self.roll(initial_rolls, required)
#         percent = self.percentage_calc(total=initial_rolls, part=asserted)
#         failed = initial_rolls - asserted
#         damage = self.D
#         notes = f"weapon damage: {damage}"
#
#         self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required, percent=percent,
#                                asserted=asserted, failed=failed, notes=notes)
#         if self.save_reroll:
#             action = "Re-rolling"
#             re_roll_type = self.save_reroll
#             re_rolls = failed
#             extra_asserted = self.roll(re_rolls, required)
#             extra_percent = self.percentage_calc(total=initial_rolls, part=extra_asserted)
#             re_failed = re_rolls - extra_asserted
#             notes = f"re-rolled {re_roll_type}"
#
#             self.create_table_line(action=action, event=event, rolls=failed, required=required,
#                                    percent=extra_percent, asserted=extra_asserted, failed=re_failed, notes=notes)
#
#             action = "Resulting"
#             asserted += extra_asserted
#             if asserted < 0:
#                 asserted = 0
#             percent += extra_percent
#             notes = f"after re-rolling {re_roll_type}"
#             self.create_table_line(action=action, event=event, rolls=initial_rolls, required=required,
#                                    percent=percent, asserted=asserted, failed=re_failed, notes=notes)
#
#         return asserted
#
#     # -> OK
#     def set_damage(self):
#         """
#         decode the WH codes for damage to be calculated
#         :return: a int amount of damage per shot
#         """
#
#         holder = self.D
#
#         damage_final = 0
#         extra = 0
#
#         if type(holder) == str:
#             holder = holder.split("d")  # is working tho, holder became a list
#
#             amount = holder[0]
#             random_y = holder[1]
#
#             if "+" in random_y:
#                 random_y, extra = random_y.split("+")
#                 random_y = int(random_y)
#                 extra = int(extra)
#
#             if not amount:
#                 amount = 1
#             else:
#                 int(amount)
#
#             if int(random_y) == 3:
#                 damage_final = math.ceil(int(random_y) / 2) * int(amount)
#             elif int(random_y) == 6:
#                 damage_final = math.ceil(int(random_y) / 2 + 0.4) * int(amount)
#
#             damage_final += int(extra)
#             # print("damage_final", damage_final)
#
#         elif type(holder) is int:
#             return holder
#
#         else:
#             damage_final = self.D
#
#         return damage_final
#
#     def feel_no_pain(self):
#
#         fail_to_save = self.stat_failed_saves
#         damage = self.set_damage()
#
#         to_fnp = fail_to_save * damage
#         action = "Rolling"
#         event = "to FNP"
#         rolls = to_fnp
#         required = self.fnp
#         asserted = self.roll(rolls, required)
#         percent = self.percentage_calc(total=rolls, part=asserted)
#         failed = rolls - asserted
#         notes = "feel no pain per weapon damage"
#
#         self.create_table_line(action=action, event=event, rolls=rolls, required=required, percent=percent,
#                                asserted=asserted, failed=failed, notes=notes)
#
#         return asserted
#
#     # todo: from a class objects_models that hods many class objects_models in it
#     def wound_allocation(self):
#
#         original_wounds_per_model = self.wounds  # holder
#         models_in_unit = self.target_comp
#         original_weapon_damage = self.stat_damage
#         weapon_damage = original_weapon_damage
#         dice_counter = self.stat_failed_saves
#         wounds_left = original_wounds_per_model
#         killed_models = 0
#         wasted_wounds = 0
#         wounds_taken = 0
#
#         if self.fnp:
#             percent_of_fnp = self.percent_of_die_roll(self.fnp)
#             weapon_damage = weapon_damage - self.percentage_calc(percent=percent_of_fnp, total=weapon_damage)
#             # print("weapon_damage", weapon_damage)
#         while dice_counter > 0 and models_in_unit > 0:
#
#             if self.target_comp > 1:
#                 wounds_left = original_wounds_per_model  # starting with a new model
#             # wounds_holder = 0
#
#             while wounds_left > 0 and dice_counter > 0:
#                 dice_counter -= 1
#                 wounds_left -= weapon_damage
#                 if wounds_left == 0:
#                     wounds_taken += weapon_damage
#                     models_in_unit -= 1
#                     killed_models += 1
#                 if wounds_left < 0:
#                     wounds_taken += wounds_left
#                     models_in_unit -= 1
#                     killed_models += 1
#                     wasted_wounds += abs(wounds_left)
#                 if wounds_left > 0:
#                     wounds_taken += weapon_damage
#                     if models_in_unit <= 0:
#                         if dice_counter > 0:
#                             wasted_wounds += dice_counter * weapon_damage
#
#         # print("wounds_taken in wound_allocation", wounds_taken)
#         "we are resolving the initial attacks vs the final results"
#         self.create_bottom_line(wounds_taken, killed_models)
#         self.create_results(wounds_taken, killed_models, models_in_unit)
#         return wounds_taken, killed_models


if __name__ == "__main__":
    print(ShootingPhase.shooting_phase)

    # TESTING
    shoot_1 = ShootingPhase(shots=5, Bs=3, w_str=4, AP=0, D=1, T=3, save=4, wounds=1, hits_reroll="1 roll of 1",
                            target_composition=5, w_name="bolter", target_name="fire warrior", wound_reroll="all fails",
                            print_on=True)

    shoot_2 = ShootingPhase(shots=5, Bs=4, w_str=5, AP=0, D=1, T=4, save=3, wounds=1, hits_reroll="fail rolls",
                            target_composition=5, w_name="pulse rifle", target_name="marine", wound_reroll='all 1s',
                            print_on=True)

    shoot_3 = ShootingPhase(shots="3d6", Bs="autohits", w_str=4, AP=0, D=1, T=3, save=4,
                            target_composition=5, w_name="flamer", target_name="fire warrior",
                            wound_reroll='1 fail roll',
                            print_on=True)

    shoot_4 = ShootingPhase(shots="2d3", Bs=3, w_str=8, AP=3, D=2, T=8, save=2, wounds=14,
                            target_composition=1, w_name="DA plasma speeder, overheated", target_name="land raider",
                            hits_reroll='all 1s', print_on=True)

    shoot_5 = ShootingPhase(shots=4, Bs=3, w_str=9, AP=3, D="d6", T=6, save=2, inv=3, wounds=16, fnp=5,
                            target_composition=1, wound_reroll="all fails", w_name="las cannons", target_name="riptide",
                            print_on=True)

    shoot_6 = ShootingPhase(shots=12, Bs=2, w_str=8, AP=1, D="d3", T=5, save=2, inv=3, wounds=6, fnp=5,
                            target_composition=1, hits_reroll="all 1s", wound_reroll="all fails",
                            w_name="cycling ion blaster", target_name="wolf lord with adamantine mantle",
                            save_reroll="all 1s", print_on=True)

    shoot_7 = ShootingPhase(shots=5, Bs=3, w_str=8, AP=4, D="d6+2", T=5, save=2, wounds=4, inv=4, fnp=5,
                            target_composition=3, hits_reroll="all 1s", wound_reroll="all 1s", w_name="combi-meltas",
                            save_reroll="all fails", target_name="thunder wolf cavalry", print_on=True)

    shoot_8 = ShootingPhase(shots=5, Bs=3, w_str=8, AP=4, D="d6+2", T=5, save=2, wounds=4, inv=4, fnp=5,
                            target_composition=3, hits_reroll="all 1s", wound_reroll="all 1s", w_name="obliteratos "
                                                                                                      "flesh-metal "
                                                                                                      "all_equipments",
                            save_reroll="all fails", target_name="", print_on=True)