import java.util.*;

public class FizzBuzz {
	
	public List<String> fizzBuzz(int n) {
		
		//List<String> output = new List<String>();
		
		List<String> output = new ArrayList<String>();
		
		for (int i=0; i < n; i++) {
			
			int num = i+1;
			
			if (num%3 == 0 && num%15 != 0) {
				output.add("Fizz");
			} else if (num%5 == 0 && num%15 != 0) {
				output.add("Buzz");
				//System.out.println("Buzz");
			} else if (num%15 == 0) {
				output.add("FizzBuzz");
				//System.out.println("FizzBuzz");
			} else {
				output.add(Integer.toString(num));
				
				
			}
			
		}
		
		//System.out.println(output);
		
		
		
		return output;
		
		
        
    }

	public static void main(String[] args) {

		FizzBuzz fb = new FizzBuzz();
		
		fb.fizzBuzz(15);

	}

}
