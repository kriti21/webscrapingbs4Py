import re  # Ignore PyLintBear (C0111)

import requests  # Ignore PyLintBear (C0111)

from bs4 import *  # Ignore PyLintBear (W0401)

# Ignore PyLintBear (C0103)
data = requests.get('http://www.geeksforgeeks.org/')
soup = BeautifulSoup(data.text, 'html.parser')
data1 = soup.find_all('hgroup')
for link in data1[1].find_all('a', href=True, text='GATE CS'):
    nextlink = link['href']
url = requests.get(str(nextlink))
soup = BeautifulSoup(url.text, 'html.parser')
i = 1  # Ignore PycodestyleBear (E225)
list1 = soup.find_all('a', href=True, text=re.compile('^GATE-CS'))
list2 = soup.find_all('a', href=True, text=re.compile('^GATE\sCS\s20..$'))
for link in list1:
    link1 = link['href']
    filename = 'gateprep-'+str(i)
    with open(filename, 'w') as handle:
        finalpage = requests.get(link1)
        soup = BeautifulSoup(finalpage.text, 'html.parser')
        data3 = soup.find('div', id='mtq_question_container-1')
        data4 = data3.find('div')
        divs = data4.find_all(
            'div', {'class': 'mtq_question mtq_scroll_item-1'})
        try:
            for div in divs:
                nd1 = div.find('div', {'class': 'mtq_question_label'})
                handle.writelines(nd1.text)
                handle.writelines('\n')
                nd2 = div.find('div', {'class': 'mtq_question_text'})
                handle.writelines(nd2.text)
                handle.writelines('\n')
                nd3 = div.find_all('div', {'class': 'mtq_answer_text'})
                count = 1
                for ans in nd3:
                    st = '('+str(count)+')'
                    handle.writelines(st)
                    handle.writelines(ans.text)
                    handle.writelines('\n')
                    count += 1
                handle.writelines('\n\n\n')
                try:
                    nd4 = div.find('div', {'class': 'mtq_explanation-label'})
                    handle.writelines(nd4.text)
                    handle.writelines('\n')
                    nd5 = div.find('div', {'class': 'mtq_explanation-text'})
                    handle.writelines(nd5.text)
                    handle.writelines('\n')
                except Exception as e:  # Ignore PyLintBear (W0703)
                    pass
                handle.writelines('\n\n\n')
            i += 1
        except Exception as e:  # Ignore PyLintBear (C0103)
            print(e)
for link in list2:
    link2 = link['href']
    filename = 'gateprep-'+str(i)
    with open(filename, 'w') as handle:
        finalpage = requests.get(link1)
        soup = BeautifulSoup(finalpage.text, 'html.parser')
        data3 = soup.find('div', id='mtq_question_container-1')
        data4 = data3.find('div')
        divs = data4.find_all(
            'div', {'class': 'mtq_question mtq_scroll_item-1'})
        try:
            for div in divs:
                nd1 = div.find('div', {'class': 'mtq_question_label'})
                handle.writelines(nd1.text)
                handle.writelines('\n')
                nd2 = div.find('div', {'class': 'mtq_question_text'})
                handle.writelines(nd2.text)
                handle.writelines('\n')
                nd3 = div.find_all('div', {'class': 'mtq_answer_text'})
                count = 1
                for ans in nd3:
                    st = '('+str(count)+')'
                    handle.writelines(st)
                    handle.writelines(ans.text)
                    handle.writelines('\n')
                    count += 1
                handle.writelines('\n\n\n')
                try:
                    nd4 = div.find('div', {'class': 'mtq_explanation-label'})
                    handle.writelines(nd4.text)
                    handle.writelines('\n')
                    nd5 = div.find('div', {'class': 'mtq_explanation-text'})
                    handle.writelines(nd5.text)
                    handle.writelines('\n')
                except Exception as e:
                    pass
                handle.writelines('\n\n\n')
            i += 1
        except Exception as e:
            print(e)
print('Successfully saved all the files :)')
