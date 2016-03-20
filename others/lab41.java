import java.util.Scanner;
class lab41 {
	public static char convertor(char upperCase){
		int offset = (int)'a' -(int)'A';
		char lowercase = (char)((int)upperCase+offset);
		return lowercase;
	}

	public static void main(String[] args){
		/*String uppercase;
		Scanner input = new Scanner(System.in);
		uppercase = input.nextLine();
		char ch = uppercase.charAt(0);
		System.out.println(convertor(ch)); */
		double sum = 0;
                for (double d = 0; d<10;) {
                    d += 0.1;
                    sum += sum + d;
                } 

	}
}
