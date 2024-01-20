
Add Two Strings Function

Overview
The add_two_strings function is designed to add two strings representing decimal numbers, taking into consideration both the integer and fractional parts of these numbers. This function is particularly useful in situations where precision of decimal arithmetic is crucial, and floating-point arithmetic might lead to precision errors.

Functionality
The main function, add_two_strings, breaks down into two separate functions:

add_two_strings_by_parts: This function handles the addition of two strings representing either the integer or fractional parts of a decimal number.

add_two_strings: This function splits each input string into its integer and fractional components, processes each part using add_two_strings_by_parts, and then combines the results into a final string representing the sum of the two input numbers.

How it Works
add_two_strings_by_parts(num1, num2, initial_carry=0):

Takes two strings, num1 and num2, and an optional initial_carry.
It pads the shorter string with leading zeros to equalize the lengths of both strings.
The function then iteratively adds corresponding digits of the two strings from right to left, keeping track of any carry.
Returns the sum as a string.
add_two_strings(num1, num2):

Takes two strings representing decimal numbers.
Splits each number into its integer and fractional parts.
Pads the fractional parts to ensure they are of equal length.
Calls add_two_strings_by_parts to add both the integer parts and the fractional parts separately.
If the addition of the fractional parts results in a carry, it is added to the integer part.
Returns the sum of the decimal numbers as a string.

Usage
This function can be used in Python scripts where precise decimal addition is required. It is particularly useful in financial calculations, scientific computations, and other domains where standard floating-point arithmetic may not provide sufficient precision.

Requirements
This function is implemented in Python and does not require any external libraries.

Limitations
The function assumes well-formed decimal strings as input.
It does not handle negative numbers or non-numeric characters.


Extra Resources:-

https://www.youtube.com/watch?v=xWBP4lzkoyM
https://www.geeksforgeeks.org/selection-sort/
https://www.simplilearn.com/tutorials/data-structure-tutorial/selection-sort-algorithm
