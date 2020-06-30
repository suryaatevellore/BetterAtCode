def main():
    """
        Entrypoint for running all leetcode programs locally
    """
    # call the parameter
    # Init an empty set.
    from LeetCode_validate_ip_address import Solution
    s = Solution()
    nums = ["1081:db8:85a3:01:-0:8A2E:0370:7334"]
    for i in nums:
        r = s.validIPAddress(i)
        print(f"{i} : {r}")


if __name__ == "__main__":
    main()
