# def make_table(data_sequence, num_o_columns):
#     table_str = ""
#     for idx, ea_item in enumerate(data_sequence):
#         table_str += str(ea_item) + "\t"
#         if (idx + 1) % num_o_columns == 0:
#             table_str += "\n"
#     return table_str
#
# days = range(1, 30)
# week_days = 7
# month_calendar = make_table(days, week_days)
# print(month_calendar)






# def get_trial_result(votes):
#     """
#     Function: get_trial_result
#     :param votes: a list containing the votes of each juror;
#                   each is a string either equal to "G" or "NG"
#     :return: a string of the jury decision
#     """
#     SUPER_MAJORITY_VOTES = 7
#     UNANIMOUS_VOTES = 9
#     guilty_cnt = 0
#
#     # Count the number of "G" votes
#     for ea_decision in votes:
#         if ea_decision == "G":
#             guilty_cnt += 1
#
#     # Determine the trial result
#     if guilty_cnt == UNANIMOUS_VOTES:
#         return "Guilty - Unanimous(%i to %i)" % (guilty_cnt, UNANIMOUS_VOTES - guilty_cnt)
#     elif guilty_cnt >= SUPER_MAJORITY_VOTES:
#         return "Guilty - Split(%i to %i)" % (guilty_cnt, UNANIMOUS_VOTES - guilty_cnt)
#     elif guilty_cnt > 0:
#         return "Hung Jury - Mistrial(%i to %i)" % (guilty_cnt, UNANIMOUS_VOTES - guilty_cnt)
#     else:
#         return "Not Guilty(%i to %i)" % (guilty_cnt, UNANIMOUS_VOTES - guilty_cnt)
#
# # Test Code
# if __name__ == "__main__":
#     jury_decision_1 = ["G", "G", "G", "G", "G", "G", "G", "G", "G"]
#     jury_decision_2 = ["NG", "NG", "NG", "NG", "NG", "NG", "NG", "NG", "NG"]
#     jury_decision_3 = ["G", "G", "G", "G", "G", "G", "G", "NG", "NG"]
#     jury_decision_4 = ["G", "G", "NG", "NG", "NG", "NG", "NG", "NG", "G"]
#     jury_decision_5 = ["NG", "NG", "NG", "NG", "NG", "NG", "NG", "NG", "G"]
#
#     verdict = get_trial_result(jury_decision_1)
#     print(verdict)
#     verdict = get_trial_result(jury_decision_2)
#     print(verdict)
#     verdict = get_trial_result(jury_decision_3)
#     print(verdict)
#     verdict = get_trial_result(jury_decision_4)
#     print(verdict)
#     verdict = get_trial_result(jury_decision_5)
#     print(verdict)






#
#
# from random import randrange
#
#
# class Die:
#     """
#     One object of this class represents one die with 6 sides. You can roll the die
#     to come up with a pseudo-random value between 1 and 6.
#     """
#
#     def __init__(self):
#         """
#         Initializes the die to 1.
#         """
#         self.value = 1
#
#     def __str__(self):
#         """
#         Returns a string representation of the die.
#         """
#         return "This die has value: " + str(self.value)
#
#     def roll(self):
#         """
#         Rolls the die to come up with a pseudo-random value between 1 and 6.
#         """
#         self.value = randrange(1, 7)
#
#
# # Main program
# def main():
#     # Create two dice objects
#     die1 = Die()
#     die2 = Die()
#
#     pair_count = 0  # To count how many pairs are rolled
#
#     # Roll the dice 10 times
#     for roll_num in range(1, 11):
#         die1.roll()
#         die2.roll()
#
#         print(f"Roll {roll_num}:")
#         print(f"Die 1: {die1.value}")
#         print(f"Die 2: {die2.value}")
#
#         # Check if both dice have the same value
#         if die1.value == die2.value:
#             print("It's a pair!")
#             pair_count += 1
#         else:
#             print("Not a pair.")
#         print("-" * 20)
#
#     # Print the total number of pairs
#     print(f"Total pairs rolled: {pair_count}")
#
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#














# a = [23, 99, 77, 39, 28]
# b = [1, 2, 4, [22, 88]]
#
# # Step 1: Extend `a` with the first three elements of `b`
# a.extend(b[:3])
#
# # Step 2: Expand `a` with the last nested list in `b` (flattened)
# a.extend(b[3])
#
# # Result
# print(a)
# # Output: [23, 99, 77, 39, 28, 1, 2, 4, 22, 88]
