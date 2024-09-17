class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # To keep track of how many flowers we can place

        # Loop through the flowerbed
        for j in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[j] == 0:
                # Check if the left and right neighbors are empty or out of bounds
                left_empty = (j == 0) or (flowerbed[j - 1] == 0)
                right_empty = (j == len(flowerbed) - 1) or (flowerbed[j + 1] == 0)

                # If both neighbors are empty, we can place a flower
                if left_empty and right_empty:
                    flowerbed[j] = 1  # Place a flower
                    count += 1  # Increment the count of flowers placed
                    
                    # If we've placed enough flowers, return True
                    if count >= n:
                        return True

        # After the loop, check if we've placed enough flowers
        return count >= n
    
