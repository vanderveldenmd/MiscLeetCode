public class Solution {
    public int KthSmallest(int[][] matrix, int k) {
      //Since this is a jagged array in C# we have to do some special methods to get the height and width of the arrays.
        int size1 = matrix.GetLength(0);
        int size2 = matrix[0].GetLength(0);
        
        //This will be our new array where we will store everything. In LeetCode terms, we are trading memory for speed.
        int[] newMat = new int[size1 * size2];
        
        //index will be where each number is stored.
        int index = 0;
        for(int i = 0; i < size2; i ++){
            for(int j = 0; j < size1; j++){
                newMat[index] = matrix[i][j];
                index++;
            }
        }
        
        //We simply sort the array using the standard method because that will give us ascending order.
        Array.Sort(newMat, 0, size1 * size2);
        return(newMat[k-1]);  //return the k-th element for the final step.
        
    }
}
