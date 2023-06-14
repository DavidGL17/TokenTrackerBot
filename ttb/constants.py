from typing import Dict


TOKEN_URLS: Dict[str, str] = {
    "cn": "https://gateway.battlenet.com.cn/data/wow/token/index?namespace=dynamic-cn&locale=zh_CN",
    "us": "https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US",
    "eu": "https://eu.api.blizzard.com/data/wow/token/index?namespace=dynamic-eu&locale=fr_CH",
    "kr": "https://kr.api.blizzard.com/data/wow/token/index?namespace=dynamic-kr&locale=en_US",
    "tw": "https://tw.api.blizzard.com/data/wow/token/index?namespace=dynamic-tw&locale=en_US",
}

OAUTH_US_HOST: str = "https://oauth.battle.net"
