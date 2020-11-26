#SPDX-FileCopyrightText: © 2011 nagadomi@nurs.or.jp
#SPDX-License-Identifier: The MIT License (MIT)
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup


def crawl_naver_webtoon(title,max_no,weekday):

    for no in range(max_no):
        no = str(no+1)
        episode_url = f'https://comic.naver.com/webtoon/detail.nhn?titleId={title}&no={no}&weekday={weekday}'
        html = requests.get(episode_url).text
        soup = BeautifulSoup(html, 'html.parser')
        iter = 0
        for img_tag in soup.select('.wt_viewer img'):
            iter+=1
            image_file_url = img_tag['src']
            image_dir_path = os.path.join(os.getcwd(), "webtoon", no)
            image_file_path = os.path.join(image_dir_path, os.path.basename(f'{no}_{iter}.jpg'))

            if not os.path.exists(image_dir_path):
                os.makedirs(image_dir_path)

            headers = {'Referer': episode_url}
            image_file_data = requests.get(image_file_url, headers=headers).content
            open(image_file_path, 'wb').write(image_file_data)
        print(f'file saved {no}')
    print('Completed !')

crawl_naver_webtoon("524520", 299, "fri")