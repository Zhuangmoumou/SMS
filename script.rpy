define I = Character('我', color="#1a1a1a")#定义人物
define npc = Character(None, kind=adv)
define jitou =Character('锦桐',color="#b39c1f",image="jitou")
define bw = Character('冰', color="#888888")
define jige = Character('鸡哥', color="#4a90e2")

image bedroom="bedroom_waifu2x_2x_2n_jpeg.png"#定义场景
image homeopen="homeopen_waifu2x_2x_2n_jpeg.png"
image homeclose="homeclose_waifu2x_2x_2n_jpeg.png"
image CityStreet="street_waifu2x_2x_2n_jpeg.png"
image tablefood="tablefood_waifu2x_2x_3n_png.png"
image tablenofood="tablenofood_waifu2x_2x_3n_png.png"




<<<<<<< Updated upstream
init python: #批量定义锦桐立绘
    attires = ["decade", "dress", "shirt", "uniform"]
    expressions = ["surprised", "happy", "sad", "angry"]
    for a in attires:
        for e in expressions:
            renpy.image("zb %s %s" % (a, e), Transform("images/zb/zb_%s_%s.png" % (a, e), zoom=0.6))


init python: #批量定义锦桐立绘
    attires = ["decade", "dress", "shirt", "uniform"]
    expressions = ["surprised", "happy", "sad", "angry"]
    for a in attires:
        for e in expressions:
            renpy.image("jitou %s %s" % (a, e), Transform("images/jitou/jitou_%s_%s.png" % (a, e), zoom=0.6))

init python: #批量定义鸡哥立绘
    attires = ["decade", "xiaofu", "shirt", "uniform"]
    expressions = ["chakoudai", "huanbao", "sad", "angry"]
    for a in attires:
        for e in expressions:
            renpy.image("jige %s %s" % (a, e), Transform("images/jige/jige_%s_%s.png" % (a, e), zoom=0.6))

init python: #批量定义兵王立绘
    attires = ["dress", "dresshat", "shirt", "uniform"]
    expressions = ["smile", "happy", "sad", "angry"]
    for a in attires:
        for e in expressions:
            renpy.image("bw %s %s" % (a, e), Transform("images/bw/bw_%s_%s.png" % (a, e), zoom=0.6))
=======
>>>>>>> Stashed changes





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

    play sound "闹钟.mp3"
    npc "（闹钟声）"
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
    play sound "电梯.mp3"
    npc "（电梯声）"
    I "诶，电梯今天怎么这么快"
    I "顺便把垃圾倒了吧"

    scene CityStreet at p1080p
    with fade
    play music "轻松.mp3" volume 0.6 fadein 1.0
    I "呼…… 可算快到了，应该赶得上吧"
    npc "我正要过公路时，左肩突然被撞了一下"
    show jitou decade_surprised at hit_three,center:
        ypos 2100
        zoom 0.6
    with fade
    jitou "啊~~~{w}\n对...对...对不起！{w}\n我没看路！"
    I "是锦桐吗，好久不见了"
    show jitou decade at center:
        ypos 2100
        zoom 0.6
    jitou  "好巧啊"
    I "(这么多年过去，她还是老样子…… 不过聚会快开始了，先进去再叙旧吧)"
    I "我们赶紧进去吧，大家应该都到得差不多了"

    scene tablenofood at p1080p
    with dissolve
<<<<<<< Updated upstream

=======
    show jige decade_huanbao at center:
        ypos 1900
        zoom 0.6
    with dissolve
    jige "(看了看手表)"
    jige "时间差不多了，人都到齐了吗"
    I "好久不见，鸡哥"
    jige "你们终于到了，其他人呢"

    show jige decade_huanbao at left:
        ypos 1900
        zoom 0.6
    show wz decade_normal at right:
        ypos 1900  
        zoom 0.6
>>>>>>> Stashed changes
