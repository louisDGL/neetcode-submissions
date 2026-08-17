class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"
        radii = [0 for _ in range(len (s_prime))]
        center = 0
        right_border = 0
        max_radius = 0
        largest_palindrome_center = 0

        for i in range(len(s_prime)):
            mirror = center - (i - center)

            if i < right_border:

                # if the mirror palindrome does not extend beyond the border of the palindrome centered at 'center'
                if radii [mirror] < right_border - i:
                    radii[i] = radii[mirror]
                    continue

                # if the mirror palindrome extends or up to the border of the palindrome centered at 'ceter' then we know that the radius of the palindrome centered at 's_prime[i]' is >= right_border - i

                else:
                    radii[i] = right_border - i
            

            # now we need to explore beyond the minimum guaranteed lenght in line 24 if 's_pirme[i]' is NOT within a larger palindrome, then 'radii[i]' would be 0 and we'd be exploring from scratch
            while i - radii[i] >= 0 \
                and i + 1 + radii[i] < len(s_prime) \
                and s_prime[i - 1 - radii[i]] == s_prime[i + 1 + radii[i]]:
                radii[i] += 1

            # if the palindrome centered at 'i' extends beyond the palindrome centered at 'center'
            if i + radii[i] > right_border:
                center = i
                right_border = i + radii[i]


            if radii[i] > max_radius:
                max_radius = radii[i]
                largest_palindrome_center = i
        
        start_index = (largest_palindrome_center - max_radius) // 2
        return s[start_index : start_index + max_radius]