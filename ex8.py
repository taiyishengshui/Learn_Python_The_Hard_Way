formatter = "{} {} {} {}"

#按顺序将值1，2，3，4存入formatter的四个空中
print(formatter.format(1, 2, 3, 4))
#按顺序将值One Two Three Four存入formatter的四个空中
print(formatter.format("One", "Two", "Three", "Four"))
#按顺序将值True False False True存入formatter的四个空中
print(formatter.format(True, False, False, True))
#按顺序将值{} {} {} {} 存入formatter的四个空中，会显示8个{}
print(formatter.format(formatter, formatter, formatter, formatter))
#按顺序将值"Try your","Own text here", "Maybe a poem", "Or a song about fear"存入formatter的四个空中，会显示8个{}
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))