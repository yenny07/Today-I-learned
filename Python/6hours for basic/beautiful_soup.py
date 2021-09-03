from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 설치된 패키지를 터미널에서 확인
# pip list
# pip show beautifulsoup
# pip install --upgrade package