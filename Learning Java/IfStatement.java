import java.util Scanner;

public class IfStatement{
	public static void main(String args[]){
		double accountBalance = 500;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter amount to withdraw: ");
		short amountToWithdraw = sc.nextShort();
		if (amountToWithdraw <= accountBalance){
			System.out.println("Please, collect money. ");
		}
		System.out.println("Thank you")
		else{
			System.out.println("Not enough balance!")
		}
		System.out.println("Bye")
	}
}