/*  Step 10 - Площадь и периметр

На одной строчке через пробел записаны два целых числа: длина и ширина прямоугольника.
Вычислите его площадь и периметр (именно в таком порядке). Результат выведите на разных строках.

test:
Sample Input:
5
10

Sample Output:
50
30
*/

import java.util.Scanner;

class Step_1_2_10
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in)) {
            int lenght = sc.nextInt();
            int width = sc.nextInt();

            System.out.println(lenght * width);
            System.out.println((lenght + width) * 2);
        }
    }
}