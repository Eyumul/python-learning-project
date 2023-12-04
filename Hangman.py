import random
words = ["express","jackpot","quality","neutral","freedom","impulse"]
live = ["           * *                   \n         *     *                 \n       *         *               \n     *             *             \n   *                 *           \n","          * * *                  \n        *   *   *                \n      *     *      *             \n    *       *        *           \n  *         *          *         \n           * *                   \n         *     *                 \n       *         *               \n     *             *             \n   *                 *           \n","          *****                  \n        *       *                \n       *         *               \n       *         *               \n         *     *                 \n          * * *                  \n          * * *                  \n          * * *                  \n        *   *   *                \n      *     *      *             \n    *       *        *           \n  *         *          *         \n           * *                   \n         *     *                 \n       *         *               \n     *             *             \n   *                 *           \n","          *****                * \n        *       *            *   \n       *         *         *     \n       *         *       *       \n         *     *      **         \n          * * *    ***           \n          * * ****               \n          * * *                  \n        *   *   *                \n      *     *      *             \n    *       *        *           \n  *         *          *         \n           * *                   \n         *     *                 \n       *         *               \n     *             *             \n   *                 *           \n","          *****                * \n        *       *            *   \n       *  X   X  *         *     \n       *         *       *       \n         *     *      **         \n          * * *    ***           \n          * * ****               \n          * * *                  \n        *   *   *                \n      *     *      *             \n    *       *        *           \n  *         *          *         \n           * *                   \n         *     *                 \n       *         *               \n     *             *             \n   *                 *           \n"]
n = random.randint(0,5)
i = 1
j = 0
length = 7
print("HANGMAN\nGuess the seven letter word.\nRules:\n1. You have 5 lives\n2. The words are all in lowercase\n3. Don't use numbers or other characters(only letters)")
upword = words[n]

while i <= 2:
    letter = input("Enter a letter: ")
    if letter not in words[n]:
        print(live[j])
        if j == 4:
            print("YOU FAILD\n")
            break
        print ("Try again\n")
        j += 1
    else:
        length -= 1
        print("\nYou are correct")
        print(str(length) + " more letters left\n")
        words[n] = words[n].replace(letter,"l")
        if length == 0:
            print("$$$YOU WON$$$")
            print("The word is '" + upword + "'.\n")
            break
        







