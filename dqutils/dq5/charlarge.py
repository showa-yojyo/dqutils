
"""dqutils.dq5.charlarge - The dictionary of large size characters.
"""

CHARMAP = {
    #0x0000:"亜",  # dqviewer では「亜」だが、うまくいかない
    0x0000:" ",
    0x0001:"園",
    0x0002:"馬",
    0x0003:"平",
    0x0004:"閉",
    0x0005:"辺",
    0x0006:"飛",
    0x0007:"匹",
    0x0008:"ぷ",
    0x0009:"亡",
    0x000A:"不",
    0x000B:"風",
    0x000C:"聞",
    0x000D:"囲",
    0x000E:"因",
    0x000F:"院",
    0x0010:"下",
    0x0011:"化",
    0x0012:"可",
    0x0013:"果",
    0x0014:"回",
    0x0015:"灰",
    0x0016:"開",
    0x0017:"階",
    0x0018:"間",
    0x0019:"ガ",
    0x001A:"グ",
    0x001B:"サ",
    0x001C:"ネ",
    0x001D:"ピ",
    0x001E:"ホ",
    0x001F:"ヤ",
    0x0020:"ヴ",
    0x0021:"兄",
    0x0022:"穴",
    0x0023:"元",
    0x0024:"幻",
    0x0025:"器",
    0x0026:"帰",
    0x0027:"記",
    0x0028:"起",
    0x0029:"局",
    0x002A:"故",
    0x002B:"語",
    0x002C:"国",
    0x002D:"困",
    0x002E:"苦",
    0x002F:"具",
    0x0030:"空",
    0x0031:"面",
    0x0032:"恩",
    0x0033:"両",
    0x0034:"再",
    0x0035:"山",
    0x0036:"世",
    0x0037:"星",
    0x0038:"生",
    0x0039:"声",
    0x003A:"石",
    0x003B:"仕",
    0x003C:"士",
    0x003D:"思",
    0x003E:"指",
    0x003F:"止",
    0x0040:"死",
    0x0041:"車",
    0x0042:"囚",
    0x0043:"上",
    0x0044:"冗",
    0x0045:"心",
    0x0046:"図",
    0x0047:"天",
    0x0048:"田",
    0x0049:"同",
    0x004A:"要",
    0x004B:"愛",
    0x004C:"悪",
    0x004D:"安",
    0x004E:"暗",
    0x004F:"案",
    0x0050:"闇",
    0x0051:"影",
    0x0052:"栄",
    0x0053:"永",
    0x0054:"英",
    0x0055:"宴",
    0x0056:"演",
    0x0057:"炎",
    0x0058:"煙",
    0x0059:"遠",
    0x005A:"派",
    0x005B:"破",
    0x005C:"敗",
    0x005D:"杯",
    0x005E:"背",
    0x005F:"配",
    0x0060:"倍",
    0x0061:"売",
    0x0062:"漠",
    0x0063:"箱",
    0x0064:"畑",
    0x0065:"発",
    0x0066:"抜",
    0x0067:"判",
    0x0068:"半",
    0x0069:"反",
    0x006A:"帆",
    0x006B:"板",
    0x006C:"犯",
    0x006D:"晩",
    0x006E:"番",
    0x006F:"兵",
    0x0070:"別",
    0x0071:"変",
    0x0072:"返",
    0x0073:"便",
    0x0074:"勉",
    0x0075:"妃",
    0x0076:"彼",
    0x0077:"悲",
    0x0078:"扉",
    0x0079:"疲",
    0x007A:"秘",
    0x007B:"非",
    0x007C:"備",
    0x007D:"美",
    0x007E:"必",
    0x007F:"姫",
    0x0080:"百",
    0x0081:"氷",
    0x0082:"表",
    0x0083:"評",
    0x0084:"描",
    0x0085:"病",
    0x0086:"品",
    0x0087:"貧",
    0x0088:"歩",
    0x0089:"募",
    0x008A:"墓",
    0x008B:"母",
    0x008C:"報",
    0x008D:"宝",
    0x008E:"抱",
    0x008F:"放",
    0x0090:"方",
    0x0091:"法",
    0x0092:"訪",
    0x0093:"豊",
    0x0094:"坊",
    0x0095:"忘",
    0x0096:"房",
    0x0097:"望",
    0x0098:"防",
    0x0099:"北",
    0x009A:"本",
    0x009B:"付",
    0x009C:"夫",
    0x009D:"婦",
    0x009E:"敷",
    0x009F:"普",
    0x00A0:"浮",
    0x00A1:"父",
    0x00A2:"負",
    0x00A3:"附",
    0x00A4:"武",
    0x00A5:"舞",
    0x00A6:"部",
    0x00A7:"封",
    0x00A8:"復",
    0x00A9:"服",
    0x00AA:"福",
    0x00AB:"腹",
    0x00AC:"払",
    0x00AD:"物",
    0x00AE:"分",
    0x00AF:"文",
    0x00B0:"以",
    0x00B1:"位",
    0x00B2:"偉",
    0x00B3:"意",
    0x00B4:"移",
    0x00B5:"違",
    0x00B6:"井",
    0x00B7:"育",
    0x00B8:"印",
    0x00B9:"飲",
    0x00BA:"何",
    0x00BB:"夏",
    0x00BC:"嫁",
    0x00BD:"家",
    0x00BE:"歌",
    0x00BF:"火",
    0x00C0:"花",
    0x00C1:"苛",
    0x00C2:"荷",
    0x00C3:"華",
    0x00C4:"我",
    0x00C5:"会",
    0x00C6:"解",
    0x00C7:"快",
    0x00C8:"怪",
    0x00C9:"悔",
    0x00CA:"改",
    0x00CB:"海",
    0x00CC:"界",
    0x00CD:"皆",
    0x00CE:"絵",
    0x00CF:"外",
    0x00D0:"格",
    0x00D1:"確",
    0x00D2:"覚",
    0x00D3:"学",
    0x00D4:"楽",
    0x00D5:"恰",
    0x00D6:"活",
    0x00D7:"寒",
    0x00D8:"完",
    0x00D9:"官",
    0x00DA:"感",
    0x00DB:"換",
    0x00DC:"汗",
    0x00DD:"甘",
    0x00DE:"看",
    0x00DF:"肝",
    0x00E0:"館",
    0x00E1:"丸",
    0x00E2:"岩",
    0x00E3:"顔",
    0x00E4:"願",
    0x00E5:"刑",
    0x00E6:"形",
    0x00E7:"恵",
    0x00E8:"敬",
    0x00E9:"景",
    0x00EA:"系",
    0x00EB:"経",
    0x00EC:"継",
    0x00ED:"計",
    0x00EE:"軽",
    0x00EF:"決",
    0x00F0:"結",
    0x00F1:"件",
    0x00F2:"剣",
    0x00F3:"堅",
    0x00F4:"建",
    0x00F5:"権",
    0x00F6:"犬",
    0x00F7:"研",
    0x00F8:"見",
    0x00F9:"険",
    0x00FA:"験",
    0x00FB:"原",
    0x00FC:"現",
    0x00FD:"言",
    0x00FE:"限",
    0x00FF:"危",
    0x0100:"奇",
    0x0101:"寄",
    0x0102:"希",
    0x0103:"忌",
    0x0104:"期",
    0x0105:"機",
    0x0106:"気",
    0x0107:"祈",
    0x0108:"季",
    0x0109:"貴",
    0x010A:"儀",
    0x010B:"技",
    0x010C:"犠",
    0x010D:"議",
    0x010E:"客",
    0x010F:"久",
    0x0110:"休",
    0x0111:"急",
    0x0112:"救",
    0x0113:"求",
    0x0114:"泣",
    0x0115:"究",
    0x0116:"去",
    0x0117:"許",
    0x0118:"供",
    0x0119:"競",
    0x011A:"共",
    0x011B:"叫",
    0x011C:"強",
    0x011D:"教",
    0x011E:"橋",
    0x011F:"胸",
    0x0120:"鏡",
    0x0121:"業",
    0x0122:"曲",
    0x0123:"禁",
    0x0124:"筋",
    0x0125:"近",
    0x0126:"金",
    0x0127:"古",
    0x0128:"呼",
    0x0129:"庫",
    0x012A:"湖",
    0x012B:"雇",
    0x012C:"後",
    0x012D:"御",
    0x012E:"護",
    0x012F:"交",
    0x0130:"光",
    0x0131:"功",
    0x0132:"効",
    0x0133:"向",
    0x0134:"好",
    0x0135:"幸",
    0x0136:"広",
    0x0137:"抗",
    0x0138:"攻",
    0x0139:"港",
    0x013A:"考",
    0x013B:"航",
    0x013C:"荒",
    0x013D:"行",
    0x013E:"降",
    0x013F:"高",
    0x0140:"合",
    0x0141:"豪",
    0x0142:"告",
    0x0143:"酷",
    0x0144:"黒",
    0x0145:"獄",
    0x0146:"腰",
    0x0147:"骨",
    0x0148:"頃",
    0x0149:"今",
    0x014A:"婚",
    0x014B:"根",
    0x014C:"句",
    0x014D:"屈",
    0x014E:"君",
    0x014F:"訓",
    0x0150:"魔",
    0x0151:"埋",
    0x0152:"妹",
    0x0153:"枚",
    0x0154:"毎",
    0x0155:"末",
    0x0156:"満",
    0x0157:"命",
    0x0158:"迷",
    0x0159:"鳴",
    0x015A:"味",
    0x015B:"未",
    0x015C:"密",
    0x015D:"妙",
    0x015E:"民",
    0x015F:"眠",
    0x0160:"戻",
    0x0161:"問",
    0x0162:"紋",
    0x0163:"門",
    0x0164:"夢",
    0x0165:"無",
    0x0166:"娘",
    0x0167:"内",
    0x0168:"謎",
    0x0169:"南",
    0x016A:"熱",
    0x016B:"年",
    0x016C:"念",
    0x016D:"尼",
    0x016E:"任",
    0x016F:"認",
    0x0170:"悩",
    0x0171:"能",
    0x0172:"農",
    0x0173:"奥",
    0x0174:"押",
    0x0175:"横",
    0x0176:"黄",
    0x0177:"屋",
    0x0178:"音",
    0x0179:"来",
    0x017A:"頼",
    0x017B:"絡",
    0x017C:"落",
    0x017D:"令",
    0x017E:"冷",
    0x017F:"礼",
    0x0180:"歴",
    0x0181:"列",
    0x0182:"恋",
    0x0183:"練",
    0x0184:"連",
    0x0185:"利",
    0x0186:"理",
    0x0187:"陸",
    0x0188:"率",
    0x0189:"立",
    0x018A:"流",
    0x018B:"留",
    0x018C:"竜",
    0x018D:"旅",
    0x018E:"料",
    0x018F:"良",
    0x0190:"量",
    0x0191:"淋",
    0x0192:"輪",
    0x0193:"路",
    0x0194:"労",
    0x0195:"牢",
    0x0196:"老",
    0x0197:"録",
    0x0198:"涙",
    0x0199:"砂",
    0x019A:"座",
    0x019B:"最",
    0x019C:"妻",
    0x019D:"才",
    0x019E:"細",
    0x019F:"在",
    0x01A0:"材",
    0x01A1:"罪",
    0x01A2:"財",
    0x01A3:"作",
    0x01A4:"昨",
    0x01A5:"札",
    0x01A6:"殺",
    0x01A7:"参",
    0x01A8:"散",
    0x01A9:"産",
    0x01AA:"残",
    0x01AB:"征",
    0x01AC:"性",
    0x01AD:"成",
    0x01AE:"晴",
    0x01AF:"清",
    0x01B0:"牲",
    0x01B1:"精",
    0x01B2:"聖",
    0x01B3:"誓",
    0x01B4:"青",
    0x01B5:"静",
    0x01B6:"税",
    0x01B7:"昔",
    0x01B8:"責",
    0x01B9:"赤",
    0x01BA:"切",
    0x01BB:"節",
    0x01BC:"説",
    0x01BD:"雪",
    0x01BE:"絶",
    0x01BF:"先",
    0x01C0:"専",
    0x01C1:"川",
    0x01C2:"戦",
    0x01C3:"泉",
    0x01C4:"潜",
    0x01C5:"船",
    0x01C6:"選",
    0x01C7:"前",
    0x01C8:"善",
    0x01C9:"然",
    0x01CA:"全",
    0x01CB:"使",
    0x01CC:"史",
    0x01CD:"始",
    0x01CE:"姉",
    0x01CF:"姿",
    0x01D0:"子",
    0x01D1:"志",
    0x01D2:"私",
    0x01D3:"糸",
    0x01D4:"紙",
    0x01D5:"至",
    0x01D6:"詩",
    0x01D7:"試",
    0x01D8:"飼",
    0x01D9:"事",
    0x01DA:"似",
    0x01DB:"字",
    0x01DC:"持",
    0x01DD:"時",
    0x01DE:"次",
    0x01DF:"治",
    0x01E0:"耳",
    0x01E1:"式",
    0x01E2:"失",
    0x01E3:"室",
    0x01E4:"実",
    0x01E5:"舎",
    0x01E6:"捨",
    0x01E7:"者",
    0x01E8:"謝",
    0x01E9:"邪",
    0x01EA:"若",
    0x01EB:"弱",
    0x01EC:"主",
    0x01ED:"取",
    0x01EE:"守",
    0x01EF:"手",
    0x01F0:"酒",
    0x01F1:"受",
    0x01F2:"呪",
    0x01F3:"樹",
    0x01F4:"収",
    0x01F5:"修",
    0x01F6:"拾",
    0x01F7:"終",
    0x01F8:"習",
    0x01F9:"舟",
    0x01FA:"集",
    0x01FB:"住",
    0x01FC:"十",
    0x01FD:"重",
    0x01FE:"宿",
    0x01FF:"祝",
    0x0200:"出",
    0x0201:"春",
    0x0202:"準",
    0x0203:"盾",
    0x0204:"純",
    0x0205:"処",
    0x0206:"初",
    0x0207:"所",
    0x0208:"暑",
    0x0209:"緒",
    0x020A:"書",
    0x020B:"助",
    0x020C:"女",
    0x020D:"勝",
    0x020E:"商",
    0x020F:"小",
    0x0210:"少",
    0x0211:"承",
    0x0212:"招",
    0x0213:"焼",
    0x0214:"照",
    0x0215:"章",
    0x0216:"笑",
    0x0217:"粧",
    0x0218:"証",
    0x0219:"丈",
    0x021A:"乗",
    0x021B:"城",
    0x021C:"場",
    0x021D:"嬢",
    0x021E:"情",
    0x021F:"条",
    0x0220:"杖",
    0x0221:"状",
    0x0222:"色",
    0x0223:"食",
    0x0224:"信",
    0x0225:"寝",
    0x0226:"新",
    0x0227:"森",
    0x0228:"深",
    0x0229:"真",
    0x022A:"神",
    0x022B:"親",
    0x022C:"身",
    0x022D:"進",
    0x022E:"祖",
    0x022F:"素",
    0x0230:"僧",
    0x0231:"倉",
    0x0232:"秦",
    0x0233:"捜",
    0x0234:"早",
    0x0235:"争",
    0x0236:"相",
    0x0237:"草",
    0x0238:"荘",
    0x0239:"装",
    0x023A:"走",
    0x023B:"送",
    0x023C:"騒",
    0x023D:"像",
    0x023E:"憎",
    0x023F:"側",
    0x0240:"即",
    0x0241:"息",
    0x0242:"束",
    0x0243:"足",
    0x0244:"族",
    0x0245:"続",
    0x0246:"存",
    0x0247:"孫",
    0x0248:"尊",
    0x0249:"村",
    0x024A:"吹",
    0x024B:"水",
    0x024C:"酔",
    0x024D:"数",
    0x024E:"他",
    0x024F:"多",
    0x0250:"太",
    0x0251:"打",
    0x0252:"体",
    0x0253:"対",
    0x0254:"待",
    0x0255:"泰",
    0x0256:"袋",
    0x0257:"貸",
    0x0258:"退",
    0x0259:"代",
    0x025A:"台",
    0x025B:"大",
    0x025C:"第",
    0x025D:"題",
    0x025E:"滝",
    0x025F:"誰",
    0x0260:"単",
    0x0261:"探",
    0x0262:"誕",
    0x0263:"団",
    0x0264:"断",
    0x0265:"段",
    0x0266:"男",
    0x0267:"談",
    0x0268:"亭",
    0x0269:"帝",
    0x026A:"底",
    0x026B:"庭",
    0x026C:"弟",
    0x026D:"敵",
    0x026E:"的",
    0x026F:"鉄",
    0x0270:"店",
    0x0271:"点",
    0x0272:"伝",
    0x0273:"殿",
    0x0274:"値",
    0x0275:"知",
    0x0276:"地",
    0x0277:"置",
    0x0278:"茶",
    0x0279:"着",
    0x027A:"中",
    0x027B:"仲",
    0x027C:"忠",
    0x027D:"昼",
    0x027E:"注",
    0x027F:"虫",
    0x0280:"兆",
    0x0281:"帳",
    0x0282:"張",
    0x0283:"挑",
    0x0284:"朝",
    0x0285:"町",
    0x0286:"調",
    0x0287:"長",
    0x0288:"頂",
    0x0289:"鳥",
    0x028A:"直",
    0x028B:"沈",
    0x028C:"渡",
    0x028D:"途",
    0x028E:"都",
    0x028F:"度",
    0x0290:"土",
    0x0291:"奴",
    0x0292:"倒",
    0x0293:"冬",
    0x0294:"凍",
    0x0295:"塔",
    0x0296:"島",
    0x0297:"投",
    0x0298:"東",
    0x0299:"盗",
    0x029A:"湯",
    0x029B:"灯",
    0x029C:"等",
    0x029D:"答",
    0x029E:"統",
    0x029F:"逃",
    0x02A0:"頭",
    0x02A1:"闘",
    0x02A2:"働",
    0x02A3:"動",
    0x02A4:"導",
    0x02A5:"洞",
    0x02A6:"道",
    0x02A7:"得",
    0x02A8:"特",
    0x02A9:"毒",
    0x02AA:"読",
    0x02AB:"突",
    0x02AC:"追",
    0x02AD:"通",
    0x02AE:"右",
    0x02AF:"運",
    0x02B0:"雲",
    0x02B1:"和",
    0x02B2:"話",
    0x02B3:"惑",
    0x02B4:"腕",
    0x02B5:"夜",
    0x02B6:"野",
    0x02B7:"役",
    0x02B8:"約",
    0x02B9:"薬",
    0x02BA:"予",
    0x02BB:"余",
    0x02BC:"与",
    0x02BD:"預",
    0x02BE:"幼",
    0x02BF:"妖",
    0x02C0:"様",
    0x02C1:"溶",
    0x02C2:"用",
    0x02C3:"羊",
    0x02C4:"葉",
    0x02C5:"踊",
    0x02C6:"養",
    0x02C7:"欲",
    0x02C8:"油",
    0x02C9:"勇",
    0x02CA:"友",
    0x02CB:"有",
    0x02CC:"由",
    0x02CD:"裕",
    0x02CE:"遊",
    0x02CF:"雄",
    0x02D0:"夕",
    0x02D1:"０",
    0x02D2:"２",
    0x02D3:"３",
    0x02D4:"４",
    0x02D5:"５",
    0x02D6:"６",
    0x02D7:"７",
    0x02D8:"８",
    0x02D9:"９",
    0x02DA:"＄",
    0x02DB:"ト",
    0x02DC:"リ",
    0x02DD:"１",
    0x02DE:"Ａ",
    0x02DF:"Ｈ",
    0x02E0:"Ｋ",
    0x02E1:"Ｑ",
    0x02E2:"Ｔ",
    0x02E3:"Ｖ",
    0x02E4:"ｈ",
    0x02E5:"き",
    0x02E6:"そ",
    0x02E7:"ち",
    0x02E8:"は",
    0x02E9:"ま",
    0x02EA:"も",
    0x02EB:"ら",
    0x02EC:"る",
    0x02ED:"ろ",
    0x02EE:"を",
    0x02EF:"ん",
    0x02F0:"ノ",
    0x02F1:"ヒ",
    0x02F2:"レ",
    0x02F3:"ワ",
    0x02F4:"Ｂ",
    0x02F5:"Ｅ",
    0x02F6:"Ｆ",
    0x02F7:"Ｌ",
    0x02F8:"Ｏ",
    0x02F9:"Ｐ",
    0x02FA:"Ｓ",
    0x02FB:"ｂ",
    0x02FC:"ｄ",
    0x02FD:"う",
    0x02FE:"く",
    0x02FF:"さ",
    0x0300:"し",
    0x0301:"じ",
    0x0302:"と",
    0x0303:"よ",
    0x0304:"り",
    0x0305:"ミ",
    0x0306:"ヲ",
    0x0307:"Ｃ",
    0x0308:"Ｄ",
    0x0309:"Ｇ",
    0x030A:"＊",
    0x030B:"メ",
    0x030C:"Ｍ",
    0x030D:"Ｗ",
    0x030E:"Ｘ",
    0x030F:"Ｙ",
    0x0310:"＋",
    0x0311:"ざ",
    0x0312:"ぢ",
    0x0313:"ど",
    0x0314:"ね",
    0x0315:"ひ",
    0x0316:"ふ",
    0x0317:"ぶ",
    0x0318:"み",
    0x0319:"め",
    0x031A:"れ",
    0x031B:"わ",
    0x031C:"セ",
    0x031D:"ム",
    0x031E:"ル",
    0x031F:"血",
    0x0320:"玉",
    0x0321:"口",
    0x0322:"王",
    0x0323:"皿",
    0x0324:"正",
    0x0325:"西",
    0x0326:"Ｕ",
    0x0327:"あ",
    0x0328:"え",
    0x0329:"お",
    0x032A:"か",
    0x032B:"け",
    0x032C:"す",
    0x032D:"せ",
    0x032E:"た",
    0x032F:"だ",
    0x0330:"な",
    0x0331:"べ",
    0x0332:"む",
    0x0333:"や",
    0x0334:"ゆ",
    0x0335:"ア",
    0x0336:"シ",
    0x0337:"ツ",
    0x0338:"テ",
    0x0339:"ラ",
    0x033A:"日",
    0x033B:"ａ",
    0x033C:"ｏ",
    0x033D:"っ",
    0x033E:"ゃ",
    0x033F:"ゅ",
    0x0340:"ァ",
    0x0341:"ｃ",
    0x0342:"ｅ",
    0x0343:"ｉ",
    0x0344:"ｌ",
    0x0345:"ｊ",
    0x0346:"“",
    0x0347:"”",
    0x0348:"ｍ",
    0x0349:"ｎ",
    0x034A:"ｕ",
    0x034B:"ｐ",
    0x034C:"こ",
    0x034D:"ｒ",
    0x034E:"ｓ",
    0x034F:"ｔ",
    0x0350:"々",
    0x0351:"v",
    0x0352:"ヨ",
    0x0353:"w",
    0x0354:"つ",
    0x0355:"エ",
    0x0356:"。",
    0x0357:"，",
    0x0358:"・",
    0x0359:"？",
    0x035A:"！",
    0x035B:"＃",
    0x035C:"＠",
    0x035D:"ウ",
    0x035E:"カ",
    0x035F:"＠",   # 要チェック
    0x0360:"ー",
    0x0361:"{",
    0x0362:"}",
    0x0363:"「",
    0x0364:"―",
    0x0365:"ヘ",
    0x0366:"…",
    0x0367:"＜",
    0x0368:"＞",
    0x0369:"％",
    0x036A:"ぺ",
    0x036B:"医",
    0x036C:"オ",
    0x036D:"キ",
    0x036E:"ケ",
    0x036F:"チ",
    0x0370:"ナ",
    0x0371:"月",
    0x0372:"巨",
    0x0373:"入",
    0x0374:"乙",
    0x0375:"臣",
    0x0376:"人",
    0x0377:"＆",
    0x0378:"イ",
    0x0379:"ク",
    0x037A:"タ",
    0x037B:"ド",
    0x037C:"買",
    0x037D:"泊",
    0x037E:"罰",
    0x037F:"冒",
    0x0380:"員",
    0x0381:"引",
    0x0382:"加",
    0x0383:"賀",
    0x0384:"枯",
    0x0385:"后",
    0x0386:"名",
    0x0387:"明",
    0x0388:"力",
    0x0389:"師",
    0x038A:"消",
    0x038B:"刃",
    0x038C:"当",
    0x038D:"届",
    0x038E:"白",
    0x038F:"目",
    0x0390:"呂",
    0x0391:"占",
    0x0392:"自",
    0x0393:"申",
    0x0394:"ぁ",
    0x0395:"ォ",
    0x0396:"ッ",
    0x0397:"ャ",
    0x0398:"い",
    0x0399:"の",
    0x039A:"ハ",
    0x039B:"モ",
    0x039C:"ニ",
    0x039D:"が",
    0x039E:"ぱ",
    0x039F:"ぴ",
    0x03A0:"ぽ",
    0x03A1:"ギ",
    0x03A2:"ゲ",
    0x03A3:"ゴ",
    0x03A4:"ザ",
    0x03A5:"ズ",
    0x03A6:"ゾ",
    0x03A7:"ダ",
    0x03A8:"ヂ",
    0x03A9:"ヅ",
    0x03AA:"バ",
    0x03AB:"パ",
    0x03AC:"ビ",
    0x03AD:"ブ",
    0x03AE:"プ",
    0x03AF:"ベ",
    0x03B0:"ボ",
    0x03B1:"ポ",
    0x03B2:"温",
    0x03B3:"ぎ",
    0x03B4:"ぐ",
    0x03B5:"ご",
    0x03B6:"ず",
    0x03B7:"ぞ",
    0x03B8:"づ",
    0x03B9:"ぬ",
    0x03BA:"ば",
    0x03BB:"び",
    0x03BC:"ぼ",
    0x03BD:"ジ",
    0x03BE:"ゼ",
    0x03BF:"デ",
    0x03C0:"げ",
    0x03C1:"ぜ",
    0x03C2:"で",
    0x03C3:"て",
    0x03C4:"マ",
    0x03C5:"ン",
    0x03C6:"に",
    0x03C7:"ほ",
    0x03C8:"コ",
    0x03C9:"ス",
    0x03CA:"ソ",
    0x03CB:"ヌ",
    0x03CC:"フ",
    0x03CD:"ロ",
    0x03CE:"ょ",
    0x03CF:"ィ",
    0x03D0:"暮",
    0x03D1:"一",
    0x03D2:"ェ",
    0x03D3:"ニ",
    0x03D4:"ユ",
    0x03D5:"ヘ",
    0x03D6:"ペ",
    0x03D7:"滅",
    0x03D8:"猛",
    0x03D9:"ュ",
    0x03DA:"ョ",
}
