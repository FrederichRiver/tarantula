def text_clean(txt: str):
    txt = txt.strip()
    txt = txt.replace(':', ",")
    txt = txt.replace('：', ",")
    txt = txt.replace('，', ",")
    txt = txt.replace('”', '')
    txt = txt.replace('“', '')
    txt = txt.replace('"', '')
    txt = txt.replace('?', '')
    txt = txt.replace('？', '')
    return txt


def export_article_to_xml(filename, title, post_time, url, content):
    with open(filename, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f"<title>{title}</title>\n")
        f.write(f"<url>{url}</url>\n")
        f.write(f"<post_time>{post_time}</post_time>\n")
        f.write(f"<content>{content}</content>")




if __name__ == '__main__':
    txt = " 瑞方“限制”我方的底气：100名中国富豪在瑞方存7.8万亿，可信吗? "
    print(text_clean(txt))