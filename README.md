# LeetCode Data Structures
This package provides three classes for working with data structures in LeetCode problems:

 - `TreeNode`: used for solving binary tree problems
 - `ListNode`: used for solving linked list problems
 - `Node`: used for solving n-ary tree problems
For each of the three classes, the structure and attribute names are the same as in LeetCode.

Additionally, two helper methods are provided for each class:

`to_array`: converts an instance of the class to an array representation, which can be used in LeetCode problems.

`from_array`: constructs an instance of the class from an array representation.
The to_array and from_array methods are useful because LeetCode often represents data structures using arrays, and converting to and from this format can be time-consuming and error-prone.

## Installation

To install the package, use pip:

```
pip install leetcode_data_structure
```

## Usage

Here we use this package to solve `Leetcode 100 same tree`:

```python
import unittest

from data_structure import TreeNode


# region Solution class to submit to leetcode.com

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# endregion


def test(testObj: unittest.TestCase, p_arr: list[int], q_arr: list[int], expected: bool) -> None:
    """
    A test function which takes the arrays. (Because leetcode only gives you arrays.)
    We can reuse this function in the test class methods.
    """
    p = TreeNode.from_array(p_arr)
    q = TreeNode.from_array(q_arr)
    so = Solution()
    actual = so.isSameTree(p, q)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        """
        In a test case, you only provide input and output,
        you can copy them from leetcode website, or use a scrapper.
        """
        test(self, [1, 2, 3], [1, 2, 3], True)

    def test_2(self):
        test(self, [1, 2], [1, None, 2], False)

    def test_3(self):
        test(self, [1, 2, 1], [1, 1, 2], False)


if __name__ == "__main__":
    unittest.main()
```


# Other leetcode related projects

[Leetcode Step by Step -- Visualization]
https://ericwebsmith.github.io/leetcode_web/