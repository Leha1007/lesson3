
def count_calls():
    global calls
    calls += 1


def string_info(st):
    count_calls()
    return [len(st), st.upper(), st.lower()]


def is_contains(st, list_to_search):
    count_calls()
    return st.lower() in list(map(lambda x: x.lower(), list_to_search))


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

