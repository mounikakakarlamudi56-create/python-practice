# Simple Python program

shopping_list = ["Apples"]

def get_shopping_list_msg(items):
    return "Current Shopping List: " + ", ".join(items)

print(get_shopping_list_msg(shopping_list))
