public class TernaryOperator{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        /*
        if (number%2 ==0){
            System.out.println("Even")
        } else {
            System.out.println("Odd")
        }
        */
        //result = condition ?, true_expression :: false_expression
        System.out.println(number + " is " (number%2 == 0 ?, "Even":"odd"))
    }
}