"""dqutils.dq3.charlarge - The dictionary of large size characters."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

CHARMAP: Final[dict[int, str]] = {
    0x0200: " ",
    0x0201: "愛",
    0x0202: "悪",
    0x0203: "安",
    0x0204: "暗",
    0x0205: "闇",
    0x0206: "栄",
    0x0207: "永",
    0x0208: "英",
    0x0209: "駅",
    0x020A: "演",
    0x020B: "炎",
    0x020C: "縁",
    0x020D: "遠",
    0x020E: "波",
    0x020F: "派",
    0x0210: "敗",
    0x0211: "背",
    0x0212: "配",
    0x0213: "売",
    0x0214: "漠",
    0x0215: "爆",
    0x0216: "箱",
    0x0217: "肌",
    0x0218: "畑",
    0x0219: "発",
    0x021A: "抜",
    0x021B: "判",
    0x021C: "半",
    0x021D: "反",
    0x021E: "版",
    0x021F: "晩",
    0x0220: "番",
    0x0221: "兵",
    0x0222: "柄",
    0x0223: "並",
    0x0224: "壁",
    0x0225: "別",
    0x0226: "変",
    0x0227: "返",
    0x0228: "便",
    0x0229: "勉",
    0x022A: "弁",
    0x022B: "妃",
    0x022C: "彼",
    0x022D: "悲",
    0x022E: "扉",
    0x022F: "疲",
    0x0230: "皮",
    0x0231: "秘",
    0x0232: "備",
    0x0233: "美",
    0x0234: "彦",
    0x0235: "必",
    0x0236: "姫",
    0x0237: "標",
    0x0238: "氷",
    0x0239: "表",
    0x023A: "病",
    0x023B: "品",
    0x023C: "保",
    0x023D: "歩",
    0x023E: "墓",
    0x023F: "母",
    0x0240: "報",
    0x0241: "宝",
    0x0242: "放",
    0x0243: "方",
    0x0244: "法",
    0x0245: "砲",
    0x0246: "訪",
    0x0247: "坊",
    0x0248: "忘",
    0x0249: "暴",
    0x024A: "望",
    0x024B: "防",
    0x024C: "北",
    0x024D: "牧",
    0x024E: "本",
    0x024F: "付",
    0x0250: "夫",
    0x0251: "婦",
    0x0252: "布",
    0x0253: "敷",
    0x0254: "浮",
    0x0255: "父",
    0x0256: "負",
    0x0257: "武",
    0x0258: "舞",
    0x0259: "部",
    0x025A: "封",
    0x025B: "復",
    0x025C: "服",
    0x025D: "福",
    0x025E: "腹",
    0x025F: "仏",
    0x0260: "物",
    0x0261: "分",
    0x0262: "粉",
    0x0263: "文",
    0x0264: "以",
    0x0265: "位",
    0x0266: "偉",
    0x0267: "意",
    0x0268: "移",
    0x0269: "遺",
    0x026A: "井",
    0x026B: "育",
    0x026C: "印",
    0x026D: "飲",
    0x026E: "隠",
    0x026F: "仮",
    0x0270: "何",
    0x0271: "価",
    0x0272: "家",
    0x0273: "架",
    0x0274: "歌",
    0x0275: "河",
    0x0276: "火",
    0x0277: "花",
    0x0278: "荷",
    0x0279: "過",
    0x027A: "我",
    0x027B: "介",
    0x027C: "会",
    0x027D: "解",
    0x027E: "怪",
    0x027F: "改",
    0x0280: "海",
    0x0281: "界",
    0x0282: "皆",
    0x0283: "絵",
    0x0284: "外",
    0x0285: "涯",
    0x0286: "格",
    0x0287: "確",
    0x0288: "覚",
    0x0289: "革",
    0x028A: "学",
    0x028B: "楽",
    0x028C: "額",
    0x028D: "割",
    0x028E: "活",
    0x028F: "官",
    0x0290: "感",
    0x0291: "慣",
    0x0292: "換",
    0x0293: "敢",
    0x0294: "甘",
    0x0295: "観",
    0x0296: "鑑",
    0x0297: "丸",
    0x0298: "岸",
    0x0299: "眼",
    0x029A: "岩",
    0x029B: "顔",
    0x029C: "願",
    0x029D: "係",
    0x029E: "刑",
    0x029F: "形",
    0x02A0: "恵",
    0x02A1: "景",
    0x02A2: "系",
    0x02A3: "経",
    0x02A4: "警",
    0x02A5: "劇",
    0x02A6: "撃",
    0x02A7: "欠",
    0x02A8: "決",
    0x02A9: "結",
    0x02AA: "件",
    0x02AB: "健",
    0x02AC: "券",
    0x02AD: "剣",
    0x02AE: "犬",
    0x02AF: "研",
    0x02B0: "肩",
    0x02B1: "見",
    0x02B2: "賢",
    0x02B3: "険",
    0x02B4: "験",
    0x02B5: "原",
    0x02B6: "源",
    0x02B7: "現",
    0x02B8: "言",
    0x02B9: "限",
    0x02BA: "危",
    0x02BB: "寄",
    0x02BC: "希",
    0x02BD: "机",
    0x02BE: "期",
    0x02BF: "機",
    0x02C0: "気",
    0x02C1: "祈",
    0x02C2: "貴",
    0x02C3: "技",
    0x02C4: "義",
    0x02C5: "議",
    0x02C6: "客",
    0x02C7: "逆",
    0x02C8: "休",
    0x02C9: "急",
    0x02CA: "救",
    0x02CB: "求",
    0x02CC: "泣",
    0x02CD: "球",
    0x02CE: "究",
    0x02CF: "牛",
    0x02D0: "去",
    0x02D1: "居",
    0x02D2: "挙",
    0x02D3: "許",
    0x02D4: "距",
    0x02D5: "魚",
    0x02D6: "供",
    0x02D7: "共",
    0x02D8: "協",
    0x02D9: "強",
    0x02DA: "教",
    0x02DB: "橋",
    0x02DC: "胸",
    0x02DD: "興",
    0x02DE: "鏡",
    0x02DF: "驚",
    0x02E0: "業",
    0x02E1: "禁",
    0x02E2: "筋",
    0x02E3: "近",
    0x02E4: "金",
    0x02E5: "吟",
    0x02E6: "銀",
    0x02E7: "個",
    0x02E8: "古",
    0x02E9: "呼",
    0x02EA: "庫",
    0x02EB: "湖",
    0x02EC: "後",
    0x02ED: "御",
    0x02EE: "護",
    0x02EF: "交",
    0x02F0: "光",
    0x02F1: "効",
    0x02F2: "向",
    0x02F3: "好",
    0x02F4: "孝",
    0x02F5: "幸",
    0x02F6: "広",
    0x02F7: "康",
    0x02F8: "攻",
    0x02F9: "更",
    0x02FA: "港",
    0x02FB: "考",
    0x02FC: "航",
    0x02FD: "荒",
    0x02FE: "行",
    0x02FF: "鋼",
    0x0300: "降",
    0x0301: "高",
    0x0302: "号",
    0x0303: "合",
    0x0304: "告",
    0x0305: "獄",
    0x0306: "骨",
    0x0307: "込",
    0x0308: "頃",
    0x0309: "今",
    0x030A: "婚",
    0x030B: "根",
    0x030C: "喰",
    0x030D: "窟",
    0x030E: "君",
    0x030F: "魔",
    0x0310: "埋",
    0x0311: "枚",
    0x0312: "毎",
    0x0313: "万",
    0x0314: "慢",
    0x0315: "満",
    0x0316: "命",
    0x0317: "迷",
    0x0318: "味",
    0x0319: "未",
    0x031A: "岬",
    0x031B: "密",
    0x031C: "民",
    0x031D: "眠",
    0x031E: "木",
    0x031F: "戻",
    0x0320: "問",
    0x0321: "門",
    0x0322: "夢",
    0x0323: "無",
    0x0324: "娘",
    0x0325: "内",
    0x0326: "南",
    0x0327: "猫",
    0x0328: "熱",
    0x0329: "年",
    0x032A: "念",
    0x032B: "虹",
    0x032C: "任",
    0x032D: "忍",
    0x032E: "認",
    0x032F: "悩",
    0x0330: "能",
    0x0331: "脳",
    0x0332: "汚",
    0x0333: "奥",
    0x0334: "押",
    0x0335: "黄",
    0x0336: "屋",
    0x0337: "憶",
    0x0338: "音",
    0x0339: "来",
    0x033A: "頼",
    0x033B: "絡",
    0x033C: "落",
    0x033D: "嵐",
    0x033E: "令",
    0x033F: "例",
    0x0340: "礼",
    0x0341: "霊",
    0x0342: "歴",
    0x0343: "列",
    0x0344: "劣",
    0x0345: "恋",
    0x0346: "練",
    0x0347: "連",
    0x0348: "利",
    0x0349: "履",
    0x034A: "理",
    0x034B: "里",
    0x034C: "離",
    0x034D: "陸",
    0x034E: "率",
    0x034F: "立",
    0x0350: "流",
    0x0351: "竜",
    0x0352: "侶",
    0x0353: "旅",
    0x0354: "料",
    0x0355: "良",
    0x0356: "緑",
    0x0357: "労",
    0x0358: "牢",
    0x0359: "老",
    0x035A: "録",
    0x035B: "涙",
    0x035C: "類",
    0x035D: "左",
    0x035E: "差",
    0x035F: "砂",
    0x0360: "座",
    0x0361: "最",
    0x0362: "塞",
    0x0363: "妻",
    0x0364: "才",
    0x0365: "災",
    0x0366: "祭",
    0x0367: "細",
    0x0368: "在",
    0x0369: "材",
    0x036A: "罪",
    0x036B: "財",
    0x036C: "作",
    0x036D: "策",
    0x036E: "札",
    0x036F: "殺",
    0x0370: "雑",
    0x0371: "参",
    0x0372: "産",
    0x0373: "算",
    0x0374: "残",
    0x0375: "瀬",
    0x0376: "制",
    0x0377: "征",
    0x0378: "性",
    0x0379: "成",
    0x037A: "政",
    0x037B: "整",
    0x037C: "清",
    0x037D: "精",
    0x037E: "聖",
    0x037F: "青",
    0x0380: "静",
    0x0381: "税",
    0x0382: "昔",
    0x0383: "積",
    0x0384: "責",
    0x0385: "赤",
    0x0386: "切",
    0x0387: "接",
    0x0388: "設",
    0x0389: "説",
    0x038A: "雪",
    0x038B: "絶",
    0x038C: "先",
    0x038D: "専",
    0x038E: "川",
    0x038F: "戦",
    0x0390: "泉",
    0x0391: "浅",
    0x0392: "洗",
    0x0393: "線",
    0x0394: "船",
    0x0395: "選",
    0x0396: "前",
    0x0397: "然",
    0x0398: "全",
    0x0399: "使",
    0x039A: "史",
    0x039B: "始",
    0x039C: "姉",
    0x039D: "姿",
    0x039E: "子",
    0x039F: "市",
    0x03A0: "志",
    0x03A1: "支",
    0x03A2: "私",
    0x03A3: "糸",
    0x03A4: "紙",
    0x03A5: "詩",
    0x03A6: "試",
    0x03A7: "事",
    0x03A8: "似",
    0x03A9: "字",
    0x03AA: "持",
    0x03AB: "時",
    0x03AC: "次",
    0x03AD: "治",
    0x03AE: "示",
    0x03AF: "耳",
    0x03B0: "式",
    0x03B1: "識",
    0x03B2: "七",
    0x03B3: "失",
    0x03B4: "室",
    0x03B5: "質",
    0x03B6: "実",
    0x03B7: "捨",
    0x03B8: "社",
    0x03B9: "者",
    0x03BA: "謝",
    0x03BB: "邪",
    0x03BC: "若",
    0x03BD: "弱",
    0x03BE: "主",
    0x03BF: "取",
    0x03C0: "守",
    0x03C1: "手",
    0x03C2: "殊",
    0x03C3: "種",
    0x03C4: "酒",
    0x03C5: "受",
    0x03C6: "呪",
    0x03C7: "修",
    0x03C8: "終",
    0x03C9: "習",
    0x03CA: "舟",
    0x03CB: "集",
    0x03CC: "住",
    0x03CD: "十",
    0x03CE: "重",
    0x03CF: "宿",
    0x03D0: "祝",
    0x03D1: "出",
    0x03D2: "術",
    0x03D3: "春",
    0x03D4: "準",
    0x03D5: "盾",
    0x03D6: "順",
    0x03D7: "初",
    0x03D8: "所",
    0x03D9: "書",
    0x03DA: "助",
    0x03DB: "女",
    0x03DC: "傷",
    0x03DD: "勝",
    0x03DE: "商",
    0x03DF: "唱",
    0x03E0: "将",
    0x03E1: "小",
    0x03E2: "少",
    0x03E3: "床",
    0x03E4: "招",
    0x03E5: "沼",
    0x03E6: "照",
    0x03E7: "省",
    0x03E8: "称",
    0x03E9: "章",
    0x03EA: "笑",
    0x03EB: "粧",
    0x03EC: "紹",
    0x03ED: "賞",
    0x03EE: "丈",
    0x03EF: "乗",
    0x03F0: "城",
    0x03F1: "場",
    0x03F2: "情",
    0x03F3: "条",
    0x03F4: "杖",
    0x03F5: "状",
    0x03F6: "飾",
    0x03F7: "色",
    0x03F8: "食",
    0x03F9: "伸",
    0x03FA: "信",
    0x03FB: "侵",
    0x03FC: "寝",
    0x03FD: "慎",
    0x03FE: "新",
    0x03FF: "森",
    0x0400: "深",
    0x0401: "真",
    0x0402: "神",
    0x0403: "親",
    0x0404: "診",
    0x0405: "身",
    0x0406: "進",
    0x0407: "震",
    0x0408: "陣",
    0x0409: "祖",
    0x040A: "素",
    0x040B: "組",
    0x040C: "僧",
    0x040D: "創",
    0x040E: "倉",
    0x040F: "想",
    0x0410: "早",
    0x0411: "争",
    0x0412: "相",
    0x0413: "草",
    0x0414: "葬",
    0x0415: "装",
    0x0416: "走",
    0x0417: "送",
    0x0418: "像",
    0x0419: "憎",
    0x041A: "造",
    0x041B: "側",
    0x041C: "息",
    0x041D: "束",
    0x041E: "足",
    0x041F: "属",
    0x0420: "賊",
    0x0421: "族",
    0x0422: "続",
    0x0423: "存",
    0x0424: "損",
    0x0425: "村",
    0x0426: "吹",
    0x0427: "水",
    0x0428: "数",
    0x0429: "他",
    0x042A: "多",
    0x042B: "太",
    0x042C: "打",
    0x042D: "体",
    0x042E: "対",
    0x042F: "耐",
    0x0430: "待",
    0x0431: "態",
    0x0432: "替",
    0x0433: "袋",
    0x0434: "退",
    0x0435: "代",
    0x0436: "台",
    0x0437: "大",
    0x0438: "題",
    0x0439: "達",
    0x043A: "脱",
    0x043B: "誰",
    0x043C: "単",
    0x043D: "探",
    0x043E: "胆",
    0x043F: "誕",
    0x0440: "壇",
    0x0441: "断",
    0x0442: "段",
    0x0443: "男",
    0x0444: "談",
    0x0445: "低",
    0x0446: "定",
    0x0447: "底",
    0x0448: "庭",
    0x0449: "弟",
    0x044A: "敵",
    0x044B: "的",
    0x044C: "笛",
    0x044D: "鉄",
    0x044E: "展",
    0x044F: "店",
    0x0450: "転",
    0x0451: "点",
    0x0452: "伝",
    0x0453: "殿",
    0x0454: "値",
    0x0455: "知",
    0x0456: "地",
    0x0457: "池",
    0x0458: "置",
    0x0459: "茶",
    0x045A: "着",
    0x045B: "中",
    0x045C: "仲",
    0x045D: "忠",
    0x045E: "昼",
    0x045F: "注",
    0x0460: "虫",
    0x0461: "兆",
    0x0462: "張",
    0x0463: "挑",
    0x0464: "朝",
    0x0465: "町",
    0x0466: "調",
    0x0467: "超",
    0x0468: "長",
    0x0469: "頂",
    0x046A: "鳥",
    0x046B: "直",
    0x046C: "沈",
    0x046D: "渡",
    0x046E: "登",
    0x046F: "途",
    0x0470: "都",
    0x0471: "努",
    0x0472: "度",
    0x0473: "土",
    0x0474: "奴",
    0x0475: "怒",
    0x0476: "倒",
    0x0477: "党",
    0x0478: "凍",
    0x0479: "塔",
    0x047A: "島",
    0x047B: "投",
    0x047C: "東",
    0x047D: "盗",
    0x047E: "湯",
    0x047F: "灯",
    0x0480: "等",
    0x0481: "答",
    0x0482: "筒",
    0x0483: "逃",
    0x0484: "透",
    0x0485: "頭",
    0x0486: "闘",
    0x0487: "働",
    0x0488: "動",
    0x0489: "洞",
    0x048A: "胴",
    0x048B: "道",
    0x048C: "銅",
    0x048D: "得",
    0x048E: "特",
    0x048F: "毒",
    0x0490: "読",
    0x0491: "突",
    0x0492: "追",
    0x0493: "痛",
    0x0494: "通",
    0x0495: "右",
    0x0496: "運",
    0x0497: "雲",
    0x0498: "和",
    0x0499: "話",
    0x049A: "惑",
    0x049B: "腕",
    0x049C: "夜",
    0x049D: "野",
    0x049E: "矢",
    0x049F: "役",
    0x04A0: "約",
    0x04A1: "薬",
    0x04A2: "予",
    0x04A3: "与",
    0x04A4: "預",
    0x04A5: "幼",
    0x04A6: "妖",
    0x04A7: "様",
    0x04A8: "用",
    0x04A9: "羊",
    0x04AA: "葉",
    0x04AB: "踊",
    0x04AC: "陽",
    0x04AD: "欲",
    0x04AE: "勇",
    0x04AF: "友",
    0x04B0: "幽",
    0x04B1: "有",
    0x04B2: "由",
    0x04B3: "遊",
    0x04B4: "雄",
    0x04B5: "０",
    0x04B6: "２",
    0x04B7: "３",
    0x04B8: "４",
    0x04B9: "５",
    0x04BA: "６",
    0x04BB: "７",
    0x04BC: "８",
    0x04BD: "９",
    0x04BE: "ト",
    0x04BF: "リ",
    0x04C0: "１",
    0x04C1: "Ａ",
    0x04C2: "Ｈ",
    0x04C3: "Ｋ",
    0x04C4: "Ｎ",
    0x04C5: "Ｑ",
    0x04C6: "Ｒ",
    0x04C7: "Ｔ",
    0x04C8: "Ｖ",
    0x04C9: "Ｚ",
    0x04CA: "〓",
    0x04CB: "△",
    0x04CC: "※",
    0x04CD: "き",
    0x04CE: "そ",
    0x04CF: "ち",
    0x04D0: "は",
    0x04D1: "ま",
    0x04D2: "も",
    0x04D3: "ら",
    0x04D4: "る",
    0x04D5: "ろ",
    0x04D6: "を",
    0x04D7: "ん",
    0x04D8: "ノ",
    0x04D9: "ヒ",
    0x04DA: "レ",
    0x04DB: "ワ",
    0x04DC: "Ｂ",
    0x04DD: "Ｅ",
    0x04DE: "Ｆ",
    0x04DF: "Ｌ",
    0x04E0: "Ｏ",
    0x04E1: "Ｐ",
    0x04E2: "Ｓ",
    0x04E3: "う",
    0x04E4: "く",
    0x04E5: "さ",
    0x04E6: "し",
    0x04E7: "じ",
    0x04E8: "と",
    0x04E9: "よ",
    0x04EA: "り",
    0x04EB: "ミ",
    0x04EC: "ヲ",
    0x04ED: "Ｃ",
    0x04EE: "Ｄ",
    0x04EF: "Ｇ",
    0x04F0: "Ｊ",
    0x04F1: "*",  # 要チェック
    0x04F2: "メ",
    0x04F3: "Ｉ",
    0x04F4: "Ｍ",
    0x04F5: "Ｗ",
    0x04F6: "Ｘ",
    0x04F7: "Ｙ",
    0x04F8: "＋",
    0x04F9: "ざ",
    0x04FA: "ぢ",
    0x04FB: "ど",
    0x04FC: "ね",
    0x04FD: "ひ",
    0x04FE: "ふ",
    0x04FF: "ぶ",
    0x0500: "み",
    0x0501: "め",
    0x0502: "れ",
    0x0503: "わ",
    0x0504: "セ",
    0x0505: "ム",
    0x0506: "ル",
    0x0507: "血",
    0x0508: "玉",
    0x0509: "口",
    0x050A: "工",
    0x050B: "王",
    0x050C: "三",
    0x050D: "正",
    0x050E: "西",
    0x050F: "Ｕ",
    0x0510: "あ",
    0x0511: "え",
    0x0512: "お",
    0x0513: "か",
    0x0514: "け",
    0x0515: "す",
    0x0516: "せ",
    0x0517: "た",
    0x0518: "だ",
    0x0519: "な",
    0x051A: "べ",
    0x051B: "む",
    0x051C: "や",
    0x051D: "ゆ",
    0x051E: "♪",
    0x051F: "ア",
    0x0520: "シ",
    0x0521: "ツ",
    0x0522: "テ",
    0x0523: "ラ",
    0x0524: "日",
    0x0525: "l",  # 要チェック
    0x0526: "(",  # 要チェック
    0x0527: ")",  # 要チェック
    0x0528: "、",
    0x0529: "。",
    0x052A: ".",
    0x052B: "・",
    0x052C: "ぃ",
    0x052D: "？",
    0x052E: "！",
    0x052F: "ウ",
    0x0530: "カ",
    0x0531: "‥",
    0x0532: "_",  # 要チェック
    0x0533: "々",
    0x0534: "×",
    0x0535: "ー",
    0x0536: "～",
    0x0537: "→",
    0x0538: "/",
    0x0539: "10",
    0x053A: "が",
    0x053B: "ぱ",
    0x053C: "ぴ",
    0x053D: "ぽ",
    0x053E: "ギ",
    0x053F: "ゲ",
    0x0540: "ゴ",
    0x0541: "ザ",
    0x0542: "ズ",
    0x0543: "ゾ",
    0x0544: "ダ",
    0x0545: "ヂ",
    0x0546: "ヅ",
    0x0547: "バ",
    0x0548: "パ",
    0x0549: "ビ",
    0x054A: "ブ",
    0x054B: "プ",
    0x054C: "ベ",
    0x054D: "ボ",
    0x054E: "ポ",
    0x054F: "温",
    0x0550: "…",
    0x0551: "”",
    0x0552: "》",
    0x0553: "『",
    0x0554: "「",
    0x0555: "』",
    0x0556: "ょ",
    0x0557: "ィ",
    0x0558: "-",  # 要チェック
    0x0559: "へ",
    0x055A: "%",  # 要チェック
    0x055B: "ぺ",
    0x055C: "オ",
    0x055D: "キ",
    0x055E: "ケ",
    0x055F: "チ",
    0x0560: "ナ",
    0x0561: "月",
    0x0562: "巨",
    0x0563: "入",
    0x0564: "臣",
    0x0565: "人",
    0x0566: "＆",
    0x0567: "イ",
    0x0568: "ク",
    0x0569: "タ",
    0x056A: "ド",
    0x056B: "★",
    0x056C: "馬",
    0x056D: "八",
    0x056E: "平",
    0x056F: "閉",
    0x0570: "辺",
    0x0571: "飛",
    0x0572: "ぷ",
    0x0573: "亡",
    0x0574: "不",
    0x0575: "風",
    0x0576: "聞",
    0x0577: "囲",
    0x0578: "異",
    0x0579: "[よ]",  # 要チェック
    0x057A: "下",
    0x057B: "化",
    0x057C: "果",
    0x057D: "牙",
    0x057E: "回",
    0x057F: "灰",
    0x0580: "開",
    0x0581: "階",
    0x0582: "間",
    0x0583: "関",
    0x0584: "ガ",
    0x0585: "グ",
    0x0586: "サ",
    0x0587: "ネ",
    0x0588: "ピ",
    0x0589: "ホ",
    0x058A: "ヤ",
    0x058B: "ヴ",
    0x058C: "兄",
    0x058D: "穴",
    0x058E: "元",
    0x058F: "器",
    0x0590: "帰",
    0x0591: "記",
    0x0592: "起",
    0x0593: "恐",
    0x0594: "局",
    0x0595: "戸",
    0x0596: "故",
    0x0597: "語",
    0x0598: "国",
    0x0599: "困",
    0x059A: "苦",
    0x059B: "具",
    0x059C: "空",
    0x059D: "軍",
    0x059E: "面",
    0x059F: "応",
    0x05A0: "恩",
    0x05A1: "両",
    0x05A2: "山",
    0x05A3: "世",
    0x05A4: "星",
    0x05A5: "生",
    0x05A6: "声",
    0x05A7: "石",
    0x05A8: "千",
    0x05A9: "仕",
    0x05AA: "士",
    0x05AB: "思",
    0x05AC: "指",
    0x05AD: "止",
    0x05AE: "死",
    0x05AF: "囚",
    0x05B0: "周",
    0x05B1: "上",
    0x05B2: "冗",
    0x05B3: "心",
    0x05B4: "図",
    0x05B5: "天",
    0x05B6: "同",
    0x05B7: "雨",
    0x05B8: "要",
    0x05B9: "○",
    0x05BA: "ぁ",
    0x05BB: "ぉ",
    0x05BC: "ォ",
    0x05BD: "ッ",
    0x05BE: "ャ",
    0x05BF: "買",
    0x05C0: "泊",
    0x05C1: "冒",
    0x05C2: "員",
    0x05C3: "引",
    0x05C4: "加",
    0x05C5: "枯",
    0x05C6: "名",
    0x05C7: "明",
    0x05C8: "力",
    0x05C9: "首",
    0x05CA: "消",
    0x05CB: "象",
    0x05CC: "当",
    0x05CD: "白",
    0x05CE: "目",
    0x05CF: "呂",
    0x05D0: "自",
    0x05D1: "申",
    0x05D2: "い",
    0x05D3: "の",
    0x05D4: "ハ",
    0x05D5: "モ",
    0x05D6: "ぅ",
    0x05D7: "ぇ",
    0x05D8: "ゥ",
    0x05D9: "ぎ",
    0x05DA: "ぐ",
    0x05DB: "ご",
    0x05DC: "ず",
    0x05DD: "ぞ",
    0x05DE: "づ",
    0x05DF: "ぬ",
    0x05E0: "ば",
    0x05E1: "び",
    0x05E2: "ぼ",
    0x05E3: "ジ",
    0x05E4: "ゼ",
    0x05E5: "デ",
    0x05E6: "げ",
    0x05E7: "ぜ",
    0x05E8: "で",
    0x05E9: "こ",
    0x05EA: "っ",
    0x05EB: "ゃ",
    0x05EC: "ゅ",
    0x05ED: "ァ",
    0x05EE: "つ",
    0x05EF: "エ",
    0x05F0: "て",
    0x05F1: "マ",
    0x05F2: "ン",
    0x05F3: "に",
    0x05F4: "ほ",
    0x05F5: ":",
    0x05F6: "コ",
    0x05F7: "ス",
    0x05F8: "ソ",
    0x05F9: "ヌ",
    0x05FA: "フ",
    0x05FB: "ロ",
    0x05FC: "暮",
    0x05FD: "一",
    0x05FE: "☆",
    0x05FF: "ェ",
    0x0600: "ニ",
    0x0601: "ユ",
    0x0602: "ヘ",
    0x0603: "ペ",
    0x0604: "鍵",
    0x0605: "極",
    0x0606: "滅",
    0x0607: "職",
    0x0608: "ュ",
    0x0609: "ョ",
    0x060A: "ヨ",
    0x060B: "了",
}
