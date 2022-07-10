/*  Step 04 - ВАЛЛ-И 4

ВАЛЛ-И решил отметить день рождения и пригласил x друзей. На каждого гостя ему необходимо приготовить 10 грамм заварки и по n пирожному.
Килограмм чая на развес стоит t рублей, а одно пирожное - k рублей. Во сколько обойдется ВАЛЛ-И чаепитие? Гарантируется, что все числа в решения задачи окажутся целыми.

Входные данные:

Вводятся 4 целых неотрицательных числа:

x - количество приглашенных друзей
t - стоимость килограмма чая
k - стоимость одного пирожного
n - количество пирожных

Выходные данные:

выведите одно целое число - ответ на задачу.

test:
Sample Input:
3
500
30
2

Sample Output:
195
*/

import java.util.Scanner;

class Step_1_3_04
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int number_of_friends = sc.nextInt();
            int tea_cost = sc.nextInt();
            int pie_cost = sc.nextInt();
            int number_of_pies = sc.nextInt();

            System.out.println(number_of_friends * (tea_cost / 100 + number_of_pies * pie_cost));
        }
    }
}