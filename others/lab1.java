import java.util.Scanner;
public class lab1{
	public  static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("radius:");
		double radius=input.nextDouble();
		System.out.println("length:");
		double length=input.nextDouble();
		System.out.println("Volume:"+length*radius*radius*3.141592653);
	}
}
		