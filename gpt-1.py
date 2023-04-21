import itertools


def generate_seeds(num_characters, num_spaces):
    operators = ["<", ">"]
    spaces = [" "] * num_spaces

    seeds = []

    for space_positions in itertools.combinations(
        range(num_characters - 1), num_spaces
    ):
        seed = [None] * num_characters
        for position in space_positions:
            seed[position] = " "

        operator_positions = [
            i for i in range(num_characters) if i not in space_positions
        ]

        for operator_combination in itertools.product(
            operators, repeat=len(operator_positions)
        ):
            for i, operator in zip(operator_positions, operator_combination):
                seed[i] = operator
            seeds.append("".join(seed))

    return seeds


def write_seeds_to_file(num_characters, num_spaces, output_file):
    seeds = generate_seeds(num_characters, num_spaces)

    with open(output_file, "w") as file:
        for i, seed in enumerate(seeds):
            file.write(seed)
            if (i + 1) % 4 == 0:
                file.write("\n")
            else:
                file.write(" " * (15 - len(seed)))


num_characters = 6
num_spaces = 2
output_file = "gpt-1..txt"

write_seeds_to_file(num_characters, num_spaces, output_file)
