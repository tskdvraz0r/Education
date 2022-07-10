/*  Step 11 - Следующее четное

Дано целое число n. Выведите следующее за ним четное число. При решении этой задачи нельзя использовать условную инструкцию if и циклы. 
Подсказка: Подумайте, что будет оставаться в остатке при делении на 2 у чётных и у нечётных чисел.

test:
Sample Input:
5

Sample Output:
6
*/

import java.util.Scanner;

class Step_1_2_11
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int number = sc.nextInt();

            System.out.println(number / 2 * 2 + 2);
        }
    }
}