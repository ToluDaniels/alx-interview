#!/usr/bin/python3
"""UTF-8 validation module."""

def validUTF8(data):
    num_bytes_to_follow = 0

    for byte in data:
        # Check the 8 least significant bits of the byte to determine the type of character
        if byte >= 256:  # If a byte is greater than 255, it's not valid UTF-8
            return False

        if num_bytes_to_follow == 0:
            # For the first byte, determine how many bytes to follow based on the first few bits
            if byte >> 7 == 0:
                num_bytes_to_follow = 0
            elif byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            # For bytes that should follow, check if they start with '10' as their two most significant bits
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1

    # If there are still bytes to follow after processing the entire data, it's not valid UTF-8
    return num_bytes_to_follow == 0

