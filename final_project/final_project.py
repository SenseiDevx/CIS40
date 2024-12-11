import random


def monty_hall_simulation(trials=10000):
    total_wins = 0

    for _ in range(trials):
        # Step 1: Randomly place the car behind one of the doors (0, 1, 2)
        car_door = random.randint(0, 2)

        # Step 2: Contestant picks a door randomly
        contestant_choice = random.randint(0, 2)

        # Step 3: Host opens a door with a goat, which is not the contestant's choice or the car
        possible_doors_to_open = [door for door in range(3) if door != contestant_choice and door != car_door]
        host_opened_door = random.choice(possible_doors_to_open)

        # Step 4: Contestant switches to the other unopened door
        remaining_door = [door for door in range(3) if door != contestant_choice and door != host_opened_door][0]

        # Step 5: Check if the contestant wins by switching
        if remaining_door == car_door:
            total_wins += 1

    # Step 6: Output the ratio of total wins to total trials
    win_ratio = total_wins / trials
    print(f"Total Wins: {total_wins} out of {trials} trials")
    print(f"Winning Probability when switching: {win_ratio * 100:.2f}%")


if __name__ == "__main__":
    monty_hall_simulation()




"""
This is my essay to game Monty Hall.


The Monty Hall Problem is a classic probability puzzle that can feel very counterintuitive at first glance, 
but once you understand it, it becomes surprisingly simple. Let me guide you through the reasoning behind 
why switching doors in this game increases your chances of winning.


The Setup
Imagine you are on a game show. You are presented with three closed doors. Behind one door is a car, and behind 
the other two are goats. You, as the contestant, want to win the car. Initially, you pick one of the three doors.
Importantly, you have a 1 in 3 chance of picking the door with the car, meaning you have a 1/3 probability of
winning. Since there are two goats, there is a 2/3 probability that you picked a goat.

After you make your initial choice, the host (Monty), who knows where the car is, opens one of the two doors you 
didn’t pick. He always opens a door with a goat behind it. Now, you are left with two closed doors: the one you 
originally chose and one other door. Monty then gives you a choice: stay with your original door or switch to the 
other remaining door. The big question is: Should you switch?


Why Switching Works
The key to understanding why switching is beneficial lies in probability and in considering all possible scenarios.

  - Initial Choice: When you first pick a door, there is a 1/3 chance that you chose the car and a 2/3 chance that 
    you chose a goat. In other words, you are more likely to pick a goat on your first try.

  - After Monty Opens a Door: Monty opens one of the other doors, which always has a goat. This action does not 
    change the probability of your initial choice. Your first choice still has a 1/3 chance of being the car. However, 
    the crucial thing is that now you have new information: Monty has revealed a goat, and the other door remains closed.

  - The Remaining Door: The remaining closed door now effectively has the full 2/3 chance of hiding the car. This is 
    because if your initial choice was wrong (which it likely was, with a probability of 2/3), the car must be behind the 
    other door. Thus, by switching, you are taking advantage of the higher probability (2/3) that the car is behind the
    remaining door.



Intuitive Explanation

To make it even clearer, think of it this way: at the start, the car is more likely to be behind one of the doors you did
not pick. Since Monty then opens a door to show a goat, the other door becomes a much more attractive choice. 
The 1/3 versus 2/3 probability distribution remains the same, but the action of Monty eliminating one door essentially
shifts all the probability weight onto the remaining door.

In simple terms, by switching, you are relying on the fact that your initial choice was probably wrong. Since Monty 
always opens a goat door, switching essentially lets you benefit from the fact that you initially had poor odds (1/3) 
and turn them into a higher success rate (2/3).


Conclusion
The Monty Hall Problem shows us that sometimes the correct solution to a problem defies our intuitive thinking. 
By switching doors, you double your chances of winning, from 1/3 to 2/3. This is a powerful lesson in probability, 
showing that what may initially seem like a 50-50 decision is actually weighted heavily in favor of switching. So next
time you find yourself on a game show, remember: always switch!
"""
