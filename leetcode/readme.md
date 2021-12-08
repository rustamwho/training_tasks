# Tasks from Leetcode

My account in [leetcode](https://leetcode.com/rustamwho/) 👈

# MEDIUM

## 1. [3Sum](medium/3Sum.py)
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 

Notice that the solution set must not contain duplicate triplets.
#### Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

## 2. [Add Two Numbers](medium/add_two_numbers.py)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#### Example:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

## 3. [Longest Substring Without Repeating Characters](medium/longest_substring_without_repeating_characters.py)
Given a string s, find the length of the longest substring without repeating characters.

#### Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

## 4. [Longest Palindromic Substring](medium/longest_palindromic_substring.py)

Given a string s, return the longest palindromic substring in s.

#### Example:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

## 5. [Zigzag Conversion](medium/zigzag_conversation.py)
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

#### Example:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I


## 6. [Reverse Integer](medium/reversed_integers.py)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

### Example:
    Input: x = -123
    Output: -321



# HARD

## 1. [Median of two sorted arrays](hard/median_two_sorted_arrays.py)
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

#### Example:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
