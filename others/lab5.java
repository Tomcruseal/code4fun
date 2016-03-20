import java.util.Scanner;
public class lab5 {
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);
	int n = input.nextInt();
	double[] score = new double[n];
    String[] name = new String[n];
    for(int i = 0;i<n; i++){
		score[i] = input.nextDouble();
		name[i] = input.nextLine();
    }
  
	Sort(score,name,n);
    for(int i = 0;i<n;i++)
    System.out.print(score[i]+" ");
    System.out.println();
    System.out.print(average(score));
	}
 
	public static void Sort(double[] score, String[] name, int n){
		for(int i = 0; i<n;i++)
		for(int j = n-1;j>i;j--)
		if(score[j]>score[j-1]){
			double temp1 = score[j];
			score[j] = score[j-1];
			score[j-1] = temp1;
			String temp2 = name[j];
			name[j] = name[j-1];
			name[j-1] = temp2;
		}
	}
 
	public static double average(double[] score){
		double sum = 0;
		for(int i = 0;i<score.length;i++)
		sum = sum + score[i];
		return sum*1.0/score.length;
	}


	public static int average(int[] score){
		int sum = 0;
		for(int i = 0;i<score.length;i++)
		sum = sum + score[i];
		return sum*1.0/score.length;
	}
}
