define I = Character('我', color="#4E342E")#定义人物
define npc = Character(None, kind=adv)
define jitou =Character('靳桐',color="#F57F17")
define bw = Character('冰', color="#888888")
define jige = Character('鸡哥', color="#4a90e2")
define wz = Character('王子', color="#50e3c2")
define zmw = Character('明薇', color="#ff6a4c9c")
define qf = Character('秋风', color="#f5a623")
define zb = Character('烛悦', color="#ff4c8dae")


image blackbg = Solid("#000000") #定义黑色背景
image whitebg = Solid("#FFFFFF") #定义白色背景

### 层叠式图像定义

layeredimage jitou:
    group pose auto default "normal"
    group cloth auto default "normal_maoyi"
    group expression auto default "normal"

transform shake_side: #定义侧向震动效果
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -5
    linear 0.1 xoffset 5
    linear 0.1 xoffset 0
    repeat

transform nod: #定义点头效果
    yoffset 0  # 初始位置
    easein 0.1 yoffset 15  # 向下移动（点头）
    easeout 0.1 yoffset 0  # 回到原位
    # 可以重复多次来模拟多次点头

transform p1080p:#定义图片为1080p
    size (1920, 1080)  # 设置为1080p全高清分辨率
    xalign 0.5         # 水平居中
    yalign 0.5         # 垂直居中

transform hit(direction=1, intensity=100, shake_intensity=10):
    # 主撞击动作
    parallel:
        easeout 0.1 xoffset direction * intensity yoffset -20
        easein 0.3 xoffset 0 yoffset 0
    parallel:
        easeout 0.1 rotate direction * 15
        easein 0.3 rotate 0
    # 撞击后的轻微震动
    parallel:
        ease 0.05 xoffset shake_intensity
        ease 0.05 xoffset -shake_intensity
        ease 0.05 xoffset shake_intensity/2
        ease 0.05 xoffset -shake_intensity/2
        ease 0.05 xoffset 0

transform hit_three:
    # 第一阶段：轻微后仰
    parallel:
        easeout 0.12 xoffset 25 yoffset -15
        easein 0.18 xoffset 0 yoffset 0
    parallel:
        easeout 0.12 rotate -6
        easein 0.18 rotate 0
    
    # 第二阶段：短促震动（3次）
    block:
        parallel:
            ease 0.06 xoffset 4 yoffset 2
            ease 0.06 xoffset -3 yoffset -1
            ease 0.06 xoffset 2 yoffset 1
            ease 0.06 xoffset -1 yoffset 0
            ease 0.06 xoffset 0 yoffset 0
    
    # 第三阶段：细微余震（逐渐减弱）
    block:
        parallel:
            ease 0.1 xoffset 2 yoffset 1 rotate 1
            ease 0.15 xoffset -1 yoffset -0.5 rotate -0.5
            ease 0.2 xoffset 0 yoffset 0 rotate 0


label start:
    window hide
    play sound alarm
    pause
    window show
    npc "（闹钟声）"
    stop sound fadeout 0.5
    scene bedroom at p1080p         #使用1080p函数
    with Dissolve(1.0)

    I "哈～～～～睡得真爽"
    npc "我随手抓过枕边的手机，屏幕亮起的瞬间，瞳孔微缩，手指顿在屏幕上"
    I "不是哥们你逗我呢，已经十一点了"
    I "不好！今天中午是高中同学聚会啊！"
    npc "我踩着拖鞋冲到衣柜前，柜门拉开时掉出一件白衬衫，单手套外套，另一只手抓过沙发上的深灰背包"
    I "（对着穿衣镜扯平衣领）得赶紧了，可别迟到了"

    scene homeclose at p1080p
    with dissolve
    npc "我抓起玄关钥匙，关门时回头瞥向挂钟，门 “咔嗒” 锁上"
    I "话说从毕业到现在，都好几年没见大家了…… 有点期待，不知道大家现在都怎么样了"

    scene homeopen at p1080p
    with dissolve
    play sound dianti
    npc "（电梯声）"
    I "诶，电梯今天怎么这么快"
    I "顺便把垃圾倒了吧"

    scene street at p1080p
    with fade
    play music relax volume 0.6 fadein 1.0
    I "呼…… 可算快到了，应该赶得上吧"
    npc "我正要过公路时，左肩突然被撞了一下"
    show jitou surprise surprise_maoyi surprise at hit_three,center:
        ypos 1700
        zoom 0.3
    with fade
    jitou "啊~~~{w}\n对...对...对不起！{w}\n我没看路！"
    I "啊...没事"
    I "欸？{w}\n是锦桐吗，好久不见了"
    show jitou at center:
        ypos 1700
        zoom 0.3
    jitou "欸...欸？\n好巧啊，在这撞到你"
    show jitou at center:
        ypos 1700
        zoom 0.3
    I "(这么多年过去，她还是老样子…… 不过聚会快开始了，先进去再叙旧吧)"
    I "我们赶紧进去吧，大家应该都到得差不多了"
    jitou "嗯，我们走吧"
    
    scene tablenofood at p1080p
    with fade
    show jige at center:
        ypos 2100
        zoom 0.3
    with dissolve
    jige "(看了看手表)"
    jige "时间差不多了，人都到齐了吗"
    I "好久不见，鸡哥"
    jige "你们终于到了，其他人呢"

    show jige decade_huanbao at left:
        ypos 2100
        xpos 200
        zoom 0.3
    with dissolve
    show wz decade_normal at right:
        ypos 1900  
        zoom 0.7
    with dissolve
    wz "等一下，鸡霸发消息了"
    wz "他说他那边堵车堵得厉害，短时间赶不过来，让我们先开始。"
    jige "行，那就先这样吧，我去跟服务员说先上菜"
    hide jige decade_huanbao
    with dissolve
    npc "鸡哥说完就站起身出门了"
    wz "我出去来一根，等下再聊"
    hide wz decade_normal
    with dissolve
    npc "这时，一道熟悉的声音传来"
    show bw dress_smile at center:
        ypos 1900
        zoom 0.3
    with Dissolve(1.0)
    bw "嘿，好久不见啊"
    bw "这几年过得怎么样？工作顺利吗？"
    I "不太好，最近刚失业，找了快一个月工作了{w}\n现在就业市场竞争太激烈，工作挺难找的"
    bw "看来大家都不容易啊"
    bw "明薇最近也不太顺利，最近公司裁员，她差点也被裁掉"

    show zmw decade_normal at left:
        ypos 1900
        zoom 0.7
    with dissolve
    zmw "(从旁边经过，听到自己的名字，停下脚步)"
    zmw "(想说句话可又不知道该说什么)"
    zmw "……"
    I "明薇，坐这里吧，大家都很想你呢"
    zmw "不了，我坐那边就好"
    hide zmw decade_normal
    with dissolve
    npc "我和王冰相视一笑，毕竟明薇以前总是这样，性格有点孤僻"
    hide bw dress_smile
    with dissolve
    npc "后来大家聊起了各自的近况，气氛渐渐热络起来"
    npc "刚才出去抽烟的王子也回来加入了谈话"
    npc "听说他最近在做自由职业，接一些平面设计的单子"

    I "王子你还会设计，说白了就是画本子吧"
    show wz decade_happy at center:
        ypos 1900
        zoom 0.6
    wz "哈哈，说得没错，不过我画的可比其他同人本子专业多了"
    npc "这倒是真的，王子画的本子曾经也是上过不少展会的"
    npc "不过要问我是怎么知道的{w}\n那就不方便透露了"

    npc "(十分钟后)"
    scene tablefood at p1080p
    with dissolve
    jige "菜终于上齐了，大家可以开饭了"
    npc "我坐下来，喝着茶的同时看着这些许久未见的老朋友们"
    npc "(餐桌上的一边)"
    show zb gete_normal at center:
        ypos 2100
        zoom 0.3
    with dissolve
    zb "这家餐厅的菜真好吃~~~~~{w}\n比高中食堂吃的强多了"
    zb "(伸直胳膊去夹餐桌中间的菜)"
    npc "主播一不小心将邻座的杯子碰倒了"
    npc "杯中的果汁洒在了桌上"
    show zb gete_nervous at center,shake_side:
        ypos 2100
        zoom 0.3
    zb "啊…… 对不起对不起{w}\n我这就找纸巾擦！"
    show zb gete_nervous at right:
        ypos 2100
        xpos 1600
        zoom 0.3
    show wz decade_surprised at left:
        ypos 1900
        xpos 200
        zoom 0.6
    with dissolve
    wz "没事没事，我这边有手帕"
    npc "王子从口袋掏出一张不到10cm见方的手帕"
    npc "手一甩就把手帕盖在了洒了果汁的地方上"
    npc "………{w}\n可惜并没有什么卵用"
    show zb gete_smile at right:
        ypos 2100
        zoom 0.3
    zb "哈哈，王子你好傻啊"
    wz "哎呀，这都被你发现了"
    npc "二人相视一笑"
    hide zb gete_smile
    hide wz decade_surprised
    with dissolve
    npc "(与此同时，餐桌的另一边)"
    show jitou at center:
        ypos 1700
        zoom 0.3
    with dissolve
    jitou "(伸长胳膊够对面的橙汁瓶，指尖还差两厘米碰到瓶子)"
    show qf decade_normal at left:
        ypos 2000
        xpos 200
        zoom 0.3
    qf "......."
    npc "秋风坐在锦桐旁边，伸手拿起饮料瓶"
    qf "给"
    show jitou decade_smile at center,nod:
        ypos 1700
        zoom 0.3
    jitou "啊谢谢！我还以为够得到呢"
    hide jitou decade_smile
    hide qf decade_normal
    npc "我看着眼前的这些老朋友们"
    npc "有人给对方夹菜，有人笑着说上学时的糗事，秋风还在帮锦桐拧瓶盖"
    I "虽然已经过了这么多年，大家都变了些模样，有了不同的生活{w}\n但现在这样坐在一起聊天吃饭，又好似回到了毕业前的时光"
    I "只不过那时候的分离，变成了现在的重聚而已……{w}\n这样真好啊"
    npc "我举起茶杯，对着众人的方向轻轻碰了下空气"
    scene whitebg
    with dissolve


