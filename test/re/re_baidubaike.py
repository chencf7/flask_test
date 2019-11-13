import re


class ReBaidubaike(object):
    base_url = 'https://baike.baidu.com'
    entry_url = 'https://baike.baidu.com/item/github/10145341?fr=aladdin'

    __bk_item = r'<a\s.+?href="(/item/.*?)".*?</a>'
    __bk_image = r'<a\sclass="image-link"[\s\S]*?</a>'

    @staticmethod
    def get_next_crawler_urls(text):
        new_urls = re.findall(ReBaidubaike.__bk_item, text)
        grp_urls = [ReBaidubaike.base_url+itm for itm in new_urls]
        # for url in grp_urls:
        #     print(url)
        return grp_urls

    @staticmethod
    def get_description():
        pass

    @staticmethod
    def download_images(data):
        new_urls = re.findall(ReBaidubaike.__bk_image, data)
        for u in new_urls:
            print(u)
        pass




