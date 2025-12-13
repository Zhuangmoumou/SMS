
define I = Character("我", color="#fffe00")
define config.adjust_view_size = True
image bg bedroom = "images/bedroom.jpeg"
image bg stairs = "images/stairs.jpeg"
image bg street = "images/street.jpeg"
image bg restaurant "images/restaurant.png"

label start:
    scene bg classroom:
        with fade
    
    I "(揉着眼睛伸懒腰，打着哈欠）：哈～"
    "我随手抓过枕边的黑色手机，屏幕亮起的瞬间，手指顿在屏幕上"
    I "已经 11:00 了！？"
    I "糟了！今天要去同学聚会啊！"
    "我踩着拖鞋冲到衣柜前，单手套外套，另一只手抓过沙发上的深灰背包"
    scene bg stairs with fade
    I "不好，要赶快了，可别迟到了"
    scene bg street with fade
    I "话说从毕业到现在，都好几年没见大家了…… 有点期待，不知道大家现在都怎么样了
    scene bg restaurant
    "擦了擦汗"
    I "呼…… 可算赶到了，还好没超过约定时间。"
    