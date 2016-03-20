/** class Person */
 class Person{
	private String name;
	private String address;
	private String phoneNumber;
	private String emailAddress;
	
	public Person(String name,String address,String phoneNumber,String emailAddress){
		this.name=name;
		this.address=address;
		this.phoneNumber=phoneNumber;
		this.emailAddress=emailAddress;
		}
		
	public String getName(){
		return name;
		}
	public void setName(String name){
		this.name=name;
		}
		
	public String getAdd(){
		return address;
		}
	public void setAdd(String address){
		this.address=address;
		}	
		
	public String getPho(){
		return phoneNumber;
		}
	public void setPho(String phoneNumber){
		this.phoneNumber=phoneNumber;
		}	
	public String getEma(){
		return emailAddress;
		}
	public void setEma(String emailAddress){
		this.emailAddress=emailAddress;
		} 	
	public void toString(){
		System.out.println("The person's name is"+name+"and the class name is"+"Person");
		}
		
}                                                                                    
/** class Student */
 class Student extends Person{  
	private final String classStatus;
	public Student(String classStatus){
		this.classStatus=classStatus;}
	public Student(String name,String address,String phoneNumber,String emailAddress,final String classStatus){
		this.classStatus=classStatus;
		setName(name);
		setAdd(address);
		setPho(phoneNumber);
		setEma(emailAddress);
		}
		
	public String getClassStatus(){
		return classStatus;}
		public void toString(){
		System.out.println("The person's name is"+name+"and the class name is"+"Student");
		}
}
/** class Employee */
 class Employee extends Person{
	private double salary;
	private String dateHired;
	
	public Employee(double salary,String dateHired){
		this.salary=salary;
		this.dateHired=dateHired;
	}
	public Employee(String name,String address,String phoneNumber,String emailAddress,double salary,String dateHired){
		this.salary=salary;
		this.dateHired=dateHired;
		setName(name);
		setAdd(address);
		setPho(phoneNumber);
		setEma(emailAddress);
		}	
	public double getSalary(){
		return salary;
	}
	public void setSalary(double salary){
		this.salary=salary;
	}		
	public String getDateHired(){
		return dateHired;
	}
	public void setDateHired(String dateHired){
		this.dateHired=dateHired;
	}		
	public void toString(){
		System.out.println("The person's name is"+name+"and the class name is"+"Employee");
		}
}
/** class Faculty */
 class Faculty extends Employee{
	private double hours;
	private int rank;
	
	public Faculty(double hours,int rank){
		this.hours=hours;
		this.rank=rank;}
	public Faculty(String name,String address,String phoneNumber,String emailAddress,double salary,String dateHired,double hours,int rank){
		this.hours=hours;
		this.rank=rank;
		setName(name);
		setAdd(address);
		setPho(phoneNumber);
		setEma(emailAddress);
		setSalary(salary);
		setDateHired(dateHired);
		}		
	public double getHours(){
		return hours;}
	public int getRank(){
		return rank;}
	public void toString(){
		System.out.println("The person's name is"+name+"and the class name is Faculty");
		}
}
/** class Staff */
 class Staff extends Employee{
	private String title;
	public Staff(String title){
		this.title=title;}
	public Staff(String name,String address,String phoneNumber,String emailAddress,double salary,String dateHired,String title){
	    this.title=title;
		setName(name);
		setAdd(address);
		setPho(phoneNumber);
		setEma(emailAddress);
		setSalary(salary);
		setDateHired(dateHired);
		}		
	public String getTitle(){
		return title;}
		public void toString(){
		System.out.println("The person's name is"+name+"and the class name is"+"Staff");
		}
}
/** class MyDate */
 class MyDate{
	private int year;
	private int month;
	private int day;
 
	
	public MyDate(int year,int month,int day){
		this.year=year;
		this.month=month;
		this.day=day;}
	public int getYear(){
		return year;}
	public int getMonth(){
		return month;}
	public int getDay(){
		return day;}		
}	

/** main function*/   
 class TeatPerson{
	public static void main(String[] args){
		Person person1 =new Person("Bob","Guangzhou","1234567","bob@gmail.com");
		Student student1 =new Student("Dijia","Guangzhou","1234467","dijia@gmail.com","freshman");
		Employee employee1 =new Employee("Kim","Guangzhou","1200067","kim@gmail.com",9999,"2000.01.01");
		Faculty faculty1 =new Faculty("Tom","Guangzhou","3234567","tom@gmail.com",1200,"2014.02.02",100,3);
		Staff staff1 =new Staff("Amy","Guangzhou","1934567","amy@gmail.com",3000,"1990.01.01","CEO");
		person1.toString();
		student1.toString();
		employee1.toString();
		faculty1.toString();
		staff1.toString();
	}
}
		
		 
		
		

		

		
		