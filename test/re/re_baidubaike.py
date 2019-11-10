import re


class ReBaidubaike(object):
    base_url = 'https://baike.baidu.com'
    entry_url = 'https://baike.baidu.com/item/github/10145341?fr=aladdin'

    __bk_item = r'<a\s.+?href="(/item/.*?)".*?</a>'

    @staticmethod
    def get_next_crawler_urls(text):
        new_urls = re.findall(ReBaidubaike.__bk_item, text)
        grp_urls = [ReBaidubaike.base_url+itm for itm in new_urls]
        return grp_urls
        # for url in grp_urls:
        #     print(url)


