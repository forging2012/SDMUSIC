xiami_search_url_first='http://api.xiami.com/web?key='
xiami_search_url_index='&v=2.0&app_key=1&r=search/songs&page='
xiami_search_url_last='&limit=10'
xiami_header = {'Referer': 'http://m.xiami.com/',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

def get_search_url(music_name,page_num):
    return xiami_search_url_first+music_name+xiami_search_url_index+str(page_num)+xiami_search_url_last

