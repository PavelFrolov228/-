s = input("введите пин код:")
if s.isnumeric() and len(s) in (4, 6):
    print("верно")
else:
    print("ошибка, попробуйте снова")
