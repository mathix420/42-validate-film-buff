# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    film_buffer.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 19:16:29 by agissing          #+#    #+#              #
#    Updated: 2018/11/11 15:10:28 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess, sys

user_id = input("Cookie user.id=")
session = input("Cookie _intra_42_session_production=")

user_agent = '-H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.75 Safari/537.1"'

page_url = 'https://elearning.intra.42.fr/videos?page='
url_list = ''

print ("Please wait until all videos are loaded !")

for i in range(0, 37):
    cmd = 'curl --silent "' + page_url + str(i) + '" ' + user_agent + ' -H "Cookie: user.id=' + user_id + '; _intra_42_session_production=' + session + '" |  grep -o "/notions/[-a-zA-Z0-9@:%_\+\.~#?&\\/=]*" | sed -e "s/$/\/seen/"'
    url_list += subprocess.check_output(['bash','-c', cmd]).decode()

print ("%s videos found !" % (url_list.count('\n') - 1))

toolbar_width = int((url_list.count('\n') - 1) / 9 + 1)
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width + 1))

i = 0
for url in url_list.split('\n'):
    cmd = 'curl --silent "https://elearning.intra.42.fr' + url + '" ' + user_agent + ' -H "Cookie: user.id=' + user_id + '; _intra_42_session_production=' + session + '"'
    out = subprocess.check_output(['bash','-c', cmd])
    if (out == b'{"seen":true}'):
        i += 1
    if (i % 9 == 0):
        sys.stdout.write("-")
        sys.stdout.flush()

sys.stdout.write("-")
sys.stdout.flush()
sys.stdout.write("\n")

print ("%s videos viewed !" % (url_list.count('\n') - 1))

if (i > 1):
    print ("You have unlocked 'Film buff 1' !")
if (i > 3):
    print ("You have unlocked 'Film buff 2' !")
if (i > 10):
    print ("You have unlocked 'Film buff 3' !")
if (i > 21):
    print ("You have unlocked 'Film buff 4' !")
if (i > 42):
    print ("You have unlocked 'Film buff 5' !")
if (i >= 924):
    print ("You have unlocked 'Watch all the things !' !")
