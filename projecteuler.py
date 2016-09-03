"""Project Euler"""
import math
import os
import itertools
import datetime
import mathhelper


def problem1():
    """ Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

    """
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


def problem2():
    """ Even Fibonacci numbers
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.

    """
    return_value = 0
    for number in mathhelper.fibonacci_number_list(4000000):
        if number % 2 == 0:
            return_value += number
    return return_value


def problem3():
    """ Largest prime factor
    What is the largest prime factor of the number 600851475143 ?

    """
    const_number = 600851475143
    for i in range(int(math.sqrt(const_number)), 2, -1):
        if const_number % i == 0 and mathhelper.is_prime(i):
            return i


def problem4():
    """ Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two
    3-digit numbers.

    """
    return max(
        x * y for (x, y) in itertools.product(range(100, 1000), range(100, 1000)) if
        mathhelper.is_palindromic(x * y))


def problem5():
    """ Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
    remainder. What is the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20?

    """
    return mathhelper.least_common_multiple(*range(1, 21))


def problem6():
    """ Sum square difference
    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.

    """
    return (sum(range(1, 101)) ** 2) - (sum(x ** 2 for x in range(1, 101)))


def problem7():
    """ 10001st prime
    What is the 10 001st prime number?

    """
    count = 0
    number = 1
    while True:
        number += 1

        if mathhelper.is_prime(number):
            count += 1

        if count == 10001:
            break
    return number


def problem8():
    """ Largest product in a series
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?

    """
    number_data = ("73167176531330624919225119674426574742355349194934"
                   "96983520312774506326239578318016984801869478851843"
                   "85861560789112949495459501737958331952853208805511"
                   "12540698747158523863050715693290963295227443043557"
                   "66896648950445244523161731856403098711121722383113"
                   "62229893423380308135336276614282806444486645238749"
                   "30358907296290491560440772390713810515859307960866"
                   "70172427121883998797908792274921901699720888093776"
                   "65727333001053367881220235421809751254540594752243"
                   "52584907711670556013604839586446706324415722155397"
                   "53697817977846174064955149290862569321978468622482"
                   "83972241375657056057490261407972968652414535100474"
                   "82166370484403199890008895243450658541227588666881"
                   "16427171479924442928230863465674813919123162824586"
                   "17866458359124566529476545682848912883142607690042"
                   "24219022671055626321111109370544217506941658960408"
                   "07198403850962455444362981230987879927244284909188"
                   "84580156166097919133875499200524063689912560717606"
                   "05886116467109405077541002256983155200055935729725"
                   "71636269561882670428252483600823257530420752963450")
    number_list = list(number_data)

    max_value = 0
    for i in range(0, len(number_list))[:-12]:
        product = 1
        for number in number_list[i:i + 13]:
            product *= int(number)
        if product > max_value:
            max_value = product

    return max_value


def problem9():
    """ Special Pythagorean triplet
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

    """
    for first in range(1, 1000 // 3):
        for second in range(first, 1000 // 2):
            third = 1000 - (first + second)
            if first ** 2 + second ** 2 == third ** 2:
                return first * second * third


def problem10():
    """ Summation of primes
    Find the sum of all the primes below two million.

    """
    return sum(x for x in range(2, 2000000) if mathhelper.is_prime(x))


def problem11():
    """ Largest product in a grid
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?

    """

    grid = ("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n"
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n"
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n"
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n"
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n"
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n"
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n"
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n"
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n"
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n"
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n"
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n"
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n"
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n"
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n"
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n"
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n"
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n"
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n"
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
    matrix = [[int(column) for column in row.split(" ")] for row in grid.split("\n")]

    largest_product = 0
    row_count = len(matrix)
    for row_number in range(row_count):
        column_count = len(matrix[row_number])
        for column_number in range(column_count):
            # ->
            if column_count > column_number + 3:
                temp = matrix[row_number][column_number] \
                       * matrix[row_number][column_number + 1] \
                       * matrix[row_number][column_number + 2] \
                       * matrix[row_number][column_number + 3]

                largest_product = max(largest_product, temp)

            # \
            if row_count > row_number + 3 and column_count > column_number + 3:
                temp = matrix[row_number][column_number] \
                       * matrix[row_number + 1][column_number + 1] \
                       * matrix[row_number + 2][column_number + 2] \
                       * matrix[row_number + 3][column_number + 3]

                largest_product = max(largest_product, temp)

            # |
            if row_count > row_number + 3:
                temp = matrix[row_number][column_number] \
                       * matrix[row_number + 1][column_number] \
                       * matrix[row_number + 2][column_number] \
                       * matrix[row_number + 3][column_number]

                largest_product = max(largest_product, temp)

            # /
            if row_count > row_number + 3 and column_number - 3 > -1:
                temp = matrix[row_number][column_number] \
                       * matrix[row_number + 1][column_number - 1] \
                       * matrix[row_number + 2][column_number - 2] \
                       * matrix[row_number + 3][column_number - 3]

                largest_product = max(largest_product, temp)

            # <-
            if column_number - 3 > -1:
                temp = matrix[row_number][column_number] \
                       * matrix[row_number][column_number - 1] \
                       * matrix[row_number][column_number - 2] \
                       * matrix[row_number][column_number - 3]

                largest_product = max(largest_product, temp)

    return largest_product


def problem12():
    """ Highly divisible triangular number
    What is the value of the first triangle number to have over five hundred divisors?

    """
    for triangle_number in mathhelper.triangle_number_list(None):
        if mathhelper.factor_count(triangle_number) > 500:
            return triangle_number


def problem13():
    """ Large sum
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    """
    data = ("37107287533902102798797998220837590246510135740250\n"
            "46376937677490009712648124896970078050417018260538\n"
            "74324986199524741059474233309513058123726617309629\n"
            "91942213363574161572522430563301811072406154908250\n"
            "23067588207539346171171980310421047513778063246676\n"
            "89261670696623633820136378418383684178734361726757\n"
            "28112879812849979408065481931592621691275889832738\n"
            "44274228917432520321923589422876796487670272189318\n"
            "47451445736001306439091167216856844588711603153276\n"
            "70386486105843025439939619828917593665686757934951\n"
            "62176457141856560629502157223196586755079324193331\n"
            "64906352462741904929101432445813822663347944758178\n"
            "92575867718337217661963751590579239728245598838407\n"
            "58203565325359399008402633568948830189458628227828\n"
            "80181199384826282014278194139940567587151170094390\n"
            "35398664372827112653829987240784473053190104293586\n"
            "86515506006295864861532075273371959191420517255829\n"
            "71693888707715466499115593487603532921714970056938\n"
            "54370070576826684624621495650076471787294438377604\n"
            "53282654108756828443191190634694037855217779295145\n"
            "36123272525000296071075082563815656710885258350721\n"
            "45876576172410976447339110607218265236877223636045\n"
            "17423706905851860660448207621209813287860733969412\n"
            "81142660418086830619328460811191061556940512689692\n"
            "51934325451728388641918047049293215058642563049483\n"
            "62467221648435076201727918039944693004732956340691\n"
            "15732444386908125794514089057706229429197107928209\n"
            "55037687525678773091862540744969844508330393682126\n"
            "18336384825330154686196124348767681297534375946515\n"
            "80386287592878490201521685554828717201219257766954\n"
            "78182833757993103614740356856449095527097864797581\n"
            "16726320100436897842553539920931837441497806860984\n"
            "48403098129077791799088218795327364475675590848030\n"
            "87086987551392711854517078544161852424320693150332\n"
            "59959406895756536782107074926966537676326235447210\n"
            "69793950679652694742597709739166693763042633987085\n"
            "41052684708299085211399427365734116182760315001271\n"
            "65378607361501080857009149939512557028198746004375\n"
            "35829035317434717326932123578154982629742552737307\n"
            "94953759765105305946966067683156574377167401875275\n"
            "88902802571733229619176668713819931811048770190271\n"
            "25267680276078003013678680992525463401061632866526\n"
            "36270218540497705585629946580636237993140746255962\n"
            "24074486908231174977792365466257246923322810917141\n"
            "91430288197103288597806669760892938638285025333403\n"
            "34413065578016127815921815005561868836468420090470\n"
            "23053081172816430487623791969842487255036638784583\n"
            "11487696932154902810424020138335124462181441773470\n"
            "63783299490636259666498587618221225225512486764533\n"
            "67720186971698544312419572409913959008952310058822\n"
            "95548255300263520781532296796249481641953868218774\n"
            "76085327132285723110424803456124867697064507995236\n"
            "37774242535411291684276865538926205024910326572967\n"
            "23701913275725675285653248258265463092207058596522\n"
            "29798860272258331913126375147341994889534765745501\n"
            "18495701454879288984856827726077713721403798879715\n"
            "38298203783031473527721580348144513491373226651381\n"
            "34829543829199918180278916522431027392251122869539\n"
            "40957953066405232632538044100059654939159879593635\n"
            "29746152185502371307642255121183693803580388584903\n"
            "41698116222072977186158236678424689157993532961922\n"
            "62467957194401269043877107275048102390895523597457\n"
            "23189706772547915061505504953922979530901129967519\n"
            "86188088225875314529584099251203829009407770775672\n"
            "11306739708304724483816533873502340845647058077308\n"
            "82959174767140363198008187129011875491310547126581\n"
            "97623331044818386269515456334926366572897563400500\n"
            "42846280183517070527831839425882145521227251250327\n"
            "55121603546981200581762165212827652751691296897789\n"
            "32238195734329339946437501907836945765883352399886\n"
            "75506164965184775180738168837861091527357929701337\n"
            "62177842752192623401942399639168044983993173312731\n"
            "32924185707147349566916674687634660915035914677504\n"
            "99518671430235219628894890102423325116913619626622\n"
            "73267460800591547471830798392868535206946944540724\n"
            "76841822524674417161514036427982273348055556214818\n"
            "97142617910342598647204516893989422179826088076852\n"
            "87783646182799346313767754307809363333018982642090\n"
            "10848802521674670883215120185883543223812876952786\n"
            "71329612474782464538636993009049310363619763878039\n"
            "62184073572399794223406235393808339651327408011116\n"
            "66627891981488087797941876876144230030984490851411\n"
            "60661826293682836764744779239180335110989069790714\n"
            "85786944089552990653640447425576083659976645795096\n"
            "66024396409905389607120198219976047599490197230297\n"
            "64913982680032973156037120041377903785566085089252\n"
            "16730939319872750275468906903707539413042652315011\n"
            "94809377245048795150954100921645863754710598436791\n"
            "78639167021187492431995700641917969777599028300699\n"
            "15368713711936614952811305876380278410754449733078\n"
            "40789923115535562561142322423255033685442488917353\n"
            "44889911501440648020369068063960672322193204149535\n"
            "41503128880339536053299340368006977710650566631954\n"
            "81234880673210146739058568557934581403627822703280\n"
            "82616570773948327592232845941706525094512325230608\n"
            "22918802058777319719839450180888072429661980811197\n"
            "77158542502016545090413245809786882778948721859617\n"
            "72107838435069186155435662884062257473692284509516\n"
            "20849603980134001723930671666823555245252804609722\n"
            "53503534226472524250874054075591789781264330331690")

    return int(str(sum(int(x) for x in data.split("\n")))[:10])


def problem14():
    """ Longest Collatz sequence
    Which starting number, under one million, produces the longest chain?

    """
    longest_chain = 1
    chain_number = 1
    for number in range(1, 1000000):
        chain_count = mathhelper.collatz_sequence_chain_count(number)
        if chain_count > longest_chain:
            longest_chain = chain_count
            chain_number = number
    return chain_number


def problem15():
    """ Lattice paths
    How many such routes are there through a 20×20 grid?

    """
    return math.factorial(40) / (math.factorial(20) ** 2)


def problem16():
    """ Power digit sum
    What is the sum of the digits of the number 2^1000?

    """
    return mathhelper.sum_digits(2 ** 1000)


def problem18():
    """ Maximum path sum I
     Find the maximum total from top to bottom of the triangle below:

    """
    data = ("75\n"
            "95 64\n"
            "17 47 82\n"
            "18 35 87 10\n"
            "20 04 82 47 65\n"
            "19 01 23 75 03 34\n"
            "88 02 77 73 07 63 67\n"
            "99 65 04 28 06 16 70 92\n"
            "41 41 26 56 83 40 80 70 33\n"
            "41 48 72 33 47 32 37 16 94 29\n"
            "53 71 44 65 25 43 91 52 97 51 14\n"
            "70 11 33 28 77 73 17 78 39 68 17 57\n"
            "91 71 52 38 17 14 91 43 58 50 27 29 48\n"
            "63 66 04 68 89 53 67 30 73 16 69 87 40 31\n"
            "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

    matrix = [[int(column) for column in row.split(" ")] for row in data.split("\n")]

    row_count = len(matrix)
    for row_number in range(1, row_count):
        column_count = len(matrix[row_number])
        for column_number in range(column_count):
            if column_number == 0:
                new_value = matrix[row_number - 1][column_number]
            elif column_number == column_count - 1:
                new_value = matrix[row_number - 1][column_number - 1]
            else:
                new_value = max(matrix[row_number - 1][column_number - 1], \
                                matrix[row_number - 1][column_number])

            matrix[row_number][column_number] += new_value

    return max(cell for cell in matrix[row_count - 1])


def problem19():
    """ Counting Sundays
     How many Sundays fell on the first of the month during the twentieth
     century (1 Jan 1901 to 31 Dec 2000)?

    """
    start_date = datetime.datetime.strptime("01/01/1901", "%d/%m/%Y")
    end_date = datetime.datetime.strptime("31/12/2000", "%d/%m/%Y")

    return_value = 0
    for day in range(int((end_date - start_date).days)):
        new_date = start_date + datetime.timedelta(day)
        if new_date.day == 1 and new_date.isoweekday() == 7:
            return_value += 1
    return return_value


def problem20():
    """ Factorial digit sum
    Find the sum of the digits in the number 100!

    """
    return mathhelper.sum_digits(math.factorial(100))


def problem21():
    """ Amicable numbers
    Evaluate the sum of all the amicable numbers under 10000.

    """
    return sum(x for x in range(1, 10000) if mathhelper.is_amicable(x))


def problem22():
    """ Names scores
    For example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    with open(os.path.join(os.path.dirname(__file__), "data", "p022_names.txt"), 'r') as file:
        data = file.read()

    names = sorted(name.strip("\"") for name in data.split(","))
    return sum(sum(ord(c) - 64 for c in list(name)) * (idx + 1) for idx, name in enumerate(names))


def problem23():
    """ Non-abundant sums
    Find the sum of all the positive integers which cannot be written
    as the sum of two abundant numbers.

    """
    abundants = [x for x in range(1, 28124) if mathhelper.sum_factors(x, proper=True) > x]
    abundants_sum = {x + y for (x, y) in itertools.product(abundants, abundants) if x + y < 28124}
    return sum(x for x in range(1, 28124) if x not in abundants_sum)


def problem24():
    """ Lexicographic permutations
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

    """
    numbers = "0123456789"
    sorted_permutations = sorted(itertools.permutations(list(numbers), len(numbers)))
    return int("".join(sorted_permutations[999999]))


def problem25():
    """ 1000-digit Fibonacci number
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

    """
    for index, fibonacci in enumerate(mathhelper.fibonacci_number_list(None)):
        if len(str(fibonacci)) == 1000:
            return index + 1


def problem67():
    """ Maximum path sum II
     Find the maximum total from top to bottom of the triangle below:

     """
    with open(os.path.join(os.path.dirname(__file__), "data", "p067_triangle.txt"), 'r') as file:
        data = file.read()

    matrix = [[int(column) for column in row.split(" ")] for row in data.split("\n")]

    row_count = len(matrix)
    for row_number in range(1, row_count):
        column_count = len(matrix[row_number])
        for column_number in range(column_count):
            if column_number == 0:
                new_value = matrix[row_number - 1][column_number]
            elif column_number == column_count - 1:
                new_value = matrix[row_number - 1][column_number - 1]
            else:
                new_value = max(matrix[row_number - 1][column_number - 1], \
                                matrix[row_number - 1][column_number])

            matrix[row_number][column_number] += new_value

    return max(cell for cell in matrix[row_count - 1])
