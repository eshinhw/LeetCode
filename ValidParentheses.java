
public class ValidParentheses {
	
    public boolean isValid (String s) {
    	
    	int[] count = new int[3];
    	
    	char[] par1 = {'(','{','['};
    	
    	char[] par2 = {')','}',']'};
    	
    	
    	char[] letters = new char[s.length()];
    	
    	for (int i=0; i < s.length(); i++) {
    		letters[i] = s.charAt(i);
    	}
    	
    	for (int i=0; i < letters.length; i++) {
    		
    		for (int j=0; j < par1.length; j++)
    			if (letters[i] == par1[j])
    				count[j]++;
    			if (letters[i] == par2[j])
    				count[j]--;    		
    	}
    	
    	for (int i=0; i < count.length; i++) {
    		if (count[i] != 0)
    			return false;
    	}
    		
    	
    	return true;
        
    }

	public static void main (String[] args) {
		// TODO Auto-generated method stub

	}

}
