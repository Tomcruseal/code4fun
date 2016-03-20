import java.util.Scanner;
public class lab2{
	public static void main(String[] args){
		Scanner input=new Scanner(System.in);
		int inputInteger=input.nextInt();
		if( inputInteger%2==1)
			{
				System.out.println("Is"+ inputInteger +"an even number?"+"   "+"false");
			}
		else
			{
				System.out.println("Is"+inputInteger+ "an even number?"+"   "+"true");
			}
	}
}
