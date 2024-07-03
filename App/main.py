from solution import Solution
from TreeNode import TreeNode

if __name__ == "__main__":
    # Example usage
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    sol = Solution()
    print(sol.maxPathSum(root))  # Output: 6
