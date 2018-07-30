import scrapy

class PoemSpider(scrapy.Spider):
    # 爬虫唯一标识
    name = 'poems'

    start_urls = ['https://www.gushiwen.org/gushi/']

    def parse(self, response):
            for article_url in response.css('a ::attr("href")').extract():
                print(article_url, '#'*10)
                yield response.follow(article_url, callback=self.parse_article)

    def parse_article(self, response):
        content = response.xpath(".//div[@class='contson']/descendant::text()").extract()
        print('=>', content)
        yield {'article': ''.join(content)}