class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGrps = new HashMap<>();

        for (String s: strs) {
            char[] key = s.toCharArray();
            Arrays.sort(key);
            String sortedKey = new String(key);
            anagramGrps.putIfAbsent(sortedKey, new ArrayList<>());
            anagramGrps.get(sortedKey).add(s);
        }
        return new ArrayList<>(anagramGrps.values());
    }
}
