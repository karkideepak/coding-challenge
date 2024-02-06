
public class LogicalAND{
	public static voild main(String args[]){
		//age restrictiion
		Scanner sc = new Scanner(Stystem.in)
		System.out.println("Name: ")
		byte age = sc.nextByte();


		//location restriction
		System.out.print("Are you in Nepal (Y/N)");
		char isInNepal = sc.next().toUpperCase().charAt(0);
		if(age >= 18 && isInNepal == 'Y'){
			System.out.println("You are eligibe to vote!")
		}
		else {
			System.out.println("You are not eligible to vote.");
		}
	}
}