#!/bin/sh

#		42 Validate film buff

if [ $# -ne 2 ]
  then
      echo "\n\tUsage :\n\t\t./03 <intra_42_session> <user.id>\n"
	  exit
fi

for i in $(seq 37)
do
	urls=$"${urls}$(curl 'https://elearning.intra.42.fr/videos?page=$i' -H 'Connection: keep-alive' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' -H "Cookie: _intra_42_session_production=$1; user.id=$2" --compressed --silent | grep -o "/notions/[-a-zA-Z0-9@:%_\+\.~#?&\\/=]*" | sed -e "s/$/\/seen/" | sed -e "s/^/https:\/\/elearning.intra.42.fr/") "
done

echo "\n\t\tAll intra's videos scanned\n"

count=0;

for url in ${urls}
do
	test $(curl $url -H 'Connection: keep-alive' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' -H "Cookie: _intra_42_session_production=$1; user.id=$2" --compressed --silent) = '{"seen":true}\n' 2>> /dev/null
	if [ $? = 1 ]
	then
		echo "✔ video seen !"
		count=$((count + 1));
	else
		echo "✘ An error occur"
		echo $url >> filmbuff.log
	fi
done

echo "All done," $count "videos viewed !"
