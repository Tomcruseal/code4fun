public class lab3 {
    public static void main(String[] args){
		final int a = 8;
    	int key = 0;
    	
    	for(int i = 0;i<=a;i++){
			for(int j = 0;j<=a;j++){
				if(a-j > i)
    				System.out.print("     ");
    			else{
    		       key = (int)Math.pow(2, j+i-a);
    	           System.out.print(String.format("%5d",key));
    	        }
    	    }
    		for(int j = i-1;j>=0;j--){
    		
    			key = (int)Math.pow(2,j);
    			System.out.print(String.format("%5d",key));
    		}
    	    System.out.println();
    	}
    }
}
