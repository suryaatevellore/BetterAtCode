import re
class Solution:
    def check_for_ipv4(self, IP):
        pattern = r"\d{1,4}"
        a_pattern = r'[A-Za-z]'
        x = IP.split(".")
        # length test
        if len(x) != 4:
            return "fail"
        # leading zeroes check
        for octet in x:
            if (len(octet) > 1 and octet[0]=='0'):
                return "fail"
            # check for alphabets
            alphas = re.search(a_pattern, octet)
            numbers = re.search(pattern, octet)
            if alphas or not numbers:
                return "fail"

            # check limits
            if int(octet) > 255 or int(octet) < 0 or '-' in octet:
                return "fail"

        return "pass"



    def check_for_ipv6(self, IP):
        pattern = r"[G-Zg-z]+"
        # check for ::
        if '::' in IP:
            print("Failing with ::")
            return "fail"
        # check for negative sign 
        if '-' in IP:
            return "fail"
        x = IP.split(":")
        # check length
        if len(x) !=8:
            print("Failing with overall length")
            return "fail"
        # check leading zero
        if IP[0]=='0':
            print("Failing with leading zero")
            return "fail"
        # check pattern
        for octet in x:
            matches = re.search(pattern, IP)
            if matches:
                print("Failing with regex match")
                return "fail"
            if len(octet) > 4:
                print("Failing with length")
                return "fail"
        return "pass"


    def validIPAddress(self, IP: str) -> str:
        status_ipv4 = self.check_for_ipv4(IP)
        status_ipv6 = self.check_for_ipv6(IP)
        if status_ipv4 == "pass" and status_ipv6=="fail":
            return "IPv4"
        if status_ipv4 == "fail" and status_ipv6=="pass":
            return "IPv6"
        if status_ipv4 == "fail" and status_ipv6=="fail":
            return "Neither"
        return "invalid"
