from olympic.rankings import get_table, get_rankings

def test_medals():
    with open('snapshot.html', 'r', encoding='utf-8') as i:
        page = i.read()
        page.replace('/n', '')

    get_table(page)

if __name__ == '__main__':
    test_medals()
    get_rankings()