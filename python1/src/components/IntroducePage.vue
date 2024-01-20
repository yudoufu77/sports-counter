<template>
  <div class="sidebar-container" :class="{ 'hideSidebar': !isCollapse }">
    <IntrSideNav/>
    <el-scrollbar class="scrollbar-wrapper">
        <el-menu
          :default-active="activeMenu"
          :collapse="isCollapse"
          :background-color="variables.menuBg"
          :text-color="variables.menuText"
          :unique-opened="true"
          :active-text-color="variables.menuActiveText"
          :collapse-transition="false"
          mode="vertical"
        >
        <SidebarItem
        v-for="item in menuItems"
        :key="item.title"
        :is-sidebar-collapsed="isCollapse"
        :title="item.title"
        :icon="item.icon"
        :to="item.to"
        :children="item.children"
        />
      </el-menu>
      </el-scrollbar>
    </div>
    <div class="main-container" :class="{ 'collapsed': !isCollapse }">
      <div class="stars"></div>
      <div class= "primary-menu" id="fengong"><p>分工说明</p>
          <div class ="secondary-menu" id="fengong-1">
            <p>张期皓</p>
            <div class="content">
              前端开发,完成了Homepage(首页）、IntroducePage（介绍页，项目文档、侧边栏）两个网页及顶部栏的实现，并撰写提交文件。
            </div>
          </div>
          <div class ="secondary-menu" id="fengong-2">
            <p>杨善翔</p>
            <div class="content">
              允许用户输入俯卧撑 蹲起 引体向上 仰卧起坐四种运动的视频地址，实现了对视频进行运动计数、视频计时并根据计时计算分均运动次数的功能，且可将上述分析数据在视频中显示出来。
            </div>
          </div>
          <div class ="secondary-menu" id="fengong-3">
            <p>李鹏</p>
            <div class="content">
              前端开发，完成About页面(团队介绍，项目介绍)和Using页面(使用教程，用户体验)
            </div>
          </div>
          <div class ="secondary-menu" id="fengong-4">
            <p>洪晓蕾</p>
            <div class="content">
              对实现四种功能的代码进行补充和完善，整合后端代码，初步书写readme，测试功能完善程度。更新功能：将分析完毕的视频输出到特定文件夹，按照分析项目的类型命名输出视频并编号。
            </div>
          </div>
          <div class ="secondary-menu" id="fengong-5">
            <p>李穹语</p>
            <div class="content">
              对寻找到的资料和代码样例进行测试，对现有的代码进行测试，测试功能的完整程度。
            </div>
          </div>
      </div>
      <div class= "primary-menu" id="common"><p>共通性难点与关键点</p>
        <div class ="secondary-menu" id="common-1">
            <p>图像处理和姿态检测</p>
            <div class="content">
              这些脚本使用OpenCV和MediaPipe进行图像处理和姿态检测，这是实现准确运动分析的关键。以下是相关代码段：
              <pre>
import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, ...):
        ...
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(...)

    def find_pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)

        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return img
              </pre>
              这部分代码负责初始化MediaPipe的Pose模块，并通过find_pose函数处理图像以检测人体姿态。这是所有脚本的基础部分。
            </div>
          </div>
      </div>
      <div class ="secondary-menu" id="common-2">
            <p>角度计算</p>
            <div class="content">
              所有脚本中计算关节角度的方法相同。这些角度用于判断运动的正确性。以下是相关代码：
              <pre>
def find_angle(self, img, p1, p2, p3, draw=True):
  x1, y1 = self.lm_list[p1][1:]
  x2, y2 = self.lm_list[p2][1:]
  x3, y3 = self.lm_list[p3][1:]

  angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
  if angle &lt; 0:
      angle += 360
  angle = 360 - angle if angle > 180 else angle

  if draw:
      ...
  return angle
              </pre>
              此函数计算由三个关键点（p1, p2, p3）形成的角度，并将其转换为0到180度的范围。这对于分析各种运动姿势至关重要。
            </div>
          </div>
          <div class ="secondary-menu" id="common-3">
            <p>性能优化</p>
            <div class="content">
              由于实时视频处理要求高性能，代码的编写方式需要考虑效率。例如，在处理每一帧时避免不必要的计算：
              <pre>
while cap.isOpened():
  ret, img = cap.read()
  if not ret:
      break

  img = detector.find_pose(img, False)
  detector.find_position(img, False)

  # 后续代码仅在必要时执行，例如当检测到关键点时
  if len(detector.lm_list) != 0:
      ...
              </pre>
              在这里，仅当视频帧有效且检测到关键点时，才进行后续的角度计算和状态更新。
            </div>
          </div>
          <div class ="secondary-menu" id="common-4">
            <p>用户界面与反馈</p>
            <div class="content">
              代码通过在视频帧上绘制文本和图形来提供用户界面和反馈：
              <pre>
cv2.putText(img, f"Count: {int(count)}", (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
...
cv2.imshow('Squat counter(press key ''q'' to exit)', img)
              </pre>
              这些代码段在视频帧上显示计数器、时间、速度以及反馈信息（如“Fix Form”），增强了用户体验并提供了实时反馈。
<br>
综上所述，这些脚本共用的关键技术点是使用OpenCV和MediaPipe进行图像处理和姿态检测、准确的角度计算、性能优化以及用户友好的界面和反馈。这些要素共同确保了程序的有效性和实用性。
            </div>
          </div>
          <div class= "primary-menu" id="pull-ups"><p>引体向上脚本分析</p>
            <div class="content">
              在引体向上脚本中，独特的难点在于正确识别并计算手臂和肩膀的角度，以及判断运动的上升和下降阶段。以下是针对这些关键点的代码分析：
            <br>
            <br>
            识别关键点：11、13、15（左肘部）和12、14、16（右肘部）
            <br>
            这些关键点分别代表左右肘部和相邻的肩膀及手腕关节。通过计算这些关键点之间的角度，可以判断手臂的弯曲程度。
            <pre>
lelbow = detector.find_angle(img, 11, 13, 15)  # 左肘部角度
lshoulder = detector.find_angle(img, 13, 11, 23)  # 左肩部角度
relbow = detector.find_angle(img, 12, 14, 16)  # 右肘部角度
rshoulder = detector.find_angle(img, 14, 12, 24)  # 右肩部角度
            </pre>
            这里，find_angle 函数计算三个关键点之间的角度。这是通过首先找到每个关键点的像素坐标，然后应用三角函数来完成的。
            <br>
            <br>
            判断运动的上升和下降阶段
            <br>
            运动的上升和下降阶段是通过检查肘部和肩膀角度的变化来判断的。
            <pre>
# 根据肘部和肩膀的角度判断运动状态
if (lelbow > 150 and lshoulder > 150) or (relbow > 150 and rshoulder > 150):
    form = 1

if form == 1:
    if per == 0:
        if (lelbow &lt; 70 and lshoulder &lt; 70) or (relbow &lt; 70 and rshoulder &lt;70):
            feedback = "Up"
            if direction == 0:
                count += 0.5
                direction = 1
        else:
            feedback = "Fix Form"

    if per == 100:
        if (lelbow > 150 and lshoulder > 150) or (relbow > 150 and rshoulder > 150):
            feedback = "Down"
            if direction == 1:
                count += 0.5
                direction = 0
        else:
            feedback = "Fix Form"
            </pre>
            这段代码首先检查肘部和肩膀的角度是否超过150度，以确定运动是否处于准备状态。随后，根据角度的变化来判断是上升还是下降阶段。如果肘部和肩膀的角度小于70度，意味着完成了一次向上的动作；如果角度再次大于150度，意味着完成了向下的动作。这样，可以准确地计数引体向上的次数并给出适当的反馈。
<br>
通过这样的处理，脚本能够有效地追踪和分析引体向上的运动，为用户提供实时反馈。
            </div>
          </div>
          <div class= "primary-menu" id="push-ups"><p>俯卧撑脚本分析</p>
            <div class="content">
            在俯卧撑脚本中，关键的挑战在于准确识别上半身关节的位置，尤其是肘部和肩部，并据此评估俯卧撑的完整性和深度。以下是针对这些关键点的代码分析：
            <br>
            <br>
            识别关键点：11、13、15（肘部）和23（肩部）
            <br>
            这些关键点代表了肘部和肩部关节，对于判断俯卧撑动作的准确性至关重要。通过计算这些关键点之间的角度，可以判断上臂和身体的相对位置。
            <pre>
elbow = detector.find_angle(img, 11, 13, 15)  # 肘部角度
shoulder = detector.find_angle(img, 13, 11, 23)  # 肩部角度
hip = detector.find_angle(img, 11, 23, 25)  # 髋部角度
            </pre>
            在这里，find_angle 函数用于计算关键点之间的角度，它通过获取每个关键点的像素坐标并应用三角计算来实现。
            <br>
            <br>
            评估俯卧撑的完整性和深度
            <br>
            评估俯卧撑的完整性和深度涉及到分析肘部和肩部关节的角度，以确定俯卧撑的每个阶段。
            <pre>
# 通过肘部和肩部的角度来判断俯卧撑的阶段
per = np.interp(elbow, (90, 160), (0, 100))
bar = np.interp(elbow, (90, 160), (380, 50))

if elbow > 160 and shoulder > 40 and hip > 160:
    form = 1

if form == 1:
    if per == 0:
        if elbow &lt;= 90 and hip > 160:
            feedback = "Up"
            if direction == 0:
                count += 0.5
                direction = 1
        else:
            feedback = "Fix Form"

    if per == 100:
        if elbow > 160 and shoulder > 40 and hip > 160:
            feedback = "Down"
            if direction == 1:
                count += 0.5
                direction = 0
        else:
            feedback = "Fix Form"
            </pre>
            在这段代码中，首先通过肘部角度的变化来判断俯卧撑的阶段。肘部角度大于160度、肩部角度大于40度和髋部角度大于160度时，表示俯卧撑开始。当肘部角度减小至90度或以下时，表示达到最低点，即“Up”阶段。随后，当肘部角度再次增大至160度以上时，表示完成了一个下降动作，即“Down”阶段。
            <br>
            通过这种方式，脚本能够准确地追踪俯卧撑的每个阶段，并根据运动的质量给出相应的反馈。这样的处理确保了俯卧撑动作的准确评估和实时监控。
            </div>
          </div>
          <div class= "primary-menu" id="quarts"><p>深蹲脚本分析</p>
            <div class="content">
              在深蹲脚本中，独特的难点在于正确识别准确判断蹲伏和站立姿势，以及评估深蹲的上升和下降动作。以下是针对这些关键点的代码分析：
            <br>
            <br>
            识别关键点：27、25、23（左膝）和28、26、24（右膝）。
            <br>
            这些关键点代表左膝和右膝的位置。通过计算这些关键点之间的角度，可以判断腿部的弯曲程度。
            <pre>
lknee = detector.find_angle(img, 27, 25, 23)  # 左膝角度
lhip = detector.find_angle(img, 11, 23, 25)   # 左髋角度
rknee = detector.find_angle(img, 28, 26, 24)  # 右膝角度
rhip = detector.find_angle(img, 12, 24, 26)   # 右髋角度
            </pre>
            在这里，find_angle 函数计算给定的三个关键点之间的角度。这涉及到从姿态检测结果中获取每个关键点的像素坐标，并应用三角学原理来计算角度。
            <br>
            <br>
            评估深蹲的上升和下降动作
            <br>
            深蹲的上升和下降动作是通过检查左膝和右膝的角度变化来评估的。
            <pre>
# 根据左膝和右膝的角度判断运动状态
if (lknee > 160 and lhip > 160) or (rknee > 160 and rhip > 160):
    form = 1

if form == 1:
    if per == 0:
        if (lknee &lt; 60 and lhip &lt; 60) or (rknee &lt; 60 and rhip &lt; 60):
            feedback = "Down"
            if direction == 0:
                count += 0.5
                direction = 1
        else:
            feedback = "Fix Form"

    if per == 100:
        if (lknee > 160 and lhip > 160) or (rknee > 160 and rhip > 160):
            feedback = "Up"
            if direction == 1:
                count += 0.5
                direction = 0
        else:
            feedback = "Fix Form"
            </pre>
            这段代码首先检查左膝和右膝的角度，以确定运动是否处于正确的起始位置。然后，根据角度的变化来判断是上升还是下降阶段。如果膝盖的角度较小且腰部角度较大，表明完成了向上的动作；反之，如果膝盖的角度较大且腰部角度较小，表明完成了向下的动作。这样，可以准确地计数仰卧起坐的次数并给出适当的反馈。
            <br>
            通过这样的处理，脚本能够有效地追踪和分析深蹲的运动，为用户提供实时反馈，帮助提高运动效果。
            </div>
          </div>
          <div class= "primary-menu" id="sit-ups"><p>仰卧起坐脚本分析</p>
            <div class="content">
              在仰卧起坐脚本中，独特的难点在于正确识别腰部和膝盖的位置，以及评估仰卧起坐的上升和下降动作。以下是针对这些关键点的代码分析：
            <br>
            <br>
            识别关键点：27、25、23（左膝）和28、26、24（右膝）
            <br>
            这些关键点代表膝盖和腰部的位置。通过计算这些关键点之间的角度，可以判断腿部和腰部的弯曲程度。
            <pre>
lknee = detector.find_angle(img, 27, 25, 23)  # 左膝角度
lhip = detector.find_angle(img, 11, 23, 25)   # 左髋角度
rknee = detector.find_angle(img, 28, 26, 24)  # 右膝角度
rhip = detector.find_angle(img, 12, 24, 26)   # 右髋角度
            </pre>
            在这里，find_angle 函数计算给定的三个关键点之间的角度。这涉及到从姿态检测结果中获取每个关键点的像素坐标，并应用三角学原理来计算角度。
            <br>
            <br>
            评估仰卧起坐的上升和下降动作
            <br>
            仰卧起坐的上升和下降动作是通过检查膝盖和腰部的角度变化来评估的。
            <pre>
# 根据膝盖和腰部的角度判断运动状态
if (45 &lt; lknee &lt; 90 and lhip > 120) or (45 &lt; rknee &lt; 90 and rhip > 120):
    form = 1

if form == 1:
    if per == 0:
        if (45 &lt; rknee &lt; 90 and lhip &lt; 50) or (45 &lt; rknee &lt; 90 and rhip &lt; 50):
            feedback = "Down"
            if direction == 0:
                count += 0.5
                direction = 1
        else:
            feedback = "Fix Form"

    if per == 100:
        if (45 &lt; lknee &lt; 90 and lhip > 120) or (45 &lt; rknee &lt; 90 and rhip > 120):
            feedback = "Up"
            if direction == 1:
                count += 0.5
                direction = 0
        else:
            feedback = "Fix Form"
            </pre>
            这段代码首先检查膝盖和腰部的角度，以确定运动是否处于正确的起始位置。然后，根据角度的变化来判断是上升还是下降阶段。如果膝盖的角度较小且腰部角度较大，表明完成了向上的动作；反之，如果膝盖的角度较大且腰部角度较小，表明完成了向下的动作。这样，可以准确地计数仰卧起坐的次数并给出适当的反馈。
            <br>
            通过这样的处理，脚本能够有效地追踪和分析仰卧起坐的运动，为用户提供实时反馈，帮助提高运动效果。
            </div>
          </div>
          <div class= "primary-menu" id="front"><p>前端</p>
          <div class ="secondary-menu" id="nb">
            <p>NavBar</p>
            <div class="content">
              通过在src/router/index.js定义路由地址及对应名称、组件，实现能够在页面内多个组件的切换，以IntroducePage为例。
              <pre>
const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/introduce',
    name: 'IntroducePage',
    component: IntroducePage,
  }
  ]
  
  const router = createRouter({
  mode:'history',
  history: createWebHistory(process.env.BASE_URL),
  routes
})
              </pre>
              其中对HomePage的跳转实现在页面左侧的图标，在src/components/NavBar.vue中实现了相关样式及路由配置后，由App.vue调用
            </div>
          </div>
          <div class ="secondary-menu" id="hp">
            <p>HomePage</p>
            <div class="content">
              实现了鼠标滚动翻页功能，通过js的switchContent、handleWheel、handleKeyDown三个方法来控制页面在接收到鼠标滚动信号时来回翻动
              <pre>
switchContent(newIndex) {
    const pageCount = 2 // 页面总数
    if (this.isScrolling || newIndex &lt; 0 || newIndex >= pageCount) {
      return
    }
    this.currentIndex = newIndex
    this.isScrolling = true
    setTimeout(() => {
      this.isScrolling = false
    }, 550)
  },
  handleWheel(e) {
    e.preventDefault()

    const now = Date.now()
    if (now - this.lastScrollTime &lt; 1000) return // 1000毫秒的防抖时间
    this.lastScrollTime = now

    let delta = e.deltaY
    if (delta > 0) {
      this.switchContent(this.currentIndex + 1)
    } else if (delta &lt; 0) {
      this.switchContent(this.currentIndex - 1)
    }
  },
  handleKeyDown(e) {
    if (e.keyCode === 40) { // Down arrow key
      this.switchContent(this.currentIndex + 1)
    } else if (e.keyCode === 38) { // Up arrow key
      this.switchContent(this.currentIndex - 1)
    }
  }
              </pre>
              同时调用homecard.vue，实现三个卡片组件，并能通过点击去往另外三个页面，使用js调用router来实现handleCardClick函数，从而在点击时能够实现页面内跳转
              <pre>
methods: {
  handleCardClick(funcName) {
    if (funcName === 'toIntroducePage') {
      this.$router.push('/introduce') 
    } else if (funcName === 'toAboutPage') {
      this.$router.push('/about') 
    } else if (funcName === 'toUsingPage') {
      this.$router.push('/using')
    }
  },
              </pre>
              此外，在css中设置了星星动画，加强了美观性
              <pre>
.stars {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2px;
    height: 2px;
    z-index: 999;
    border-radius: 50%;
    box-shadow: -447px 387px #c4c4c4, -401px 118px #fafafa, -109px 217px #d9d9d9, -680px -436px #e3e3e3, 514px 360px #cccccc, -708px 298px #e8e8e8, -696px -270px #ededed, 116px -128px #f7f7f7, 179px 35px white, -404px -90px whitesmoke, -331px -309px #c4c4c4, -363px -24px #d1d1d1, 277px 416px #fafafa, -145px -244px whitesmoke, 123px 62px #d4d4d4, -407px 418px #d9d9d9, 535px 237px #d9d9d9, -466px -78px #f7f7f7, 257px 287px #dedede, 327px -398px #e0e0e0, -602px -38px #c2c2c2, 128px 398px #e6e6e6, 274px -446px #d1d1d1, -602px -298px #c7c7c7, 526px -5px #c4c4c4, -90px -158px #fcfcfc, 5px 294px whitesmoke, -633px 229px #c4c4c4, -475px 427px #dedede, 586px -453px #f2f2f2, 180px -432px #c7c7c7, -637px -88px #cfcfcf, -453px 308px #d6d6d6, -111px 1px #d9d9d9, 573px -450px #ededed, 198px 300px #d6d6d6, -355px 166px #dedede, -715px 13px #e3e3e3, 262px -104px #d1d1d1, 147px 325px #dbdbdb, 1px 399px #dbdbdb, 286px -100px white, 43px -329px #e8e8e8, 617px 55px #d9d9d9, -168px -392px #cccccc, 84px 219px #c9c9c9, 507px -226px #d9d9d9, -327px -70px #e6e6e6, 386px -212px #c4c4c4, -717px 4px #cfcfcf, 502px -231px #e3e3e3, 302px 56px #ededed, 649px 341px #c7c7c7, 569px 350px #c9c9c9, 516px -31px #e6e6e6, 689px 447px #c2c2c2, 591px -206px #fafafa, 422px -137px #e6e6e6, -510px -324px #cccccc, -649px 287px #c2c2c2, -194px -48px #f7f7f7, -279px -329px #d1d1d1, -406px 478px #dbdbdb, -735px -87px #c9c9c9, 30px -197px #dedede, -564px 233px #e6e6e6, -486px -324px #ededed, -54px -7px #ededed, -441px -194px #e3e3e3, -133px -95px #e0e0e0, -722px -73px #d6d6d6, 595px 423px #ededed, 568px -39px #ededed, 370px 377px #d1d1d1, -419px -102px #fcfcfc, -450px 109px #c4c4c4, -57px -119px #d1d1d1, -582px 150px #e6e6e6, 206px -263px #cfcfcf, 582px -461px #c9c9c9, -268px -141px #d9d9d9, -148px 291px #c7c7c7, 254px -179px #c9c9c9, 725px 424px #f0f0f0, 391px -150px #ebebeb, 89px -299px #d4d4d4, 170px 1px #c9c9c9, 243px 209px #c7c7c7, 27px 460px #c9c9c9, -465px -380px #d4d4d4, 530px -360px whitesmoke, -626px 53px #e0e0e0, 706px 218px #d9d9d9, 40px -82px #cccccc, -5px -212px #e6e6e6, -742px 33px #ebebeb, -714px 478px #e0e0e0, -585px -125px #cccccc, -216px 348px #cfcfcf, 601px 332px #ededed, 344px -88px #c4c4c4, 659px -22px #d1d1d1, -411px 188px #d6d6d6, -423px -206px #fcfcfc, -359px -136px #cfcfcf, 612px 406px whitesmoke, 725px 96px whitesmoke, 363px -446px white, -204px 325px #c9c9c9, 740px 176px #fafafa, -489px -352px white, -638px 64px #dbdbdb, 537px -65px #dbdbdb, 151px -32px #ebebeb, 681px 212px #fcfcfc, 604px -149px #e6e6e6, -542px -398px #c4c4c4, -707px 66px whitesmoke, -381px 258px #cfcfcf, -30px 332px #d6d6d6, 512px -381px #c9c9c9, 195px 288px #cccccc, -278px 479px #c7c7c7, 27px -208px #d6d6d6, -288px 15px white, -680px 248px #dedede, 433px 31px #c9c9c9, 150px -206px #d4d4d4, -79px 247px white, -594px 115px #e0e0e0, 99px 292px #e0e0e0, 673px -269px #dedede, -257px -64px #d1d1d1, 449px 81px #f2f2f2, 18px -99px #d1d1d1, -694px 415px #f7f7f7, 240px 264px #e0e0e0, 450px -172px white, 383px 7px #e8e8e8, 338px -73px #c9c9c9, 291px -19px #ebebeb, 659px 137px #d1d1d1, 602px -6px #fcfcfc, 554px 249px #ebebeb, 625px 356px #d9d9d9, 579px -183px #d6d6d6, -20px 250px white, -401px 431px #c4c4c4, -645px -232px #cccccc, -265px -148px white, 553px 258px #d1d1d1, 166px -360px #ebebeb, 719px 51px #ededed, 612px -129px #ebebeb, -465px -104px #f2f2f2, -154px -121px #d9d9d9, -1px 330px #f2f2f2, -666px 248px #f7f7f7, -720px 264px #ededed, 148px -365px #e6e6e6, -388px -349px #c4c4c4, 128px -88px #e3e3e3, -683px -274px #fafafa, -341px 41px #c9c9c9, -59px -471px #f0f0f0, -3px -427px #c2c2c2, 418px 167px #d6d6d6, 343px 247px #c7c7c7, 623px -347px #d1d1d1, 716px -217px white, 243px -409px whitesmoke, -75px -126px #d6d6d6, -730px -91px #c9c9c9, -210px -397px #cfcfcf, -349px 180px #c9c9c9, -567px -281px #e0e0e0, -460px 381px #fcfcfc, -310px -22px #ededed, 450px -1px #dbdbdb, -405px -328px #e3e3e3, 5px 332px #d6d6d6, -294px 302px #fcfcfc, -398px 97px whitesmoke, -696px 325px #cfcfcf, -589px 110px #d6d6d6, 353px -411px #dbdbdb, -697px -318px #ebebeb, -114px -72px #f0f0f0, 259px -193px #fcfcfc, 60px 26px #e6e6e6, -63px -232px white, 205px -372px #f7f7f7, -464px -333px #f2f2f2, -374px 123px white, -377px -386px #c7c7c7, -80px 337px #cccccc, 478px -178px #dbdbdb, 222px 420px #ebebeb, -707px 99px #c4c4c4, 716px -132px #fafafa, -253px -286px #e3e3e3, 646px 178px #f0f0f0, 201px 24px #d1d1d1, 178px -58px #c7c7c7, -557px 368px #ededed, 0px 219px #d9d9d9, -266px -269px #cccccc, 242px -197px #c9c9c9, -419px 193px #c2c2c2, -47px 91px #c7c7c7, -109px 75px #c2c2c2, -146px -453px #d6d6d6, 671px -350px #f2f2f2, 421px -91px #d9d9d9, 738px 19px #ededed, -316px -155px #dedede, 419px 244px #fcfcfc, -278px -418px #d6d6d6, -581px -181px #fcfcfc, 139px 264px #d9d9d9, 691px -11px #ebebeb, -622px 402px #c2c2c2, 219px 396px #f0f0f0, -149px -423px white, -716px -78px #d9d9d9, -590px 341px #e6e6e6, -208px 79px #d6d6d6, -227px -24px #f7f7f7, 239px 262px #d1d1d1, 740px 443px #f7f7f7, 509px 134px #d6d6d6, -555px 232px #e8e8e8, -67px -427px #cfcfcf, -368px 250px #f7f7f7, 715px -415px #fafafa, 411px -301px #f0f0f0, -322px 287px #d9d9d9, -429px -90px #f2f2f2, -327px -387px #f0f0f0, -491px 183px #c2c2c2, -133px 250px #d4d4d4, 538px 139px #e3e3e3, -417px -125px #f0f0f0, 653px -351px #e6e6e6, -549px 38px #d4d4d4, 602px 110px whitesmoke, 415px 105px #e0e0e0, -733px -371px #cfcfcf, 286px 403px #d4d4d4, 11px 320px #c4c4c4, -597px 158px whitesmoke, 716px -350px whitesmoke, 321px 67px #fafafa, -237px -300px #cfcfcf, 74px 152px #c9c9c9, 587px -123px #fcfcfc, 699px -332px whitesmoke, 399px 355px #f7f7f7, -323px 314px #dbdbdb, 89px 416px #c7c7c7, 445px 38px #e3e3e3, 572px 122px #c4c4c4, -258px 372px white, 49px 306px #d9d9d9, 437px -35px #dedede, 566px 174px #f2f2f2, 732px -299px whitesmoke, -410px 394px #ededed, 131px -415px white, 19px -326px #e8e8e8, -700px -188px #d1d1d1, 96px -1px #e0e0e0, -328px -396px #f0f0f0, -117px -214px #fcfcfc, -53px 261px #ebebeb, 80px 134px #d6d6d6, -364px -216px white, -636px -125px #dbdbdb, -639px -265px #e3e3e3, 208px 98px #c7c7c7, 172px 467px #e0e0e0, 435px 309px #e3e3e3, 194px -259px #f0f0f0, 209px -186px #c9c9c9, -312px 418px #fafafa, 229px 407px #c9c9c9, -449px -357px #fafafa, 674px 121px #e8e8e8, 608px -429px #ebebeb, -431px -428px #cfcfcf, 105px 462px #e3e3e3, -179px -372px #e3e3e3, 143px -317px #d6d6d6, -449px -149px #fafafa, -544px 250px #dedede, -220px -323px whitesmoke, 658px 8px whitesmoke, -656px -244px #e8e8e8, 347px 11px whitesmoke, 694px -230px #f7f7f7, -317px 1px #c4c4c4, 28px 23px #fcfcfc, -382px 321px #dbdbdb, 632px -74px #c4c4c4, 154px -245px #c2c2c2, -553px 337px #d6d6d6, -48px -243px #d1d1d1, 92px -391px #cccccc, -71px -256px #cfcfcf, -372px 57px #d9d9d9, 369px -140px #fcfcfc, 675px 81px #c2c2c2, -663px 254px #cccccc, 703px -203px #ededed, 74px -363px #c2c2c2, 643px -458px #d1d1d1, 198px 359px #cccccc, 265px 309px #d4d4d4, -353px -368px #e8e8e8, -465px 439px whitesmoke, 693px 360px #c9c9c9, 634px -397px #d1d1d1, 467px 25px whitesmoke, -558px -272px #e6e6e6, 671px 69px #dbdbdb, 407px 357px #cfcfcf, 379px 80px white, 10px -203px #c9c9c9, 104px -292px #f0f0f0, -667px -29px #d1d1d1, 557px -155px #e6e6e6, -505px 115px #cfcfcf, -605px 164px #f2f2f2, -108px -223px #e0e0e0, 523px -156px #ebebeb, 691px 230px white, -507px -13px #d1d1d1, -349px 332px #dedede, 520px 266px whitesmoke, -66px -250px #e6e6e6, -496px -449px #ebebeb, 414px -170px #dedede, -649px 230px #ebebeb, 598px -92px #c7c7c7, -638px 113px #c2c2c2, 151px 363px #f7f7f7, -445px -241px #f0f0f0, 527px -14px #dedede, 203px -61px #cfcfcf, -716px -284px #ebebeb, -525px 134px #c2c2c2;
    animation: fly 15s linear infinite;
    transform-style: preserve-3d;
}

.stars:before,
.stars:after {
    content: "";
    position: absolute;
    width: inherit;
    height: inherit;
    box-shadow: inherit;
}

.stars:before {
    transform: translateZ(-300px);
    opacity: .6;
}

.stars:after {
    transform: translateZ(-600px);
    opacity: .4;
}

@keyframes fly {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(2);
        opacity: 0.5;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}
              </pre>
            </div>
          </div>
          <div class ="secondary-menu" id="ip">
            <p>IntroducePage</p>
            <div class="content">
              实现了侧边栏，通过调用Hamburger.vue、IntrSideNav.vue、SidebarItem.vue实现基本功能，并通过src/assets/styles/variables.scss实现基本的样式，该侧边栏能够实现一级目录和二级目录的展开与折叠，（小缺点是折叠时无法隐藏文字导致图标拉的很长），并且折叠时能够禁用二级目录的展开与折叠，同时点击菜单栏能够实现文档跳转至相应位置。
              <br>
              如下，handleClick实现的是锚点路由跳转，toggle实现的是子菜单的折叠与跳转逻辑
              <pre>
handleClick() {
    if (this.to) {
      if (this.to.startsWith('#')) { // 检查 to 属性是否是锚点
        const section = document.querySelector(this.to)
        if (section) {
          section.scrollIntoView({ behavior: 'smooth' })
        }
      } else {
        this.$router.push(this.to) // 对于非锚点路由，使用正常的路由跳转
      }
    }
  },
  toggle() {
    if (this.hasChildren) {
      this.isExpanded = !this.isExpanded // 切换展开/折叠状态
      if (this.isSidebarCollapsed) {
        // 当侧边栏未折叠时
      }
      if (this.to) {
        this.handleClick() // 执行跳转逻辑
      }
    } else {
      this.handleClick() // 如果没有子菜单，直接执行跳转
    }
  },
              </pre>
              另外在IntroducePage中定义了一级目录、二级目录及正文还有代码的相关格式，在这里不再列出。
            </div>
          </div>
          <div class ="secondary-menu" id="ap">
            <p>AboutPage</p>
            <div class="content">
              实现了about-page、header、mission等类的相关格式，并介绍了本项目的基本信息与人员构成。
            </div>
          </div>
          <div class ="secondary-menu" id="up">
            <p>UsingPage</p>
            <div class="content">
              实现了与后端功能对应的接口按钮，能够在点击按钮时触发相应的后端代码，同时采用循环方式添加了一些展示精彩时刻的卡片
              <pre><code v-html="formattedCode"></code></pre>
              <br>
              <pre><code v-html="formattedCode1"></code></pre>
            </div>
          </div>
      </div>
    </div>
</template>

<script type="text/ecmascript-6">
import { mapGetters } from 'vuex'
import SidebarItem from './SidebarItem.vue'
import IntrSideNav from './IntrSideNav.vue'
import variables from '@/assets/styles/variables.scss'

export default {
  components: {
    SidebarItem,
    IntrSideNav
  },
  data() {
    return {
      menuItems: [
        { 
          title: '分工说明', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#fengong',
          children: [
            { title: '张期皓', to: '#fengong-1' },
            { title: '杨善翔', to: '#fengong-2' },
            { title: '李鹏', to: '#fengong-3' },
            { title: '洪晓蕾', to: '#fengong-4' },
            { title: '李穹语', to: '#fengong-3' }
          ]
        },
        {
          title: '共通性难点与关键点', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#common',
          children: [
            { title: '图像处理和姿态检测', to: '#common-1' },
            { title: '角度计算', to: '#common-2' },
            { title: '性能优化', to: '#common-3' },
            { title: '用户界面与反馈', to: '#common-4' },
          ]
        },
        {
          title: '引体向上脚本分析', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#pull-ups',
        },
        {
          title: '俯卧撑脚本分析', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#push-ups',
          
        },
        {
          title: '深蹲脚本分析', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#squats',
        },
        {
          title: '仰卧起坐脚本分析', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#sit-ups',
        },
        {
          title: '前端', 
          icon: require('@/assets/IntrSideItem/Python1.png'),  
          to: '#front',
          children: [
            { title: 'NavBar', to: '#nb' },
            { title: 'HomePage', to: '#hp' },
            { title: 'IntroducePage', to: '#ip' },
            { title: 'AboutPage', to: '#ap' },
            { title: 'UsingPage', to: '#up' },
          ]
        },
      ]
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    },
    scrollToSection(item) {
      this.$nextTick(() => {
        const section = document.querySelector(item.to)
        if (section) {
          section.scrollIntoView({ behavior: 'smooth' })
        }
      })
    }
  },
  mounted() {
    console.log(this.sidebar) // 这应该输出 sidebar 对象或 undefined
  },
  computed: {
    ...mapGetters('intrSide', ['permission_routes', 'sidebar']),
    activeMenu() {
      const route = this.$route
      const { meta, path } = route
      // if set path, the sidebar will highlight the path you set
      if (meta.activeMenu) {
        return meta.activeMenu
      }
      return path
    },
    variables() {
      return variables
    },
    isCollapse() {
      return !this.sidebar.opened
    },
    formattedCode() {
      return `
&lt;!-- 以循环方式添加一些展示精彩时刻的卡片 --&gt;
&lt;div v-for="moment in moments" :key="moment.id" class="moment-card"&gt;
  &lt;img :src="moment.image" alt="Moment Image"&gt;
  &lt;p&gt;{{ moment.description }}&lt;/p&gt;
&lt;/div&gt;
      `.trim()
    },
    formattedCode1() {
      return `
&amp;lt;!-- FeatureButtons 组件 --&amp;gt;
&amp;lt;div class="feature-buttons"&amp;gt;
  &amp;lt;h1&amp;gt;选择功能&amp;lt;/h1&amp;gt;
  &amp;lt;div class="button-container"&amp;gt;
    &amp;lt;button class="feature-button"&amp;gt;
      &amp;lt;span&amp;gt;跳  绳&amp;lt;/span&amp;gt;
    &amp;lt;/button&amp;gt;
    &amp;lt;button class="feature-button"&amp;gt;
      &amp;lt;span&amp;gt;俯 卧 撑&amp;lt;/span&amp;gt;
    &amp;lt;/button&amp;gt;
    &amp;lt;button class="feature-button"&amp;gt;
      &amp;lt;span&amp;gt;引体向上&amp;lt;/span&amp;gt;
    &amp;lt;/button&amp;gt;
  &amp;lt;/div&amp;gt;
&amp;lt;/div&amp;gt;
      `.trim()
    }
  }
}
</script>

<style lang="scss" scoped>
.stars {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2px;
    height: 2px;
    z-index: 999;
    border-radius: 50%;
    box-shadow: -447px 387px #c4c4c4, -401px 118px #fafafa, -109px 217px #d9d9d9, -680px -436px #e3e3e3, 514px 360px #cccccc, -708px 298px #e8e8e8, -696px -270px #ededed, 116px -128px #f7f7f7, 179px 35px white, -404px -90px whitesmoke, -331px -309px #c4c4c4, -363px -24px #d1d1d1, 277px 416px #fafafa, -145px -244px whitesmoke, 123px 62px #d4d4d4, -407px 418px #d9d9d9, 535px 237px #d9d9d9, -466px -78px #f7f7f7, 257px 287px #dedede, 327px -398px #e0e0e0, -602px -38px #c2c2c2, 128px 398px #e6e6e6, 274px -446px #d1d1d1, -602px -298px #c7c7c7, 526px -5px #c4c4c4, -90px -158px #fcfcfc, 5px 294px whitesmoke, -633px 229px #c4c4c4, -475px 427px #dedede, 586px -453px #f2f2f2, 180px -432px #c7c7c7, -637px -88px #cfcfcf, -453px 308px #d6d6d6, -111px 1px #d9d9d9, 573px -450px #ededed, 198px 300px #d6d6d6, -355px 166px #dedede, -715px 13px #e3e3e3, 262px -104px #d1d1d1, 147px 325px #dbdbdb, 1px 399px #dbdbdb, 286px -100px white, 43px -329px #e8e8e8, 617px 55px #d9d9d9, -168px -392px #cccccc, 84px 219px #c9c9c9, 507px -226px #d9d9d9, -327px -70px #e6e6e6, 386px -212px #c4c4c4, -717px 4px #cfcfcf, 502px -231px #e3e3e3, 302px 56px #ededed, 649px 341px #c7c7c7, 569px 350px #c9c9c9, 516px -31px #e6e6e6, 689px 447px #c2c2c2, 591px -206px #fafafa, 422px -137px #e6e6e6, -510px -324px #cccccc, -649px 287px #c2c2c2, -194px -48px #f7f7f7, -279px -329px #d1d1d1, -406px 478px #dbdbdb, -735px -87px #c9c9c9, 30px -197px #dedede, -564px 233px #e6e6e6, -486px -324px #ededed, -54px -7px #ededed, -441px -194px #e3e3e3, -133px -95px #e0e0e0, -722px -73px #d6d6d6, 595px 423px #ededed, 568px -39px #ededed, 370px 377px #d1d1d1, -419px -102px #fcfcfc, -450px 109px #c4c4c4, -57px -119px #d1d1d1, -582px 150px #e6e6e6, 206px -263px #cfcfcf, 582px -461px #c9c9c9, -268px -141px #d9d9d9, -148px 291px #c7c7c7, 254px -179px #c9c9c9, 725px 424px #f0f0f0, 391px -150px #ebebeb, 89px -299px #d4d4d4, 170px 1px #c9c9c9, 243px 209px #c7c7c7, 27px 460px #c9c9c9, -465px -380px #d4d4d4, 530px -360px whitesmoke, -626px 53px #e0e0e0, 706px 218px #d9d9d9, 40px -82px #cccccc, -5px -212px #e6e6e6, -742px 33px #ebebeb, -714px 478px #e0e0e0, -585px -125px #cccccc, -216px 348px #cfcfcf, 601px 332px #ededed, 344px -88px #c4c4c4, 659px -22px #d1d1d1, -411px 188px #d6d6d6, -423px -206px #fcfcfc, -359px -136px #cfcfcf, 612px 406px whitesmoke, 725px 96px whitesmoke, 363px -446px white, -204px 325px #c9c9c9, 740px 176px #fafafa, -489px -352px white, -638px 64px #dbdbdb, 537px -65px #dbdbdb, 151px -32px #ebebeb, 681px 212px #fcfcfc, 604px -149px #e6e6e6, -542px -398px #c4c4c4, -707px 66px whitesmoke, -381px 258px #cfcfcf, -30px 332px #d6d6d6, 512px -381px #c9c9c9, 195px 288px #cccccc, -278px 479px #c7c7c7, 27px -208px #d6d6d6, -288px 15px white, -680px 248px #dedede, 433px 31px #c9c9c9, 150px -206px #d4d4d4, -79px 247px white, -594px 115px #e0e0e0, 99px 292px #e0e0e0, 673px -269px #dedede, -257px -64px #d1d1d1, 449px 81px #f2f2f2, 18px -99px #d1d1d1, -694px 415px #f7f7f7, 240px 264px #e0e0e0, 450px -172px white, 383px 7px #e8e8e8, 338px -73px #c9c9c9, 291px -19px #ebebeb, 659px 137px #d1d1d1, 602px -6px #fcfcfc, 554px 249px #ebebeb, 625px 356px #d9d9d9, 579px -183px #d6d6d6, -20px 250px white, -401px 431px #c4c4c4, -645px -232px #cccccc, -265px -148px white, 553px 258px #d1d1d1, 166px -360px #ebebeb, 719px 51px #ededed, 612px -129px #ebebeb, -465px -104px #f2f2f2, -154px -121px #d9d9d9, -1px 330px #f2f2f2, -666px 248px #f7f7f7, -720px 264px #ededed, 148px -365px #e6e6e6, -388px -349px #c4c4c4, 128px -88px #e3e3e3, -683px -274px #fafafa, -341px 41px #c9c9c9, -59px -471px #f0f0f0, -3px -427px #c2c2c2, 418px 167px #d6d6d6, 343px 247px #c7c7c7, 623px -347px #d1d1d1, 716px -217px white, 243px -409px whitesmoke, -75px -126px #d6d6d6, -730px -91px #c9c9c9, -210px -397px #cfcfcf, -349px 180px #c9c9c9, -567px -281px #e0e0e0, -460px 381px #fcfcfc, -310px -22px #ededed, 450px -1px #dbdbdb, -405px -328px #e3e3e3, 5px 332px #d6d6d6, -294px 302px #fcfcfc, -398px 97px whitesmoke, -696px 325px #cfcfcf, -589px 110px #d6d6d6, 353px -411px #dbdbdb, -697px -318px #ebebeb, -114px -72px #f0f0f0, 259px -193px #fcfcfc, 60px 26px #e6e6e6, -63px -232px white, 205px -372px #f7f7f7, -464px -333px #f2f2f2, -374px 123px white, -377px -386px #c7c7c7, -80px 337px #cccccc, 478px -178px #dbdbdb, 222px 420px #ebebeb, -707px 99px #c4c4c4, 716px -132px #fafafa, -253px -286px #e3e3e3, 646px 178px #f0f0f0, 201px 24px #d1d1d1, 178px -58px #c7c7c7, -557px 368px #ededed, 0px 219px #d9d9d9, -266px -269px #cccccc, 242px -197px #c9c9c9, -419px 193px #c2c2c2, -47px 91px #c7c7c7, -109px 75px #c2c2c2, -146px -453px #d6d6d6, 671px -350px #f2f2f2, 421px -91px #d9d9d9, 738px 19px #ededed, -316px -155px #dedede, 419px 244px #fcfcfc, -278px -418px #d6d6d6, -581px -181px #fcfcfc, 139px 264px #d9d9d9, 691px -11px #ebebeb, -622px 402px #c2c2c2, 219px 396px #f0f0f0, -149px -423px white, -716px -78px #d9d9d9, -590px 341px #e6e6e6, -208px 79px #d6d6d6, -227px -24px #f7f7f7, 239px 262px #d1d1d1, 740px 443px #f7f7f7, 509px 134px #d6d6d6, -555px 232px #e8e8e8, -67px -427px #cfcfcf, -368px 250px #f7f7f7, 715px -415px #fafafa, 411px -301px #f0f0f0, -322px 287px #d9d9d9, -429px -90px #f2f2f2, -327px -387px #f0f0f0, -491px 183px #c2c2c2, -133px 250px #d4d4d4, 538px 139px #e3e3e3, -417px -125px #f0f0f0, 653px -351px #e6e6e6, -549px 38px #d4d4d4, 602px 110px whitesmoke, 415px 105px #e0e0e0, -733px -371px #cfcfcf, 286px 403px #d4d4d4, 11px 320px #c4c4c4, -597px 158px whitesmoke, 716px -350px whitesmoke, 321px 67px #fafafa, -237px -300px #cfcfcf, 74px 152px #c9c9c9, 587px -123px #fcfcfc, 699px -332px whitesmoke, 399px 355px #f7f7f7, -323px 314px #dbdbdb, 89px 416px #c7c7c7, 445px 38px #e3e3e3, 572px 122px #c4c4c4, -258px 372px white, 49px 306px #d9d9d9, 437px -35px #dedede, 566px 174px #f2f2f2, 732px -299px whitesmoke, -410px 394px #ededed, 131px -415px white, 19px -326px #e8e8e8, -700px -188px #d1d1d1, 96px -1px #e0e0e0, -328px -396px #f0f0f0, -117px -214px #fcfcfc, -53px 261px #ebebeb, 80px 134px #d6d6d6, -364px -216px white, -636px -125px #dbdbdb, -639px -265px #e3e3e3, 208px 98px #c7c7c7, 172px 467px #e0e0e0, 435px 309px #e3e3e3, 194px -259px #f0f0f0, 209px -186px #c9c9c9, -312px 418px #fafafa, 229px 407px #c9c9c9, -449px -357px #fafafa, 674px 121px #e8e8e8, 608px -429px #ebebeb, -431px -428px #cfcfcf, 105px 462px #e3e3e3, -179px -372px #e3e3e3, 143px -317px #d6d6d6, -449px -149px #fafafa, -544px 250px #dedede, -220px -323px whitesmoke, 658px 8px whitesmoke, -656px -244px #e8e8e8, 347px 11px whitesmoke, 694px -230px #f7f7f7, -317px 1px #c4c4c4, 28px 23px #fcfcfc, -382px 321px #dbdbdb, 632px -74px #c4c4c4, 154px -245px #c2c2c2, -553px 337px #d6d6d6, -48px -243px #d1d1d1, 92px -391px #cccccc, -71px -256px #cfcfcf, -372px 57px #d9d9d9, 369px -140px #fcfcfc, 675px 81px #c2c2c2, -663px 254px #cccccc, 703px -203px #ededed, 74px -363px #c2c2c2, 643px -458px #d1d1d1, 198px 359px #cccccc, 265px 309px #d4d4d4, -353px -368px #e8e8e8, -465px 439px whitesmoke, 693px 360px #c9c9c9, 634px -397px #d1d1d1, 467px 25px whitesmoke, -558px -272px #e6e6e6, 671px 69px #dbdbdb, 407px 357px #cfcfcf, 379px 80px white, 10px -203px #c9c9c9, 104px -292px #f0f0f0, -667px -29px #d1d1d1, 557px -155px #e6e6e6, -505px 115px #cfcfcf, -605px 164px #f2f2f2, -108px -223px #e0e0e0, 523px -156px #ebebeb, 691px 230px white, -507px -13px #d1d1d1, -349px 332px #dedede, 520px 266px whitesmoke, -66px -250px #e6e6e6, -496px -449px #ebebeb, 414px -170px #dedede, -649px 230px #ebebeb, 598px -92px #c7c7c7, -638px 113px #c2c2c2, 151px 363px #f7f7f7, -445px -241px #f0f0f0, 527px -14px #dedede, 203px -61px #cfcfcf, -716px -284px #ebebeb, -525px 134px #c2c2c2;
    animation: fly 15s linear infinite;
    transform-style: preserve-3d;
}

.stars:before,
.stars:after {
    content: "";
    position: absolute;
    width: inherit;
    height: inherit;
    box-shadow: inherit;
}

.stars:before {
    transform: translateZ(-300px);
    opacity: .6;
}

.stars:after {
    transform: translateZ(-600px);
    opacity: .4;
}

@keyframes fly {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(2);
        opacity: 0.5;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}
// 一级目录样式
.primary-menu {
    color: #b04f48;
    padding: 0px 20px;
    text-align: center;

    p{
      font-size: 32px;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
    }

    li {
        display: inline-block;
        margin-right: 20px;
    }

    a {
        color: #b04f48;
        text-decoration: none;
        font-size: 16px;

        &:hover {
            text-decoration: underline;
        }
    }
}

// 二级目录样式
.secondary-menu {
    color: #104f8d;
    padding: 0px 40px;
    text-align: center;
    p {
      font-size: 24px;
      text-align: left;
    }
    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
    }

    li {
        display: inline-block;
        margin-right: 10px;
    }

    a {
        color: #104f8d;
        text-decoration: none;
        font-size: 14px;

        &:hover {
            color: #007bff;
        }
    }
}

// 正文样式
.content {
    padding: 0px 40px;
    font-size: 16px;
    color: #edcc86;
    line-height: 1.8;
    text-align: left;
}

.content pre {
    position: relative;
}

</style>