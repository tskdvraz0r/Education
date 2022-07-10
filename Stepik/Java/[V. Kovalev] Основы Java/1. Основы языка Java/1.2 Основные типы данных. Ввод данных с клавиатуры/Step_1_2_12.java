/*  Step 12 - Стоимость покупки

Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.

Программа получает на вход три числа: a, b, n.
Программа должна вывести два числа: стоимость покупки в рублях и копейках.

test:
Sample Input:
10
15
2

Sample Output:
20 30
*/

import java.util.Scanner;

class Step_1_2_12
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int cost_rub = sc.nextInt();
            int cost_cent = sc.nextInt();
            int pies = sc.nextInt();

            System.out.print((pies * ((cost_rub * 100) + cost_cent)) / 100);
            System.out.print(" ");
            System.out.println((pies * ((cost_rub * 100) + cost_cent)) % 100);
        }
    }
}