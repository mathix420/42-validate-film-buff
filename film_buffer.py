# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    film_buffer.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 19:16:29 by agissing          #+#    #+#              #
#    Updated: 2018/11/10 19:39:02 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess

user_id = input("Cookie user.id=")
session = input("Cookie _intra_42_session_production=")

user_agent = '-H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.75 Safari/537.1"'

page_url = 'https://elearning.intra.42.fr/videos?page='
url_list = ''

for i in range(0, 37):
    cmd = 'curl --silent "' + page_url + str(i) + '" ' + user_agent + ' -H "Cookie: user.id=' + user_id + '; _intra_42_session_production=' + session + '" |  grep -o "/notions/[-a-zA-Z0-9@:%_\+\.~#?&\\/=]*" | sed -e "s/$/\/seen/"'
    url_list += subprocess.check_output(['bash','-c', cmd]).decode()

print ("%s videos found !" % (url_list.count('\n') - 1))

for url in url_list.split('\n'):
    cmd = 'curl --silent "' + url + i + '" ' + user_agent + ' -H "Cookie: user.id=' + user_id + '; _intra_42_session_production=' + session + '"'
    out = subprocess.check_output(['bash','-c', cmd])

print ("%s videos viewed !" % (url_list.count('\n') - 1))
