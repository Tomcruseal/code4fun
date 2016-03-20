import java.util.Scanner;
public class lab42{
	public static int sumDigits(long n){
		int sum=0;
		while(n>0){
			sum=sum+sum%10;
		}
		return sum;
	}
	public static void main(String[] args ){
		Scanner input =new Scanner(System.in);
		long nums=input.nextLong();
		System.out.println(sumDigits(nums));
	}
}
	