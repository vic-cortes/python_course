import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

HOME_DEPOT_URL = "https://www.homedepot.com.mx/b/linea-blanca-y-cocinas/lavadoras-y-secadoras/lavadoras"
SORIANA_URL = (
    "https://www.soriana.com/hogar-y-electrodomesticos/linea-blanca/lavadoras/"
)
PALACIO_DE_HIERRO_URL = "https://www.elpalaciodehierro.com/buscar?q=lavadoras"

LIVERPOOL_TEST_URL = "https://www.liverpool.com.mx/tienda/pdp/lavadora-samsung-25-kg-autom%C3%A1tica-carga-superior-wa25dg5505awax/1173832954?skuid=1173832954"


# https://www.homedepot.com.mx/p/maytag-lavadora-maytag-22-kg-load-go-he-7mmhw6621hw-151135


# cookies = {
#     "DCC": "SiteC",
#     "sfEngine": "google",
#     "PS": "true",
#     "SelectedTab": "Parati",
#     "ak_bmsc": "98BEC2BC72517587F31706D69FEEBBFF~000000000000000000000000000000~YAAQTc/3vZ6EezSYAQAAh5B/NxwOnRn6NMIQMwg4uNOhvT3sTkw4SnZP6VkJCfDP6AEXxDl+xzuZ5ROMUCrr4cQ34bBwAcFSmVe9LR2svO1E1YUc42iwtU7BleQv6fB+K0e+69p5yRjyttAh30wK62pCTrS1xPTrprcN4EaNxQtrvj9rdHuc32JhYPcCQ941bxpjSVgOjOhOHqnN2hjW3Jh9l0WHoZ/R31T/882PaTG/r7biGFL0efzOQfvOC6FBAX63chB3PT+TbfRLglEFAI59voPyP2x1w6Psj4xOcixhp/jtXmmzPcrkCh0W6InzC212xCfQP1C1AdjnmWWDykM4yvWXVcL06JVYKP+aiQ0WXft7e0cgDGNwlOHjXxJ2RCQp4MlNRG7tr4132p+U2w==",
#     "rxVisitor": "1753277763755J11VMKJKRNKQ6V9S8V4ACI0PMPB72G2P",
#     "dtSa": "-",
#     "_evga_fb08": "{%22uuid%22:%22c0ed94f2f7ca2578%22}",
#     "_sfid_a127": "{%22anonymousId%22:%22c0ed94f2f7ca2578%22%2C%22consents%22:[]}",
#     "dtCookie": "v_4_srv_6_sn_80O6GL0E36I55URB1F5L2920NMV3CTTP_perc_100000_ol_0_mul_1_app-3Afb4b113cea6706c5_1",
#     "gbi_visitorId": "cmdg0b9a400013b7sq9adrcoz",
#     "_gcl_au": "1.1.1746237055.1753277765",
#     "genero": "x",
#     "segment": "fuero",
#     "nearByStore": "",
#     "homeDeliveryStore": "",
#     "opcId": "MDItMjEzMTQwMzY3Ng==",
#     "enblNeEdCaFCrt": "true",
#     "enblNeEdCaFPdp": "true",
#     "_gid": "GA1.3.899036427.1753277765",
#     "_tt_enable_cookie": "1",
#     "_ttp": "01K0VQZ5EYK21B4BYJX100M2C5_.tt.2",
#     "_pin_unauth": "dWlkPU1UaGxORGxqT1RNdE1UVm1NeTAwTWpGakxUazRORFl0TldFeFpUQmpNV00xTVdWag",
#     "_fbp": "fb.2.1753277765296.495316514580432135",
#     "FPID": "FPID2.3.KWdcW7OjJavkVWtZUGrQ7ld5ykJbypVFFPn2YxJf4WM%3D.1753277765",
#     "FPLC": "hXKQEDIvv7LBY%2BfSZk2veddAUve4ejX7PvOnqZM8bC%2FBIJusaHw%2BWu57REP7S23B%2FvG1cv%2Fea28q4XSq4L6g6hlukgFGG5Oj%2FcVQfn%2Fanke81QuaVOJLpCmxzRbx6A%3D%3D",
#     "kampyle_userid": "1944-7512-ce81-3311-75a4-2fe1-930c-1578",
#     "QuantumMetricUserID": "88d0a647c2b6eb7dc3d100fcbd3d89b3",
#     "QuantumMetricSessionID": "499084a2cc9dcd78bc633f0ff3c27358",
#     "gbi_sessionId": "cmdg1t4gk00003b7ccq0ls9q3",
#     "session_dc_qv": "1",
#     "JSESSIONID": "xhA3pe4YOhg7cLSC8gheU_bVHcUVq9i86xEQQIgd1BXjEu9ltjNm!1874454380",
#     "__rtbh.aid": "%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222026-07-23T14%3A24%3A54.285Z%22%7D",
#     "__rtbh.lid": "%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22jKaU5XZOH7bnmyLKEir7%22%2C%22expiryDate%22%3A%222026-07-23T14%3A24%3A54.285Z%22%7D",
#     "_ga": "GA1.1.1693801045.1753277765",
#     "TT3bl": "false",
#     "TURNTO_VISITOR_SESSION": "1",
#     "TURNTO_VISITOR_COOKIE": "Hg20G6MPJ2R9me0,1,0,0,null,,,0,0,0,0,0,0,0",
#     "bm_sz": "07CC5FE9CB9833E62ACD4120A75BDE0B~YAAQTc/3vc5HfzSYAQAADvO0NxxAu8a4If5w732liGTCTqIM58x/5U68apx9NBjj1sH44SGWhYazp/R/h0UYj4v1cuV0+1LVxok6FexsoRofAHQ5xvqeXKk1o7KkH58G6/xPRB5epXoWmX6a/hLcIVk63ogcZITlc8GHHNEF5PYU8epjM9mn+CbCzVss4QJQ0PTYKgqVO/xNZTd8ByFu17kcBgIoQhXqodT6j2UCeRxmHNx+8n34sVMuR6BGCIu9wtKpUNarEC3MTtgqO4z9ux3mEMgUpG+/rK01FgrBJmvse6o/jLYSXm7il+mJGRK4L31MsNw0asVI3mMrdmGeO8cX7H/eCn6J7JKggTxSXfvDXPofYtHZ9hYQmoOiAGtlxTWKip/l5mdqCsXajzhhkWpYahXJIhtCsX2YtWPtY1+SxqoDLurNcJWHlE2GKcCM0fZJblKWIcE52sexdeL1TLNI+2uLCyI=~3686713~3290935",
#     "RT": '"z=1&dm=www.liverpool.com.mx&si=85c70c1a-3fb4-4072-83cf-7c04b7e1c732&ss=mdg1t2vv&sl=4&tt=lx0&bcn=%2F%2F17de4c1e.akstat.io%2F&obo=1&rl=1"',
#     "_ga_171XPPQ282": "GS2.1.s1753280277$o2$g1$t1753281262$j60$l0$h0",
#     "_uetsid": "fb6a6ad067c911f0ab9de18e5ca7437b",
#     "_uetvid": "fb6a7f8067c911f0a32ee345a022b738",
#     "_ga_0WY68EFMNB": "GS2.1.s1753280277$o2$g1$t1753281263$j59$l0$h1418896096",
#     "_ga_XXXXXXXXXX": "GS2.1.s1753280276$o2$g1$t1753281263$j59$l0$h1457956222",
#     "kampyleUserSession": "1753281264483",
#     "kampyleUserSessionsCount": "7",
#     "kampyleUserPercentile": "28.75210386538377",
#     "kampyleSessionPageCounter": "1",
#     "ttcsid": "1753280280682::qvTFFx7uTYYJ8oQ0k7aq.2.1753281264498",
#     "ttcsid_C9APTGJC77U7KEORBI90": "1753280280682::I-IVRkWjS0UWKP9dk5dd.2.1753281264718",
#     "TURNTO_TEASER_SHOWN": "1753281265413",
#     "_abck": "DB6F38B3EFFF621B91643A0F7B051625~-1~YAAQTc/3veRqfzSYAQAAbmS2Nw5dfX270uB7t8Foq1RzO2899fS5oX4+VILHL7dZv2yHq27mVYMR1zu4xrRf2uVWwIpLzRwN0bhe4aNq1nD+BURciSx5ptVY0rfL1DVhvzOBxgrqQ9qtZfxSm8PJSWDEcsMAMicmlDDBGHWG7PSTUfeXjPBPsksEjMJ66l1bIF2cULCIUT5bCIpTyyF2WHthk04UhHIohzeJSms0K0X7rZ6l9k5d5u13xQw9Me3tUbnq78x9LcyDZpAgy1Ry9hLR5dUJ5u6oDkfYdRC90/ry2/zitEt7A/AD53f30DrtHY+zlCuzuFi/Gpul2jRV4Y+/m220TwfySVnfkwhCJQ+pZlYzWLdIgutmNADgbo4e15lU20tpZPREHp5twTz6BImnM3OrLbVJp6p04nBpOXCncSaFqU6PukTESAkXHZ3xLKWhGv+ZmCUv8+UucrEzof6ep/CtNQMe9jCMfX6D7xurc0hQfUn2PdQUzIJoRp9gpOPf020Mr1g7~-1~||0||~-1",
#     "rxvt": "1753283348622|1753280165431",
#     "dtPC": "6$81262310_576h-vFCRPKUUGDHTSAOMMCOFCUPVKUPWQHWGO-0e0",
#     "_ga_ZF6SNY8CLK": "GS2.1.s1753280169$o2$g1$t1753281549$j60$l0$h0",
#     "akavpau_allow": "1753281611~id=832f9a9e19c3d82a70231220e4e0ec25",
#     "bm_sv": "376493171D9DE5280BA22AC68F724346~YAAQN8VXuPbz7xKYAQAA+F25Nxx9t6DV6Oto0CTJImjZ1CIboIpMQInetCpfcQoxCWv0dHkyU8fo+qzsNpN5M20mo+kKIVAfUxQ6iZ1ODevp0D+vKVzzXEKI+T0h9Oesage+X8Jjy9TqsVszBYSRPQjYq62P6Cb9a0PTqOwPoT3diMIve1PzBvTvRlceUXlNX9hzmcAIUTn9XjDj712bZFf77KK8FwJMZIUGNLTbzI/AY7PsC3T4phGd7L8ZLwyjHGUas9l2IBE=~1",
# }

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "max-age=0",
#     "priority": "u=0, i",
#     "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"macOS"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
#     # 'cookie': 'DCC=SiteC; sfEngine=google; PS=true; SelectedTab=Parati; ak_bmsc=98BEC2BC72517587F31706D69FEEBBFF~000000000000000000000000000000~YAAQTc/3vZ6EezSYAQAAh5B/NxwOnRn6NMIQMwg4uNOhvT3sTkw4SnZP6VkJCfDP6AEXxDl+xzuZ5ROMUCrr4cQ34bBwAcFSmVe9LR2svO1E1YUc42iwtU7BleQv6fB+K0e+69p5yRjyttAh30wK62pCTrS1xPTrprcN4EaNxQtrvj9rdHuc32JhYPcCQ941bxpjSVgOjOhOHqnN2hjW3Jh9l0WHoZ/R31T/882PaTG/r7biGFL0efzOQfvOC6FBAX63chB3PT+TbfRLglEFAI59voPyP2x1w6Psj4xOcixhp/jtXmmzPcrkCh0W6InzC212xCfQP1C1AdjnmWWDykM4yvWXVcL06JVYKP+aiQ0WXft7e0cgDGNwlOHjXxJ2RCQp4MlNRG7tr4132p+U2w==; rxVisitor=1753277763755J11VMKJKRNKQ6V9S8V4ACI0PMPB72G2P; dtSa=-; _evga_fb08={%22uuid%22:%22c0ed94f2f7ca2578%22}; _sfid_a127={%22anonymousId%22:%22c0ed94f2f7ca2578%22%2C%22consents%22:[]}; dtCookie=v_4_srv_6_sn_80O6GL0E36I55URB1F5L2920NMV3CTTP_perc_100000_ol_0_mul_1_app-3Afb4b113cea6706c5_1; gbi_visitorId=cmdg0b9a400013b7sq9adrcoz; _gcl_au=1.1.1746237055.1753277765; genero=x; segment=fuero; nearByStore=; homeDeliveryStore=; opcId=MDItMjEzMTQwMzY3Ng==; enblNeEdCaFCrt=true; enblNeEdCaFPdp=true; _gid=GA1.3.899036427.1753277765; _tt_enable_cookie=1; _ttp=01K0VQZ5EYK21B4BYJX100M2C5_.tt.2; _pin_unauth=dWlkPU1UaGxORGxqT1RNdE1UVm1NeTAwTWpGakxUazRORFl0TldFeFpUQmpNV00xTVdWag; _fbp=fb.2.1753277765296.495316514580432135; FPID=FPID2.3.KWdcW7OjJavkVWtZUGrQ7ld5ykJbypVFFPn2YxJf4WM%3D.1753277765; FPLC=hXKQEDIvv7LBY%2BfSZk2veddAUve4ejX7PvOnqZM8bC%2FBIJusaHw%2BWu57REP7S23B%2FvG1cv%2Fea28q4XSq4L6g6hlukgFGG5Oj%2FcVQfn%2Fanke81QuaVOJLpCmxzRbx6A%3D%3D; kampyle_userid=1944-7512-ce81-3311-75a4-2fe1-930c-1578; QuantumMetricUserID=88d0a647c2b6eb7dc3d100fcbd3d89b3; QuantumMetricSessionID=499084a2cc9dcd78bc633f0ff3c27358; gbi_sessionId=cmdg1t4gk00003b7ccq0ls9q3; session_dc_qv=1; JSESSIONID=xhA3pe4YOhg7cLSC8gheU_bVHcUVq9i86xEQQIgd1BXjEu9ltjNm!1874454380; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222026-07-23T14%3A24%3A54.285Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22jKaU5XZOH7bnmyLKEir7%22%2C%22expiryDate%22%3A%222026-07-23T14%3A24%3A54.285Z%22%7D; _ga=GA1.1.1693801045.1753277765; TT3bl=false; TURNTO_VISITOR_SESSION=1; TURNTO_VISITOR_COOKIE=Hg20G6MPJ2R9me0,1,0,0,null,,,0,0,0,0,0,0,0; bm_sz=07CC5FE9CB9833E62ACD4120A75BDE0B~YAAQTc/3vc5HfzSYAQAADvO0NxxAu8a4If5w732liGTCTqIM58x/5U68apx9NBjj1sH44SGWhYazp/R/h0UYj4v1cuV0+1LVxok6FexsoRofAHQ5xvqeXKk1o7KkH58G6/xPRB5epXoWmX6a/hLcIVk63ogcZITlc8GHHNEF5PYU8epjM9mn+CbCzVss4QJQ0PTYKgqVO/xNZTd8ByFu17kcBgIoQhXqodT6j2UCeRxmHNx+8n34sVMuR6BGCIu9wtKpUNarEC3MTtgqO4z9ux3mEMgUpG+/rK01FgrBJmvse6o/jLYSXm7il+mJGRK4L31MsNw0asVI3mMrdmGeO8cX7H/eCn6J7JKggTxSXfvDXPofYtHZ9hYQmoOiAGtlxTWKip/l5mdqCsXajzhhkWpYahXJIhtCsX2YtWPtY1+SxqoDLurNcJWHlE2GKcCM0fZJblKWIcE52sexdeL1TLNI+2uLCyI=~3686713~3290935; RT="z=1&dm=www.liverpool.com.mx&si=85c70c1a-3fb4-4072-83cf-7c04b7e1c732&ss=mdg1t2vv&sl=4&tt=lx0&bcn=%2F%2F17de4c1e.akstat.io%2F&obo=1&rl=1"; _ga_171XPPQ282=GS2.1.s1753280277$o2$g1$t1753281262$j60$l0$h0; _uetsid=fb6a6ad067c911f0ab9de18e5ca7437b; _uetvid=fb6a7f8067c911f0a32ee345a022b738; _ga_0WY68EFMNB=GS2.1.s1753280277$o2$g1$t1753281263$j59$l0$h1418896096; _ga_XXXXXXXXXX=GS2.1.s1753280276$o2$g1$t1753281263$j59$l0$h1457956222; kampyleUserSession=1753281264483; kampyleUserSessionsCount=7; kampyleUserPercentile=28.75210386538377; kampyleSessionPageCounter=1; ttcsid=1753280280682::qvTFFx7uTYYJ8oQ0k7aq.2.1753281264498; ttcsid_C9APTGJC77U7KEORBI90=1753280280682::I-IVRkWjS0UWKP9dk5dd.2.1753281264718; TURNTO_TEASER_SHOWN=1753281265413; _abck=DB6F38B3EFFF621B91643A0F7B051625~-1~YAAQTc/3veRqfzSYAQAAbmS2Nw5dfX270uB7t8Foq1RzO2899fS5oX4+VILHL7dZv2yHq27mVYMR1zu4xrRf2uVWwIpLzRwN0bhe4aNq1nD+BURciSx5ptVY0rfL1DVhvzOBxgrqQ9qtZfxSm8PJSWDEcsMAMicmlDDBGHWG7PSTUfeXjPBPsksEjMJ66l1bIF2cULCIUT5bCIpTyyF2WHthk04UhHIohzeJSms0K0X7rZ6l9k5d5u13xQw9Me3tUbnq78x9LcyDZpAgy1Ry9hLR5dUJ5u6oDkfYdRC90/ry2/zitEt7A/AD53f30DrtHY+zlCuzuFi/Gpul2jRV4Y+/m220TwfySVnfkwhCJQ+pZlYzWLdIgutmNADgbo4e15lU20tpZPREHp5twTz6BImnM3OrLbVJp6p04nBpOXCncSaFqU6PukTESAkXHZ3xLKWhGv+ZmCUv8+UucrEzof6ep/CtNQMe9jCMfX6D7xurc0hQfUn2PdQUzIJoRp9gpOPf020Mr1g7~-1~||0||~-1; rxvt=1753283348622|1753280165431; dtPC=6$81262310_576h-vFCRPKUUGDHTSAOMMCOFCUPVKUPWQHWGO-0e0; _ga_ZF6SNY8CLK=GS2.1.s1753280169$o2$g1$t1753281549$j60$l0$h0; akavpau_allow=1753281611~id=832f9a9e19c3d82a70231220e4e0ec25; bm_sv=376493171D9DE5280BA22AC68F724346~YAAQN8VXuPbz7xKYAQAA+F25Nxx9t6DV6Oto0CTJImjZ1CIboIpMQInetCpfcQoxCWv0dHkyU8fo+qzsNpN5M20mo+kKIVAfUxQ6iZ1ODevp0D+vKVzzXEKI+T0h9Oesage+X8Jjy9TqsVszBYSRPQjYq62P6Cb9a0PTqOwPoT3diMIve1PzBvTvRlceUXlNX9hzmcAIUTn9XjDj712bZFf77KK8FwJMZIUGNLTbzI/AY7PsC3T4phGd7L8ZLwyjHGUas9l2IBE=~1',
# }

# params = {
#     "skuid": "1173832954",
# }

# response = requests.get(
#     LIVERPOOL_TEST_URL,
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )


# response = requests.get(LIVERPOOL_TEST_URL)
# soup = BeautifulSoup(response.content, "html.parser")

# response_soriana = requests.get(SORIANA_URL)
# soup_soriana = BeautifulSoup(response_soriana.content, "html.parser")

# response_palacio = requests.get(PALACIO_DE_HIERRO_URL)
# soup_palacio = BeautifulSoup(response_palacio.content, "html.parser")

# headers = {
#     "WCTrustedToken": "365818367%2CA%2Fy2rRq2lfBwvwQHgeBHS3cqROS4tQzG8%2FfO9fNJMAE%3D",
#     "sec-ch-ua-platform": '"macOS"',
#     "Referer": "https://www.homedepot.com.mx/b/linea-blanca-y-cocinas/lavadoras-y-secadoras/lavadoras",
#     "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     "sec-ch-ua-mobile": "?0",
#     "WCToken": "365818367%2CejjOoDZhy3c9If0hOxSHVDMQBE6kiRrOTGfrxyrUA6oksn1SJ6Kv7CdJy6JB7c34L61xKKZeYuVxA8f0tHGZ9fXtES8lDszK00AU049lcO0Zc45%2BgrhN%2Br03M2P1BctYHBeB6PKXM5WXXQ7mvHHLgpkth2OKYAgwIZJ3HEuuTEZPHyc4lSfnF%2BYHaBAuaIW0JXoHRpHk2LWfok1q8FrO%2F7LGWLiyTsbrZHK%2FxGQdq%2FSsI%2BFtD0wNUXl73hTeJnoIWsDhqU2kB47losDzPAmr4Q%3D%3D",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
# }

# params = {
#     "storeId": "10351",
#     "categoryId": "24008",
#     "limit": "28",
#     "offset": "0",
#     "contractId": "4000000000000000003",
#     "currency": "MXN",
#     "langId": "-5",
#     "marketId": "21",
#     "stLocId": "12605",
#     "extendedCatalog": "false",
#     "marketOnly": "true",
#     "physicalStoreId": "8702",
#     "profileName": "HCL_V2_findProductsByCategoryWithPriceRangeSequenceTest",
#     "selectedFacets": "[object Object]",
#     "minPrice": "-1",
#     "maxPrice": "-1",
#     "selectedPageOffset": "0",
#     "orderBy": "0",
# }

# response = requests.get(
#     "https://www.homedepot.com.mx/search/resources/api/v2/products",
#     params=params,
#     headers=headers,
# )

# print(response)

import os

from constants import GECKO_DRIVER_PATH
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOAD_TIMEOUT = 10
STRATEGY = "none"

options = Options()
options.headless = False  # No mostrar explorador

options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/110.0",
)


capabilities = DesiredCapabilities.FIREFOX
capabilities["pageLoadStrategy"] = STRATEGY


service = Service(executable_path=GECKO_DRIVER_PATH, log_path=os.path.devnull)
driver = webdriver.Firefox(options=options, service=service)
driver.set_page_load_timeout(LOAD_TIMEOUT)

driver.get(LIVERPOOL_TEST_URL)


# Esperar a que un elemento importante esté presente
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "div#productCard_a_1_2044157"))
# )
html = BeautifulSoup(driver.page_source, "html.parser")
products_container = html.find("div", class_="product-listing-container")


def normalize_string(raw_string: str) -> str:
    """
    Remove accents from a given string and convert it to lowercase.
    """
    if raw_string is None:
        raise ValueError("Input string cannot be None")

    ACCENTS = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
        "ü": "u",
    }
    raw_string = "_".join(raw_string.split()).lower()

    for accent, replacement in ACCENTS.items():
        raw_string = raw_string.replace(accent, replacement)

    return raw_string


# Retrieve tags from specifications
tag_product_spec_titles = html.find_all("span", class_="productSpecsGrouped_bold")
tag_product_specs = html.find_all("span", class_="productSpecsGrouped_regular")

# Retrieve text from tags and normalize it
product_spec_titles = [normalize_string(el.text) for el in tag_product_spec_titles]
product_spec = [el.text for el in tag_product_specs]

# Create a dictionary with product specifications
product_specs = dict(zip(product_spec_titles, product_spec))


driver.quit()
