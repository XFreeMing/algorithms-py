import pytest

from two_sum_1 import Solution


class TestTwoSum:
    """Test cases for Two Sum algorithm using pytest"""

    @pytest.fixture
    def solution(self):
        """Fixture to provide Solution instance"""
        return Solution()

    @pytest.mark.unit
    def test_example_1(self, solution):
        """Test case from Example 1"""
        nums = [2, 7, 11, 15]
        target = 9
        result = solution.twoSum(nums, target)
        assert result == [0, 1]

    @pytest.mark.unit
    def test_example_2(self, solution):
        """Test case from Example 2"""
        nums = [3, 2, 4]
        target = 6
        result = solution.twoSum(nums, target)
        assert result == [1, 2]

    @pytest.mark.unit
    def test_example_3(self, solution):
        """Test case from Example 3"""
        nums = [3, 3]
        target = 6
        result = solution.twoSum(nums, target)
        assert result == [0, 1]

    @pytest.mark.unit
    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = solution.twoSum(nums, target)
        assert result == [2, 4]

    @pytest.mark.unit
    def test_zero_target(self, solution):
        """Test with target zero"""
        nums = [0, 4, 3, 0]
        target = 0
        result = solution.twoSum(nums, target)
        assert result == [0, 3]

    @pytest.mark.unit
    def test_large_numbers(self, solution):
        """Test with large numbers"""
        nums = [1000000000, 7, 11, 999999993]
        target = 2000000000
        result = solution.twoSum(nums, target)
        assert result == [0, 3]

    @pytest.mark.parametrize(
        "nums,target,expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
            ([0, 4, 3, 0], 0, [0, 3]),
        ],
    )
    def test_parametrized_cases(self, solution, nums, target, expected):
        """Parametrized test cases"""
        result = solution.twoSum(nums, target)
        assert result == expected

    @pytest.mark.unit
    def test_two_elements_only(self, solution):
        """Test with minimum array size"""
        nums = [1, 2]
        target = 3
        result = solution.twoSum(nums, target)
        assert result == [0, 1]

    @pytest.mark.unit
    def test_no_solution_returns_empty(self, solution):
        """Test that no solution returns empty list"""
        nums = [1, 2, 3]
        target = 10
        result = solution.twoSum(nums, target)
        assert result == []
