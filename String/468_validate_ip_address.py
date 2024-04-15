class Solution:
    # Split the queryIP either by . or :.
    # If either split array is larger than length 1, we evaluate them.
    # IpV4's nums must have at least a length of 1 and at most a length of 3. 
    # If the length is larger than 1, it cannot have a leading 0. 
    # If the value of the num is larger than 255, it is not allowed.
    # Each char in each num must be a number. 
    # Ipv6 addresses must have a length of 8. 
    # It can only contain hex characters and no segment can be more than lenth 4. 
    def validIPAddress(self, queryIP: str) -> str:
        ipV4 = queryIP.split(".")
        ipV6 = queryIP.split(":")
        hex_vals = "0123456789abcdefABCDEF"
        
        # IPv4 cases:
        # 1. Only numbers
        # 2. No number over 255
        # 3. No leading 0s unless len(1)
        if len(ipV4) > 1:
            for nums in ipV4:
                # Segment can't be 0 length
                if len(nums) == 0:
                    return "Neither"
                # If length is larger than 1
                if len(nums) > 1:
                    # No leading 0s
                    if nums[0] == '0':
                        return "Neither"
                    # Each segment can't have more than 3 values
                    elif len(nums) > 3:
                        return "Neither"
                # All values in nums must be digits
                for char in nums:
                    if not char.isdigit():
                        return "Neither"
                # If any value is larger than 255, that's not allowed.
                if int(nums) > 255:
                    return "Neither"
            # IpV4 can only have 4 segments
            if len(ipV4) > 4 or len(ipV4) < 4:
                return "Neither"
            return "IPv4"
        # 1. Length between 1 and 4
        # 2. Only hex values
        # 3. Cannot have more than 8 segments
        if len(ipV6) > 1:
            for nums in ipV6:
                # Length must be between 1 and 4
                if len(nums) == 0 or len(nums) > 4:
                    return "Neither"
                # Only hex chars allowed
                for char in nums:
                    if char not in hex_vals:
                        return "Neither"
            # Cannot have more than 8 segments
            if len(ipV6) > 8:
                return "Neither"
            return "IPv6"
        
        return "Neither"

# T: O(N) - Goes through all characters in string at worst
# S: O(N) - Must copy string values into split array