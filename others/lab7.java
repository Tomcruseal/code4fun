/** class Geometric */
 class Geometric{
	private String color="white";
	private boolean filled;  
	public Geometric(){}
	public Geometric(String color,boolean filled){
	this.color=color;
	this.filled=filled;}
	
	public String getColor(){
		return color;}
	
	public void setColor(String color){
		this.color=color;
		}
		
	public boolean isFilled(){
		return filled;
		}
		
	public void setFilled(boolean filled){
		this.filled=filled;
		}
	}
		
/** class Triangle */		
 class Triangle extends Geometric{
	private double side1=1.0;
	private double side2=1.0;
	private double side3=1.0;
	public Triangle(){}
	
	public Triangle(double side1,double side2,double side3){
		this.side1=side1;
		this.side2=side2;
		this.side3=side3;}	
	public Triangle(String color,boolean filled,double side1,double side2,double side3){
		setColor(color);
		setFilled(false);
		this.side1=side1;
		this.side2=side2;
		this.side3=side3;}	
	public double getSide1(){
		return side1;}
	public double getSide2(){
		return side2;}
	public double getSide3(){
		return side3;}		
	public double getArea(){
		double s;
		double area;
		s=(side1+side2+side3)/2.0;
		area=Math.sqrt(s*(s-side1)*(s-side2)*(s-side3));
		return area;}
	public double getPermeter(){
		return (side1+side2+side3);}
	public String toString(){
		return "Triangle: side1 ="+side1+"side2 = "+side2+"side3 = "+side3;}
	}

/** main function */	
 class TestTriangle{
	public static void main(String[] args){
		Triangle triangle=new Triangle("yellow",true ,1,1.5,1);
		System.out.println("The area is"+triangle.getArea());
		System.out.println("The perimeter is"+triangle.getPermeter());
		System.out.println("The colour is"+triangle.getColor());
		if(triangle.isFilled()==true)
			System.out.println("The triangle is filled");
		else	
			System.out.println("The triangle is not filled");
	}
}	
		
		
		
		
		