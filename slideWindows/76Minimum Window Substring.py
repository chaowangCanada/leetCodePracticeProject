def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(t) > len(s):
        return ""

    if len(t) == len(s):
        if t == s:
            return t

    s_list = list(s)
    t_list = list(t)
    t_table = dict()
    for i in t_list:
        t_table[i] = t_table.get(i, 0) + 1
    t_table_original = t_table.copy()
    left = 0
    right = 0
    count = len(t)
    min_length = len(s)
    min_substring = s
    found = False

    while right < len(s_list):
        if s_list[right] in t_table:
            t_table[s_list[right]] -= 1
            if t_table[s_list[right]] >= 0:
                count -= 1
        right += 1

        if count == 0:
            while count == 0:
                if s_list[left] in t_table:
                    t_table[s_list[left]] += 1
                    if t_table[s_list[left]] > 0:
                        count += 1
                left += 1
            found = True
            if len(s_list[left - 1: right]) < min_length:
                min_substring = s_list[left - 1: right]
                min_length = len(min_substring)

    return ''.join(min_substring) if found else ""

if __name__ == '__main__':
    print("final output",minWindow("tfsxfpbgrvlgngmrtgotjumbaxosseklkckrrlzljnrytfpolgjxcvycvounteafgkyaxylgleeglwuycfvecvgxmbmfhmmoykoykbgxhndsjzqneorjlzgxctckhqaibqgnrolybqskskxyyqhmqojsjocqeeyhugvlvglwwfjqqipqzwcrmmjvcoogsmopvjaqroontzglivcjtgagslbwbpdwetlbcnrtdhizhokploafvanpnqmpirnmkynmnghrnrqwicltrlaonndbersmihyshnguvplkhdhpgukxillvyqycksoszongdvbyloluusjamvzugmsfesjolahkqwturuuekhyezjgoffilrcswvekgetsurlqjhnpuuoywxfkcmuqexicumocsiupbihkrwclrqkpnrzsdvijuslohaqzknqlxyyouaansmehddzibjuvcfkjhcktrdhobhdxjfnbrriwxkgytatvifgpktlbwsqxzvwiajltdtradxazytugbdxlwimscerbbnldzwwcspexnewnzrvausnsdckfibhkquprrmvjdzgqfdffwahsvxkyzwdhzmtpjjhaxclaettjyyqwbaqwxauyyzfxobpxkyzjakjgfesediaekrchtwhuxnrlqikcgjljvwpbbhfgshmcaomwmtqjijxysjaatnjokzrlgwragddirrefkwqvintazwasjkitlaetyxueazptqtycsrxaetcfpcxaogwbicvgarncqcwixwmpnkpufrzwwzwmhsopvlxxckzumxcmwoblatffmhbiiaxpulgrydoaqquenyqjouvpncwzlaktahkwuqouweumuqqiohtcbotqtqpesbyukiqgbgaxlujfkzpagjfjzyzsqrxksxedfvjidkfogowtqltyuaiubjoraletiiyqfhyjtgzcuvvkhqjdrtzucoldbrymaweffcqbkqdflyruqcyjvzd", "ynrdribdizhqelgfwwid"))
