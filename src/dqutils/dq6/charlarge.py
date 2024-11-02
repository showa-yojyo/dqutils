"""dqutils.dq6.charlarge - The dictionary of large size characters."""

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
    0x0205: "案",
    0x0206: "闇",
    0x0207: "栄",
    0x0208: "永",
    0x0209: "泳",
    0x020A: "英",
    0x020B: "炎",
    0x020C: "遠",
    0x020D: "波",
    0x020E: "派",
    0x020F: "破",
    0x0210: "敗",
    0x0211: "杯",
    0x0212: "背",
    0x0213: "配",
    0x0214: "倍",
    0x0215: "売",
    0x0216: "漠",
    0x0217: "箱",
    0x0218: "畑",
    0x0219: "発",
    0x021A: "抜",
    0x021B: "判",
    0x021C: "半",
    0x021D: "反",
    0x021E: "板",
    0x021F: "汎",
    0x0220: "犯",
    0x0221: "般",
    0x0222: "晩",
    0x0223: "番",
    0x0224: "兵",
    0x0225: "並",
    0x0226: "陛",
    0x0227: "米",
    0x0228: "壁",
    0x0229: "別",
    0x022A: "変",
    0x022B: "返",
    0x022C: "便",
    0x022D: "勉",
    0x022E: "妃",
    0x022F: "彼",
    0x0230: "悲",
    0x0231: "扉",
    0x0232: "秘",
    0x0233: "費",
    0x0234: "非",
    0x0235: "備",
    0x0236: "美",
    0x0237: "必",
    0x0238: "姫",
    0x0239: "標",
    0x023A: "氷",
    0x023B: "表",
    0x023C: "病",
    0x023D: "品",
    0x023E: "貧",
    0x023F: "捕",
    0x0240: "歩",
    0x0241: "募",
    0x0242: "墓",
    0x0243: "母",
    0x0244: "報",
    0x0245: "宝",
    0x0246: "抱",
    0x0247: "放",
    0x0248: "方",
    0x0249: "法",
    0x024A: "胞",
    0x024B: "訪",
    0x024C: "乏",
    0x024D: "坊",
    0x024E: "忘",
    0x024F: "房",
    0x0250: "望",
    0x0251: "防",
    0x0252: "北",
    0x0253: "没",
    0x0254: "本",
    0x0255: "付",
    0x0256: "夫",
    0x0257: "婦",
    0x0258: "布",
    0x0259: "普",
    0x025A: "浮",
    0x025B: "父",
    0x025C: "負",
    0x025D: "武",
    0x025E: "舞",
    0x025F: "部",
    0x0260: "封",
    0x0261: "復",
    0x0262: "服",
    0x0263: "福",
    0x0264: "腹",
    0x0265: "物",
    0x0266: "分",
    0x0267: "文",
    0x0268: "以",
    0x0269: "位",
    0x026A: "意",
    0x026B: "移",
    0x026C: "違",
    0x026D: "井",
    0x026E: "育",
    0x026F: "印",
    0x0270: "飲",
    0x0271: "隠",
    0x0272: "〓",  # フォーン王の呪文用
    0x0273: "仮",
    0x0274: "何",
    0x0275: "価",
    0x0276: "嫁",
    0x0277: "家",
    0x0278: "架",
    0x0279: "歌",
    0x027A: "火",
    0x027B: "花",
    0x027C: "貨",
    0x027D: "過",
    0x027E: "我",
    0x027F: "介",
    0x0280: "会",
    0x0281: "解",
    0x0282: "壊",
    0x0283: "怪",
    0x0284: "悔",
    0x0285: "拐",
    0x0286: "改",
    0x0287: "海",
    0x0288: "界",
    0x0289: "皆",
    0x028A: "絵",
    0x028B: "外",
    0x028C: "崖",
    0x028D: "拡",
    0x028E: "格",
    0x028F: "確",
    0x0290: "覚",
    0x0291: "学",
    0x0292: "楽",
    0x0293: "活",
    0x0294: "寒",
    0x0295: "完",
    0x0296: "官",
    0x0297: "感",
    0x0298: "換",
    0x0299: "棺",
    0x029A: "甘",
    0x029B: "看",
    0x029C: "管",
    0x029D: "観",
    0x029E: "鑑",
    0x029F: "館",
    0x02A0: "含",
    0x02A1: "眼",
    0x02A2: "岩",
    0x02A3: "顔",
    0x02A4: "願",
    0x02A5: "係",
    0x02A6: "刑",
    0x02A7: "形",
    0x02A8: "恵",
    0x02A9: "景",
    0x02AA: "系",
    0x02AB: "経",
    0x02AC: "計",
    0x02AD: "軽",
    0x02AE: "芸",
    0x02AF: "劇",
    0x02B0: "撃",
    0x02B1: "決",
    0x02B2: "結",
    0x02B3: "件",
    0x02B4: "券",
    0x02B5: "剣",
    0x02B6: "犬",
    0x02B7: "研",
    0x02B8: "肩",
    0x02B9: "見",
    0x02BA: "賢",
    0x02BB: "険",
    0x02BC: "験",
    0x02BD: "原",
    0x02BE: "現",
    0x02BF: "言",
    0x02C0: "限",
    0x02C1: "奇",
    0x02C2: "寄",
    0x02C3: "希",
    0x02C4: "忌",
    0x02C5: "期",
    0x02C6: "機",
    0x02C7: "気",
    0x02C8: "祈",
    0x02C9: "季",
    0x02CA: "貴",
    0x02CB: "輝",
    0x02CC: "騎",
    0x02CD: "鬼",
    0x02CE: "儀",
    0x02CF: "技",
    0x02D0: "義",
    0x02D1: "議",
    0x02D2: "客",
    0x02D3: "久",
    0x02D4: "休",
    0x02D5: "吸",
    0x02D6: "宮",
    0x02D7: "急",
    0x02D8: "救",
    0x02D9: "求",
    0x02DA: "泣",
    0x02DB: "究",
    0x02DC: "級",
    0x02DD: "給",
    0x02DE: "牛",
    0x02DF: "去",
    0x02E0: "居",
    0x02E1: "拠",
    0x02E2: "許",
    0x02E3: "漁",
    0x02E4: "魚",
    0x02E5: "供",
    0x02E6: "共",
    0x02E7: "協",
    0x02E8: "境",
    0x02E9: "強",
    0x02EA: "教",
    0x02EB: "橋",
    0x02EC: "胸",
    0x02ED: "鏡",
    0x02EE: "業",
    0x02EF: "禁",
    0x02F0: "近",
    0x02F1: "金",
    0x02F2: "銀",
    0x02F3: "個",
    0x02F4: "古",
    0x02F5: "呼",
    0x02F6: "庫",
    0x02F7: "湖",
    0x02F8: "後",
    0x02F9: "護",
    0x02FA: "交",
    0x02FB: "光",
    0x02FC: "効",
    0x02FD: "向",
    0x02FE: "好",
    0x02FF: "孝",
    0x0300: "幸",
    0x0301: "広",
    0x0302: "攻",
    0x0303: "更",
    0x0304: "港",
    0x0305: "考",
    0x0306: "航",
    0x0307: "荒",
    0x0308: "行",
    0x0309: "鉱",
    0x030A: "降",
    0x030B: "香",
    0x030C: "高",
    0x030D: "合",
    0x030E: "告",
    0x030F: "黒",
    0x0310: "獄",
    0x0311: "腰",
    0x0312: "骨",
    0x0313: "込",
    0x0314: "頃",
    0x0315: "今",
    0x0316: "婚",
    0x0317: "根",
    0x0318: "句",
    0x0319: "駆",
    0x031A: "遇",
    0x031B: "掘",
    0x031C: "窟",
    0x031D: "君",
    0x031E: "訓",
    0x031F: "魔",
    0x0320: "麻",
    0x0321: "埋",
    0x0322: "妹",
    0x0323: "枚",
    0x0324: "毎",
    0x0325: "幕",
    0x0326: "末",
    0x0327: "万",
    0x0328: "満",
    0x0329: "漫",
    0x032A: "命",
    0x032B: "迷",
    0x032C: "鳴",
    0x032D: "味",
    0x032E: "未",
    0x032F: "岬",
    0x0330: "密",
    0x0331: "妙",
    0x0332: "民",
    0x0333: "眠",
    0x0334: "茂",
    0x0335: "毛",
    0x0336: "木",
    0x0337: "戻",
    0x0338: "問",
    0x0339: "門",
    0x033A: "務",
    0x033B: "夢",
    0x033C: "無",
    0x033D: "娘",
    0x033E: "内",
    0x033F: "南",
    0x0340: "難",
    0x0341: "猫",
    0x0342: "熱",
    0x0343: "年",
    0x0344: "念",
    0x0345: "尼",
    0x0346: "肉",
    0x0347: "任",
    0x0348: "認",
    0x0349: "納",
    0x034A: "能",
    0x034B: "奥",
    0x034C: "押",
    0x034D: "横",
    0x034E: "黄",
    0x034F: "沖",
    0x0350: "屋",
    0x0351: "憶",
    0x0352: "桶",
    0x0353: "音",
    0x0354: "来",
    0x0355: "頼",
    0x0356: "雷",
    0x0357: "絡",
    0x0358: "落",
    0x0359: "乱",
    0x035A: "嵐",
    0x035B: "令",
    0x035C: "例",
    0x035D: "冷",
    0x035E: "礼",
    0x035F: "霊",
    0x0360: "歴",
    0x0361: "列",
    0x0362: "恋",
    0x0363: "練",
    0x0364: "連",
    0x0365: "利",
    0x0366: "履",
    0x0367: "理",
    0x0368: "里",
    0x0369: "陸",
    0x036A: "率",
    0x036B: "立",
    0x036C: "流",
    0x036D: "留",
    0x036E: "侶",
    0x036F: "旅",
    0x0370: "料",
    0x0371: "療",
    0x0372: "良",
    0x0373: "領",
    0x0374: "緑",
    0x0375: "淋",
    0x0376: "輪",
    0x0377: "路",
    0x0378: "労",
    0x0379: "牢",
    0x037A: "老",
    0x037B: "録",
    0x037C: "涙",
    0x037D: "左",
    0x037E: "差",
    0x037F: "砂",
    0x0380: "座",
    0x0381: "最",
    0x0382: "妻",
    0x0383: "才",
    0x0384: "採",
    0x0385: "済",
    0x0386: "祭",
    0x0387: "細",
    0x0388: "在",
    0x0389: "材",
    0x038A: "罪",
    0x038B: "財",
    0x038C: "咲",
    0x038D: "作",
    0x038E: "昨",
    0x038F: "礼",
    0x0390: "殺",
    0x0391: "参",
    0x0392: "散",
    0x0393: "産",
    0x0394: "斬",
    0x0395: "残",
    0x0396: "制",
    0x0397: "征",
    0x0398: "性",
    0x0399: "成",
    0x039A: "清",
    0x039B: "盛",
    0x039C: "精",
    0x039D: "聖",
    0x039E: "製",
    0x039F: "誠",
    0x03A0: "青",
    0x03A1: "静",
    0x03A2: "税",
    0x03A3: "席",
    0x03A4: "昔",
    0x03A5: "積",
    0x03A6: "責",
    0x03A7: "赤",
    0x03A8: "跡",
    0x03A9: "切",
    0x03AA: "接",
    0x03AB: "設",
    0x03AC: "節",
    0x03AD: "説",
    0x03AE: "雪",
    0x03AF: "絶",
    0x03B0: "舌",
    0x03B1: "先",
    0x03B2: "川",
    0x03B3: "戦",
    0x03B4: "泉",
    0x03B5: "洗",
    0x03B6: "染",
    0x03B7: "船",
    0x03B8: "選",
    0x03B9: "前",
    0x03BA: "然",
    0x03BB: "全",
    0x03BC: "使",
    0x03BD: "始",
    0x03BE: "姉",
    0x03BF: "姿",
    0x03C0: "子",
    0x03C1: "市",
    0x03C2: "志",
    0x03C3: "支",
    0x03C4: "私",
    0x03C5: "糸",
    0x03C6: "紙",
    0x03C7: "詩",
    0x03C8: "試",
    0x03C9: "飼",
    0x03CA: "歯",
    0x03CB: "事",
    0x03CC: "似",
    0x03CD: "字",
    0x03CE: "持",
    0x03CF: "時",
    0x03D0: "次",
    0x03D1: "治",
    0x03D2: "耳",
    0x03D3: "式",
    0x03D4: "識",
    0x03D5: "失",
    0x03D6: "室",
    0x03D7: "質",
    0x03D8: "実",
    0x03D9: "舎",
    0x03DA: "捨",
    0x03DB: "者",
    0x03DC: "謝",
    0x03DD: "邪",
    0x03DE: "若",
    0x03DF: "弱",
    0x03E0: "主",
    0x03E1: "取",
    0x03E2: "守",
    0x03E3: "手",
    0x03E4: "殊",
    0x03E5: "狩",
    0x03E6: "種",
    0x03E7: "酒",
    0x03E8: "受",
    0x03E9: "呪",
    0x03EA: "収",
    0x03EB: "修",
    0x03EC: "秀",
    0x03ED: "終",
    0x03EE: "習",
    0x03EF: "舟",
    0x03F0: "週",
    0x03F1: "集",
    0x03F2: "住",
    0x03F3: "十",
    0x03F4: "重",
    0x03F5: "宿",
    0x03F6: "祝",
    0x03F7: "出",
    0x03F8: "術",
    0x03F9: "春",
    0x03FA: "準",
    0x03FB: "盾",
    0x03FC: "処",
    0x03FD: "初",
    0x03FE: "所",
    0x03FF: "緒",
    0x0400: "書",
    0x0401: "助",
    0x0402: "女",
    0x0403: "除",
    0x0404: "勝",
    0x0405: "商",
    0x0406: "小",
    0x0407: "少",
    0x0408: "床",
    0x0409: "招",
    0x040A: "焼",
    0x040B: "省",
    0x040C: "章",
    0x040D: "笑",
    0x040E: "紹",
    0x040F: "証",
    0x0410: "賞",
    0x0411: "鐘",
    0x0412: "丈",
    0x0413: "乗",
    0x0414: "城",
    0x0415: "場",
    0x0416: "常",
    0x0417: "情",
    0x0418: "杖",
    0x0419: "状",
    0x041A: "色",
    0x041B: "食",
    0x041C: "信",
    0x041D: "寝",
    0x041E: "慎",
    0x041F: "新",
    0x0420: "森",
    0x0421: "深",
    0x0422: "真",
    0x0423: "神",
    0x0424: "親",
    0x0425: "身",
    0x0426: "進",
    0x0427: "素",
    0x0428: "組",
    0x0429: "僧",
    0x042A: "倉",
    0x042B: "想",
    0x042C: "早",
    0x042D: "巣",
    0x042E: "相",
    0x042F: "窓",
    0x0430: "草",
    0x0431: "装",
    0x0432: "走",
    0x0433: "送",
    0x0434: "像",
    0x0435: "増",
    0x0436: "贈",
    0x0437: "造",
    0x0438: "側",
    0x0439: "息",
    0x043A: "束",
    0x043B: "足",
    0x043C: "族",
    0x043D: "続",
    0x043E: "存",
    0x043F: "孫",
    0x0440: "村",
    0x0441: "吹",
    0x0442: "水",
    0x0443: "数",
    0x0444: "寸",
    0x0445: "他",
    0x0446: "多",
    0x0447: "太",
    0x0448: "打",
    0x0449: "体",
    0x044A: "対",
    0x044B: "待",
    0x044C: "袋",
    0x044D: "退",
    0x044E: "隊",
    0x044F: "代",
    0x0450: "台",
    0x0451: "大",
    0x0452: "題",
    0x0453: "滝",
    0x0454: "択",
    0x0455: "脱",
    0x0456: "棚",
    0x0457: "誰",
    0x0458: "単",
    0x0459: "探",
    0x045A: "炭",
    0x045B: "短",
    0x045C: "誕",
    0x045D: "団",
    0x045E: "断",
    0x045F: "段",
    0x0460: "男",
    0x0461: "談",
    0x0462: "低",
    0x0463: "定",
    0x0464: "帝",
    0x0465: "底",
    0x0466: "庭",
    0x0467: "弟",
    0x0468: "敵",
    0x0469: "的",
    0x046A: "笛",
    0x046B: "哲",
    0x046C: "鉄",
    0x046D: "店",
    0x046E: "貼",
    0x046F: "転",
    0x0470: "点",
    0x0471: "伝",
    0x0472: "殿",
    0x0473: "値",
    0x0474: "知",
    0x0475: "地",
    0x0476: "恥",
    0x0477: "置",
    0x0478: "茶",
    0x0479: "着",
    0x047A: "中",
    0x047B: "仲",
    0x047C: "忠",
    0x047D: "昼",
    0x047E: "柱",
    0x047F: "注",
    0x0480: "虫",
    0x0481: "張",
    0x0482: "挑",
    0x0483: "朝",
    0x0484: "町",
    0x0485: "調",
    0x0486: "長",
    0x0487: "頂",
    0x0488: "直",
    0x0489: "沈",
    0x048A: "吐",
    0x048B: "徒",
    0x048C: "渡",
    0x048D: "登",
    0x048E: "途",
    0x048F: "都",
    0x0490: "努",
    0x0491: "度",
    0x0492: "土",
    0x0493: "奴",
    0x0494: "怒",
    0x0495: "倒",
    0x0496: "党",
    0x0497: "凍",
    0x0498: "塔",
    0x0499: "島",
    0x049A: "投",
    0x049B: "東",
    0x049C: "答",
    0x049D: "統",
    0x049E: "到",
    0x049F: "討",
    0x04A0: "逃",
    0x04A1: "頭",
    0x04A2: "闘",
    0x04A3: "動",
    0x04A4: "堂",
    0x04A5: "洞",
    0x04A6: "胴",
    0x04A7: "道",
    0x04A8: "得",
    0x04A9: "特",
    0x04AA: "毒",
    0x04AB: "読",
    0x04AC: "突",
    0x04AD: "追",
    0x04AE: "痛",
    0x04AF: "通",
    0x04B0: "右",
    0x04B1: "運",
    0x04B2: "雲",
    0x04B3: "和",
    0x04B4: "話",
    0x04B5: "夜",
    0x04B6: "野",
    0x04B7: "役",
    0x04B8: "約",
    0x04B9: "薬",
    0x04BA: "躍",
    0x04BB: "予",
    0x04BC: "与",
    0x04BD: "預",
    0x04BE: "幼",
    0x04BF: "妖",
    0x04C0: "様",
    0x04C1: "洋",
    0x04C2: "熔",
    0x04C3: "用",
    0x04C4: "羊",
    0x04C5: "葉",
    0x04C6: "踊",
    0x04C7: "陽",
    0x04C8: "養",
    0x04C9: "欲",
    0x04CA: "翌",
    0x04CB: "油",
    0x04CC: "優",
    0x04CD: "勇",
    0x04CE: "友",
    0x04CF: "有",
    0x04D0: "由",
    0x04D1: "誘",
    0x04D2: "遊",
    0x04D3: "雄",
    0x04D4: "夕",
    0x04D5: "０",
    0x04D6: "２",
    0x04D7: "３",
    0x04D8: "４",
    0x04D9: "５",
    0x04DA: "６",
    0x04DB: "７",
    0x04DC: "８",
    0x04DD: "９",
    0x04DE: "ト",
    0x04DF: "リ",
    0x04E0: "１",
    0x04E1: "Ａ",
    0x04E2: "Ｈ",
    0x04E3: "Ｋ",
    0x04E4: "Ｎ",
    0x04E5: "Ｑ",
    0x04E6: "Ｒ",
    0x04E7: "Ｔ",
    0x04E8: "Ｖ",
    0x04E9: "Ｚ",
    0x04EA: "〓",
    0x04EB: "◇",
    0x04EC: "※",
    0x04ED: "き",
    0x04EE: "そ",
    0x04EF: "ち",
    0x04F0: "は",
    0x04F1: "ま",
    0x04F2: "も",
    0x04F3: "ら",
    0x04F4: "る",
    0x04F5: "ろ",
    0x04F6: "を",
    0x04F7: "ん",
    0x04F8: "ノ",
    0x04F9: "ヒ",
    0x04FA: "レ",
    0x04FB: "ワ",
    0x04FC: "Ｂ",
    0x04FD: "Ｅ",
    0x04FE: "Ｆ",
    0x04FF: "Ｌ",
    0x0500: "Ｏ",
    0x0501: "Ｐ",
    0x0502: "Ｓ",
    0x0503: "う",
    0x0504: "く",
    0x0505: "さ",
    0x0506: "し",
    0x0507: "じ",
    0x0508: "と",
    0x0509: "よ",
    0x050A: "り",
    0x050B: "ミ",
    0x050C: "ヲ",
    0x050D: "Ｃ",
    0x050E: "Ｄ",
    0x050F: "Ｇ",
    0x0510: "Ｊ",
    0x0511: "＊",  # TEST CASE
    0x0512: "メ",
    0x0513: "Ｉ",
    0x0514: "Ｍ",
    0x0515: "Ｗ",
    0x0516: "Ｘ",
    0x0517: "Ｙ",
    0x0518: "＋",
    0x0519: "ざ",
    0x051A: "ぢ",
    0x051B: "ど",
    0x051C: "ね",
    0x051D: "ひ",
    0x051E: "ふ",
    0x051F: "ぶ",
    0x0520: "み",
    0x0521: "め",
    0x0522: "れ",
    0x0523: "わ",
    0x0524: "セ",
    0x0525: "ム",
    0x0526: "ル",
    0x0527: "血",
    0x0528: "玉",
    0x0529: "五",
    0x052A: "口",
    0x052B: "工",
    0x052C: "王",
    0x052D: "皿",
    0x052E: "正",
    0x052F: "西",
    0x0530: "Ｕ",
    0x0531: "あ",
    0x0532: "え",
    0x0533: "お",
    0x0534: "か",
    0x0535: "け",
    0x0536: "す",
    0x0537: "せ",
    0x0538: "た",
    0x0539: "だ",
    0x053A: "な",
    0x053B: "べ",
    0x053C: "む",
    0x053D: "や",
    0x053E: "ゆ",
    0x053F: "〓",  # フォーン王の呪文用
    0x0540: "♪",
    0x0541: "ア",
    0x0542: "シ",
    0x0543: "ツ",
    0x0544: "テ",
    0x0545: "ラ",
    0x0546: "日",
    0x0547: "e",
    0x0548: "l",  # 要チェック
    0x0549: "(",
    0x054A: ")",
    0x054B: "、",
    0x054C: "。",
    0x054D: ".",  # 要チェック
    0x054E: "・",
    0x054F: "ぃ",
    0x0550: "？",
    0x0551: "！",
    0x0552: "◎",
    0x0553: "ウ",
    0x0554: "カ",
    0x0555: "‥",  # 要チェック
    0x0556: "々",
    0x0557: "×",
    0x0558: "ー",
    0x0559: "～",
    0x055A: "→",
    0x055B: "／",
    0x055C: "10",
    0x055D: "が",
    0x055E: "ぱ",
    0x055F: "ぴ",
    0x0560: "ぽ",
    0x0561: "ギ",
    0x0562: "ゲ",
    0x0563: "ゴ",
    0x0564: "ザ",
    0x0565: "ズ",
    0x0566: "ゾ",
    0x0567: "ダ",
    0x0568: "ヂ",
    0x0569: "ヅ",
    0x056A: "バ",
    0x056B: "パ",
    0x056C: "ビ",
    0x056D: "ブ",
    0x056E: "プ",
    0x056F: "ベ",
    0x0570: "ボ",
    0x0571: "ポ",
    0x0572: "温",
    0x0573: "…",
    0x0574: "”",
    0x0575: "》",
    0x0576: "『",
    0x0577: "「",
    0x0578: "」",
    0x0579: "』",
    0x057A: "ょ",
    0x057B: "ィ",
    0x057C: "─",  # TEST CASE
    0x057D: "へ",
    0x057E: "％",
    0x057F: "ぺ",
    0x0580: "医",
    0x0581: "〓",  # フォーン王の呪文用
    0x0582: "オ",
    0x0583: "キ",
    0x0584: "ケ",
    0x0585: "チ",
    0x0586: "ナ",
    0x0587: "月",
    0x0588: "巨",
    0x0589: "入",
    0x058A: "司",
    0x058B: "臣",
    0x058C: "人",
    0x058D: "★",
    0x058E: "円",
    0x058F: "園",
    0x0590: "馬",
    0x0591: "平",
    0x0592: "閉",
    0x0593: "辺",
    0x0594: "飛",
    0x0595: "匹",
    0x0596: "ぷ",
    0x0597: "亡",
    0x0598: "不",
    0x0599: "風",
    0x059A: "聞",
    0x059B: "異",
    0x059C: "因",
    0x059D: "〓",  # フォーン王の呪文用
    0x059E: "[よ]",
    0x059F: "下",
    0x05A0: "化",
    0x05A1: "可",
    0x05A2: "果",
    0x05A3: "画",
    0x05A4: "回",
    0x05A5: "開",
    0x05A6: "階",
    0x05A7: "間",
    0x05A8: "関",
    0x05A9: "ガ",
    0x05AA: "グ",
    0x05AB: "サ",
    0x05AC: "ネ",
    0x05AD: "ピ",
    0x05AE: "ホ",
    0x05AF: "ヤ",
    0x05B0: "ヴ",
    0x05B1: "兄",
    0x05B2: "穴",
    0x05B3: "元",
    0x05B4: "幻",
    0x05B5: "器",
    0x05B6: "帰",
    0x05B7: "記",
    0x05B8: "起",
    0x05B9: "局",
    0x05BA: "固",
    0x05BB: "戸",
    0x05BC: "故",
    0x05BD: "語",
    0x05BE: "皇",
    0x05BF: "国",
    0x05C0: "困",
    0x05C1: "苦",
    0x05C2: "具",
    0x05C3: "空",
    0x05C4: "軍",
    0x05C5: "面",
    0x05C6: "応",
    0x05C7: "恩",
    0x05C8: "両",
    0x05C9: "再",
    0x05CA: "山",
    0x05CB: "世",
    0x05CC: "星",
    0x05CD: "生",
    0x05CE: "声",
    0x05CF: "石",
    0x05D0: "千",
    0x05D1: "閃",
    0x05D2: "仕",
    0x05D3: "士",
    0x05D4: "思",
    0x05D5: "指",
    0x05D6: "止",
    0x05D7: "死",
    0x05D8: "車",
    0x05D9: "囚",
    0x05DA: "召",
    0x05DB: "上",
    0x05DC: "心",
    0x05DD: "図",
    0x05DE: "天",
    0x05DF: "田",
    0x05E0: "同",
    0x05E1: "羽",
    0x05E2: "雨",
    0x05E3: "要",
    0x05E4: "○",
    0x05E5: "ぁ",
    0x05E6: "ぉ",
    0x05E7: "ォ",
    0x05E8: "ッ",
    0x05E9: "ャ",
    0x05EA: "買",
    0x05EB: "泊",
    0x05EC: "罰",
    0x05ED: "崩",
    0x05EE: "冒",
    0x05EF: "員",
    0x05F0: "引",
    0x05F1: "〓",  # フォーン王の呪文用
    0x05F2: "〓",  # フォーン王の呪文用
    0x05F3: "〓",  # フォーン王の呪文用
    0x05F4: "加",
    0x05F5: "各",
    0x05F6: "枯",
    0x05F7: "后",
    0x05F8: "名",
    0x05F9: "明",
    0x05FA: "力",
    0x05FB: "師",
    0x05FC: "首",
    0x05FD: "消",
    0x05FE: "刃",
    0x05FF: "当",
    0x0600: "届",
    0x0601: "湧",
    0x0602: "白",
    0x0603: "甲",
    0x0604: "目",
    0x0605: "占",
    0x0606: "自",
    0x0607: "申",
    0x0608: "い",
    0x0609: "の",
    0x060A: "ハ",
    0x060B: "モ",
    0x060C: "二",
    0x060D: "ぅ",
    0x060E: "ぇ",
    0x060F: "ぎ",
    0x0610: "ぐ",
    0x0611: "ご",
    0x0612: "ず",
    0x0613: "ぞ",
    0x0614: "づ",
    0x0615: "ぬ",
    0x0616: "ば",
    0x0617: "び",
    0x0618: "ぼ",
    0x0619: "ジ",
    0x061A: "ゼ",
    0x061B: "デ",
    0x061C: "げ",
    0x061D: "ぜ",
    0x061E: "で",
    0x061F: "こ",
    0x0620: "っ",
    0x0621: "ゃ",
    0x0622: "ゅ",
    0x0623: "ァ",
    0x0624: "つ",
    0x0625: "エ",
    0x0626: "て",
    0x0627: "マ",
    0x0628: "ン",
    0x0629: "に",
    0x062A: "ほ",
    0x062B: "：",
    0x062C: "コ",
    0x062D: "ス",
    0x062E: "ソ",
    0x062F: "ヌ",
    0x0630: "フ",
    0x0631: "ロ",
    0x0632: "暮",
    0x0633: "一",
    0x0634: "〓",  # ハートマークなのでなんとかしたい
    0x0635: "〓",  # フォーン王の呪文用
    0x0636: "イ",
    0x0637: "ク",
    0x0638: "タ",
    0x0639: "ド",
    0x063A: "ェ",
    0x063B: "ニ",
    0x063C: "ユ",
    0x063D: "ヘ",
    0x063E: "ペ",
    0x063F: "鍵",
    0x0640: "極",
    0x0641: "公",
    0x0642: "滅",
    0x0643: "職",
    0x0644: "ュ",
    0x0645: "ョ",
    0x0646: "ヨ",
    0x0647: "了",
}
