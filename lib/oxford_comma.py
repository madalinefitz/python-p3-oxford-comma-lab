import ipdb

def oxford_comma(items):
        if len(items) == 1:
            return ''.join(items)
        elif len(items) == 2:
            return " and ".join(items)
        elif len(items) == 3:
            return (f"{items[0]}, {items[1]}, and {items[2]}")
        elif len(items) > 3:
            last_item=items.pop()
            new_string=", ".join(items)
            add_and = (", and ")
            final_string= new_string + add_and + last_item
            return final_string
            
            

 

# ipdb.set_trace()

