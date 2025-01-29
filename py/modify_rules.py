# 文件路径
file_path = "cfg/Custom_Clash.ini"

def modify_rules():
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 添加"原生IP"节点组
    content = content.replace(
        "custom_proxy_group=🇻🇳 越南节点`url-test`(越南|Vietnam)`https://cp.cloudflare.com/generate_204`300,,50",
        "custom_proxy_group=🇻🇳 越南节点`url-test`(越南|Vietnam)`https://cp.cloudflare.com/generate_204`300,,50"
        +"\ncustom_proxy_group=🇺🇳 原生IP`url-test`(家宽)`https://cp.cloudflare.com/generate_204`300,,50"
    )

    # 添加"原生IP"节点组到各节点组
    content = content.replace(
        "`[]🇻🇳 越南节点",
        "`[]🇻🇳 越南节点`[]🇺🇳 原生IP"
    )

    #添加 EHentai 节点组并更改ChatGPT的默认节点
    content = content.replace(
        "custom_proxy_group=💬 ChatGPT`select`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🇺🇳 原生IP`[]🚀 节点选择`[]♻️ 自动选择`.*",
        "custom_proxy_group=💬 ChatGPT`select`[]🇺🇳 原生IP`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🚀 节点选择`[]♻️ 自动选择`.*"
        +"\ncustom_proxy_group=🔞 EHentai(EXHentai)`select`[]🇺🇳 原生IP`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🚀 节点选择"
    )

    #更改漏网之鱼策略组默认节点为全球直连
    content = content.replace(
        "custom_proxy_group=🐟 漏网之鱼`select`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🇺🇳 原生IP`[]🚀 节点选择`[]♻️ 自动选择`[]🎯 全球直连`.*",
        "custom_proxy_group=🐟 漏网之鱼`select`[]🎯 全球直连`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🇺🇳 原生IP`[]🚀 节点选择`[]♻️ 自动选择`.*"
    )

    #添加 Pixiv 节点组
    content = content.replace(
        "custom_proxy_group=💬 ChatGPT`select`[]🇺🇳 原生IP`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🚀 节点选择`[]♻️ 自动选择`.*",
        "custom_proxy_group=💬 ChatGPT`select`[]🇺🇳 原生IP`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🚀 节点选择`[]♻️ 自动选择`.*"
        +"\ncustom_proxy_group=🅿️ Pixiv`select`[]🇯🇵 日本节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇸🇬 新加坡节点`[]🇹🇼 台湾节点`[]🇰🇷 韩国节点`[]🇨🇦 加拿大节点`[]🇬🇧 英国节点`[]🇫🇷 法国节点`[]🇩🇪 德国节点`[]🇳🇱 荷兰节点`[]🇹🇷 土耳其节点`[]🇻🇳 越南节点`[]🇺🇳 原生IP`[]🚀 节点选择`[]♻️ 自动选择`.*"
    )

    # 添加 EHentai 规则集
    content = content.replace(
        "ruleset=💬 ChatGPT,[]GEOSITE,openai",
        "ruleset=💬 ChatGPT,[]GEOSITE,openai"
        +"\nruleset=🔞 EHentai(EXHentai),https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/EHGallery/EHGallery.list,28800"
        +"\nruleset=🔞 EHentai(EXHentai),[]GEOSITE,ehentai"
    )

    #添加 Pixiv 规则集
    content = content.replace(
        "ruleset=💬 ChatGPT,[]GEOSITE,openai",
        "ruleset=💬 ChatGPT,[]GEOSITE,openai"
        +"\nruleset=🅿️ Pixiv,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.list,28800"
        +"\nruleset=🅿️ Pixiv,[]GEOSITE,pixiv"
    )

    # 写入文件2
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    modify_rules()
    print(f"File '{file_path}' has been modified.")