import random

# (a)
def yahtzee_probability(num_simulations):
    count = 0
    for i in range(num_simulations):
        rolls = [random.randint(1, 6) for _ in range(5)]
        if len(set(rolls)) == 1:
            count += 1
    return count / num_simulations


print("Probability of rolling a Yahtzee:", yahtzee_probability(100000))


def large_straight_probability(num_simulations):
    count = 0
    for i in range(num_simulations):
        rolls = set([random.randint(1, 6) for _ in range(5)])
        if rolls in [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]:
            count += 1
        return count / num_simulations


print("Probability of rolling a large straight:", large_straight_probability(100000))


def longest_run(num_simulations):
    max_run_sum = 0
    for i in range(num_simulations):
        flips = [random.randint(0, 1) for _ in range(200)]
        current_run = 1
        max_run = 1
        for j in range(1, 200):
            if flips[j] == flips[j-1]:
                current_run += 1
            else:
                if current_run > max_run:
                    max_run = current_run
                current_run = 1
        if current_run > max_run:
            max_run = current_run
        max_run_sum += max_run
    return max_run_sum / num_simulations


print("Average longest run of heads or tails in 200 coin flips:", longest_run(100000))


def five_heads(num_simulations):
    flips_sum = 0
    for i in range(num_simulations):
        flips = 0
        consecutive_heads = 0
        while consecutive_heads < 5:
            flips += 1
            if random.randint(0, 1) == 1:
                consecutive_heads += 1
            else:
                consecutive_heads = 0
        flips_sum += flips
    return flips_sum / num_simulations

print("Average number of coin flips before 5 heads in a row:", five_heads(100000))


def string_probability(num_simulations, s):
    flips_sum = 0
    for i in range(num_simulations):
        flips = 0
        while True:
            flips += 1
            if ''.join([random.choice(['H', 'T']) for _ in range(len(s))]) == s:
                flips_sum += flips
                break
    return flips_sum / num_simulations


print("Average number of coin flips before HHTTH comes up:", string_probability(100000, "HHTTH"))