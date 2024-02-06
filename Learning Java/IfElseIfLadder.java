
public class IfElseIfLadder{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your score: ");
        float percentage = sc.nextFloat();
        if(percentazge >= 80){
            System.out.println("Disctinction");
        } else if(percentage >= 70){
            System.out.println("First Division");
        } else if(percentage >= 60){
            System.out.println("Second Division");

        } else if (percentage >= 50){
            System.out.println("Third Divison");
        } else if (percentage >= 40){
            System.out.println("Passed")
        } else {
            System.out.println("Failed")
        }
    }
}