class Solution {
    public boolean isValid(String s) {
      Stack<Character> stack = new Stack<>();
      for(int i = 0; i < s.length(); i++){
        char var = s.charAt(i);
        
        if(var == '(' || var == '[' || var == '{'){
            stack.push(var);
        }

        else if(var == ')' || var == ']' || var == '}'){
            if(stack.isEmpty())  return false; 
            char val = stack.pop();

            if((var == ')' && val != '(') ||
               (var == ']' && val != '[') ||
               (var == '}' && val != '{')) {
                return false;
              }
        }
      }
    return stack.isEmpty();
    }
}


        