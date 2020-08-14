init python:
    import random

    def options (dic,correct):
        #generate options
        #choose random vocab as options
        opt = [correct]
        while len(opt) < 5:
            i = dic.values()[int(random.random()*len(dic))][0]
            if i != correct and i not in opt:
                opt.append(i)

        #arrange options randomly
        rand = [random.random() for i in range(4)]
        ind = [i[0] for i in sorted(enumerate(rand), key=lambda x:x[1])]
        opt = [opt[ind[i]] for i in range(4)]

        for i in range(4):
            if ind[i] == 0:
                correctInd = i

        return opt, correctInd


    #intialize a dic for vocabularies
    dic = {}
    #'Chinese':['English','score','lastSeen']
    #score: familarity of the word, the higher the better
    #lastSeen: days ago last get the word correct/ seen

# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

image p = im.Scale('en.png',450,1000)

label start:

    #host of the game
    define h = Character('Shawn')

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg whitehouse:
        zoom 1.5

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    h "欢迎来到English{b}Daily{/b}!"
    h '我们将模拟您新到美国的日常生活。'
    h '您可以在日常情景对话中学习地道的美式英语。'

    $day=1
    $correct=0
    $wrong=0

    scene bg room
    show eileen happy at right
    show p at left

    '第[day]天'

    init python:
        #vocabulary for this module
        dic1 = {'好':['Good', 0, 0],
                '我':['I', 0, 0],
                '你':['You', 0, 0],
                '早上':['Morning', 0, 0],
                '下午':['Afternoon', 0, 0],
                '晚上':['Evening', 0, 0]}
        #update full dic
        dic.update(dic1)
        #generate vocabulary list
        lst = ''
        for i in dic1:
            lst+='{} {}\n'.format(i, dic1[i][0])

    """生词表\n
        [lst]
        """

    #flashcard setion here

    h '早上{color=#f09fffff}好{/color}！(请选择彩色词语的英文翻译)'

    $opt,correctInd = options(dic, 'Good')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：Good'

    h '{color=#f09fffff}我{/color}叫Shawn。'

    $opt,correctInd = options(dic, 'I')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：I'

    h    '请问您叫什么名字？'

    #user input name
    $name = 'User'
    define e = Character('[name]')

    e '{color=#f09fffff}你{/color}好！我叫[name]。'

    $opt,correctInd = options(dic, 'You')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：You'

    e '我今天{color=#f09fffff}早上{/color}刚到美国。'

    $opt,correctInd = options(dic, 'Morning')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：Morning'

    h '欢迎到美国来！'
    h '{color=#f09fffff}下午{/color}我带您去吃美国快餐？'
    $opt,correctInd = options(dic, 'Afternoon')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：Afternoon'

    e '好啊！'
    h '吃完快餐，{color=#f09fffff}晚上{/color}您可以在家好好儿休息。'

    $opt,correctInd = options(dic, 'Evening')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：Evening'

    e '{color=#f09fffff}好的{/color}。'

    $opt,correctInd = options(dic, 'Good')
    menu:
        '[opt[0]]':
            $choose = 0
        '[opt[1]]':
            $choose = 1
        '[opt[2]]':
            $choose = 2
        '[opt[3]]':
            $choose = 3

    if choose == correctInd:
        $correct += 1
        '回答正确!'
    else:
        $wrong +=1
        '回答错误:(\n正确答案：Good'

    $score=correct/(correct+wrong)
    if score < .8:
        '对不起,您未能正确选择80\%的答案。'
        jump start
    else:
        h '恭喜完成第[day]天的学习！'
        h "今天学习了:\n[lst]"
        h '从明天起，您可以每天选择三个话题学习。每个话题必须要达到80\%的正确率才算完成。'
        h '要坚持每天学习哦~'
        h '明天见！:)'
        jump daily

label daily:
    $day+=1
    'Day [day]'

    # 此处为游戏结尾。

    return
