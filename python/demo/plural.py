# Filename: plural.py

# 如果在讲英语的国家长大，或在正规的学校学习过英语，您可能对下面的基本规则很熟悉 ：
# 
# 如果某个单词以 S 、X 或 Z 结尾，添加 ES 。Bass 变成 basses， fax 变成 faxes，而 waltz 变成 waltzes。
# 如果某个单词以发音的 H 结尾，加 ES；如果以不发音的 H 结尾，只需加上 S 。什么是发音的 H ？指的是它和其它字母组合在一起发出能够听到的声音。因此 coach 变成 coaches 而 rash 变成 rashes，因为在说这两个单词的时候，能够听到 CH 和 SH 的发音。但是 cheetah 变成 cheetahs，因为 H 不发音。
# 如果某个单词以发 I 音的字母 Y 结尾，将 Y 改成 IES；如果 Y 与某个原因字母组合发其它音的话，只需加上 S 。因此 vacancy 变成 vacancies，但 day 变成 days 。
# 如果所有这些规则都不适用，只需加上 S 并作最好的打算。

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def rules(rules_filename):
    with open(rules_filename, encoding = 'utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace  =  line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename = 'plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
