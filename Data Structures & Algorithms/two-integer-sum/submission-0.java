class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hashmap.containsKey(complement)) {
                return new int[]{hashmap.get(complement), i};
            }
            hashmap.put(nums[i], i); // store value ➝ index
        }
        return new int[0];
    /**
    * Create a hashmap
    * Iterate through the array and add every element to the hashmap
    * Compute the target - current hashmap element, to find other num needed
    * Return the position/key of the two elements in the hashmap 
    */

    }
}
