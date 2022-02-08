from bs4 import BeautifulSoup
import requests

def print1():
    return ("good")

def user_search(search_val):
    arr = []
    tags_count=0
    h1_string=" "
    search=search_val.replace(" ","+")
    my_url="https://www.etsy.com/search?q="+search+"&ref=auto-1"
    print(my_url)
    r0=requests.get(my_url)
    soup0 = BeautifulSoup(r0.text, "html.parser")
    search_res=soup0.find_all(class_="listing-link wt-display-inline-block organic-impression")
    href_res = []
    for item4 in search_res:
        if 'href' in item4.attrs:
            href_res.append(item4['href'])

    #show tags only###################################################################
    # for i in href_res:
    #     arr.append(show_deatils(i))
    # for r in arr:
    #     h1_string = h1_string + "<h2>tags:</h2>"
    #     for c in r:
    #         h1_string=h1_string+" <button type='button'>"+c+"</button>"
    #         print(c, end=" ")

    for i in href_res:
        arr.append(show_deatils(i))
    for r in arr:
        temp=3
        # h1_string = h1_string + "<h2>tags:</h2>"

        for c in r:
            new_line = 1
            new_line2 = 1
            if temp == 3:
                #main title
                h1_string = h1_string + "</div>"
                h1_string = h1_string + "</div>"
                h1_string = h1_string + " <h4 class='main_title'>" + c + "</h4>"
                h1_string = h1_string + '<br>'
            for d in c:
                if temp==0 :
                    #tags img
                    if new_line2==1:
                        h1_string = h1_string + '<br>'
                        new_line2 = 0
                    h1_string = h1_string + "<img src='" + d + "' alt='alternatetext'>"
                elif temp==1 :
                    #tags buttons
                    tags_count=tags_count+1
                    if new_line==1:
                        h1_string = h1_string + "</div>"
                        h1_string = h1_string + "<div class='right_div'>"
                        # h1_string = h1_string + "<div class='left_div'>"
                        h1_string = h1_string + '<h5> click tag button for copy </h5> '
                        new_line = 0

                    h1_string=h1_string+" <button class='tags_button' onclick='autoCopy(this.id)' id="+str(tags_count)+" type='button'>"+d+"</button>"


                elif temp==2 :
                    #main img
                    h1_string = h1_string+"<div class='wrapper'>"
                    h1_string = h1_string + "<div class='left_div'>"
                    h1_string = h1_string + "<img style = 'width: 58%;' src='" + d + "'  alt='alternatetext'>"
                    h1_string = h1_string +'<br>'


                ##############
                # arr.append(listtitlehtml.text.strip())33333333
                # arr.append(list_img)111111111111111
                # arr.append(titles)222222222222222
                # arr.append(img)333333333333333333

                ##############
                #     h1_string = h1_string + "<img src='" + d + "' alt='alternatetext'>"
                # else:
                #     h1_string=h1_string+" <button type='button'>"+d+"</button>"
                # print(c, end=" ")
            temp=temp-1



    return  h1_string



def show_deatils(url):
    arr = []
    r=requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    listtitlehtml=soup.find('h1', {'class' : 'wt-text-body-03 wt-line-height-tight wt-break-word'})
    listpichtml=soup.find_all(class_="wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded")
    mydivs=soup.find_all(class_="wt-circle wt-horizontal-center tag-image wt-mb-xs-1 wt-b-xs")
    h4=soup.find_all(class_="tag-card-title wt-text-caption-title wt-text-center-xs wt-line-height-tight wt-text-truncate--multi-line tag-with-image-text-internal")

    list_img = []
    titles = []
    img = []

    i=0

    #לקיחת תמונה ראשית
    # print(listpichtml)
    for item1 in listpichtml:
        if 'src' in item1.attrs:
            # print(item['title'])
            list_img.append(item1['src'])

    ###############print("pic="+str(len(list_img)))
    #
    # for i in list_img:
    #     print(i)


    #לקיחת כותרת ראשית
   ################################# print(listtitlehtml.text.strip())

    #לקיחת תגיות
    for item in h4:
        if 'title' in item.attrs:
            # print(item['title'])
            titles.append(item['title'])

    ###############################print("titles="+str(len(titles)))
    #
    # for i in titles:
    #     print(i)

    #לקיחת תמונת תגיות
    for pic in mydivs:
        if 'src' in pic.attrs:
            print(item['title'])
            img.append(pic['src'])

    ###############################print("pic="+str(len(img)))

    arr.append(listtitlehtml.text.strip())
    arr.append(list_img)
    arr.append(titles)
    arr.append(img)

    print("dddddddddddd"+arr)
    return arr

# search = input("what is your product?")

