# Helpers Tests

This section holds all the tests done to obtain the values of the helpers bonus. Although in-game we are shown 4 gloves icons representing the helpers bonus, the actual number of Pokémons placed in the power spot matter (until 15, which is the maximum, represented with 4 gloves). Each file here holds all the tests done with a specific number of Pokémons placed on the power spot, and the obtained results with a summary of them all.

For each test, this information is represented:
- A title, indicating all the necessary info of the tests (boss, attackers, bonuses), so to be able to replicate it (both in-game and with maths).
- The segment sequence, which is the obtained result from the test, in the form of how many segments were dropped after each attack.
- Python code holding all the stats that represents the tests. Use it as the input for the `mult_test.main` method. For convenience, replace this code on the `help_test.py` file, optionally use the segment sequence, adjust the values range and execute it to obtain the result from the test.
- Resulting damage values as a list of sets. Each set holds the possible damage values for each type of attack. These values are the only ones that are able to reproduce the segment sequence.
- Resulting helper bonus values range, the only values that produce the previous damage values.
