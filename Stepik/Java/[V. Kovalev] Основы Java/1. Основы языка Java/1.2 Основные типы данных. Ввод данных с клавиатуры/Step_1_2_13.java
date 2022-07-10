/*  Step 13 - Последняя цифра

Дано произвольное положительное натуральное число. Найдите его последнюю цифру.

test:
Sample Input:
345

Sample Output:
5
*/

import java.util.Scanner;

class Step_1_2_13
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int number = sc.nextInt();

            System.out.println(number % 10);
        }
    }
}