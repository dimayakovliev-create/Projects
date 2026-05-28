song = """Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh"""

print(song)

print("          is little\rMy sister")
s = "Hi there people!"
print(s[0])
print(s[1:4])
print(s[-1])
print(s[:5])
print(s[3:])
print(s[1::3])
print(s.find("e",2,6))
print(s.count("e",2,6))

print(s.split(maxsplit=1))

list_of_strings = ['Hello', 'world']
print(" ".join(list_of_strings))
elements = ['earth', 'air', 'fire', 'water']
print(", ".join(elements))
dirty_string = "      Hello, world!          "
clean_string = dirty_string.strip()
print(clean_string)
text = "Hello world"
print(text.replace("world", "Python", 1))

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
query, _ = query.split('>')
print(query)
obj_query = {}
for el in query.split('&'):
    print(el)
    key, value = el.split('=')
    print(f"key: {key}, value: {value}")
    obj_query.update({key: value.replace('+', ' ')})    
print(type(obj_query))
print(obj_query)
