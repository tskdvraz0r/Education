/*  Step 02 - ВАЛЛ-И 2

Робот ВАЛЛ-И каждый день меняет пароль от своей учетной записи на обучающей платформе. Ему нравится придумывать числа разной длины и суммировать их последние цифры.
К получившемуся значению он добавляет строчные согласные буквы, входящие в его имя на латинице.
Составьте программу для ВАЛЛ-И, которая позволяла бы ему придумывать 3 любых целых числа и выдавала бы пароль на текущий день.

test:
Sample Input:
123
204
15689

Sample Output:
16vll
*/

import java.util.Scanner;

class Step_1_3_02
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int first_number = sc.nextInt() % 10;
            int second_number = sc.nextInt() % 10;
            int third_number = sc.nextInt() % 10;

            System.out.println((first_number + second_number + third_number) + "vll");
        }
        
    }
}