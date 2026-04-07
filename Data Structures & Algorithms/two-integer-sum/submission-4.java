class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sumTrack = new HashMap<>();
        // 7-3 = 4
        // 7-4 = 3
        // 7-5 = 2
        // 7-6 = 1
        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (sumTrack.containsKey(diff)) {
                return new int [] { sumTrack.get(diff), i };
            }
            sumTrack.put(nums[i], i);
        }
        return new int [] {};
    }
}
