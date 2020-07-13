
public class LongestCommonPrefix {
	
	public String HorizontalScanning (String[] strs) {
		
		// If no words are given in String array, return ""
		if (strs.length == 0) return ""; 
		
	    // The first word of the String array becomes prefix
		String prefix = strs[0];
		
		// Iterate the String array from the second element since the first element is prefix
	    
	    for (int i = 1; i < strs.length; i++) {
	    	
	    	// Run the while loop until strs[i].indexOf(prefix) == 0 >> returns the index of prefix in strs[i]
	    	
	        while (strs[i].indexOf(prefix) != 0) {
	            prefix = prefix.substring(0, prefix.length() - 1);
	            if (prefix.isEmpty()) return "";
	        }
	    }
	    
	    
	    return prefix;
        
    }
	
	public String VerticalScanning (String[] strs) {
		
	    if (strs == null || strs.length == 0) return "";
	    
	    
	    for (int i = 0; i < strs[0].length() ; i++){
	    	
	        char c = strs[0].charAt(i); // Store the first letter of the first word in c
	        
	        for (int j = 1; j < strs.length; j ++) {
	            if (i == strs[j].length() || strs[j].charAt(i) != c)
	                return strs[0].substring(0, i);             
	        }
	    }
	    
	    return strs[0];
	}
	
	

	public static void main(String[] args) {
		
		LongestCommonPrefix lcp = new LongestCommonPrefix();
		
		String[] test1 = {"flower","flow","flight"};
		String[] test2 = {"dog","racecar","car"};
		
//		lcp.longestCommonPrefix(test1);
//		lcp.longestCommonPrefix(test2);
		
		System.out.println("flow".indexOf("flow"));
		System.out.println("flower".substring(0, 5));
	}

}
