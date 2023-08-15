import java.util.ArrayList;
class LeetCode {
    // public int removeDuplicates(int[] nums) {
    //     for (int number: nums) {
    //         int copy = nums
    //     }
    // }
    public boolean checkTags(String word) {
        char[] myArray = new char[word.length()];
        word.getChars(0, word.length(), myArray, 0);
        //Tag coolTag = new Tag();
        for (int i = 0; i < myArray.length; i++) {
            if (myArray[i] == ' ' && myArray[i-1] != ',') {
                return false;
            }
        }
        ArrayList<Tag> listArray = new ArrayList<Tag>();
        String newString = "";
        for (int i = 0; i < myArray.length; i++) {
            newString += myArray[i];
            if (myArray[i] ==  ',' || i == myArray.length - 1) {
                newString = newString.replace(',' , ' ');
                newString = newString.trim();
                Tag newTag = new Tag(newString);
                listArray.add(newTag);
                newString = "";
                continue;
            }
            
        }
        return true;
    }
}