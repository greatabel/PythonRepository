// 初始化变量
let score = 0;
let currentHour = 0;
let currentMinute = 0;
let correctHour = 0;
let correctMinute = 0;
let timeChangeMinutes = 0; // 记录时间变化的分钟数
let isPaused = false;
let animationInterval = null;
let nextQuestionTimeout = null;
let animationStep = 0;
let countdownInterval = null; // 倒计时计时器
let countdownTime = 10; // 倒计时时间

// 夸赞语句数组
const compliments = [
    "做得好！",
    "太棒了！",
    "你真聪明！",
    "继续加油！",
    "优秀！"
];

// 初始化下拉菜单、时钟数字和刻度
function init() {
    let hourSelect = document.getElementById('hour-select');
    let minuteSelect = document.getElementById('minute-select');

    for (let i = 0; i < 12; i++) {
        let option = document.createElement('option');
        option.value = i;
        option.text = i + '点';
        hourSelect.add(option);
    }

    for (let i = 0; i < 60; i++) {
        let option = document.createElement('option');
        option.value = i;
        option.text = i + '分';
        minuteSelect.add(option);
    }

    // 初始化时钟数字
    let clockNumbers = document.getElementById('clock-numbers');
    for (let i = 1; i <= 12; i++) {
        let angle = (i * 30 - 90) * Math.PI / 180;
        let x = 150 + 110 * Math.cos(angle);
        let y = 150 + 110 * Math.sin(angle);
        let text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", x);
        text.setAttribute("y", y);
        text.setAttribute("class", "clock-number");
        text.textContent = i;
        clockNumbers.appendChild(text);
    }

    // 初始化时钟刻度
    let clockTicks = document.getElementById('clock-ticks');
    for (let i = 0; i < 60; i++) {
        let angle = (i * 6 - 90) * Math.PI / 180;
        let x1 = 150 + 125 * Math.cos(angle);
        let y1 = 150 + 125 * Math.sin(angle);
        let x2 = 150 + (i % 5 === 0 ? 115 : 120) * Math.cos(angle);
        let y2 = 150 + (i % 5 === 0 ? 115 : 120) * Math.sin(angle);
        let line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", x1);
        line.setAttribute("y1", y1);
        line.setAttribute("x2", x2);
        line.setAttribute("y2", y2);
        line.setAttribute("class", i % 5 === 0 ? "clock-tick" : "clock-tick-small");
        clockTicks.appendChild(line);
    }
}

// 更新时钟显示
function updateClock(hour, minute) {
    let hourAngle = (hour % 12) * 30 + (minute / 60) * 30;
    let minuteAngle = (minute % 60) * 6;

    document.getElementById('hour-hand').setAttribute('transform', `rotate(${hourAngle}, 150, 150)`);
    document.getElementById('minute-hand').setAttribute('transform', `rotate(${minuteAngle}, 150, 150)`);
}

// 绘制颜色区域
function updateColorArea(startAngle, currentAngle, clockwise) {
    // 调整角度在0-360度范围内
    startAngle = (startAngle + 360) % 360;
    let endAngle = (startAngle + currentAngle + 360) % 360;

    let angleDiff = (currentAngle + 360) % 360;

    let largeArcFlag = angleDiff > 180 ? 1 : 0;
    let sweepFlag = clockwise ? 1 : 0;

    // 如果是逆时针，需要交换起始和结束角度
    if (!clockwise) {
        let temp = startAngle;
        startAngle = endAngle;
        endAngle = temp;
    }

    let startX = 150 + 140 * Math.cos(Math.PI * (startAngle - 90) / 180);
    let startY = 150 + 140 * Math.sin(Math.PI * (startAngle - 90) / 180);
    let endX = 150 + 140 * Math.cos(Math.PI * (endAngle - 90) / 180);
    let endY = 150 + 140 * Math.sin(Math.PI * (endAngle - 90) / 180);

    let d = `
        M 150 150
        L ${startX} ${startY}
        A 140 140 0 ${largeArcFlag} ${sweepFlag} ${endX} ${endY}
        Z
    `;

    document.getElementById('color-area').setAttribute('d', d);
}

// 生成随机题目
function generateQuestion() {
    // 清除可能存在的计时器和动画
    clearInterval(animationInterval);
    clearTimeout(nextQuestionTimeout);
    clearInterval(countdownInterval);
    animationInterval = null;
    nextQuestionTimeout = null;
    countdownInterval = null;
    animationStep = 0;

    // 隐藏结果显示区域
    document.getElementById('result-container').style.display = 'none';

    // 清除颜色区域
    document.getElementById('color-area').setAttribute('d', '');

    // 隐藏倒计时
    document.getElementById('countdown').style.display = 'none';

    // 重置倒计时
    countdownTime = 10;

    // 随机初始时间
    currentHour = Math.floor(Math.random() * 12);
    currentMinute = Math.floor(Math.random() * 60);

    // 随机加减时间
    timeChangeMinutes = (Math.floor(Math.random() * 2) === 0 ? -1 : 1) * (Math.floor(Math.random() * 59) + 1);

    // 生成题目文本
    let questionText = `${currentHour}点${currentMinute}分，${timeChangeMinutes > 0 ? '过' : '前'}${Math.abs(timeChangeMinutes)}分钟，是几点？`;
    document.getElementById('question').innerText = questionText;

    // 计算正确答案
    let totalMinutes = (currentHour * 60 + currentMinute + timeChangeMinutes + 720) % 720; // 防止负数
    correctHour = Math.floor(totalMinutes / 60) % 12;
    correctMinute = totalMinutes % 60;

    // 更新时钟显示
    updateClock(currentHour, currentMinute);
}

// 检查答案
function checkAnswer() {
    let hourSelect = document.getElementById('hour-select');
    let minuteSelect = document.getElementById('minute-select');

    let answerHour = parseInt(hourSelect.value);
    let answerMinute = parseInt(minuteSelect.value);

    // 保存用户答案的正确性
    let isCorrect = (answerHour === correctHour && answerMinute === correctMinute);

    // 显示结果
    showResult(isCorrect);

    // 运行动画
    animateClock(correctHour, correctMinute);

    // 在动画结束后，等待10秒，然后生成下一个题目
    function proceedToNextQuestion() {
        if (isPaused) {
            // 如果暂停，等待直到恢复
            setTimeout(proceedToNextQuestion, 1000);
        } else {
            generateQuestion();
        }
    }

    // 设置等待时间（在动画完成后启动倒计时）
    nextQuestionTimeout = setTimeout(proceedToNextQuestion, 10000 + animationDuration()); // 等待时间改为10000毫秒（10秒）
}

// 计算动画持续时间
function animationDuration() {
    // 每步50ms，共stepCount步
    let stepCount = 60;
    return stepCount * 50;
}

// 时钟动画
function animateClock(targetHour, targetMinute) {
    let stepCount = 60;
    animationStep = 0;

    // 计算分针总移动角度
    let startTotalMinutes = currentHour * 60 + currentMinute;
    let endTotalMinutes = targetHour * 60 + targetMinute;

    // 分针移动的实际分钟差，可能为负数
    let minuteDifference = endTotalMinutes - startTotalMinutes;

    // 调整分钟差到 [-360, 360] 范围内
    if (minuteDifference > 360) {
        minuteDifference -= 720;
    } else if (minuteDifference < -360) {
        minuteDifference += 720;
    }

    // 分针移动的角度
    let totalAngle = minuteDifference * 6;

    // 每一步的角度增量
    let angleStepValue = totalAngle / stepCount;

    // 确定移动方向
    let clockwise = angleStepValue >= 0;

    if (animationInterval) {
        clearInterval(animationInterval);
    }

    animationInterval = setInterval(function() {
        if (isPaused) return;

        animationStep++;
        let currentTotalMinutes = startTotalMinutes + (minuteDifference * (animationStep / stepCount));
        let hour = Math.floor((currentTotalMinutes / 60) % 12);
        let minute = currentTotalMinutes % 60;
        updateClock(hour, minute);

        // 更新颜色区域
        let startAngle = currentMinute * 6;
        let currentAngle = angleStepValue * animationStep;
        updateColorArea(startAngle, currentAngle, clockwise);

        if (animationStep >= stepCount) {
            clearInterval(animationInterval);
            // 在动画完成后启动倒计时
            startCountdown();
        }
    }, 50);
}

// 显示结果
function showResult(isCorrect) {
    let resultContainer = document.getElementById('result-container');
    let resultImage = document.getElementById('result-image');
    let resultText = document.getElementById('result-text');
    let additionalMessage = document.getElementById('additional-message');

    if (isCorrect) {
        resultImage.src = 'kd_right.jpg';
        resultText.innerText = '✅ 正确';
        resultText.classList.add('correct');
        resultText.classList.remove('wrong');
        score += 10; // 每次加10分
        document.getElementById('score').innerText = score;

        // 随机选择一条夸赞语句
        let compliment = '楚楚' + compliments[Math.floor(Math.random() * compliments.length)];
        additionalMessage.innerText = compliment;
        additionalMessage.style.color = 'green';

        // 触发撒花效果
        triggerConfetti();
    } else {
        resultImage.src = 'kd_wrong.jpg';
        resultText.innerText = '❌ 错误';
        resultText.classList.add('wrong');
        resultText.classList.remove('correct');

        // 显示正确答案
        additionalMessage.innerText = `正确答案是：${correctHour}点${correctMinute}分`;
        additionalMessage.style.color = 'red';
    }

    resultContainer.style.display = 'flex';
}

// 触发撒花效果
function triggerConfetti() {
    // 使用canvas-confetti库
    var duration = 2 * 1000;
    var animationEnd = Date.now() + duration;
    var defaults = {
        startVelocity: 60, // 增加初始速度
        spread: 720,       // 增加散射角度
        ticks: 60,
        zIndex: 9999,
        scalar: 1.5        // 增加粒子大小
    };

    function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    var interval = setInterval(function() {
        var timeLeft = animationEnd - Date.now();

        if (timeLeft <= 0) {
            return clearInterval(interval);
        }

        var particleCount = 100 * (timeLeft / duration); // 增加粒子数量
        // 从全屏范围内随机位置开始
        confetti(Object.assign({}, defaults, {
            particleCount,
            origin: {
                x: Math.random(),
                // 确保粒子从顶部落下
                y: Math.random() * 0.5
            }
        }));
    }, 250);
}

// 开始倒计时
function startCountdown() {
    let countdownElement = document.getElementById('countdown');
    countdownElement.style.display = 'block';
    countdownElement.innerText = countdownTime;

    countdownInterval = setInterval(function() {
        if (isPaused) return;

        countdownTime--;
        countdownElement.innerText = countdownTime;

        if (countdownTime <= 0) {
            clearInterval(countdownInterval);
            countdownElement.style.display = 'none';
        }
    }, 1000);
}

// 暂停或恢复动画和计时器
function togglePause() {
    isPaused = !isPaused;
    document.getElementById('pause-button').innerText = isPaused ? '继续' : '暂停';
}

// 初始化
document.getElementById('submit-answer').addEventListener('click', checkAnswer);
document.getElementById('pause-button').addEventListener('click', togglePause);
init();
generateQuestion();
