public class SwitchCondition{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter day of the week (1 - 7):");
        byte day = sc.nextByte();
        switch(day){
            case 1:{ //if (day == 1)
                System.out.println("Sunday");
                break;
            }
            case 2:{
                System.out.println("Monday");
                break;
            }
            case 7:{
                System.out.println("Saturday");
                break;
            }
        }
        default:
            System.out.println("Invalid selection");
    }
}