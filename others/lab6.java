/** class Fan */
public class Fan{
	private final int SLOW = 1;
	private final int MEDIUM = 2;
	private final int FAST = 3;
	private int speed = SLOW;
	private boolean on = false;
	private double radius = 5;
	private String color = "blue";
	
	public Fan(){
	}
	
	public int getSpeed(){
		return speed;
	}
	public void setSpeed(int speed){
		this.speed=speed;
	}
	
	public boolean getOn(){
		return on;
	}
	public void setOn(boolean on){
		this.on=on;
	}
	
	public double getRadius(){
		return radius;
	}
	public void setRadius(double radius){
		this.radius=radius;
	}
	
	public String getColor(){
		return color;
	}
	public void setColor(String color){
		this.color=color;
	}
	
	public String toString(){
		if(on==true)
			return speed+" "+radius+color;
		else
			return radius+" "+color+"fan is off";
	}
}
/** main function*/
public class lab6{
		public static void main (String[] args){
			Fan fan1=new Fan();
			fan1.setSpeed(3);
			fan1.setRadius(10);
			fan1.setColor("yellow");
			fan1.setOn(true);
			Fan fan2=new Fan();
			fan2.setSpeed(1);
			fan2.setRadius(5);
			fan2.setColor("blue");
			fan2.setOn(false);
			System.out.println(fan1.toString());
			System.out.println(fan2.toString());
		}
}		
		