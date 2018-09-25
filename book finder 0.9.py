import selenium.webdriver as webdriver
import sys
import time
sites = ["http://b-ok.org","http://gen.lib.rus.ec/"]
results = []
name_results = []
no_digits = []
links_config='Enabled'
def spinning_cursor():
    while True:
        for cursor in '*':
            yield cursor
spinner = spinning_cursor()
def options():
    print('\n*******\nOptions\n*******\n')
    optionChoice = input('[1]links\n[2]sources\n\nInput a number: ')
    if optionChoice == '1':
        print('\n*****\nLinks\n*****\n')
        print('[1]Links [{}]'.format(links_config))
        toggle = input('\nInput 1 to toggle: ')
        if toggle == '1':
            links_config = 'Disabled'
    if optionChoice == '2':
        print('\n*******\nSources\n*******\n')
        for i in sites:
            print('[{}]{}'.format(sites.index(i),i))
        input('\nInput a number to toggle the source on or off: ')
def getresults(search):
    print('\nLoading: ')
    def loading():
        for i in range(5):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.3)
    for i in sites:
        loading()
        url = i
        browser = webdriver.Chrome()
        loading()
        browser.get(i)
        loading()
        def searchBox(find, trueurl):
            searchbox = browser.find_element_by_id(find)
            searchbox.send_keys('{}'.format(trueurl))
            searchbox.submit()
        loading()
        if i == "http://b-ok.org":searchId = 'searchFieldx'
        loading()
        if i == "http://gen.lib.rus.ec/":searchId = 'searchform'
        searchBox(searchId, search)
        loading()
        if i == "http://b-ok.org":
            webname='bookzz'
            links = browser.find_elements_by_class_name('tdn')
            names = browser.find_elements_by_class_name('color1')
        loading()
        if i == "http://gen.lib.rus.ec/":
            webname='libgen'
            LinksElement = '//a[text()="[1]"]'
            NamesElement = '//a[text()="[1]"]//parent::td//preceding-sibling::td[@width]//a'
            links = browser.find_elements_by_xpath(LinksElement)
            names = browser.find_elements_by_xpath(NamesElement)
        loading()
        for link in links:
            href = link.get_attribute("href")
            results.append(href)
        loading()
        for name in names:
            n = '[{}]{}'.format(webname,name.text)
            name_results.append(n)
        loading()
        no_digits=name_results
##        for i in name_results:
##            a = filter(lambda x: x.isalpha(), i)
##            a = '[{}]{}'.format(webname,"".join(list(a)))
##            no_digits.append(a)        
        browser.quit()
    a,b,running,dw=0,5,True,False
    while running:
        num=1
        print('\n\n*******\nResults\n*******\n')
        for i in results[a:b]:
            print('\n[{}]{}\n{}\n'.format(num, no_digits[results.index(i)], i))
            num += 1
        choice = input('[6]Next Page\n[7]Quit\n[8]Options\n\nInput a number: ')
        for i in results:
            if choice == '8':
                options()
                break
            if choice == str(results.index(i)+1):
                print('your choice is {}'.format(i))
                url=i
                running,dw = False,True
                break
            if choice == '6':
                a,b=b,b+5
                break
            if choice == '7':
                running=False
                break
    if dw == True:
        browser = webdriver.Chrome()
        browser.get(proxy)
        searchBox('input', url)
def main():
    while True:
        print('\n*********\nMain Menu\n*********\n')
        startup = input('[1]Start Search\n[2]Options\n[3]quit\n\nInput a number: ')
        if startup == '1':
            getresults(input('\nenter the book you want to read: '))
        if startup == '2':
            options()
if __name__=='__main__':
    main()
