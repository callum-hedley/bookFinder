#python script that uses selenium to go to different webpages and return book titles along with a download link that will open up a web page and allow the user to download the book
import selenium.webdriver as webdriver
import sys
#list of sites to get books from
sites = ["http://b-ok.org","http://gen.lib.rus.ec/"]
#initalising list variables
results = []
name_results = []
no_digits = []
#getting book results for a users search        
def getresults(search):
    #a loop that will loop through the sites in the list above
    for i in sites:
        url = i
        browser = webdriver.PhantomJS()
        browser.get(i)
        #function that takes in a search element from a webpage(find) and then searches for the book (trueurl)
        def searchBox(find, trueurl):
            searchbox = browser.find_element_by_id(find)
            searchbox.send_keys('{}'.format(trueurl))
            searchbox.submit()
        #gets the element id name depending on the site   
        if i == "http://b-ok.org":searchId = 'searchFieldx'
        if i == "http://gen.lib.rus.ec/":searchId = 'searchform'
        #enters the users book into the search
        searchBox(searchId, search)
        #grabs the downloadlinks and book names from the results page
        if i == "http://b-ok.org":
            webname='bookzz'
            links = browser.find_elements_by_class_name('tdn')
            names = browser.find_elements_by_class_name('color1')
        if i == "http://gen.lib.rus.ec/":
            webname='libgen'
            LinksElement = '//a[text()="[1]"]'
            NamesElement = '//a[text()="[1]"]//parent::td//preceding-sibling::td[@width]//a'
            links = browser.find_elements_by_xpath(LinksElement)
            names = browser.find_elements_by_xpath(NamesElement)
        #appends downloadlinks and book titles to lists
        for link in links:
            href = link.get_attribute("href")
            results.append(href)
        for name in names:
            n = '[{}]{}'.format(webname,name.text)
            name_results.append(n)
        #closes the selenium browser
        browser.quit()
    startNum,endNum,running,downloadPage=0,5,True,False
    #displays the search results with info on source and options for pages
    while running:
        num=1
        print('\n\n*******\nResults\n*******\n')
        for i in results[startNum:endNum]:
            print('\n[{}]{}\n{}\n'.format(num, name_results[results.index(i)], i))
            num += 1
        choice = input('[6]Next Page\n[7]Quit\n\nInput a number: ')
        for i in results:
            if choice == str(results.index(i)+1):
                print('your choice is {}'.format(i))
                url=i
                running,downloadPage = False,True
                break
            if choice == '6':
                startNum,endNum=endNum,endNum+5
                break
            if choice == '7':
                running=False
                break
    #opens the download page after selection
    if downloadPage == True:
        browser = webdriver.Chrome()
        browser.get(url)
#opens main menu with options to quit or search
def main():
    while True:
        print('\n*********\nMain Menu\n*********\n')
        startup = input('[1]Start Search\n[2]quit\n\nInput a number: ')
        if startup == '1':
            getresults(input('\nenter the book you want to read: '))
        if startup == '2':
            sys.exit()
if __name__=='__main__':
    main()
