# -*- coding: utf-8 -*-
"""batch6_verify.py —— 批次6选目语料核对：按（词牌/题名, 作者, 首句指纹）从语料库取原文。"""
import glob, io, json, os, sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'chinese-poetry'))

# (标签, 匹配关键词(题名或词牌), 作者, 首句指纹用于人工辨认——只打印不自动判)
CANDS = [
    ('忆秦娥', '忆秦娥', '李白'), ('菩萨蛮·平林', '菩萨蛮', '李白'), ('菩萨蛮·小山', '菩萨蛮', '温庭筠'),
    ('菩萨蛮·人人', '菩萨蛮', '韦庄'), ('相见欢·林花', '相见欢', '李煜'), ('浪淘沙·帘外', '浪淘沙令', '李煜'),
    ('浪淘沙·帘外b', '浪淘沙', '李煜'), ('清平乐·别来', '清平乐', '李煜'), ('长相思·一重山', '长相思', '李煜'),
    ('谒金门', '谒金门', '冯延巳'), ('苏幕遮·碧云天', '苏幕遮', '范仲淹'), ('浣溪沙·一曲', '浣溪沙', '晏殊'),
    ('蝶恋花·槛菊', '蝶恋花', '晏殊'), ('蝶恋花·庭院', '蝶恋花', '欧阳修'), ('生查子·元夕', '生查子', '欧阳修'),
    ('玉楼春·东城', '玉楼春', '宋祁'), ('雨霖铃', '雨霖铃', '柳永'), ('蝶恋花·伫倚', '蝶恋花', '柳永'),
    ('八声甘州', '八声甘州', '柳永'), ('桂枝香', '桂枝香', '王安石'), ('鹧鸪天·彩袖', '鹧鸪天', '晏几道'),
    ('临江仙·梦后', '临江仙', '晏几道'), ('江城子·十年', '江城子', '苏轼'), ('蝶恋花·花褪', '蝶恋花', '苏轼'),
    ('浣溪沙·山下', '浣溪沙', '苏轼'), ('卜算子·黄州', '卜算子', '苏轼'), ('望江南·春未老', '望江南', '苏轼'),
    ('望江南/望江梅', '望江梅', '苏轼'), ('卜算子·长江头', '卜算子', '李之仪'), ('清平乐·春归', '清平乐', '黄庭坚'),
    ('鹊桥仙', '鹊桥仙', '秦观'), ('踏莎行·郴州', '踏莎行', '秦观'), ('行香子·树绕', '行香子', '秦观'),
    ('苏幕遮·燎沉香', '苏幕遮', '周邦彦'), ('醉花阴', '醉花阴', '李清照'), ('如梦令·常记', '如梦令', '李清照'),
    ('一剪梅·红藕', '一剪梅', '李清照'), ('武陵春', '武陵春', '李清照'), ('点绛唇·蹴罢', '点绛唇', '李清照'),
    ('丑奴儿/采桑子·少年', '采桑子', '辛弃疾'), ('丑奴儿b', '丑奴儿', '辛弃疾'), ('菩萨蛮·郁孤台', '菩萨蛮', '辛弃疾'),
    ('南乡子', '南乡子', '辛弃疾'), ('永遇乐', '永遇乐', '辛弃疾'), ('钗头凤', '钗头凤', '陆游'),
    ('诉衷情', '诉衷情', '陆游'), ('扬州慢', '扬州慢', '姜夔'), ('虞美人·听雨', '虞美人', '蒋捷'),
    ('一剪梅·舟过吴江', '一剪梅', '蒋捷'), ('念奴娇·过洞庭', '念奴娇', '张孝祥'), ('长相思·山一程', '长相思', '纳兰性德'),
    ('木兰花/玉楼红·初见', '木兰花', '纳兰性德'), ('木兰花b/玉楼春', '玉楼春', '纳兰性德'), ('浣溪沙·西风', '浣溪沙', '纳兰性德'),
    ('山居秋暝', '山居秋暝', '王维'), ('从军行', '从军行', '王昌龄'), ('登高', '登高', '杜甫'),
    ('客至', '客至', '杜甫'), ('春夜洛城闻笛', '春夜洛城闻笛', '李白'), ('金缕衣', '金缕衣', '杜秋娘'),
    ('游园不值', '游园不值', '叶绍翁'), ('约客', '约客', '赵师秀'), ('苔', '苔', '袁枚'), ('舟夜书所见', '舟夜书所见', '查慎行'),
]


def norm(s):
    try:
        import zhconv
        return zhconv.convert(s, 'zh-hans')
    except ImportError:
        return s


def main():
    files = []
    for sub in ('宋词', '五代诗词', '纳兰性德', '全唐诗', '水墨唐诗', '宋诗', '金元明清诗'):
        files += glob.glob(os.path.join(ROOT, sub, '**', '*.json'), recursive=True)
    files = [f for f in files if 'author' not in os.path.basename(f) and os.path.getsize(f) < 40 * 1024 * 1024]
    print('loading %d corpus files…' % len(files), file=sys.stderr)
    ents = []
    for f in files:
        try:
            d = json.load(io.open(f, encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(d, list):
            continue
        for e in d:
            if not isinstance(e, dict):
                continue
            t = e.get('title') or e.get('rhythmic') or ''
            a = e.get('author') or ''
            p = e.get('paragraphs') or e.get('paras') or []
            if t and p:
                ents.append((t, a, p))
    print('corpus entries: %d' % len(ents), file=sys.stderr)
    for label, key, author in CANDS:
        hits = []
        for t, a, p in ents:
            if author.split('·')[0] not in a and author not in a:
                continue
            tn = norm(t)
            if key in t or key in tn:
                txt = norm(''.join(p))
                hits.append((t, a, txt))
        print('### %s [%s·%s] %d hits' % (label, author, key, len(hits)))
        for t, a, txt in hits[:4]:
            print('  %s·%s: %s' % (a, t, txt[:130]))
        if not hits:
            print('  !! NOT FOUND')


if __name__ == '__main__':
    main()
