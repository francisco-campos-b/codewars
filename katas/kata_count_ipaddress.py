"""
5kyu
Description:
Implement a function that receives two IPv4 addresses
Returns the number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.
Examples:
* With input "10.0.0.0", "10.0.0.50"  => return   50
* With input "10.0.0.0", "10.0.1.0"   => return  256
* With input "20.0.0.10", "20.0.1.0"  => return  246
"""


def ips_between(start: str, end: str) -> int:
    """Returns the number of ip addresses between the two give addresses"""
    start_ip = list(map(int, start.split(".")))
    end_ip = list(map(int, end.split(".")))
    num_addresses = 0
    for i in range(4):
        num_addresses *= 256 + (end_ip[i] - start_ip[i])
    return num_addresses


print(ips_between("10.0.0.1", "10.0.0.3"))
