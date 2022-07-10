/*  Step 05 - ВАЛЛ-И 5

ВАЛЛ-И хочет по электронным часам, показывающим часы и минуты,  узнать сколько времени в минутах прошло от начала суток.

Входные данные:
два числа: часы (0 <= h < 24) и минуты (0 <= m < 60)

Выходные данные:
время от начала суток в минутах

test:
Sample Input:
2
45

Sample Output:
165
*/

import java.util.Scanner;

class Step_1_3_05
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int hours = sc.nextInt() * 60;
            int minutes = sc.nextInt();

            System.out.println(hours + minutes);
        }
    }
}