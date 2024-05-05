class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occurrence = {}  # Dictionary to store the last occurrence index of each character
        for i, char in enumerate(s):
            last_occurrence[char] = i

        result = []  # List to store the sizes of partitions
        start, end = 0, 0  # Pointers for partition boundaries

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result